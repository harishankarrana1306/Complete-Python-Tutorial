#   KBC - Kaun Banega Crorepatti
# 1. Create a program capable of displaying questions to the user like KBC.
# 2. Use list data type to store the questions and their correct answers
# 3. Display the final amount the person is taking home after playing the game.

print("Welcome to KAUN BANEGA CROREPATI with Harishankar Singh\n")

print("The first question is \n")
print("How many players are there in Cricket Team :") 

print("A     13",end="               ")
print("B     14",end="               ")
print()
print("C     11",end="               ")
print("D     10",end="               ")
print()

inp=(input("Whats your answer(Choose as A,B,C,D) :\n"))

match inp:

    case A :
      print("Your answer is Wrong and u have been Disqualified \n")
      print("The correct answer is --     C     (11) \n")
    
    case B :
      print("Your answer is Wrong and u have been Disqualified \n")
      print("The correct answer is --     C     (11) \n")
