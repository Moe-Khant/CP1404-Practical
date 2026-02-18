import random
NUMBERS_IN_LINE = 6

number_of_picks = int(input("How many quick picks? "))

for i in range(number_of_picks):
    picks = [random.randint(1,45) for number in range(6)]
    print(*sorted(picks))
