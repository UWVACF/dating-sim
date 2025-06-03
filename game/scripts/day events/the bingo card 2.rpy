label day_event_the_bingo_card_2:
    scene bg lounge
    n "You walk past the lounge and hear chattering from within. Curious, you take a peek through the doorway."
    n "You see that everyone is holding a sheet."
    if "the_bingo_card_1" in seen_events:
        n "Ah. Bingo again."

    show caffi at appear(x_align = 0.2)
    #show helco at appear(x_align = 0.2)
    show deceased pensive at appear (x_align = 0.5)
    show aikha at appear (x_align = 0.85)
    n "The crowd have spotted you as well. Dr. Aikha waves enthusiastically at you."
    aikha happy "New recruit! You're just in time."
    aikha "I have a presentation to attend, so can you fill in for me for this bingo game?"
    show aikha at disappear
    n "Without waiting for your response, Dr. Aikha places the sheet in your hand before dashing out of the lounge."
    show ryz unique at appear (x_align = 0.8)
    n "The rest stare excitedly at you. Guess you don't have a choice."
    ryz "So, [player_name], I assume you know how to play bingo."
    ryz happy "Just for the sake of clearity, I'll still read you the rules."
    ryz "Firstly, you are not allowed to directly cause something on your bingo card to happen."
    ryz "Secondly, you are not supposed to peek at other's cards."
    ryz "Thirdly-"
    show ryz upset
    caffi "We got it, {i}Dr. Rizz{/i}. Just let us continue the game."
    show ryz neutral
    n "You look down at Dr. Aikha's bingo sheet."
    # bingo cg here onlayer almost top
    n "...You decide not to question how some of these boxes got marked off today."
    # hide bingo cg
    show helco pensive:
        xalign -0.15
    show caffi at disappear
    show ryz at disappear
    show uriel pensive:
        xalign 1.15
    n "You briefly glance around the room. Dr. Helco has placed his sheet publically and openly on the table, and you can't help but take a glimpse of it."
    # show helco bingo sheet cg
    n "..."
    n "Something doesn't feel right about his sheet."
    # hide helco bingo sheet cg
    n "You watch as Dr. Helco erases a random box everytime someone else marks one off on their own sheet."
    n "His empty boxes could almost form a bingo now."
    show caffi happy:
        xalign 0.2
    n "You meet Caffi's eyes and she started laughing hysterically."
    menu:
        n "You feel a little bad for Dr. Helco."
        "Tell Dr. Helco he's playing wrong.":
            jump bingo2_help_helco
        "Don't tell him. It's one less opponent to worry about.":
            jump bingo2_dont_help_helco
        
    label bingo2_help_helco:
        player "Dr. Helco, you are playing wrong."

    label bingo2_dont_help_helco:
        n "You keep your mouth shut."






# caffi, helco, deceased, uriel, ryz
    # player is playing this time- 6 players
    # prize: miku keychain
    # caffi - does not tell helco how to play correctly, decently competitive when closed to winning
    # helco - there for fun, isn't playing the game properly, he marks everything, and erases boxes randomly. doesn't know he could've "won"
    # deceased - very competitive (miku keychain)
    # uriel - extreme lawful competitive
    # ryz - moral competitive (less than uriel)

# short intro dr ryz clearifies the rules (not enforced but anyways)
    # supposingly, not allowed to forcefully make what's on your bingo card happen
    # not supposed to peek at other's card
    # tell the player normal bingo rules

