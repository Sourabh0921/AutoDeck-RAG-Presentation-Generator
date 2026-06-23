import json
import os


class JSONSaver:

    @staticmethod
    def save(
        data,
        file_name
    ):

        os.makedirs(
            "outputs/json_outputs",
            exist_ok=True
        )

        path = (
            f"outputs/json_outputs/{file_name}.json"
        )

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(
            f"Saved: {path}"
        )