def find_name_in_wordlist(wordlist,name):
    count =0
    index_list =[]

    for word in wordlist:
        index = word.find(name)
        if index!= -1:
            count +=1
            index_list.append(index)
        else:
            index_list.append(-1)
    
    return(count,index_list)

words=input("Enter the words: ")
wordlist=list(map(str,words.split()))

name=input("Enter the name to search: ")


result = find_name_in_wordlist(wordlist,name)

print("Result:", result)