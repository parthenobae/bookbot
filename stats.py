def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    count_hash_st={}
    for char in text:
        if char.lower() not in count_hash_st:
            count_hash_st[char.lower()] = 1
        else : count_hash_st[char.lower()] += 1
    return count_hash_st
