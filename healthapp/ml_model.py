import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


class HealthMLAgent:

    def __init__(self):

        self.model = None

        self.dataset_path = "health_dataset_100000.csv"


    def train_model(self):

        df = pd.read_csv(self.dataset_path)

        X = df[
            [
                "age",
                "gender",
                "height",
                "weight",
                "blood_pressure",
                "cholesterol"
            ]
        ]

        y = df["health_status"]

        categorical_columns = ["gender"]

        preprocessor = ColumnTransformer(
            transformers=[
                (
                    "cat",
                    OneHotEncoder(handle_unknown="ignore"),
                    categorical_columns
                )
            ],
            remainder="passthrough"
        )

        self.model = Pipeline(
            steps=[
                (
                    "preprocessor",
                    preprocessor
                ),

                (
                    "classifier",
                    RandomForestClassifier(
                        n_estimators=200,
                        max_depth=12,
                        random_state=42
                    )
                )
            ]
        )

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.20,
            random_state=42
        )

        self.model.fit(
            X_train,
            y_train
        )

        y_pred = self.model.predict(
            X_test
        )

        accuracy = accuracy_score(
            y_test,
            y_pred
        )

        print(
            "Model Accuracy:",
            accuracy
        )

        return self.model


    def predict(
        self,
        age,
        gender,
        height,
        weight,
        blood_pressure,
        cholesterol
    ):

        if self.model is None:

            self.train_model()


        input_data = pd.DataFrame(
            [
                {
                    "age": age,
                    "gender": gender,
                    "height": height,
                    "weight": weight,
                    "blood_pressure": blood_pressure,
                    "cholesterol": cholesterol
                }
            ]
        )


        prediction = self.model.predict(
            input_data
        )[0]


        probability = self.model.predict_proba(
            input_data
        )[0]


        confidence = round(
            max(probability) * 100,
            2
        )


        return prediction, confidence


health_agent = HealthMLAgent()