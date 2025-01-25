import random


def create_random_sentence(filename, num_words):
    """
    Creates a random sentence with a specified number of words from a file.

    Args:
        filename (str): Path to the file containing the words.
        num_words (int): Number of words to include in the sentence.
    
    Returns:
        str: A random sentence with the specified number of words.
    """
    with open(filename, 'r') as f:
        words = f.read().split()
    return ' '.join(random.sample(words, num_words))


if __name__ == '__main__':
    filename = '/usr/share/dict/words'
    num_words = 5
    sentence = create_random_sentence(filename, num_words)
    print(sentence)


    