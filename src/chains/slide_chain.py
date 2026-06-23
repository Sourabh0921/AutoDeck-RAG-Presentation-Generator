import os
import json

from dotenv import load_dotenv
from groq import Groq

load_dotenv()


class SlideChain:

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv(
                "GROQ_API_KEY"
            )
        )

    def generate_slide(
        self,
        topic,
        slide_title,
        context,
        source
    ):

        prompt = f"""
You are an expert presentation creator.

Using ONLY the provided context.

Generate content for ONE presentation slide.

Rules:

1. Create concise presentation bullets.
2. Maximum 5 bullets.
3. Each bullet should be short and informative.
4. Do not hallucinate.
5. Use only provided context.
6. Return ONLY valid JSON.

Topic:
{topic}

Slide Title:
{slide_title}

Context:
{context}

Output Format:

{{
    "title":"{slide_title}",
    "bullets":[
        "bullet 1",
        "bullet 2",
        "bullet 3",
        "bullet 4"
    ],
    "source":"{source}"
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

        response = (
            response
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        try:

            return json.loads(
                response
            )

        except Exception:

            print(
                "Slide JSON Parsing Failed"
            )

            print(response)

            return {
                "title": slide_title,
                "bullets": [
                    "Content generation failed"
                ],
                "source": source
            }