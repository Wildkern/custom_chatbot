LangChain Chatbot with Flask & Streamlit

This project is a custom chatbot built using LangChain, ChromaDB, BGE embeddings, Flask, and Streamlit.
It extracts course data, stores embeddings in a vector database (ChromaDB), and provides an API for searching similar courses.
🚀 Features

✅ Scrapes course data from brainlox.com (or uses sample data)
✅ Generates embeddings using BGE-small-en (SentenceTransformer)
✅ Stores embeddings in ChromaDB
✅ Provides a Flask API for searching similar courses
✅ Offers a Streamlit UI for user interaction
📁 Project Structure

#Screenshots
![Screenshot from 2025-02-07 09-06-36](https://github.com/user-attachments/assets/289c1bd2-f3dc-4115-9ac2-f9a3cbc3df73)


📂 langchain-chatbot
│── 📄 data.py            # Prepares embeddings & stores in ChromaDB
│── 📄 flask_api.py       # Flask API for querying courses
│── 📄 streamlit_ui.py    # Streamlit frontend for chatbot
│── 📄 requirements.txt   # Required dependencies
│── 📄 README.md          # Project documentation

🛠 Installation & Setup
1️⃣ Clone the Repository

git clone https://github.com/your-username/langchain-chatbot.git
cd langchain-chatbot

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run Data Processing (Only Once)

python data.py

This script generates embeddings and stores them in ChromaDB.
🚀 Running the Flask API

python flask_api.py

The API will start on http://127.0.0.1:5000/.
🔎 Test the API with cURL

curl -X POST "http://127.0.0.1:5000/search" -H "Content-Type: application/json" -d '{"query": "Learn Python"}'

💻 Running the Streamlit UI

streamlit run streamlit_ui.py

Open http://localhost:8501/ in your browser.
📜 API Endpoints
🔹 Search Courses

    URL: /search
    Method: POST
    Request Body:

{
  "query": "Learn Python"
}

Response Example:

{
  "matches": [
    "Data Science with Python",
    "Machine Learning Basics",
    "Advanced AI Techniques"
  ]
}
