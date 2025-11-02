# -math-adaptive-prototype
AI-Powered Adaptive Math Learning App — A Streamlit-based hybrid AI system that adjusts question difficulty dynamically using rule-based logic and machine learning.
# 🧮 Math Adventures — Adaptive Learning Prototype  
**AI-Powered Personalized Math Practice System**

---

### 🌟 Overview  
**Math Adventures** is an **AI-driven adaptive learning prototype** that dynamically adjusts the difficulty of math puzzles based on each learner’s performance.  
The goal is to keep students (ages 5–10) in their *optimal challenge zone* — not too easy, not too hard — using both **rule-based logic** and a **lightweight machine-learning model**.

---

### 🚀 Key Features  
- 🧩 **Automatic Difficulty Adjustment**  
  Learners start at a chosen level (Easy / Medium / Hard), and difficulty adapts after every round.  
- 📊 **Hybrid AI Engine**  
  Combines simple rule-based logic with a Logistic Regression model for intelligent prediction.  
- ⏱️ **Performance Tracking**  
  Logs accuracy, response time, and progress across puzzles.  
- 🎨 **Interactive Streamlit Interface**  
  Clean, responsive UI for smooth question-answer flow.  
- 📈 **Session Summary Dashboard**  
  Shows total accuracy, average solving time, and next recommended level.  

---




### 🧩 Tech Stack  
| Category | Tools / Libraries |
|-----------|------------------|
| Frontend UI | Streamlit |
| Machine Learning | scikit-learn (Logistic Regression) |
| Data Processing | NumPy |
| Logic | Rule-based + ML Hybrid |
| Language | Python 3.10+ |

---





🎯 How It Works

1. User starts with chosen difficulty.
   
3. Puzzle Generator creates arithmetic question.
   
3.Tracker records correctness & time.

4.Adaptive Engine:

5.Uses Rule-based logic initially.

6.Switches to ML model when enough data is collected.

7.Difficulty updates automatically for the next puzzle.

8.Session summary shown with performance metrics & recommended next level.


----

🧩 Example Flow
User → 3 + 4 = 7 ✅ → Difficulty ↑

User → 23 × 3 = 66 ❌ → Difficulty ↓

System learns patterns → predicts next level automatically

----


🧠 Learning Approach

1.Rule-based adaptation: quick and interpretable early-stage logic.

2.ML-based adaptation: Logistic Regression learns from user data to make nuanced predictions.

3.Hybrid model: ensures consistent behavior even with limited data.


----

🌍 Future Improvements

1.Add reinforcement learning for continuous personalization.

2.Expand subjects (Science / Language).

3.Store user profiles & progress in a small database.

4.Add leaderboard or gamification for engagement.


----

👨‍💻 Author
Pranjal Tiwari
AI & ML Engineering Student | Passionate about adaptive education & intelligent systems.



