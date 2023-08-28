def find_longest_words(sentence):
    words = sentence.split()
    longest_words = []
    max_length = 0
    
    for word in words:
        word_length = len(word)
        if word_length > max_length:
            max_length = word_length
            longest_words = [word]
        elif word_length == max_length:
            longest_words.append(word)
    
    return longest_words

input_sentence = input("Enter a sentence: ")
longest_words = find_longest_words(input_sentence)

if longest_words:
    print("Longest word(s):")
    for word in longest_words:
        print(word)
else:
    print("No words found in the input sentence.")
