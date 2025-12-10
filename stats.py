def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    count_hash_st={}
    for char in text:
        if char.lower() not in count_hash_st:
            count_hash_st[char.lower()] = 1
        else : count_hash_st[char.lower()] += 1
    return count_hash_st

def sort_on(item):
    return item["num"]

def sorted_char_count(char_count):
    list_char_count = []
    for char in char_count:
        temp = {}
        temp["char"] = char
        temp["num"] = char_count[char]
        list_char_count.append(temp)
    list_char_count.sort(reverse=True, key=sort_on)
    return list_char_count

