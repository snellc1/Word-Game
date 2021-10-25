# Creating player input for word
player_1 = input("Please enter a word: ").lower()
player_2 = input("Please enter a word: ").lower()

#Establishing the scoring for each word
scores = [3, 2, 1, 4, 2, 2, 3, 1, 1, 3, 4, 2, 1, 3, 1, 2, 3, 2, 2, 1, 1, 3, 2, 2, 3, 5]
letters = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Creating variables to store the score for each player
score_1 = 0
score_2 = 0

# Obtaining the score for player 1 and player 2
for score in player_1:
    score_1 +=  scores[letters.index(score)]

for score in player_2:
    score_2 +=  scores[letters.index(score)]

# Determine winner
if score_1 > score_2:
    print("Player 1 wins!")
elif score_1 < score_2:
    print("Player 2 wins!")
else:
    print("Tie!")