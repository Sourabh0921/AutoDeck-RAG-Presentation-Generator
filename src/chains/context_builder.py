class ContextBuilder:

    def build_context(
        self,
        retrieved_docs
    ):

        return "\n\n".join(
            doc.page_content
            for doc in retrieved_docs
        )