import chromadb
from flask import Flask, request, jsonify


# Initialize ChromaDB client
chroma_client = chromadb.PersistentClient(path="./chroma_db")

# Load the existing collection
collection = chroma_client.get_collection(name="courses_collection")

# Initialize Flask app
app = Flask(__name__)

@app.route("/search", methods=["POST"])
def search():
    """Search for similar courses using vector embeddings."""
    query = request.json.get("query")
    
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    # Perform similarity search in the same way you tested it
    results = collection.query(
        query_texts=[query],  # Ensure proper querying format
        n_results=3  # Retrieve top 3 matches
    )

    matched_courses = results.get("documents", [[]])[0]  # Extract matches

    return jsonify({"matches": matched_courses})

if __name__ == "__main__":
    app.run(debug=True)
