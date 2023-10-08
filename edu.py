voted = {}
def check_voter(name):
    if (voted.get(name)):
        print("name is identify")
    else:
        voted[name] = True
        print("name is not idenrify")

check_voter("aLEX")
print(voted)