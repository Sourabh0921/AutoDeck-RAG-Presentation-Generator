import sys
import os

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.append(project_root)

from src.chains.outline_chain import OutlineChain

chain = OutlineChain()

outline = chain.generate_outline(
    topic="Science Assessment",
    context="Science assessment standards, blueprint and timeline..."
)

print(outline)