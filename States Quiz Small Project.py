############ Omar Cooper
###States Quiz

def StateQuiz():
    import random
    n = random.randint(10, 100)
    random.seed(n)
    # Define terms
    stateslist = []
    statesdict = {}
    # Open and read file to list
    with open("US_States.txt", "r") as statesfile:
        filecontent = statesfile.readlines()
        for line in filecontent:
            pair = line.split("\t")
            del pair[-1]
            stateslist.append(pair)
    # Convert list to dictionary
    for item in stateslist:
        x = 0
        statesdict.update({(item[x]) : (item[x - 1])})
    # Quiz User
    correct = 0
    incorrect = 0
    quizstates = statesdict.keys()
    quizcapitals = statesdict.values()
    print("Let's test your state capitals! (Enter 'exit' to quit the quiz) ")
    for x in range(0, 50):
        randomstate = random.choice(list(quizstates))
        answer = input(f"What is the capital of {randomstate}? ")
        if answer.lower() == statesdict[randomstate].lower():
            print("That is correct! ")  
            correct += 1
        elif answer.lower() == "exit":
            break
        else:
            print(f"Incorrect! The captial of {randomstate} is {statesdict[randomstate]} ")
            incorrect += 1
    print(f"You got {correct} answers correct and {incorrect} answers incorrect! ")
StateQuiz()

