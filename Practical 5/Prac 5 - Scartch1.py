def main():
    text = input("Enter string:")
    print(word_count(text))

def word_count(text):
    counts = dict()
    words = text.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

main()




