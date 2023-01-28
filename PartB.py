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
                if token.isalnum():
                    tokens.add(token)
    return tokens

def common_tokens(file1, file2):
    tokens1 = tokenize(file1)
    tokens2 = tokenize(file2)
    common = tokens1.intersection(tokens2)
    return len(common)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Two text files needed")
    else:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        num_common = common_tokens(file1, file2)
        print(num_common)
