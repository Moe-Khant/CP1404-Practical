"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def main():
    score = float(input("Enter score: "))
    grade = determine_score(score)
    print(f"User score: {grade}")

    random_score = random.randint(0,100)
    random_grade = determine_score(random_score)
    print(f"Random: {random_score} = {random_grade}")

def determine_score(score):
    """determine score based on input"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()