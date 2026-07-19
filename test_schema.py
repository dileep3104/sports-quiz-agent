from src.schema import QuizQuestion

q = QuizQuestion(
    question="Who won the 1983 World Cup?",
    options=["India", "Australia", "England", "Pakistan"],
    answer="India",
    explanation="India defeated West Indies."
)

print(q)