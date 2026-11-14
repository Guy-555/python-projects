import data
import random
import logo

play = True
score = 0
data1 = random.choice(data.data)
data2 = random.choice(data.data)
result = []

def follower(data1, data2, ans):
    if data1["follower_count"] > data2["follower_count"] and ans == 'A':
        return [data2, "Correct"]
    elif data1["follower_count"] < data2["follower_count"] and ans == 'B':
        return [data2, "Correct"]
    else:
        return "Incorrect"

while play:
    if data1 == data2:
        data2 = random.choice(data.data)
    else:
        print(logo.HigherLower)
        if score != 0:
            print(f"You're right! Current score: {score}.")
        print(f"Against A: {data1["name"]}, a {data1["description"]}, from {data1["country"]}.")
        print(logo.vs)
        print(f"Against B: {data2["name"]}, a {data2["description"]}, from {data2["country"]}.")
        ans = input("Who has more followers? Type 'A' or 'B': ").upper()
        result = follower(data1, data2, ans)
        if result[1] == "Correct":
            data1 = result[0]
            score += 1
        else:
            play = False
            print("\n" *20)
            print(logo.HigherLower)
            print(f"Sorry, that's wrong. Final score: {score}.")
