import re


class TextCleaner:

    @staticmethod
    def clean_text(text):

        if not text:
            return ""

        # Remove tabs
        text = text.replace("\t", " ")

        # Remove carriage returns
        text = text.replace("\r", " ")

        # Collapse multiple newlines
        text = re.sub(r"\n+", "\n", text)

        # Collapse multiple spaces
        text = re.sub(r"\s+", " ", text)

        # Remove extra whitespace
        text = text.strip()

        return text