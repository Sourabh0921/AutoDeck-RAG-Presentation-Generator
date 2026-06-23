import json
import streamlit as st

from src.chains.presentation_chain import (
    PresentationChain
)

# ---------------------------------
# Streamlit Config
# ---------------------------------

st.set_page_config(
    page_title="AutoDeck AI",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------
# Load Chain
# ---------------------------------

@st.cache_resource
def load_chain():

    return PresentationChain()

presentation_chain = load_chain()

# ---------------------------------
# Header
# ---------------------------------

st.title(
    "📊 AutoDeck AI Presentation Generator"
)

st.markdown(
    """
Generate structured presentations using Retrieval-Augmented Generation (RAG),
FAISS Vector Search, and Groq LLM.
"""
)

# ---------------------------------
# User Input
# ---------------------------------

topic = st.text_input(
    "Enter Presentation Topic",
    placeholder="Applications of AI in Healthcare"
)

# ---------------------------------
# Generate Button
# ---------------------------------

if st.button(
    "🚀 Generate Presentation",
    use_container_width=True
):

    if not topic.strip():

        st.warning(
            "Please enter a presentation topic."
        )

    else:

        try:

            with st.spinner(
                "Generating Presentation..."
            ):

                presentation = (
                    presentation_chain
                    .generate_presentation(
                        topic
                    )
                )

                slides = (
                    presentation["slides"]
                )

            st.success(
                "Presentation Generated Successfully!"
            )

            # ---------------------------------
            # Metrics
            # ---------------------------------

            unique_sources = len(
                set(
                    slide["source"]
                    for slide in slides
                )
            )

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Slides Generated",
                    len(slides)
                )

            with col2:

                st.metric(
                    "Sources Used",
                    unique_sources
                )

            st.divider()

            # ---------------------------------
            # Download JSON
            # ---------------------------------

            st.download_button(
                label="📥 Download Presentation JSON",
                data=json.dumps(
                    presentation,
                    indent=4
                ),
                file_name="presentation.json",
                mime="application/json"
            )

            st.divider()

            # ---------------------------------
            # Slides
            # ---------------------------------

            for idx, slide in enumerate(
                slides,
                start=1
            ):

                with st.expander(
                    f"Slide {idx}: {slide['title']}",
                    expanded=(idx == 1)
                ):

                    for bullet in slide[
                        "bullets"
                    ]:

                        st.write(
                            f"• {bullet}"
                        )

                    source_name = (
                        slide["source"]
                        .replace(".ppt", "")
                        .replace(".pptx", "")
                    )

                    st.caption(
                        f"📄 Source Document: {source_name}"
                    )

            st.divider()
        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )
            