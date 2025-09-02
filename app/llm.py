import os, json,re
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_text(text: str):
    prompt = f"""
    You are an advanced text analysis assistant. Your task is to analyze a block of text and produce:
    1. A clear, concise 1–2 sentence summary (no more than 40 words).
    2. A structured JSON object containing:
       - "title": Extract the title if explicitly present; otherwise infer one (≤10 words).
       - "topics": Identify the 3 most relevant high-level topics.
       - "sentiment": Classify as "positive", "neutral", or "negative".
       - "keywords": Leave as an empty list.

    ### Rules for Summarization
    - Keep it objective and concise.
    - Avoid repetition.
    - Do not include metadata in the summary.
    - Use plain language.

    ### Example Output
    Summary: "OpenAI released a new model that enhances summarization accuracy and reduces latency."

    JSON:
    {{
      "title": "OpenAI Model Release",
      "topics": ["AI", "Text Summarization", "Efficiency"],
      "sentiment": "positive",
      "keywords": []
    }}

    ### Now analyze the following text:
    {text}
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0  
    )
    content = response.choices[0].message.content
    summary_line = content.split("\n", 1)[0].replace("Summary:", "").strip()
    json_part = content.split("JSON:", 1)[-1].strip()
    json_part = re.sub(r"```json|```", "", json_part).strip()
    metadata = json.loads(json_part)
    return summary_line, metadata
