words = ["cat", "elephant", "dog", "bat", "lion"]
filtered_words = list(filter(lambda x: len(x) > 3, words))
print(filtered_words)