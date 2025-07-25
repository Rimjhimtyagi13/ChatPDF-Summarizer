import streamlit as st
import tempfile
from utils.pdf_reader import extract_text_from_pdf
from utils.spillter import split_text
from utils.llm_interface import summarize_chunk, ask_question_about_chunk

st.set_page_config(page_title="ChatPDF + Q&A Tool", layout="centered")
st.title("📄 ChatPDF Summarizer + Q&A (Ollama-powered)")

uploaded_file = st.file_uploader("📁 Upload a PDF file", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_pdf_path = tmp_file.name

    st.success("✅ PDF uploaded successfully!")

   # Step: Inside 'Extract & Summarize' button
    if st.button("🔍 Extract & Summarize"):
        with st.spinner("⏳ Processing PDF..."):
            full_text = extract_text_from_pdf(temp_pdf_path)
        chunks = split_text(full_text, max_chunk_size=500, overlap=50)
        st.session_state.chunks = chunks  # 🔄 Store for later use

        # Summarize (optional)
        summaries = []
        for i, chunk in enumerate(chunks):
            st.info(f"Summarizing chunk {i+1}/{len(chunks)}...")
            summary = summarize_chunk(chunk, model="gemma3")
            summaries.append(summary)

        final_summary = "\n\n".join(summaries)
        st.session_state.summary = final_summary  # 🔄 Store summary
        st.success("✅ Summary generated!")

        st.subheader("📝 Summary")
        st.text_area("Generated Summary", value=final_summary, height=300)


    # Q&A section
if "chunks" in st.session_state:
    st.markdown("---")
    st.subheader("❓ Ask Questions About the PDF")
    user_question = st.text_input("Type your question:")

    if user_question:
        with st.spinner("💬 Thinking..."):
            answers = []
            for i, chunk in enumerate(st.session_state.chunks):
                st.write(f"Checking chunk {i+1}/{len(st.session_state.chunks)}...")
                try:
                    answer = ask_question_about_chunk(chunk, user_question, model="gemma3")
                    answers.append(f"Chunk {i+1}:\n{answer}")
                except Exception as e:
                    answers.append(f"Chunk {i+1} failed: {e}")

            final_answer = "\n\n".join(answers)
            st.success("🧠 Answer generated!")
            st.text_area("Answer", value=final_answer, height=300)
else:
    st.info("📄 Please extract & summarize the PDF before asking questions.")

