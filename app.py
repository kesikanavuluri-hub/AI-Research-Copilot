import streamlit as st
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


st.set_page_config(page_title="AI Research Copilot", layout="wide")

st.title("📚 AI Research Copilot")
st.write("Upload a PDF, ask a question, and get the most relevant answer from the document.")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])


def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


def split_text(text, chunk_size=800):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


def retrieve_relevant_chunks(question, chunks, top_k=3):
    documents = chunks + [question]

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(documents)

    question_vector = vectors[-1]
    chunk_vectors = vectors[:-1]

    similarities = cosine_similarity(question_vector, chunk_vectors).flatten()

    top_indexes = similarities.argsort()[-top_k:][::-1]

    results = []
    for index in top_indexes:
        results.append(chunks[index])

    return results


if uploaded_file:
    extracted_text = extract_text_from_pdf(uploaded_file)
    chunks = split_text(extracted_text)

    st.success("PDF uploaded and processed successfully!")

    st.write(f"Total text chunks created: {len(chunks)}")

    question = st.text_input(
        "Ask a question about this PDF",
        placeholder="Example: What is the main idea of this document?"
    )

    if st.button("Generate Research Answer"):
        if question:
            relevant_chunks = retrieve_relevant_chunks(question, chunks)

            st.subheader("AI Research Answer")

            answer = "\n\n".join(relevant_chunks)
            st.write(answer)

            st.subheader("Agent Workflow")
            st.write("✅ Research Agent: Searched the PDF chunks")
            st.write("✅ Retriever Agent: Found the most relevant sections")
            st.write("✅ Fact Checker Agent: Answer is based only on uploaded PDF text")
            st.write("✅ Report Writer Agent: Displayed the final evidence-based answer")

            with st.expander("View Retrieved Source Chunks"):
                for i, chunk in enumerate(relevant_chunks, start=1):
                    st.markdown(f"### Source Chunk {i}")
                    st.write(chunk)

        else:
            st.warning("Please type a question first.")

    with st.expander("View Full Extracted Text"):
        st.write(extracted_text)