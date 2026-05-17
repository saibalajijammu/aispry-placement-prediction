from feast import FeatureStore

store = FeatureStore(
    repo_path="../placement_feature_store/feature_repo"
)

def get_student_features(student_id):

    features = store.get_online_features(
        features=[
            "student_features:Age",
            "student_features:CGPA",
            "student_features:Internships",
            "student_features:Coding_Skills",
            "student_features:Communication_Skills",
            "student_features:Backlogs",
            "student_features:Gender",
            "student_features:Degree_B.Tech",
            "student_features:Degree_BCA",
            "student_features:Degree_MCA",
            "student_features:Branch_Civil",
            "student_features:Branch_ECE",
            "student_features:Branch_IT",
            "student_features:Branch_ME",
        ],

        entity_rows=[
            {
                "student_id": student_id
            }
        ]
    ).to_dict()

    return features