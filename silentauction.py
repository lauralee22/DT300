#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gouldenl
#
# Created:     30/08/2016
# Copyright:   (c) gouldenl 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

def get_reserve():
#Collects reserve price
    print ("Collecting Reserve")
    global reserve
    reserve = 0
    reserve = (read_int("What is the reserve price?"))

def get_bid(name, names, bid, bids):
#Collects order information - name, amount of bid in a loop
    print ("Auction has started")
    highestbid = 0
    print ("The highest bid so far is $" + str(highestbid))
    name = ""
    while name.upper() != 'F':
        name = input("What is the your name? (\"F\" to finish)")
        if name.upper()!= "F":
            bid = (read_int("What is your bid, " + name + " ?"))
            if bid > highestbid:
                global highestbid
                global highestbidder
                highestbid = bid
                highestbidder = name
                names.append(name)
                bids.append(bid)
            else:
                print("Sorry, " + name + ", you will need to make another, higher bid.")
            print ("The highest bid so far is $" + str(highestbid))

def show_bids(reserve, names, bid, bids, highestbid, highestbidder):
    #displays summary - total bids, highest bid, average bid per customer
    if len(names) == 0:
        print ("No bids")
    else:
        total = 0
        print ("Summary")
        print ("The reserve price was $" + str(reserve))
        for i in range(len(bids)):
            total += bids[i]
            print("{} bid {}.".format(names[i], bids[i]))
            average = 0
        if len(bids) > 0:
            average = total / len(bids)
        print ("Average bid per customer: {0:.1f}".format(average))
        if highestbid >= reserve:
            print("Auction won by " + highestbidder + " with a bid of $" + str(highestbid))
        else:
            print("Auction did not meet reserve price")


def read_int(prompt):
    choice = -1;
    while choice == -1:
        try:
            choice = int(input(prompt))
        except ValueError:
            print ("Not a valid integer")
    return choice

#main routine
reserve = 0
names = []
name = ""
bid = 0
bids = []
highestbid = 0
highestbidder = ""
get_reserve()
get_bid(name, names, bid, bids)
show_bids(reserve, names, bid, bids, highestbid, highestbidder)