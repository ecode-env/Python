# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo
print(logo)

bidders = {}
winner = None

other = True

while other:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid
    yes_or_no = input("Are there any other bidders: Type 'yes' or 'no'")
    print("\n" * 100)
    if yes_or_no == 'no':
        other = False


for key in bidders:
        if bidders[key] > 0:
            winner = key

print(f"The winner is {winner}. with a bid of ${bidders[winner]}")

