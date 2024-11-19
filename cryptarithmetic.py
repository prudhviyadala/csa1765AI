from itertools import permutations
def is_valid_mapping(mapping, word):
    return int("".join(str(mapping[letter]) for letter in word))
def solve_cryptarithmetic(words, result):
    unique_chars = set("".join(words) + result)
    if len(unique_chars) > 10:
        print("Too many unique characters for digits!")
        return None
    for perm in permutations(range(10), len(unique_chars)):
        mapping = dict(zip(unique_chars, perm))
        if any(mapping[word[0]] == 0 for word in words + [result]):
            continue
        word_sum = sum(is_valid_mapping(mapping, word) for word in words)
        if word_sum == is_valid_mapping(mapping, result):
            return mapping
    return None
words = ["SEND", "MORE"]
result = "MONEY"
solution = solve_cryptarithmetic(words, result)
if solution:
    print("Solution found:")
    for letter, digit in solution.items():
        print(f"{letter} -> {digit}")
else:
    print("No solution exists.")

