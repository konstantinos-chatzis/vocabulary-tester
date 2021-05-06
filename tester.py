from random import shuffle
from os import system

vocabulary = None

# UI
def print_menu():
	print() # Empty Line
	print('===================')
	print('-------Menu--------')
	print('===================')
	print('\nWhat do you want to do?')
	print('\n1 - Select A Vocabulary \n2 - Start Test \n3 - Add A Word To The Vocabulary \n4 - Create A New Vocabulary \n5 - Exit')
	print() # Empty Line

# Select a vocabulary
def select_vocabulary(name):
    global allWords, wordCount, vocabulary

    try:
        vocabulary = name

        allWords = [] # Define the allWords list

        with open(f"vocabularies\\{name}.vcb", 'r', encoding='utf-8') as f: # Open the selected file
            for line in f: # Loop through every line of the file
                splitted = line.split() # Split the words of the line to a list
                type = splitted[0] # Set the type of the word to the type in the line (index[0])
                if type == 'n': # If the word is a noun
                    equalSignIndex = splitted.index('=') # Get the index of the '=' sign on the line
                    itemList = []
                    article = splitted[1] # Set the article to the article in the line (index[1])
                    main_word = splitted[2] # Set the article to the article in the line (index[1])
                    meaning = "" # Avoid Unbound Error
                    for i in range(equalSignIndex + 1, len(splitted)): # Loop throuh every word after the '=' sign
                        itemList.append(str(splitted[i]))
                        meaning = ' '.join(itemList)
                        meaning = meaning.replace(main_word, '')
                        meaning = meaning.lstrip() # Remove whitespace at the beginning

                    word = [article, main_word, meaning] # Define the final word list with the article, main_word part, and the meaning 
                    allWords.append(word) # Add the word to the allWords list
                elif type == 'v': # If the word is a verb
                    equalSignIndex = splitted.index('=') # Get the index of the '=' sign on the line
                    itemList = []

                    meaning = "" # Avoid Unbound Error
                    main_word = "" # Avoid Unbound Error

                    # Word Selection
                    for i in range(1,equalSignIndex): # Loop through every number before the '=' sign index
                        itemList.append(str(splitted[i])) # Append the word of the current index to the list
                        main_word = ' '.join(itemList) # Combine all the words together
                    # Meaning Selection
                    for i in range(equalSignIndex + 1, len(splitted)): # Loop throuh every word after the '=' sign
                        itemList.append(str(splitted[i])) #
                        meaning = ' '.join(itemList)
                        meaning = meaning.replace(main_word, '')
                        meaning = meaning.lstrip() # Remove whitespace at the beginning

                    word = [main_word, meaning] # Define the final word list with the main_word part, and the meaning
                    allWords.append(word) # Add the word to the allWords list
                elif type == 'a': # If the word is an adjective
                    equalSignIndex = splitted.index('=')
                    itemList = []
                    meaning = "" # Avoid Unbound Error
                    main_word = "" # Avoid Unbound Error
                    for i in range(1,equalSignIndex):
                        itemList.append(str(splitted[i]))
                        main_word = ' '.join(itemList)
                    for i in range(equalSignIndex + 1, len(splitted)):
                        itemList.append(str(splitted[i]))
                        meaning = ' '.join(itemList)
                        meaning = meaning.replace(main_word, '')
                        meaning = meaning.lstrip() # Remove whitespace at the beginning

                    word = [main_word, meaning] # Define the final word list with the main_word part, and the meaning
                    allWords.append(word) # Add the word to the allWords list

        # Put all words to a list and count them
        wordCount = 0
        for word in allWords: # Loop through every word in the allWords list
            wordCount += 1
        shuffle(allWords) # Mix up the elements of the list (all the words)
    
    except:
        print() # Empty Line
        print(f"Vocabulary {name} was not found")

# Create a new vocabulary
def create_vocabulary(name):
    # Create the new vocabulary file
    with open(f"vocabularies\\{name}.vcb", "w"):
        pass
    
    #Select the new vocabulary file
    select_vocabulary(name)

