class PerformanceTracker:
    def __init__(self):
        self.records = []

    def log(self, question, user_ans, correct_ans, response_time, difficulty):
        """Log one question’s performance details"""
        correct = abs(user_ans - correct_ans) < 0.01
        self.records.append({
            "question": question,
            "user_ans": user_ans,
            "correct_ans": correct_ans,
            "response_time": response_time,
            "difficulty": difficulty,
            "correct": correct
        })

    def summary(self):
        """Summarize user performance across session"""
        total = len(self.records)
        correct = sum(1 for r in self.records if r["correct"])
        avg_time = sum(r["response_time"] for r in self.records) / total if total else 0
        accuracy = (correct / total) * 100 if total else 0
        return {
            "total": total,
            "correct": correct,
            "accuracy": round(accuracy, 2),
            "avg_time": round(avg_time, 2)
        }


