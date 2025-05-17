
def get_num_words(input_string):
    word_list = input_string.split()
    return (len(word_list))

def get_num_characters(input_string):

    text = input_string.lower()
    count_dict = {}

    for char in text:
        if(char in count_dict):
            count_dict[char] +=  1
        else:
            count_dict[char] = 1
        
    return count_dict
def sort_on_num(dict):
    return dict["num"]
def get_sorted_dict_list(input_dict):
    dict_list = []
    for value in input_dict:
        if value.isalpha():
            num = input_dict[value]
            temp_dict = {"char":value,"num":num}
            dict_list.append(temp_dict)
    dict_list.sort(reverse=True, key=sort_on_num)
    return dict_list
        