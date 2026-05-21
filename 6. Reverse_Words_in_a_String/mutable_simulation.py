def clean_up(s) -> list:
    converted_list = list(s)
    print(converted_list) #print for checking current state
    write = 0
    for read in range(len(converted_list)):
        #print(converted_list[read])
        if converted_list[read] != " ":
            converted_list[write] = converted_list[read]
            write +=1
        elif write > 0 and converted_list[write-1] != " ":
            converted_list[write] = converted_list[read]
            write +=1

    print(converted_list[:write])
    print(converted_list[write-1])
    print("test") # test print to visualize the blank space

    if write > 0 and converted_list[write - 1] == " ":
        print(converted_list[:write-1])
        write -= 1

    return converted_list[:write]

def reverse_list(l, left = 0, right = None):
    if right is None:
        right = len(l)-1

    while left < right:
        temp = l[left]
        l[left] = l[right]
        l[right] = temp
        left += 1
        right -= 1
    return l

def reverse_each_word(l):
    i = 0
    word_start_index = 0
    word_end_index = 0
    while i < len(l):
        if l[i] == " ":
            word_end_index = i-1
            reverse_list(l, word_start_index, word_end_index)
            word_start_index = i+1
        i += 1
    reverse_list(l, word_start_index, len(l)-1)
    return l



def mutable_simulation(s):
    cleaned_up_list = clean_up(s)
    reversed_list = reverse_list(cleaned_up_list)
    print(reversed_list) # test print to see the reversed list
    result_list = reverse_each_word(reversed_list)
    print(result_list)
    return "".join(result_list)


print(mutable_simulation(" and good  example "))