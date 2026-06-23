import json
import requests
import streamlit as st

st.set_page_config(
    page_title="AutoDeck AI",
    page_icon="📊",
    layout="wide"
)

st.title(
    "📊 AutoDeck AI Presentation Generator"
)

st.markdown(
    """
Generate structured presentations using
RAG, FAISS, Groq LLM, and PowerPoint knowledge bases.
"""
)

topic = st.text_input(
    "Enter Presentation Topic",
    placeholder="Applications of AI in Healthcare"
)

if st.button(
    "🚀 Generate Presentation",
    use_container_width=True
):

    if not topic.strip():

        st.warning(
            "Please enter a presentation topic."
        )

    else:

        with st.spinner(
            "Generating Presentation..."
        ):

            payload = {
                "topic": topic
            }

            response = requests.post(
                "http://127.0.0.1:8000/api/generate",
                json=payload
            )

            if response.status_code == 200:

                presentation = response.json()

                slides = presentation["slides"]

                st.success(
                    "Presentation Generated Successfully!"
                )

                # -----------------------------
                # Metrics
                # -----------------------------

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

                # -----------------------------
                # Download JSON
                # -----------------------------

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

                # -----------------------------
                # Slides
                # -----------------------------

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

                        st.caption(
                            f"📄 Source Document: {slide['source']}"
                        )

                st.divider()
                

            else:

                st.error(
                    f"API Error: {response.status_code}"
                )