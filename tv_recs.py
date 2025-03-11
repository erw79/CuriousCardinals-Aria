# Asks the question and checks if the answer is valid.

def ask_question(question):

    corect_answer = True
    while corect_answer:
        answer = input(question)
        if answer == "a" or answer == "b" or answer == "c":
            corect_answer = False
      
        else:
            print ("invalid answer")
    return answer 
d = {}
d ["aaa"] = "Nobody Wants This"
d ["aab"] = "Emily in Paris"
d ["aac"] = "Brooklyn Nine Nine"
d ["aba"] = "The White Lotus"
d ["abb"] = "Hacks"
d ["abc"] = "Young Sheldon"
d ["aca"] = "How to Die Alone"
d ["acb"] = "Abbot Elementry"
d ["acc"] = "Modern Family"
d ["baa"] = "The Queens Gambit"
d ["bab"] = "Never Have I Ever"
d ["bac"] = "The Crown"
d ["bba"] = "Big Little Lies"
d ["bbb"] = "Succesion"
d ["bbc"] = "Veep"
d ["bca"] = "Tell Me Lies"
d ["bcb"] = "Only Murders in the Building"
d ["bcc"] = "Blue Bloods"
d ["caa"] = "Squid Game"
d ["cab"] = "Stranger Things"
d ["cac"] = "The Walking Dead"
d ["cba"] = "The Last of Us"
d ["cbb"] = "Wellington Paranormal"
d ["cbc"] = "True Blood"
d ["cca"] = "In the Flesh"
d ["ccb"] = "What We do in the Shadows"
d ["ccc"] = "True Blood"



 #print instructions
print (" Welcome to the TV Show Recomender. I will be asking you three questions based on your responses to the questions I will then pick a TV show best fit for you.")

 #Ask first question about the genre and store the answer  
answer1 = ask_question ("what kind of genre? Answer a(comedy), b(Drama), or c(Horror)")


# Ask second question about the streaming services used and store the answer.
answer2 = ask_question ("Where do you prefer to stream TV? Answer a(Netflix), b(MAX), or c(Hulu)")

#Ask third question about the number of seasons and store the answer.
answer3 = ask_question ("How many seasons? Annswer a(2 or less), b(4), or c(6 or more)")

print (d[answer1 + answer2 + answer3])
