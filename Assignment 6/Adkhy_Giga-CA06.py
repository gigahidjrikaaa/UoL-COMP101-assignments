# Adkhy_Giga Nov2024 CA-5.py
# Alien name generator - No inputs needed - Lists actor names - Randomize the letters to create alien names

def getNameLists():
    '''
    Returns two lists of actor names, one for the given names and one for the family names.
    '''
    actorGivenList = ['andrei','harry','yuan','sadiq','zeng']
    actorFamilyList = ['stephens','venables','spield','elbahi','ergan']
    return actorGivenList, actorFamilyList

def getAlienNames(actorGivenList, actorFamilyList):
    '''
    Takes in two lists of actor names and combines them to create alien names.
    The alien names are created by taking the first 3 letters of the family name and the first 2 letters of the given name of each actor.
    '''
    # Initialize list to store alien names
    alien_names = []
    # Loop through the actor names and combine them to create using append method
    for i in range(len(actorGivenList)):
        alien_names.append(actorFamilyList[i][:3] + actorGivenList[i][:2])

    return alien_names

#! Output Enhancement
def getDirectorsName(alien_names):
    '''
    Takes in a list of alien names and returns the director's name. Director name is hidden in the alien names.
    '''
    # Initialize empty string to store director's name
    director_name = ""
    # Loop through the alien names and combine the first 3 letters of each alien name to get the director's name (stevenspielberg)
    for i in range(len(alien_names)):
        director_name += alien_names[i][:3]

    return director_name

def printLine(width=80):
    '''
    Prints a line of width times equal signs.
    '''
    print("=" * width)
    return

def printCentered(text, width=80):
    '''
    Takes in a string and prints it out centered on the screen (relative to width).
    '''
    print(text.center(width, " "))
    return
        
def printCredits(actor_first_names, actor_last_names, alien_names, director_name):
    '''
    Takes in a list of alien names and prints them out in a formatted way.
    '''
    printLine()
    printCentered(director_name)
    printCentered("Presents")
    printLine()
    printCentered("ALIEN")
    printLine()
    printCentered("Starring")
    print("The Cast:\t\t       played the part of: \t\tAlien Name:")
    # Loop through the alien names and print them out in a formatted way
    for i in range(len(alien_names)):
        print(actor_first_names[i], actor_last_names[i], "     \t\t\t\t\t\t" + alien_names[i])

    return

def main():
    actor_first_names, actor_last_names = getNameLists()
    alien_names = getAlienNames(actor_first_names, actor_last_names)
    directors_name = getDirectorsName(alien_names)
    printCredits(actor_first_names, actor_last_names, alien_names, directors_name)

if __name__ == "__main__":
    main()