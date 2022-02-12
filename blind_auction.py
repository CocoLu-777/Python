from replit import clear

bids = {}
bid_finished = False

def highest_bidder(bid_record):
  highest_bid = 0
  winner = ""
  for bidder in bid_record:
    bid_amount = bid_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with bid ${highest_bid}.")
  

while not bid_finished:
  name = input("What's your name?\n")
  bid = int(input("What's the bid price? $"))
  bids[name] = bid
  continued_bid = input("Any other users want to bid? Yes or No\n")
  if continued_bid == "no":
    bid_finished = True
    highest_bidder(bids)
  else:
    clear()
