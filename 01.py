import os
import random
import time
import json


def clear():
    os.system("cls")


def writing(data):
    with open("high_scores.json", "w") as file:
        json.dump(data, file, indent=4)


def load():
    with open("high_scores.json", "r") as file:
        data = json.load(file)
    return data


def play():
    score = 0
    while True:
        num = random.randint(0, 9999)
        clear()
        print(f"Remember this number: {num}")
        time.sleep(2)
        clear()
        start = time.time()
        imp = int(input("Please enter the number: "))
        resptime = time.time() - start
        score += int(100/resptime)
        if imp != num:
            break
    clear()
    return score


def main():
    print("Welcome to my memory guessing game!")
    time.sleep(2)
    name = input("Please enter your name: ").strip()
    data = load()
    for i in range(len(data)):
        print(f"{data[i]["name"]} : {data[i]["score"]}")
        time.sleep(1)
    cont = input("Would you like to continue?: ").strip().lower()
    if cont != "q":
        score = play()
        for e in range(5):
            if score > data[e]["score"]:
                data.insert(e, {"name": name, "score": score})
                data.pop()
                break
        data.sort(key=lambda data: data["score"], reverse=True)
        writing(data)
        for i in range(len(data)):
            print(f"{data[i]["name"]} : {data[i]["score"]}")
            time.sleep(1)
    return cont


if __name__ == "__main__":
    yesno = "gfghcjcghcjhcj"
    while not yesno in "no":
        cont = main()
        if cont != "q":
            yesno = input("Would you like to play again? ").strip().lower()
