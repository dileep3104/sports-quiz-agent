from google import genai
from google.genai import types
from src.prompts import build_prompt
from src.config import GEMINI_API_KEY, MODEL_NAME
from src.database import query_database
from src.search import get_live_news
import json
from src.schema import QuizQuestion
client = genai.Client(api_key=GEMINI_API_KEY)

def generate_quiz(sport, difficulty):

    historical_facts = query_database(
        sport=sport,
        query_text=f"{sport} history",
        n_results=3
    )

    live_news = get_live_news(sport)

    prompt = build_prompt(
        sport,
        difficulty,
        historical_facts,
        live_news
    )

    response = client.models.generate_content(
    model=MODEL_NAME,
    contents=prompt,
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=list[QuizQuestion],
    ),
)
    '''
    quiz = json.loads(response.text)
    return quiz
    '''

    return response.parsed
