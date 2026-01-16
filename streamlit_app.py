import streamlit as st
import requests

st.set_page_config(page_title="RAG Chat with PDF", page_icon="📄", layout="wide")

st.title("📄 RAG Chat with PDF Assistant")
st.caption("Upload a PDF and ask questions. The system answers only from the document with citations.")

API_URL = "https://rag-chat-with-pdf-fastapi.onrender.com/ask"


pdf_file = st.file_uploader("Upload PDF", type=["pdf"])
question = st.text_input("Ask a question", placeholder="Example: What is this PDF about?")

if st.button("Ask Question"):
    if pdf_file is None:
        st.error("Please upload a PDF first.")
    elif not question.strip():
        st.error("Please enter a question.")
    else:
        with st.spinner("Sending request to FastAPI backend..."):
            files = {"pdf": (pdf_file.name, pdf_file.getvalue(), "application/pdf")}
            data = {"question": question}

            try:
                response = requests.post(API_URL, files=files, data=data, timeout=120)

                if response.status_code != 200:
                    st.error(f"API Error {response.status_code}: {response.text}")
                else:
                    result = response.json()

                    st.subheader("✅ Answer")
                    st.write(result.get("answer", "No answer returned"))

                    st.subheader("📌 Citations")
                    citations = result.get("citations", [])
                    if not citations:
                        st.info("No citations returned.")
                    else:
                        for c in citations:
                            st.markdown(
                                f"- **Chunk {c.get('chunk')}** | **Page {c.get('page')}**: `{c.get('preview')}`"
                            )
            except Exception as e:
                st.error(f"Request failed: {e}")

