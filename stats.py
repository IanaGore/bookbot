def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    for char in text:
        lowerchar = char.lower()
        if lowerchar in characters:
            characters[lowerchar] += 1
        else:
            characters[lowerchar] = 1
    return characters

def sort_on(items):
    return items["num"]

def sort_dictionary(text):
    sorted_list = []
    for key, value in text.items():
        if key.isalpha():
            sorted_list.append({"char" : key, "num" : value})
    return sorted(sorted_list, key=sort_on, reverse=True)




