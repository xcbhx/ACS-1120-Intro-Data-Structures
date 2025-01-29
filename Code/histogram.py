import string

def histogram(filename):
    """Reads a file, processes its text, and returns a dictionary mapping
    each word to its frequency in the file.

    Args: 
        filename (str): The path to the file to be processed.

    Returns:
        dict: A dictionary where keys are words and values are their occurrence counts. 
    """
    with open(filename, 'r') as f:
        text = f.read().lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.split()

        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        return word_freq
    
def unique_words(histogram_dict):
    """Returns the number of unique words ina given histogram dictonary.

    Args:
        histogram_dict (dict): A dictonary mapping words to their frequencies.

    Returns:
        int: The count of unique words in the histogram.
    """
    return len(histogram_dict)

def frequency(histogram_dict, word):
    """Returns the number of times a given word appears in the histogram.

    Args:
        histogram_dict (dict): A dictonary mapping words to their frequencies.
        word (str): The word whose frequency is to be retrieved.

    Returns:
        int: The frequency of the word in the histogram.
    """
    return histogram_dict.get(word, 0)



if __name__ == '__main__':
    filename = 'Code/histogram_book.txt'
    word_histogram = histogram(filename)

    unique_results = unique_words(word_histogram)
    print(f"Total unique words: {unique_results}")

    word_to_count = "drink"
    frequency_result = frequency(word_histogram, word_to_count)
    print(f"The word '{word_to_count}' appears {frequency_result} times in the file.")
