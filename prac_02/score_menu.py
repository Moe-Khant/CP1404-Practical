"""Score Menu"""

def main():
    print("(G)et a valid score "
          "\n(P)rint result "
          "\n(S)how stars "
          "\n(Q)uit")
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            mark = get_valid_score("Enter score between 0 and 100: ",0,100)
        elif choice == "S":
            result = determine_score(mark)
        else:
            print("Invalid choice")
        print("(G)et a valid score "
              "\n(P)rint result "
              "\n(S)how stars "
              "\n(Q)uit")
        choice = input(">>> ").upper()


def get_valid_score(prompt, low, high):
    mark = int(input(prompt))
    while mark < low or mark > high:
        print("Invalid input")
        mark = int(input(prompt))
    return mark

main()