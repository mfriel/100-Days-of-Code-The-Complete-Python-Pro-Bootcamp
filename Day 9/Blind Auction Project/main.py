#get logo art
from art import logo
print(logo)

def get_max_bid(bidding_dictionary):
    for bidder in bidding_dictionary:
        winner = ""
        highest_bid = 0
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
#or use the max function
#print(max(bids)) #prints key of max value

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
bids = {}
other_bidders = True
while other_bidders:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: €"))
    bids[name] = price
    any_other_bidders = input("Are there any other bidders? Type Yes or No: ").lower()
    if any_other_bidders == "no":
        other_bidders = False
        get_max_bid(bids)
    else:
        print("\n" * 20)

# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary method 3 https://www.geeksforgeeks.org/python-keys-with-maximum-value/




