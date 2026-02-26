def text_analyzer(texts):
    contain = {"length": 0, "words": 0 , "most repeated": []}
    freq = {}
    contain["length"] = len(texts)
    contain["words"] = len(texts.split())
    for word in texts.split():
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1
    contain["most repeated"] = max(freq, key=freq.get)
    return contain

text = input("Enter the text:")
print(text_analyzer(text))

