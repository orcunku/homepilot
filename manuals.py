import sqlite3

import database
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def setup_manuals():
    conn = sqlite3.connect(database.DB_FILE)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS manuals (
            id TEXT PRIMARY KEY,
            text TEXT
        )
    """)
    conn.commit()
    conn.close()


def add_manual_text(doc_id, text):
    conn = sqlite3.connect(database.DB_FILE)
    conn.execute(
        "INSERT OR REPLACE INTO manuals (id, text) VALUES (?, ?)",
        (doc_id, text),
    )
    conn.commit()
    conn.close()


def _all_texts():
    conn = sqlite3.connect(database.DB_FILE)
    rows = conn.execute("SELECT text FROM manuals").fetchall()
    conn.close()
    return [row[0] for row in rows]


def search_manuals(question, n_results=2):
    texts = _all_texts()
    if not texts:
        return []

    vectorizer = TfidfVectorizer(stop_words="english")
    doc_vectors = vectorizer.fit_transform(texts)
    question_vector = vectorizer.transform([question])

    scores = cosine_similarity(question_vector, doc_vectors)[0]

    ranked = sorted(zip(scores, texts), reverse=True)
    return [text for score, text in ranked[:n_results] if score > 0]


if __name__ == "__main__":
    setup_manuals()

    add_manual_text("doc1", "To descale the coffee machine, run a vinegar and water solution through it once a month.")
    add_manual_text("doc2", "Rinse the water filter under running water monthly to keep it clean.")
    add_manual_text("doc3", "The appliance warranty lasts two years from the date of purchase.")
    add_manual_text("doc4", "To set the clock, hold the display button for three seconds until it blinks.")

    print("Stored", len(_all_texts()), "manual chunks\n")

    question = "How do I descale the coffee machine?"
    print("Question:", question)
    print("\nBest matches:")
    for doc in search_manuals(question):
        print(" -", doc)