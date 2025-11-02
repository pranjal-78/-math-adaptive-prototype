import streamlit as st
import time
from puzzle_generator import PuzzleGenerator
from tracker import PerformanceTracker
from adaptive_engine import AdaptiveEngine

st.set_page_config(page_title="Math Adventures", page_icon="🧮", layout="centered")

# Safe rerun helper (works for all versions)
def safe_rerun():
    try:
        st.rerun()
    except AttributeError:
        st.experimental_rerun()

# Initialize session state
if "tracker" not in st.session_state:
    st.session_state.tracker = PerformanceTracker()
if "engine" not in st.session_state:
    st.session_state.engine = AdaptiveEngine()
if "puzzle" not in st.session_state:
    st.session_state.puzzle = None
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.title("🧠 Math Adventures — Adaptive Learning Game")

# Sidebar controls
st.sidebar.header("Game Controls")
name = st.sidebar.text_input("Enter your name", value="Player")
if st.sidebar.button("Restart Game"):
    st.session_state.tracker = PerformanceTracker()
    st.session_state.engine = AdaptiveEngine()
    st.session_state.puzzle = None
    st.session_state.game_over = False
    safe_rerun()

difficulty = st.sidebar.selectbox("Select Starting Difficulty", ["Easy", "Medium", "Hard"])
num_questions = st.sidebar.slider("Number of Questions", 3, 10, 5)
st.session_state.engine.difficulty = difficulty
generator = PuzzleGenerator()

# Start new puzzle
if not st.session_state.puzzle and not st.session_state.game_over:
    st.session_state.puzzle = generator.generate(st.session_state.engine.difficulty)
    st.session_state.start_time = time.time()

# Game loop
if not st.session_state.game_over:
    q, ans = st.session_state.puzzle
    st.subheader(f"🧩 Solve this ({st.session_state.engine.difficulty}) question:")
    st.markdown(f"### {q}")
    user_input = st.text_input("Enter your answer:", key=f"answer_{len(st.session_state.tracker.records)}")

    if st.button("Submit"):
        try:
            user_ans = float(user_input)
        except ValueError:
            st.error("❌ Invalid input! Please enter a number.")
            user_ans = -999

        response_time = time.time() - st.session_state.start_time

        # ✅ Log user performance
        st.session_state.tracker.log(
            q, user_ans, ans, response_time, st.session_state.engine.difficulty
        )

        # Feedback
        if abs(user_ans - ans) < 0.01:
            st.success(f"✅ Correct! ({ans}) in {response_time:.2f}s")
        else:
            st.error(f"❌ Wrong! Correct answer was {ans}")

        # Generate next question or end
        if len(st.session_state.tracker.records) < num_questions:
            st.session_state.puzzle = generator.generate(st.session_state.engine.difficulty)
            st.session_state.start_time = time.time()
            safe_rerun()
        else:
            st.session_state.game_over = True
            safe_rerun()

# End of session summary
if st.session_state.game_over:
    summary = st.session_state.tracker.summary()
    st.success("🎉 Session Completed!")
    st.write(f"**Total Questions:** {summary['total']}")
    st.write(f"**Accuracy:** {summary['accuracy']}%")
    st.write(f"**Average Time:** {summary['avg_time']}s")

    # Hybrid adaptive update (Rule + ML)
    next_level = st.session_state.engine.update_difficulty(
        summary, st.session_state.tracker.records
    )
    st.info(f"👉 Recommended Next Level: **{next_level}**")

    st.write("### 📊 Detailed Results:")
    st.table(st.session_state.tracker.records)