# plot
# player takes over for dr aikha
# player CAN win
# peek at helco's card (he's not really hiding it), see him playing wrong. everyong minus uriel saw helco's card, no one really say anything because 1 less competitor
# caffi sabotages dr. ryz's attempts at ticking boxes off

    # game begins
    # tension, someone else probably initiate something
    # you see helco's card, it is wrong. You see Caffi giggling on the side
        # choice:
            # tell him he's playing wrong +1 -> jump help helco
            # do not tell him  -1 -> jump don't help helco

        # help helco (gain +1 for helco, make sure you can only gain one more +1)
            # deceased finds hampter's wires
            # a wal walk past outside. You look at your winning box (start a fire)
            ## Choice: stick to the rules or cheat by attempting to combust a wal
            # so either stick to the rules (uriel +1), caffi stabotages dr ryz, you win
                # decide not to cheat (don't show the wires to the wal)
                # since you've decided not to cheat, you next winning bet is to make someone leave the room without the door.
                # hm. the only one who can leave this way is dr. ryz. How can you convince him to leave by phasing through the wall, without it being cheating?
                # you noticed someone else who is also looking at dr ryz. It is caffi, who is peeking at dr ryz's biogo sheet. she has a grimlin smile on her face.
                # dr chan walks past outside "what the fuck are you guys doing", ethy screams at caffi
                # caffi downs an entire pot of coffee while laughing at dr ryz
                # dr ryz flipps off caffi, you win

            # you were exposed of cheating and deceased wins (dece +1)
                # attempted to take the wires from deceased to show to the wal to get it to combust
                # deceased calls you out, others agree due to how destructive that could've been (and incident reports to write)
                # spiteful, you grab the miku and run out of the hallway. unfortunately you run into pochi, who takes an interest in your loot. he chomp on your hand and taks it from you.
                # deceased wins as <pochi commits thievery>. Happy with her miku prize

        # don't help helco (Can still gain +1 for 2 more person)
            # everyone is just tense and not doing anything.
            # an hour pass...you break is over. You really should get going.
            # you forfit - ryz gets a point for "someone forfits the game" ryz +1
            ## Choice: + point deceased OR Uriel 
            # deceased pspspspsp at you (or hand you a slip of paper) while you get your coffee, whispers to you to help them win the miku by setting off the anomaly breakout alarm outside. 
            # Choice: help deceased (+1) or don't help deceased and report them (uriel +1)
            # Help deceased:
                # you leave the lounge and set off the alarm. Surely no one saw that, right. 
                # you hear deceased's laughter in the lounge. It seems they've won. Good for them. 
                # you turn around and see Uriel glaring at you from within in the lounge through the doorway. ah.
            # Don't help Uriel: you stick to the rules (uriel +1) and ryz wins <someone gets reported for cheating>
                # report deceased for cheating
                # deceased is pissed at you
                # ryz wins, happy for winning
        

#scoring groups
#Helco, Uriel, Deceased, Ryz
#> + Helco, Uriel -
#> + Uriel, Ryz
#> + Ryz, Deceased
#> + Deceased, Helco -

# if you stick to the rules, +1 for uriel, -1 otherwise
# gets caught cheating, disqualified, deceased wins +1. -1 otherwise cause they really want that keychain
# cheat but don't get caught, you win. 
    # ryz +1 from some choices you make tha help their bingo, -1 otherwise
# +1 with helco if you tell him he's playing wrong



# player's bingo card (5+/24)
        #1 someone does conservative backflip
#2 nobody gets coffee for the entire duration of the game
    #3 a fire starts in the foundation building
#4 someone enters or exits without using the door
        #5 someone gets shot
    #6 someone does a radical backflip
    #7 moon cameo (start a fire!)
#8 ethy screams (possible lie)
    #9 a breakout happen (anomaly, dos not include pochi)
#10 someone gets flip off 
#11 FOR THE WAL
            #12 wayne pickpockets someone
    #13 someone accepts a bribe
#14 someone find Hampter's half eaten stash of wires
#15 speak a foreign language
#16 vaguely threatening statement
    #17 someone obtain external body parts
    #18 day drinking
    #19 brainrot statement
    #20 pochi commits thievery
    #21 canabilism (accidental) 
            #22 canabilism (intentional)
            #23 paul bio hazard
    #24 drug dealing