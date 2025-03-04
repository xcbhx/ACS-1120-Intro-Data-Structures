from flask import Flask, render_template
from .markov import MarkovChain, read_file
import os


app = Flask(__name__)

# Load the book and create the Markov Chain
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "histogram_book.txt")
book = read_file(file_path)
markov = MarkovChain(book, order=2) # Create the markov chain.

@app.route("/")
def home():
    # Generate a sentence using the Markov Chain's walk method.
    sentence = markov.walk(10).capitalize()
    return render_template("index.html", sentence=sentence)

if __name__ == "__main__":
    app.run(debug=True, port=5001)