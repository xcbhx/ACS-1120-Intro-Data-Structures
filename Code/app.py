from flask import Flask
from .histogram import histogram
import random

app = Flask(__name__)

# Initialize the hsitogram once when the server starts
hist = histogram("Code/histogram_book.txt")

def weighted_choice(histogram):
    total = sum(histogram.values())
    random_value = random.uniform(0, total)
    cumulative = 0
    for word, count in histogram.items():
        cumulative += count
        if cumulative >= random_value:
            return word

@app.route("/")
def home():
    # Generate a list of 10 words using weighted_choice.
    words = [weighted_choice(hist) for _ in range(10)]
    sentence = " ".join(words)
    return f"<p>{sentence}.</p>"

if __name__ == "__main__":
    app.run(debug=True, port=5001)