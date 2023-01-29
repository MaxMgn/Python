with open ('text.txt', 'r') as data:
    words_list = []
    copy_list = []
    for line in data:
        words = line.split(" ")
        words_list += words
        copy_list += words
    print (words_list)
    print (copy_list)    
    for word in copy_list:
        print(word)
        if "abc" in word:
            print(word + " to delete")
            if (words_list.index(word) != 0 and word[-1].isalpha() == False and words_list[words_list.index(word) - 1][-1].isalpha()):
                print(word, 'the condition')
                words_list[words_list.index(word) - 1] += word[-1]
            words_list.pop (words_list.index(word))
print (words_list)
with open ('result.txt', 'w') as data: 
    for word in words_list:
        data.write(" "+word)