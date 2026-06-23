from tika import parser
from pathlib import Path
import json


class PPTDocumentLoader:

    def extract_text(self, file_path):

        parsed = parser.from_file(str(file_path))

        text = parsed.get("content")

        return text if text else ""


    def process_folder(self, folder_path):

        documents = []

        folder = Path(folder_path)

        ppt_files = list(folder.glob("*.ppt"))

        print(f"Found {len(ppt_files)} files")

        for file in ppt_files:

            try:

                text = self.extract_text(file)

                documents.append(
                    {
                        "doc_id": file.name,
                        "content": text
                    }
                )

                print(f"Processed : {file.name}")

            except Exception as e:

                print(f"Error : {file.name}")
                print(e)

        return documents


    def save_documents(
        self,
        documents,
        output_path
    ):

        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                documents,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(f"Saved : {output_path}")