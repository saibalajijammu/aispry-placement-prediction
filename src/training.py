import pandas as pd
import mlflow
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score,precision_score,recall_score,f1_score,classification_report)
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

df = pd.read_csv(r'c:\aispry\data\processed\training_dataset.csv')
df.head()
X = df.drop("Placement_Status", axis=1)
y = df["Placement_Status"]

X = X.drop(columns=[
    "Projects",
    "Certifications",
    "Aptitude_Test_Score",
    "Soft_Skills_Rating"
])

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

print(X_train.columns.tolist())
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

mlflow.set_experiment("Placement_Prediction")

with mlflow.start_run(run_name="Logistic_Regression"):
    log_model = LogisticRegression(max_iter=1000)
    mlflow.log_param("model", "Logistic Regression")
    mlflow.log_param("max_iter", 1000)
    log_model.fit(X_train_scaled, y_train)
    y_pred_log = log_model.predict(X_test_scaled)
    log_accuracy = accuracy_score(y_test, y_pred_log)
    mlflow.log_metric("accuracy", log_accuracy)
    print(f"\nAccuracy  : {log_accuracy:.4f}")
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred_log))
    mlflow.sklearn.log_model(
        log_model,
        "logistic_regression_model"
    )

with mlflow.start_run(run_name="Random_Forest"):
    rf_model = RandomForestClassifier(n_estimators=100,max_depth=5,min_samples_split=10,min_samples_leaf=5,random_state=42)
    mlflow.log_param("model", "Random Forest")
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("max_depth", 5)
    rf_model.fit(X_train, y_train)
    y_pred_rf = rf_model.predict(X_test)
    rf_accuracy = accuracy_score(y_test, y_pred_rf)
    mlflow.log_metric("accuracy", rf_accuracy)
    print(f"\nAccuracy  : {rf_accuracy:.4f}")
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred_rf))
    mlflow.sklearn.log_model(
        rf_model,
        "random_forest_model"
    )


with mlflow.start_run(run_name="XGBoost"):
    xgb_model = XGBClassifier(max_depth=4,learning_rate=0.1,n_estimators=100,subsample=0.8,colsample_bytree=0.8,eval_metric="logloss",random_state=42)
    mlflow.log_param("model", "XGBoost")
    mlflow.log_param("max_depth", 4)
    mlflow.log_param("learning_rate", 0.1)
    mlflow.log_param("n_estimators", 100)
    xgb_model.fit(X_train, y_train)
    y_pred_xgb = xgb_model.predict(X_test)
    xgb_accuracy = accuracy_score(y_test, y_pred_xgb)
    print(f"\nAccuracy  : {xgb_accuracy:.4f}")
    mlflow.log_metric("accuracy", xgb_accuracy)
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred_xgb))
    mlflow.sklearn.log_model(
        xgb_model,
        "xgboost_model"
    )

comparison_df = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Random Forest",
        "XGBoost"
    ],

    "Accuracy": [
        log_accuracy,
        rf_accuracy,
        xgb_accuracy
    ]
})

print(comparison_df)

import os

os.makedirs("models", exist_ok=True)

joblib.dump(xgb_model, "models/best_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("Model and scaler saved successfully!")

from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
y_prob = xgb_model.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_prob)

roc_auc = auc(fpr, tpr)

print("\nAUC Score:", roc_auc)
plt.figure(figsize=(8, 6))

plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.4f}")

plt.plot([0, 1], [0, 1], linestyle="--")

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")

plt.title("ROC Curve - XGBoost")

plt.legend()

plt.show()


import pandas as pd
import matplotlib.pyplot as plt

importance = xgb_model.feature_importances_

feature_names = X_train.columns

importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importance
})


importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance:\n")
print(importance_df)
plt.figure(figsize=(10, 6))

plt.barh(
    importance_df["Feature"],
    importance_df["Importance"]
)

plt.xlabel("Importance Score")
plt.ylabel("Features")

plt.title("XGBoost Feature Importance")

plt.gca().invert_yaxis()

plt.show()
