import random

# We want to generate a random sentence based on word patterns found in a given text file. 
# This is done using a Markov Chain, which models how words transition from one to another.

def build_markov_chain(words):
  markov_chain = {} # Initialize an empty dictionary to store word transitions
  for i in range(len(words) - 1): # Loop through the words, stopping at the second to last word
    word, next_word = words[i], words[i + 1] # Get the current word and the next word
    if word not in markov_chain: # If the word is not yet in the dictionary 
      markov_chain[word] = {} # Create an empty dictionary for this word
    if next_word not in markov_chain[word]: # If the next_word hasn't been seen before
      markov_chain[word][next_word] = 0 # Initialize its count
    markov_chain[word][next_word] += 1 # Increase the count of how often this transition happens
  return markov_chain # Return the completed dictionary 

def generate_sentence(markov_chain, start_word, length=10):
  word = start_word # We start at start start_word which is "i"
  sentence = [word] # Store word as a list
  for _ in range(length - 1): # Loop through to generate more words
    if word not in markov_chain: # If the current word has no recoreded transitions, stop 
      break 
    next_words = list(markov_chain[word].keys()) # Get possible next words
    weights = list(markov_chain[word].values()) # Get the frequencies 
    word = random.choices(next_words, weights=weights)[0] # Pick a randomly based on frequency 
    sentence.append(word) # Add it to the sentence
  return " ".join(sentence) # Convert list to a string and return it 

with open("Code/histogram_book.txt", "r") as file:
  text = file.read().lower().replace(".", "").split()

# Build Markov Chain
markov_chain = build_markov_chain(text) # Calls build_markov_chain() on the processed text and stores the result.

# Generate a random sentence starting from "i"
random_sentence = generate_sentence(markov_chain, "i", length=10)
print(random_sentence)