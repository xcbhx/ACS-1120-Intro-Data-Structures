import random
from dictogram import Dictogram

# We want to generate a random sentence based on word patterns found in a given text file. 
# This is done using a Markov Chain, which models how words transition from one to another.
class MarkovChain(dict):
  """A class that represents an first-order Markov Chain for text generation."""
  MARKOV_END_TOKEN = 'MARKOVEND'
  DEFAULT_WALK_DISTANCE = 8

  def __init__(self, book, order=1):
    self.windows = [] # Stores the sliding window sequences
    
    # Loop through the words in the book, stopping at 'len(book) - order'
    for word_index in range(len(book) - order):
      # Create a tuple containing 'order' words (key in dictionary)
      window = tuple(book[word_index : word_index + order])
      self.windows.append(window) # Store the window

      # Grab the next word following this window
      next_word = book[word_index + order]

      # If window already exists in the dictionary, add the next_word to the count
      if window in self:
        self[window].add_count(next_word)
      else:
        # Otherwise, create a new Dictogram instance,
        # and initialize it with the next_word
        self[window] = Dictogram([next_word])

  def walk(self, distance=DEFAULT_WALK_DISTANCE):
    """Walk the Markov Chain instance to generate a new sentence."""
    if not self.windows:
      return ""
    
    window = random.choice(self.windows) # Pick a random starting window
    words = list(window) # Start the sentence with the initial words

    for _ in range(distance - len(window)): # Generate remaining words
      if window not in self: # Stop if the sequence isn't in the chain
        break
      next_word = self[window].sample() # Choose the next word based on frequency
      if next_word == self.MARKOV_END_TOKEN:
        break
      words.append(next_word) # Add the word to the sentence
      window = tuple(words[-len(window):]) # Update the window

    return " ".join(words) # Return the generated sentence as a string
  
def read_file(source_text):
  """Read a text file, remove punctuation, and convert it into a list of words."""
  import re

  with open(source_text, "r", encoding="utf-8") as file:
    text = file.read().lower() # Convert text to lowercase
    book_text = re.sub(r'[^\w\s]', '', text) # Removes punctuation
    words = book_text.split() # Split into a list of words

  return words
  

if __name__ == '__main__':
  import pprint

  # Read the text file and process it into words
  book = read_file("Code/histogram_book.txt")

  # Create the Markov Chain with an order of 2 
  markov = MarkovChain(book=book, order=2)

  # Print the Markov Chain dictionary
  print("MARKOV CHAIN: ")
  pprint.pprint(markov, indent=4)

  # Generate a sentence using the Markov Chain
  print("=" * 120)
  print(f"Random Walk: {markov.walk(10)}.")
