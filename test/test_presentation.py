import json
import sys
import os

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.append(project_root)
import json
from src.utils.save_json import JSONSaver

from src.chains.presentation_chain import (
    PresentationChain
)

chain = PresentationChain()

presentation = (
    chain.generate_presentation(
        "Science Assessment"
    )
)

JSONSaver.save(
    presentation,
    "science_assessment"
)