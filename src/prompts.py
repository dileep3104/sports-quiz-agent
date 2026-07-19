def build_prompt(sport, difficulty, historical_facts, live_news):
    """
    Builds the prompt for Gemini.
    """

    historical_text = "\n".join(historical_facts)
    if difficulty == "Easy":

            difficulty_instruction = """
    - Questions should be simple and suitable for beginners.
    - Focus on famous players, popular teams, basic rules, major tournaments, and well-known records.
    - Avoid obscure historical facts or difficult statistics.
    """

    elif difficulty == "Medium":
        difficulty_instruction = """
    - Questions should require moderate sports knowledge.
    - Include famous matches, player achievements, historical tournaments, rankings, and notable records.
    - Mix straightforward and slightly challenging questions.
    """

    else:  # Hard
        difficulty_instruction = """
    - Questions should be challenging.
    - Focus on rare records, lesser-known players, historical milestones, detailed statistics, and recent developments.
    - Avoid very obvious questions.
    """

    prompt = f"""
You are an expert sports quiz generator.

Generate exactly 5 multiple-choice questions.

Sport: {sport}
Difficulty: {difficulty}

Difficulty Guidelines:
{difficulty_instruction}

Historical Facts:
{historical_text}

Latest News:
{live_news}

IMPORTANT RULES:
- Use ONLY the historical facts and latest sports news provided.
- Do NOT invent facts.
- Do NOT change years, names, statistics, or events.
- Generate exactly 5 questions.
- Each question must have exactly 4 options.
- One correct answer only.
- Include a short explanation for the correct answer.

Question Requirements:
- Questions must be about sports events, players, teams, tournaments, or records.
- Do NOT ask questions about websites, news sources, article titles, or publishers.
- Use the latest news only for cricket events, tournaments, rankings, or announcements—not for the source of the news.
- Exactly 3 questions must be based on the historical facts.
- Exactly 2 questions must be based on the latest sports news.
- make sure the questions are relevant to the sport and difficulty level.
-make sure the questions are not repeated and are unique.
Return ONLY valid JSON.

The JSON format must be:

[
    {{
        "question": "...",
        "options": [
            "...",
            "...",
            "...",
            "..."
        ],
        "answer": "...",
        "explanation": "..."
    }}
]

Do NOT include markdown.
Do NOT wrap the JSON inside ```json.
Return ONLY the JSON array.

"""

    return prompt