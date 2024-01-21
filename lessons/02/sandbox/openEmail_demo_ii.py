#!/usr/bin/env python3
""" Demo program"""

mylist =[
    "Bob Bye,bob@big.com",
    "Julie Roth,Jroth@thinktank.com", 
    "John Davis,JDavis@KingOfTheWorld.com",
    "Tylor Swift,tSwift@Swifter.com",
    "The Hulk,greenThumb@gardeningHelp.com",
    "Sherlock Holmes,sHolmes@consultingDetective.com"
        ]

print("\n Opening mylist :{mylist}")
for line in mylist:
    print(f"\t + line : {line}, {type(line)}")
    name, email = line.split(",")
    if name == "John Davis":
        print(f"\t Name found: {email}")
    if "Sherlock" in name:
        print(f"\t Detective's Name found: {email}")
