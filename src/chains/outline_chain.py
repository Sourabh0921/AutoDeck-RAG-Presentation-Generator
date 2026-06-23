import os
import json

from dotenv import load_dotenv
from groq import Groq

load_dotenv()


class OutlineChain:

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv(
                "GROQ_API_KEY"
            )
        )

    def generate_outline(
        self,
        topic,
        context
    ):

        prompt = f"""
You are an expert presentation designer.

Using ONLY the provided context.

Create a professional presentation outline.

Rules:

1. Generate between 5 and 8 slides.
2. Slide titles must be concise.
3. Cover the topic completely.
4. Do not hallucinate.
5. Return ONLY valid JSON.

Context:
{context}

Topic:
{topic}

Output Format:

{{
  "slides": [
    "Introduction",
    "Overview",
    "Applications",
    "Benefits",
    "Challenges",
    "Future Trends",
    "Conclusion"
  ]
}}
"""

        completion = (
            self.client.chat.completions.create(
                # model="openai/gpt-oss-120b",
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.2
            )
        )

        response = (
            completion
            .choices[0]
            .message
            .content
        )

        try:

            return json.loads(
                response
            )

        except Exception:

            print(
                "JSON Parsing Failed"
            )

            print(response)

            return {
                "slides": [
                    "Introduction",
                    "Overview",
                    "Applications",
                    "Benefits",
                    "Challenges",
                    "Conclusion"
                ]
            }