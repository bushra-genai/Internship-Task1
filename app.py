import streamlit as st
import torch
from transformers import pipeline

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(
    page_title="Customer Review Sentiment Analyzer",
    page_icon="📝",
    layout="centered"
)

# ---------------------------
# Custom CSS Theme
# ---------------------------
# ---------------------------
# Custom CSS Theme
# ---------------------------
st.markdown(
    """
    <style>
    body {
        background-color: #0e1117;
        color: #fafafa;
    }
    .stTextArea textarea {
        background-color: #1e2130 !important;
        color: #ffffff !important;
        border-radius: 10px;
    }
    /* Default Buttons (main page) */
    .stButton button {
        background-color: #06402B;
        color: white;
        border-radius: 10px;
        font-weight: bold;
        padding: 0.5em 1em;
        transition: 0.3s;
    }
    .stButton button:hover {
        background-color: #357ABD;
        transform: scale(1.05);
    }
    /* Sidebar Buttons (Clear & Download) */
section[data-testid="stSidebar"] .stButton button {
    background-color: transparent !important;
    color: inherit !important;
    border: 1px solid #444 !important;
    border-radius: 5px !important;
    font-weight: normal !important;
    box-shadow: none !important;
}
section[data-testid="stSidebar"] .stButton button:hover {
    background-color: #222 !important;
    color: white !important;
}
    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------------
# Title & Description (Header Rich Red)
# ---------------------------
st.markdown(
    "<h1 style='color:#B22222; text-align: center;'>📝 Customer Review Sentiment Analyzer</h1>",
    unsafe_allow_html=True
)

st.write(
    "This app uses a **Transformer model (DistilBERT)** from Hugging Face "
    "to analyze the sentiment of customer reviews with high accuracy."
)

# ---------------------------
# Load model only once (Cache)
# ---------------------------
@st.cache_resource
def load_pipeline():
    return pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )

sentiment_pipeline = load_pipeline()

# ---------------------------
# Session state for storing chat history
# ---------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------------------
# User Input
# ---------------------------
st.subheader("Enter a customer review below 👇")
user_review = st.text_area("Review:", placeholder="Type your review here...")

if st.button("🔍 Analyze Sentiment"):
    if user_review.strip():
        with st.spinner("Analyzing sentiment..."):
            result = sentiment_pipeline(user_review)[0]
            label = result["label"]
            score = result["score"]

        # Save to history
        st.session_state.history.append(f"Review: {user_review} → {label} ({score:.2%})")

        # Display Result
        if label == "POSITIVE":
            st.success(f"😊 Positive Review (Confidence: {score:.2%})")
        else:
            st.error(f"😞 Negative Review (Confidence: {score:.2%})")
    else:
        st.warning("⚠️ Please enter a review before analyzing.")

# ---------------------------
# Multiple Reviews Option
# ---------------------------
st.subheader("📋 Batch Analysis (Optional)")
st.write("Paste multiple reviews (one per line):")

multi_reviews = st.text_area("Multiple Reviews:")

if st.button("📊 Analyze Multiple"):
    if multi_reviews.strip():
        reviews_list = [r.strip() for r in multi_reviews.split("\n") if r.strip()]
        with st.spinner("Analyzing multiple reviews..."):
            results = sentiment_pipeline(reviews_list)

        for review, result in zip(reviews_list, results):
            st.session_state.history.append(f"Review: {review} → {result['label']} ({result['score']:.2%})")
            if result['label'] == "POSITIVE":
                st.markdown(f"✅ **Review:** {review}")
                st.markdown(f"😊 Sentiment: **{result['label']}** (Confidence: {result['score']:.2%})")
            else:
                st.markdown(f"❌ **Review:** {review}")
                st.markdown(f"😞 Sentiment: **{result['label']}** (Confidence: {result['score']:.2%})")
            st.markdown("---")
    else:
        st.warning("⚠️ Please enter at least one review for batch analysis.")

# ---------------------------
# Sidebar Options
# ---------------------------
st.sidebar.header("⚙️ Options")


# Clear Chat
if st.sidebar.button("🧹 Clear Chat"):
    st.session_state.history = []
    st.rerun()

# Download Chat
if st.sidebar.button("⬇️ Download Chat"):
    if st.session_state.history:
        chat_text = "\n".join(st.session_state.history)
        st.sidebar.download_button(
            label="Save Chat History",
            data=chat_text,
            file_name="chat_history.txt",
            mime="text/plain"
        )
    else:
        st.sidebar.warning("No chat history to download.")


# ---------------------------
# Main Footer
# ---------------------------
st.markdown(
    """
    <hr style="border:1px solid #ddd;">
    <div style="text-align: center; color: white; font-size: 14px;">
        🚀 Developed by <b>Bushra Mubeen</b>
    </div>
    """, 
    unsafe_allow_html=True
)
