def reverse_each_word_in_string(input_string):
    words = input_string.split(' ')
    reversed_words = [word[::-1] for word in words]
    reversed_string = ' '.join(reversed_words)
    return reversed_string


print(reverse_each_word_in_string('Do u think it is working?'))