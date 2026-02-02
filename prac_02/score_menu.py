"""Score Menu"""

def main():
    print("(G)et a valid score "
          "\n(P)rint result "
          "\n(S)how stars "
          "\n(Q)uit")
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score("Enter score between 0 and 100: ",0,100)
        elif choice == "P":
            result = determine_score(score)
            print(result)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")
        print("(G)et a valid score "
              "\n(P)rint result "
              "\n(S)how stars "
              "\n(Q)uit")
        choice = input(">>> ").upper()


def get_valid_score(prompt, low, high):
    score = int(input(prompt))
    while score < low or score > high:
        print("Invalid input")
        score = int(input(prompt))
    return score

def determine_score(score):
    """determine score based on input"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent" + "\nYou got a prize!"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    print("*" * score)

main()