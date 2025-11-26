import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def dream_to_financial_plan(user_dream):
    prompt = f"""
    Convert the following dream into a basic financial plan.

    User Dream: "{user_dream}"

    Provide:
    1. Key steps required
    2. Rough cost estimate in INR (approx)
    3. 3 timeline options: Aggressive, Normal, Luxury
    4. Suggested monthly savings needed

    Respond in clean JSON format.
    """

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message["content"]
