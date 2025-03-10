# This program gets three test scores and displays
# their average. It congratulates the user if the
# average is a high score

# The HIGH_SCORE named constant holds the value that is
# considered a high score.

HIGH_SCORE = 95

# INPUT (Prompt the user to enter their test scores)
test1 = int(input('Enter your score for test 1: '))
test2 = int(input('Enter your score for test 2:'))
test3 = int(input('Enter your score for test3: '))

# PROCESSING (Calculate the average of the test scores)
average_score = (test1 + test2 + test3) / 3
print(f'\nYour average score is {average_score:.1f}')

# If statement for the boolean expression
# using a relational operator
if average_score > + HIGH_SCORE:
    print(f'\nCongratulations! on achieving a high score')
