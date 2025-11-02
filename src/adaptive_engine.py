import numpy as np
from sklearn.linear_model import LogisticRegression

class AdaptiveEngine:
    def __init__(self):
        self.difficulty = "Easy"
        self.ml_model = None
        self.trained = False

    # -------------------------------
    # Mapping helpers
    # -------------------------------
    def difficulty_to_num(self, level):
        mapping = {"Easy": 0, "Medium": 1, "Hard": 2}
        return mapping.get(level, 0)

    def num_to_difficulty(self, num):
        mapping = {0: "Easy", 1: "Medium", 2: "Hard"}
        return mapping.get(num, "Medium")

    # -------------------------------
    # ML model training
    # -------------------------------
    def train_model(self, tracker_records):
        """
        Train a Logistic Regression model based on performance data.
        Will only train if there is enough diverse data (≥5 samples and ≥2 classes).
        """
        if len(tracker_records) < 5:
            self.trained = False
            self.ml_model = None
            return None

        X, y = [], []
        for r in tracker_records[:-1]:
            curr_level = self.difficulty_to_num(r["difficulty"])
            acc = 1 if r["correct"] else 0
            time_taken = r["response_time"]
            X.append([curr_level, acc, time_taken])

        # Target is the next difficulty level
        for r in tracker_records[1:]:
            y.append(self.difficulty_to_num(r["difficulty"]))

        # ✅ Ensure there are at least 2 different difficulty levels
        if len(set(y)) < 2:
            self.trained = False
            self.ml_model = None
            return None

        # Train logistic regression
        model = LogisticRegression(max_iter=200)
        model.fit(X, y)
        self.ml_model = model
        self.trained = True

    # -------------------------------
    # Prediction (ML or fallback)
    # -------------------------------
    def predict_next_level(self, curr_diff, acc, avg_time):
        """
        Use ML model if trained; else fallback to rule-based logic.
        """
        if self.trained and self.ml_model:
            X_new = np.array([[self.difficulty_to_num(curr_diff), acc, avg_time]])
            pred = self.ml_model.predict(X_new)[0]
            return self.num_to_difficulty(pred)
        else:
            # Rule-based fallback logic
            if acc > 80 and avg_time < 5:
                return "Hard"
            elif acc < 50:
                return "Easy"
            else:
                return "Medium"

    # -------------------------------
    # Update difficulty
    # -------------------------------
    def update_difficulty(self, summary, tracker_records):
        """
        Decides the next difficulty using hybrid (Rule + ML) logic.
        """
        # Try to train model using recent records
        self.train_model(tracker_records)

        # Predict next difficulty
        next_level = self.predict_next_level(
            self.difficulty, summary["accuracy"], summary["avg_time"]
        )

        self.difficulty = next_level
        return next_level

