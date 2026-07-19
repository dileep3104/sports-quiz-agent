def build_prompt(sport, difficulty, historical_facts, live_news):
    """
    Builds the prompt for Gemini.
    """

    historical_text = "\n".join(historical_facts)

    prompt = f"""
You are an expert sports quiz generator.

Generate exactly 5 multiple-choice questions.

Sport: {sport}
Difficulty: {difficulty}

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
- At least 3 questions should come from historical facts.
- At least 2 questions should come from recent sports news.
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