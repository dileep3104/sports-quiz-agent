import streamlit as st
from src.generator import generate_quiz

# ---------------- Session State ---------------- #

if "quiz" not in st.session_state:
    st.session_state.quiz = None

if "submitted" not in st.session_state:
    st.session_state.submitted = False

# ---------------- Page Config ---------------- #

st.set_page_config(
    page_title="AI Sports Quiz Generator",
    page_icon="🏏",
    layout="centered"
)

st.title("🏏 AI Sports Quiz Generator")
st.write("Generate sports quizzes using AI, historical facts, and live sports news.")

# ---------------- Inputs ---------------- #

sport = st.selectbox(
    "Select a Sport",
    [
        "Cricket",
        "Football",
        "Basketball",
        "Tennis"
    ]
)

difficulty = st.selectbox(
    "Select Difficulty",
    [
        "Easy",
        "Medium",
        "Hard"
    ]
)

# ---------------- Generate Quiz ---------------- #

if st.button("Generate Quiz"):

    with st.spinner("Generating quiz..."):
        st.session_state.quiz = generate_quiz(sport, difficulty)

    st.session_state.submitted = False
    for i in range(1, 6):
        key = f"question_{i}"
        if key in st.session_state:
            del st.session_state[key]
    st.success("Quiz generated successfully!")

# ---------------- Display Quiz ---------------- #

if st.session_state.quiz:

    for i, question in enumerate(st.session_state.quiz, start=1):

        st.subheader(f"Question {i}")

        st.write(question.question)

        st.radio(
            "Choose your answer",
            question.options,
            key=f"question_{i}",
            disabled=st.session_state.submitted
        )

        # Show feedback after submission
        if st.session_state.submitted:

            selected_answer = st.session_state[f"question_{i}"]

            if selected_answer == question.answer:
                st.success("✅ Correct!")
            else:
                st.error("❌ Incorrect!")
                st.write(f"**Correct Answer:** {question.answer}")

            st.info(question.explanation)

        st.divider()

    # ---------------- Submit Button ---------------- #

    if not st.session_state.submitted:

        if st.button("Submit Quiz"):
            st.session_state.submitted = True
            st.rerun()

    # ---------------- Show Score ---------------- #

    if st.session_state.submitted:

        score = 0

        for i, question in enumerate(st.session_state.quiz, start=1):

            selected_answer = st.session_state[f"question_{i}"]

            if selected_answer == question.answer:
                score += 1

        st.success(f"🎉 Your Score: {score}/{len(st.session_state.quiz)}")