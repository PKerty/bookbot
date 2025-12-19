def count_words(text):
    return len(text.split())

def count_chararacters_apparitions(text):
    characters = {}
    for char in text.lower():
        if char in characters: 
            characters[char] += 1
        else:
            characters[char] = 1

    return characters

def sort_key(items):
    return items["count"]

def sort_dicts(my_dict:dict):
    unsorted = []
    for key in my_dict:
        unsorted.append({"char":key, "count":my_dict[key]})

    unsorted.sort(reverse=True, key=sort_key)
    return unsorted
