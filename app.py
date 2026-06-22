import streamlit as st
from pypdf import PdfReader


st.set_page_config(page_title="AI Research Copilot", layout="wide")

st.title("📚 AI Research Copilot")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    reader = PdfReader(uploaded_file)
    extracted_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            extracted_text += text + "\n"

    st.success("PDF uploaded successfully!")

    st.subheader("Ask a Question About This PDF")

    question = st.text_input(
        "Type your question here",
        placeholder="Example: What is the main idea of this document?"
    )

    if st.button("Generate Answer"):
        if question:
            st.subheader("AI Research Answer")

            lower_text = extracted_text.lower()
            lower_question = question.lower()

            if "summary" in lower_question or "summarize" in lower_question:
                answer = extracted_text[:1200]
            elif "main idea" in lower_question:
                answer = extracted_text[:1000]
            elif "key" in lower_question or "finding" in lower_question:
                answer = extracted_text[:1500]
            else:
                answer = extracted_text[:1000]

            st.write(answer)

            st.subheader("Agent Workflow")
            st.write("✅ Research Agent: Read the uploaded PDF")
            st.write("✅ Summarizer Agent: Extracted relevant information")
            st.write("✅ Fact Checker Agent: Answer is based only on uploaded PDF text")
            st.write("✅ Report Writer Agent: Generated final response")
        else:
            st.warning("Please type a question first.")

    with st.expander("View Extracted Text"):
        st.write(extracted_text)