words = ["cat", "dog", "cat", "bird", "dog", "cat"]
def count_words(words):
    res = {}
    for word in words:
        if word in res:
            res[word] += 1
        else:
            res[word] = 1
    return res
print(count_words(words))
