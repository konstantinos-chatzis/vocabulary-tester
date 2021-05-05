import mysql.connector
from random import shuffle
from os import system

# Initialize database
db = mysql.connector.connect(host="localhost", user="root", passwd="2468123")
cur = db.cursor(buffered=True)

# Update database
def SelectDatabase(name):
    global cur, db
    db = mysql.connector.connect(host="localhost", user="root", passwd="2468123", database=name) # Select the database (vocabulary) to use
    cur = db.cursor(buffered=True)

# Create a new database (vocabulary)
def CreateDatabase(name):
    cur.execute(f"CREATE DATABASE {name}")
    cur.execute(f"USE {name}")
    cur.execute("CREATE TABLE nouns (article VARCHAR(3), word VARCHAR(45), meaning VARCHAR(45) )")
    cur.execute("CREATE TABLE verbs (word VARCHAR(45), meaning VARCHAR(45) )")
    cur.execute("CREATE TABLE adjectives (word VARCHAR(45), meaning VARCHAR(45) )")


def StartTest():
    wordTypes = ['adjectives', 'nouns', 'verbs'] # Declare all the available word types

    with open ('C:\\Users\\chatzis\\Desktop\\correction.txt', 'w', encoding="utf-8"): # Erase the 'Mistakes' file 
        pass

    # Put all words to a list and count them
    allWords = []
    wordCount = 0
    for wordType in wordTypes: # Lopp through all word types
        cur.execute("SELECT * FROM " + wordType) # Select all the columns from the 'wordType' table
        for word in cur: # Loop through every word in the cursor output
            allWords.append(list(word)) # Append the word to the list
            wordCount += 1
    shuffle(allWords) # Mix up the elements of the list (all the words)

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
    percentage = f'{int(len(correctAnswers) / len(allWords) * 100)}%' # Calculate the percentage of the correct answers
    if incorrectAnswers != []: # If the incorrectAnswers list is not empty
        print('---Correction---')
        print() # Empty line
        print(f'Score: {percentage}') # Print the score as a percentage
        print() # Empty line
        with open ('C:\\Users\\chatzis\\Desktop\\correction.txt', 'a', encoding="utf-8") as file:
            for incorrectAnswer in incorrectAnswers: # Loop through every incorrect answer in the incorrectAnswers list
                if (incorrectAnswer[0] == 'der') or (incorrectAnswer[0] == 'die') or (incorrectAnswer[0] == 'das'): # If the incorrectAnswer is a noun
                    print(f'{incorrectAnswer[2]} = {incorrectAnswer[0]} {incorrectAnswer[1]}') # Print the correction of the noun ('meaning' = 'article' 'word')
                    print() # Empty line
                    file.write(f'{incorrectAnswer[2]} = {incorrectAnswer[0]} {incorrectAnswer[1]}') # Print the correction to a file
                    file.write("%s\n" % '')
                else: # If the incorrectAnswer is not a noun
                    print(f'{incorrectAnswer[1]} = {incorrectAnswer[0]}')
                    print() # Empty line
                    file.write(f'{incorrectAnswer[1]} = {incorrectAnswer[0]}')# Print the correction to a file
                    file.write("%s\n" % '')

    input("Press the 'Enter' key to continue")
    system('cls')
    PrintMenu()

# Manually Add new word to the vocabulary
def AddNewWords(word, meaning, wordType, article):
    if wordType == 'n': # Check if the word is a noun
        args = (article, word, meaning)
        cur.execute("INSERT INTO nouns VALUES (%s,%s, %s)", args)
    elif wordType == 'v': # Check if the word is a verb
        args = (word, meaning)
        cur.execute("INSERT INTO verbs VALUES (%s,%s)", args)
    elif wordType == 'a': # Check if the word is a adjective
        args = (word, meaning)
        cur.execute("INSERT INTO adjectives VALUES (%s,%s)", args)
    else:
        print('Invalid argument')

    db.commit()

# Automatically Add new word to the vocabulary
def AutoAddNewWords():
    global cur, db

    with open(file, 'r', encoding='utf-8') as f: # Open the selected file
        for line in f: # Loop through every line of the file
            splitted = line.split() # Split the words of the line to a list
            type = splitted[0] # Set the type of the word to the type in the line (index[0])
            if type == 'n': # If the word is a noun
                equalSignIndex = splitted.index('=') # Get the index of the '=' sign on the line
                itemList = []
                article = splitted[1] # Set the article to the article in the line (index[1])
                word = splitted[2] # Set the article to the article in the line (index[1])
                for i in range(equalSignIndex + 1, len(splitted)): # Loop throuh every word after the '=' sign
                    itemList.append(str(splitted[i])) #
                    meaning = ' '.join(itemList)
                    meaning = meaning.replace(word, '')
                    meaning = meaning.lstrip() # Remove whitespace at the beginning
                args = (article, word, meaning)
                cur.execute("INSERT INTO nouns VALUES (%s,%s, %s)", args) # Add the word to the 'nouns' table
            elif type == 'v': # If the word is a verb
                equalSignIndex = splitted.index('=') # Get the index of the '=' sign on the line
                itemList = []
                # Word Selection
                for i in range(1,equalSignIndex): # Loop through every number before the '=' sign index
                    itemList.append(str(splitted[i])) # Append the word of the current index to the list
                    word = ' '.join(itemList) # Combine all the words together
                # Meaning Selection
                for i in range(equalSignIndex + 1, len(splitted)): # Loop throuh every word after the '=' sign
                    itemList.append(str(splitted[i])) #
                    meaning = ' '.join(itemList)
                    meaning = meaning.replace(word, '')
                    meaning = meaning.lstrip() # Remove whitespace at the beginning

                args = (word, meaning)
                cur.execute("INSERT INTO verbs VALUES (%s,%s)", args)
            elif type == 'a': # If the word is an adjective
                equalSignIndex = splitted.index('=')
                itemList = []
                for i in range(1,equalSignIndex):
                    itemList.append(str(splitted[i]))
                    word = ' '.join(itemList)
                for i in range(equalSignIndex + 1, len(splitted)):
                    itemList.append(str(splitted[i]))
                    meaning = ' '.join(itemList)
                    meaning = meaning.replace(word, '')
                    meaning = meaning.lstrip() # Remove whitespace at the beginning

                args = (word, meaning)
                cur.execute("INSERT INTO verbs VALUES (%s,%s)", args)
    db.commit()
