# Adkhy_Giga Nov2024 CA-5.py
# Alien name generator - No inputs needed

def getNameLists():
    actorGivenList = ['andrei','harry','yuan','sadiq','zeng']
    actorFamilyList = ['stephens','venables','spield','elbahi','ergan']
    return actorGivenList, actorFamilyList

def getAlienNames(actorGivenList, actorFamilyList):
    alien_names = []
    idx = 0
    while idx < len(actorGivenList):
        alien_names[idx] = actorGivenList[idx].split(0,3) + actorFamilyList[idx].split(3,4)
        idx+=1
        

def main():
    actor_first_names, actor_last_names = getNameLists()
    getAlienNames(actor_first_names, actor_last_names)

main()