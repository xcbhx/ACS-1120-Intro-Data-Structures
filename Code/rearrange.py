import random
import sys

def random_script(words):
    random.shuffle(words)
    return words

if __name__ == "__main__":
    words = sys.argv[1:]
    random_script = random_script(words)
    print(" ".join(random_script))