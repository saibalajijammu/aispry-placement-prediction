import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("students.csv")
df.head()
df.shape
df.info()
df.describe()
df.isnull().sum()
df.drop(columns=["Student_ID"], inplace=True)
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
df = df[(df["Age"] >= 18) & (df["Age"] <= 23)]
df["Gender"] = df["Gender"].str.strip().str.lower()
df.drop_duplicates(inplace=True)

df["Gender"] = df["Gender"].map({ "male": 0, "female": 1})
df["Placement_Status"] = df["Placement_Status"].map({ "Not Placed": 0,"Placed": 1})
df = pd.get_dummies(df,columns=["Degree", "Branch"],drop_first=True)

df.to_csv("training_dataset.csv", index=False)
