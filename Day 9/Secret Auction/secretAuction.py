import art

print(art.logo)

def check_highest_bid(d):
    highest_bid = 0
    bid_key = ''
    for key in d:
        if d[key] > highest_bid:
            highest_bid = d[key]
    return highest_bid, bid_key

secret_auction_dict = {}

while True:
    name = input("What is your name? ")
    bid = eval(input("What is your bid? "))
    secret_auction_dict[name] = bid
    is_other_bidder = input("Are there any other bidder? Type 'yes' or 'no': ")
    if is_other_bidder == "yes":
        continue
    else:
        highest_bid, bid_key = check_highest_bid(secret_auction_dict)
        print(f"The winner is {bid_key} with a bid of ${highest_bid}")
        break