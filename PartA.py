import re
import sys


# O(n) where n is the number of characters in the text file
def tokenize(filepath):
    tokens = set()
    with open(filepath, 'r') as f:
        text = f.read()
        text = text.lower()
        tokens = re.findall(r'\b\w+\b', text)
    return tokens


# O(n) where n is the number of tokens
def computeWordFrequencies(tokens):
    cmap = {}
    for word in tokens:
        if word in cmap:
            cmap[word] = cmap[word] + 1
        else:
            cmap[word] = 1
    return cmap


# O(n log n) where n is the number of tokens in the list
def printWordFrequencies(word_freq):
    for word, count in sorted(word_freq.items(), key=lambda item: (-item[1], item[0])):
        print(f'{word} = {count}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("One text file needed")
    else:
        filepath = sys.argv[1]
        tokens = tokenize(filepath)
        word_freq = computeWordFrequencies(tokens)
        printWordFrequencies(word_freq)
