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
from src.retrieval.retriever import Retriever

from src.chains.context_builder import (
    ContextBuilder
)

from src.chains.outline_chain import (
    OutlineChain
)
import time

from src.chains.slide_chain import (
    SlideChain
)
from src.utils.logger import Logger

logger = Logger.setup_logger()

class PresentationChain:

    def __init__(self):

        self.retriever = Retriever()

        self.context_builder = (
            ContextBuilder()
        )

        self.outline_chain = (
            OutlineChain()
        )

        self.slide_chain = (
            SlideChain()
        )

    def generate_presentation(
        self,
        topic
    ):

        start_time = time.time()

        logger.info(
            f"Presentation Topic: {topic}"
        )

        docs = self.retriever.search(
            topic,
            k=10
        )

        logger.info(
            f"Retrieved {len(docs)} documents for topic"
        )

        context = (
            self.context_builder
            .build_context(docs)
        )

        logger.info(
            f"Context Length: {len(context)} characters"
        )

        outline = (
            self.outline_chain
            .generate_outline(
                topic,
                context
            )
        )

        logger.info(
            f"Generated Outline: {outline}"
        )

        slides = []

        source = (
            docs[0]
            .metadata["doc_id"]
        )

        logger.info(
            f"Primary Source: {source}"
        )

        for slide_title in outline["slides"]:

            logger.info(
                f"Generating Slide: {slide_title}"
            )

            slide_docs = self.retriever.search(
                f"{topic} {slide_title}",
                k=5
            )

            logger.info(
                f"Retrieved {len(slide_docs)} chunks for slide"
            )

            slide_context = (
                self.context_builder.build_context(
                    slide_docs
                )
            )

            slide_source = (
                slide_docs[0]
                .metadata["doc_id"]
            )

            slide = self.slide_chain.generate_slide(
                topic=topic,
                slide_title=slide_title,
                context=slide_context,
                source=slide_source
            )

            logger.info(
                f"Generated Slide Successfully: {slide['title']}"
            )

            slides.append(slide)

        end_time = time.time()

        execution_time = round(
            end_time - start_time,
            2
        )

        logger.info(
            f"Presentation Generated Successfully"
        )

        logger.info(
            f"Total Slides: {len(slides)}"
        )

        logger.info(
            f"Execution Time: {execution_time} sec"
        )

        return {
            "slides": slides
        }