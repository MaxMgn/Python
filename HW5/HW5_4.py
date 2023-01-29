def archive (initial_file, archived_file):
    data = ""
    with open (initial_file, 'r') as f:    
        for line in f:
            data += line
    f.close()
    archived_data = ""
    i = 0
    # the number of the current symbol in the source data
    count = 1 # repeat counter
    print("data: " + data)
    print("len_data = "+ str(len(data)))
    while True:
        # print("i: " + str(i))
        repeat = False # initially no repeats 
        if data[i] == data[i+1]:
            repeat = True # there are repetitions, because this character is equal to the next one
            count +=1
            print("count = "+ str(count))
        # I've added a condition: count == 9 as I encode the length with only one digit, otherwise it will be impossible to understand if 102 means 10 of '2's or 1 '0' + 2 other characters
        if  count == 9: 
            print("add to string = "+ str(count) + data[i])
            archived_data = archived_data + str(count) + data[i]
            count = 0 # count = 0 as the next 9th in a row symbol has been included in this sequence.
        
        if repeat == False: 
            print("add to string = "+ str(count) + data[i])
            archived_data = archived_data + str(count) + data[i]
            count = 1

        
        i+=1
        if (i > len(data)-2):
            print("add to string = "+ str(count) + data[i])
            archived_data = archived_data + str(count) + data[i]
            break

    with open (archived_file, 'w') as f:
        f.write(archived_data)
    f.close()

def extract (initial_archive, extracted_archive):
    with open (initial_archive, 'r') as a:    
        data = ""
        for line in a:
            data += line
    a.close()
    print(data)
    extracted_data = ""
    for i in range(0, len(data)-1, 2):
        print(int(data[i]) * data[i+1])
        extracted_data += int(data[i]) * data[i+1]
    with open (extracted_archive, 'w') as f:
        f.write(extracted_data)
    f.close()
        
archive('to_be_archived.txt', 'archived.txt')
extract ('archived.txt', 'extracted.txt')