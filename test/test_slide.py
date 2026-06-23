import sys
import os

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.append(project_root)

from src.retrieval.retriever import Retriever
from src.chains.context_builder import ContextBuilder
from src.chains.slide_chain import SlideChain

topic = "Science Assessment"

retriever = Retriever()

docs = retriever.search(
    topic,
    k=5
)

context_builder = ContextBuilder()

context = (
    context_builder.build_context(
        docs
    )
)

source = (
    docs[0]
    .metadata["doc_id"]
)

slide_chain = SlideChain()

slide = (
    slide_chain.generate_slide(
        topic=topic,
        slide_title="Assessment Timeline",
        context=context,
        source=source
    )
)

print(slide)