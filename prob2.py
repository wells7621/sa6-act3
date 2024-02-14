words = ["apple", "orange", "banana", "avocado", "coconut"]
animals = ["elephant", "lion", "tiger", "zebra", "cat"]

sort_words = sorted(words, key=lambda x: (len(x), x))

print(sort_words)
