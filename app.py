import streamlit as st

from src.rag_pipeline import ask


# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="Enterprise Basel III RAG",
    page_icon="🏦",
    layout="wide"
)


# ----------------------------------------------------
# Custom CSS
# ----------------------------------------------------

st.markdown("""
<style>

.main{
    background-color:#F7F9FC;
}

.title{
    text-align:center;
    color:#003366;
    font-size:42px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:gray;
    font-size:18px;
}

.answer{
    background:#EAF4FF;
    padding:18px;
    border-radius:10px;
    border-left:8px solid #0066CC;
}

.sources{
    background:#F3F6FA;
    padding:15px;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)


# ----------------------------------------------------
# Header
# ----------------------------------------------------

st.markdown(
    "<div class='title'>🏦 Enterprise Basel III RAG Assistant</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Ask questions from the Basel III Regulatory Framework</div>",
    unsafe_allow_html=True
)

st.divider()

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

with st.sidebar:

    st.header("📘 About")

    st.write(
        """
        **Enterprise Basel III RAG**

        Retrieval-Augmented Generation chatbot built using

        - LangChain
        - FAISS
        - Sentence Transformers
        - Groq Llama 3
        - Streamlit
        """
    )

    st.divider()

    st.markdown("### Technologies")

    st.success("✓ Semantic Search")
    st.success("✓ Vector Database")
    st.success("✓ Prompt Engineering")
    st.success("✓ Source Attribution")


# ----------------------------------------------------
# Input
# ----------------------------------------------------

query = st.text_area(
    "Enter your question",
    placeholder="Example: What is Common Equity Tier 1?"
)

# ----------------------------------------------------
# Button
# ----------------------------------------------------

if st.button("🚀 Generate Answer", use_container_width=True):

    if query.strip() == "":

        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching Basel III documents..."):

            result = ask(query)

        st.markdown("## 📖 Answer")

        st.markdown(
            f"""
            <div class="answer">
            {result['answer']}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        st.markdown("## 📑 Source Pages")

        st.markdown(
            f"""
            <div class="sources">
            {", ".join(map(str, result["sources"]))}
            </div>
            """,
            unsafe_allow_html=True
        )

st.divider()

st.caption(
    "Enterprise Basel III RAG | Built using LangChain, FAISS, Sentence Transformers, Groq & Streamlit"
)