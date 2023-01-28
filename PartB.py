import sys
import re

def tokenize(file_path):
    """
    Complexity: O(n), where n is the number of characters in the text file.
    """
    tokens = set()
    with open(file_path, 'r') as f:
        for line in f:
            for token in re.findall(r'\b\w+\b', line.lower()):
                tokens.add(token)
    return tokens

def common_tokens(file1, file2):
    """
    Complexity: O(n), where n is the number of characters in the text files combined.
    """
    tokens1 = tokenize(file1)
    tokens2 = tokenize(file2)
    common = tokens1.intersection(tokens2)
    return len(common)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Please provide two text file paths as arguments.")
    else:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        num_common = common_tokens(file1, file2)
        print(num_common)
