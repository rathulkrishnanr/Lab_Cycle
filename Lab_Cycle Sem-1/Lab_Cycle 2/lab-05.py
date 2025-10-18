import pandas as pd

def word_analyzer():

    num_sentences = int(input("Enter a number: "))
    sentences= []

    for i in range(num_sentences):
        sentence=input(f"Sentence {i+1}: ")
        sentences.append(sentence)

    search_word = input("\nEnter the word to search for: ")

    df=pd.DataFrame({"sentence":sentences})

    total_count = 0
    positions_dict = {}

    for idx, sentence in enumerate(sentences):
        sentence_lower = sentence.lower()
        search_word_lower = search_word.lower()

        position = sentence_lower.find(search_word_lower)
        positions_dict[idx] = position

        if position != -1:
            total_count += sentence_lower.count(search_word_lower)
    
    print(f"\nTotal Count: {total_count}")
    print(f"Positions pf sentence: {positions_dict}")
    
    return {
        'total_count': total_count,
        'positions': positions_dict,
        'dataframe': df
    }

word_analyzer()