def start_test():
    global allWords, wordCount

    # Ask a word from the list
    correctAnswers = [] # Define the user's correct answers 
    incorrectAnswers = [] # Define the user's incorrect answers
    for word in allWords: # Loop through all the words in the list
        answer = input(str(word[-1]) + ': ') # Ask for the word, given the last element for the 'word' list (the meaning)
        if (word[0] == 'der') or (word[0] == 'die') or (word[0] == 'das'): # Check if the word is an noun
            correctAnswer =  f'{word[0]} {word[1]}' # Set the correct answer to the article and the word
            if answer != correctAnswer: # Check if the answer matches the correct answer
                print('FALSE')
                print(f'{word[2]} = {correctAnswer}')
                print() # Empty line
                incorrectAnswers.append(word) # Append the mistaken word to the incorrect answers list
            else:
                print('CORRECT!')
                print() # Empty line
                correctAnswers.append(word) # Append the correct word to the correct answers list
        else: # If the word is not an noun
            correctAnswer = word[0] # Set the correct answer to the word
            if answer != correctAnswer: # Check if the answer matches the correct answer           
                print('FALSE')
                print(f'{word[1]} = {correctAnswer}')
                print() # Empty line
                incorrectAnswers.append(word) # Append the mistaken word to the incorrect answers list
            else:
                print('CORRECT!')
                print() # Empty line
                correctAnswers.append(word) # Append the correct word to the correct answers list
            
    # Calculate result
    percentage = f'{round(len(correctAnswers) / len(allWords) * 100)}%' # Calculate the percentage of the correct answers
    if incorrectAnswers != []: # If the incorrectAnswers list is not empty
        print('---Correction---')
        print() # Empty line

        for incorrectAnswer in incorrectAnswers: # Loop through every incorrect answer in the incorrectAnswers list
            if (incorrectAnswer[0] == 'der') or (incorrectAnswer[0] == 'die') or (incorrectAnswer[0] == 'das'): # If the incorrectAnswer is a noun
                print(f'{incorrectAnswer[2]} = {incorrectAnswer[0]} {incorrectAnswer[1]}') # Print the correction of the noun ('meaning' = 'article' 'word')
                print() # Empty line
            else: # If the incorrectAnswer is not a noun
                print(f'{incorrectAnswer[1]} = {incorrectAnswer[0]}')
                print() # Empty line

        print(f'Score: {percentage}') # Print the score as a percentage
        print() # Empty line

# Manually Add new word to the selected vocabulary
def add_word(word, meaning, wordType):
    global vocabulary

    if vocabulary == None:
        raise WindowsError

    if wordType == 'n': # Check if the word is a noun
        article = input('Article: ')
        with open(f"vocabularies\\{vocabulary}.vcb", "a", encoding="utf-8") as file:
            file.write(f"n {article} {word} = {meaning}\n")
    elif wordType == 'v': # Check if the word is a verb
        with open(f"vocabularies\\{vocabulary}.vcb", "a", encoding="utf-8") as file:
            file.write(f"v {word} = {meaning}\n")
    elif wordType == 'a': # Check if the word is a adjective
        with open(f"vocabularies\\{vocabulary}.vcb", "a", encoding="utf-8") as file:
            file.write(f"a {word} = {meaning}\n")
    else:
        print('Invalid word type')

# Console Menu

def Option_SelectVocabulary():
    system("cls")
    print() # Empty Line
    print('-------------------')
    print(" Select Vocabulary ")
    print('-------------------')
    print() # Empty Line
    select_vocabulary(input('Vocabulary name: '))
    print() # Empty Line
    input("Press the 'Enter' key to continue")
    system("cls")
    print_menu()
    
def Option_StartTest():
    system("cls")
    try:
        start_test()
    except:
        print() # Empty Line
        print("This vocabulary is empty!")
    print() # Empty Line
    input("Press the 'Enter' key to continue")
    system('cls')
    print_menu()

def Option_AddWord():
    system("cls")
    print() # Empty Line
    print('--------------------')
    print("     Add A Word     ")
    print('--------------------')

    # Ask for word info
    word = input('Word: ')
    meaning = input('Meaning: ')
    wordType = input('Type (n, v, a): ')
    try:
        add_word(word, meaning, wordType)
    except:
        print() # Empty Line
        print("No vocabulary selected!")

    print() # Empty line
    input("Press the 'Enter' key to continue")
    system('cls')
    print_menu()

def Option_CreateVocabulary():
    system("cls")
    print('-------------------')
    print(" Create Vocabulary ")
    print('-------------------')

    create_vocabulary(input("Vocabulary Name: "))

    print() # Empty line
    input("Press the 'Enter' key to continue")
    system('cls')
    print_menu()

print_menu()

# Command line
while True:
    command = ''
    command = input("Tester> ")
    if command == '1':
        Option_SelectVocabulary()
    elif command == '2':
        Option_StartTest()
    elif command == '3':
        Option_AddWord()
    elif command == '4':
        Option_CreateVocabulary()
    elif command == "5":
        raise Exception('Program terminated by user operation')
    else:
        system("cls")
        print('Invalid argument')
        print_menu()