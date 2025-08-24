def count_words(test:str):
    words = test.split()
    return len(words)

def count_letters(text:str)-> dict[str,int]:
    output ={}
    for letter in text.lower():
        if letter in output.keys():
            output[letter] += 1
        else:
            output[letter] = 1

    return output

def statistics(text:str):
    counts = count_letters(text)
    sorted = []
    for key, value in counts.items():
        sorted.append({"char": key, "num": value})
    sorted.sort(key=lambda x: -x["num"])
    return sorted
