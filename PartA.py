import re
import sys
from collections import Counter

# O(n) where n is the number of characters in the text file
def tokenize(filepath):
    with open(filepath, 'r') as f:
        text = f.read()
        text = text.lower() # convert text to lowercase
        tokens = re.findall(r'\b\w+\b', text) # use regex to find all alphanumeric tokens
    return tokens

# O(n) where n is the number of tokens in the list
def computeWordFrequencies(tokens):
    word_freq = Counter(tokens)
    return word_freq

# O(n log n) where n is the number of tokens in the list
def printWordFrequencies(word_freq):
    for word, count in sorted(word_freq.items(), key=lambda item: (-item[1], item[0])):
        print(f'{word} = {count}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide a filepath as an argument")
    else:
        filepath = sys.argv[1]
        tokens = tokenize(filepath)
        word_freq = computeWordFrequencies(tokens)
        printWordFrequencies(word_freq)
