📝 Customer Review Sentiment Analyzer

This project is a Streamlit web application that uses a Transformer model (DistilBERT) from Hugging Face to analyze customer reviews and determine whether they express a Positive or Negative sentiment.

It allows users to analyze a single review or perform batch sentiment analysis on multiple reviews at once.

🚀 Features

✅ Single Review Analysis – Enter one review and instantly see the sentiment result.
✅ Batch Review Analysis – Paste multiple reviews (one per line) and get results for all.
✅ Transformer Model (DistilBERT) – Uses Hugging Face’s pre-trained model for high accuracy.
✅ Interactive Web Interface – Built with Streamlit for simplicity and usability.
✅ Confidence Score – Shows how confident the model is in its prediction.

📂 Project Structure
Customer-Review-Sentiment-Analyzer/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation

🛠️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/bushra-genai/Internship-Task1
cd customer-review-sentiment-analyzer

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate   # For Mac/Linux
venv\Scripts\activate      # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Streamlit App
streamlit run app.py

📦 Requirements

Your requirements.txt should include:

streamlit
torch
transformers

💻 Usage

Open the app in your browser (Streamlit will provide a local URL).

Single Review Analysis:

Enter a review in the text box.

Click Analyze Sentiment.

Get the sentiment result + confidence score.

Batch Review Analysis:

Paste multiple reviews (one per line).

Click Analyze Multiple.

Get results for all reviews.

📊 Example

Input Review:

The product stopped working after just two days, very disappointed.


Output:

Sentiment: NEGATIVE (Confidence: 99.98%)


Input Review:

Great value for money, I will definitely buy again.


Output:

Sentiment: POSITIVE (Confidence: 99.98%)


📜 License

This project is licensed under the MIT License – feel free to use and modify it.

✨ Developed with Bushra Mubeen
