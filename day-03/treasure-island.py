print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("Written by Stanislav Fatkhutdinov")

intro = '''\n\n
\tAfter disembarking from your ship, you landed on the clear beach surrounded by the thick impenetrable jungles. 
\tAfter closer investigation of the jungles, your crew was able to find two passageways.
\tThe left clearing looked like it a large beast made it. 
\tSome of your sailors noted claw marks on some of the tree trunks.
\tThe right passageway seems to be human-made and looked after. 
\tThe trail is clearly defined, and foot imprints are easily spotted.\n
'''
# first decision either left or right
first_act = '''
\tFollowing the beast tracks deep into the jungle, you and your crew found an enormous behemoth carcass. 
\tUpon closer investigation, you noticed that a poisoned dart had struck the creature. 
\tLooking around, you found an intricate contraption connected by a complicated system of ropes and pullies. 
\tOne of your crewmates suggests to try and disarm the trap;
\tor you can try your luck going around this area deep into the jungle towards your treasure.\n  
'''
# second decision either disarm or circumvent
second_act = '''
\tOnce the trap was disabled, you continued your journey through the thicket of jungles. 
\tThe passageway became challenging and treacherous, and some of your crew noticed that local preditors are stalking your group. 
\tRight as you heard a loud growl on your left, your group entered a large clearing. 
\tIn the center of the clearing suspended in the air floated a huge diamond the size of a watermelon. 
\tAs you adjust your eyes to see this bright object, you hear screaming and horrible crunching sounds behind you. 
\tThe jungle beasts are taking out your crew one by one.\n
'''
# third decision is to either run, fight, plea
finale = '''
\tYou dropped your saber in front of you and raised your hands. 
\tA humongous black panther slowly emerged from the jungle thicket. 
\tIts yellow eyes were watching your every move. 
\tA beast growled, and you felt your entire body reverberated from the sound. 
\tThe panther walked past you and interposed itself between you and the gem. You didn't dare to move a muscle. 
\tAfter some time staring at each other, you began to slowly back away into the jungle. 
\tThe beast allowed you to flee. 

\tUpon returning to the ship, you realized that the only treasure you found on that island was your spared life. 

Thank you for playing Treasure Island!
'''

game_over = "Sorry, you're dead. \nGame over."
print(intro)
first_decision = (input("Which passage would you like to explore, left or right?\n")).lower()

if first_decision == "left":
    print(first_act)
    second_decision = (input("Do you want to disarm or circumvent the trap?\n")).lower()
    if second_decision == "disarm":
        print(second_act)
        third_decision = input(
            "Do you run towards the gem, fight the beast or attempt to plea with these creatures?\n").lower()
        if third_decision == "run" or third_decision == "fight":
            print("In two leaps the panther gains on you and rips your throat out.")
            print(game_over)
        elif third_decision == "plea":
            print(finale)
    else:
        print("You decided to walk through the uncharted jungles where you were devoured by the beasts.")
        print(game_over)
else:
    print("Just about ten steps in, you've triggered a trap and was shot by a poison dart.")
    print(game_over)
