#for analytic functions
def count_words(text):
    return len(text.split())
def character_count(text):
    char_dict = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char.isalnum():  # Only consider alphanumeric characters
            if lowercase_char in char_dict:
                char_dict[lowercase_char] += 1
            else:
                char_dict[lowercase_char] = 1
    return char_dict  
def sort_char(char_dict):
    sorted_items = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    dict_list = [{"char": item[0], "count": item[1]} for item in sorted_items]
    return dict_list
