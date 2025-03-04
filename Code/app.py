from flask import Flask, render_template
from .markov import MarkovChain, read_file


app = Flask(__name__)

# Load the book and create the Markov Chain
book = read_file("Code/histogram_book.txt")
markov = MarkovChain(book, order=2) # Create the markov chain.

@app.route("/")
def home():
    # Generate a sentence using the Markov Chain's walk method.
    sentence = markov.walk(10).capitalize()
    return render_template("index.html", sentence=sentence)

if __name__ == "__main__":
    app.run(debug=True, port=5001)