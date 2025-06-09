label day_event_the_bingo_card_2:
    image censor = "images/cgs/censor pixel filter.png" 

    scene bg lounge
    n "You walk past the lounge and hear chattering from within. Curious, you take a peek through the doorway."
    n "You see that everyone is holding a sheet."
    if "the_bingo_card_1" in seen_events:
        n "Ah. Bingo again."

    show caffi at appear(x_align = 0.0)
    #show helco at appear(x_align = 0.2)
    show deceased pensive at appear (x_align = 0.5)
    show aikha at appear (x_align = 1.0)
    n "The crowd have spotted you as well. Dr. Aikha flags you down."
    aikha surprise "Just in time."
    show aikha neutral
    aikha "Got a presentation to attend, mind filling in for me this bingo game?"
    show aikha at disappear
    n "Without waiting for your response, Dr. Aikha places the sheet in your hand before dashing out of the lounge."
    show ryz unique at appear (x_align = 1.0)
    n "The rest stare excitedly at you. Guess you don't have a choice."
    ryz "So, [player_name], I assume you know how to play bingo. The prize this time is a miku keychain."
    ryz happy "Just for the sake of clarity, I'll still read you the special rules."
    ryz "Firstly, you are not allowed to directly cause something on your bingo card to happen."
    ryz "Secondly, you are not supposed to peek at other's cards."
    n "Isn't... Dr. Aikha technically always breaking rule two?"
    ryz "Thirdly-"
    show ryz upset
    caffi "We got it, {i}Dr. Rizz{/i}. Just let us continue the game."
    show ryz neutral
    n "You look down at Dr. Aikha's bingo sheet."
    # bingo cg here onlayer almost top
    n "...You decide not to question how some of these boxes got marked off today."
    # hide bingo cg
    show helco pensive at appear(x_align = 0.5)
    show deceased at disappear
    show caffi at disappear
    show ryz at disappear
    show uriel pensive:
        xzoom -1.0
        appear(x_align = 1.0)
    n "You briefly glance around the room. Dr. Helco has placed his sheet publically and openly on the table, and you can't help but take a glimpse of it."
    hide ryz
    hide caffi
    hide deceased
    # show helco bingo sheet cg
    n "..."
    n "Something doesn't feel right about his sheet."
    # hide helco bingo sheet cg
    n "You watch as Dr. Helco erases a random box everytime someone else marks one off on their own sheet."
    n "His empty boxes could almost form a bingo now."
    show caffi happy at appear(x_align = 0.0)
    n "You meet Caffi's eyes and she starts laughing hysterically."
    menu:
        n "You feel a little bad for Dr. Helco."
        "Tell Dr. Helco he's playing wrong.":
            jump bingo2_help_helco
        "Don't tell him. It's one less opponent to worry about.":
            jump bingo2_dont_help_helco
        
    label bingo2_help_helco:
        player "Dr. Helco, you are playing wrong."
        helco surprise "Hmm?"
        n "He look up and stare right into your soul. Then he look down at your sheet into its soul. If it has one."
        show uriel pensive:
            xzoom -1.0
        n "Seems like nobody really follows rule 2 here."
        n "Except Uriel, who's trying very hard not to look at everyone's undefensed sheets."
        n "Dr. Helco seems to have realized something after blantently reading off your sheet."
        show helco pensive
        n "He proceeds to erase his whole sheet, then checking off the same squares on your grid."
        show helco happy
        n "He gives you a smile of thankfullness. Then returns to staring intensely at you and your bingo sheet."
        n "..Seems like nobody has ever told him the basic rules of bingo."
        show helco happy at disappear
        show uriel pensive at disappear
        show caffi happy at disappear
        n "You look away to avoid his piercing gaze."
        hide helco
        hide uriel
        hide caffi
        n "On the other side, you see Dr. Deceased has stood up from their seat and is now fiddling something by the vent."
        show deceased pensive at appear(x_align = 0.5)
        deceased happy "Aha! Wires left by Hampter."
        n "You see them discreetly shove the wire pieces back into the vent, then look around suspicously to check if anyone has seen what they're doing, as if they didn't just announced their discovery out loud."
        show deceased at disappear
        # show bingo sheet updated 1
        n "Well, that's another step closer to winning. Not too difficult, huh?"
        hide deceased
        n "Let's see...you're almost at bingo! Your next go-tos are...a fire starts, or someone enters/exits without the door."
        n "The first one seems a lot more likely, given the amount of walbots running around the foundation."
        # hide bingo sheet
        show bg room hall
        show firewal at appear
        n "Speaking of which, you see one walking past right outside the lounge." 
        hide firewal
        show bg lounge
        show uriel pensive at appear(x_align = 0.5)
        show deceased pensive at appear(x_align = 0.0)
        show ryz at appear(x_align = 1.0)
        n "You remember the wires that Dr. Deceased found. A devious plan pieces itself together in your head."
        n "Technically...if a wal combusts on its own, it wouldn't count as you \"directly\" causing it, no?"
        n "Plus, nobody is really following the rules anyways."
        ethy "{sc}{size=+3}{b}AAAAA!!!{/b}{/size}{sc}"
        n "Ethy's piercing scream fills your head, acting as the embodiment of your conscience."
        if "ethics presentation" in seen_events:
            n "You think back to Dr. Chan's ethics presentation. Ethics should be applied to all areas of life, not just at work."
            n "And that includes a bingo game."
        else:
            n "Yes, winning is important. But is it really worth cheating?"
            n "Even if others are not following the rules, you don't have to follow their immoral ways."
        n "You can still win this bingo game fair and square. And get bragging rights for it."
        menu:
            n "You hear the walbot's footstep getting further and further. Make your decision now."
            "Don't do it - you should follow the rules.":
                jump bingo2_follow_rules
            "Do it - your competitive spirit urges you to.":
                jump bingo2_cheat

        label bingo2_follow_rules:
            n "You decide to not follow through with your plan. A wal gets to live another day!"
            n "Now then, you can only wait for things to happen so that you can fill your bingo."
            n "A fire seems a bit worse than someone not using the door. You pray for the latter in your head for it to manifest."
            show deceased at move_to(x_align = -0.8)
            show uriel pensive at move_to(x_align = 0.0)
            show ryz at move_to(x_align = 0.5)
            n "The only person capable of leaving the room without the door would be Dr. Ryz, who could phase throgh things. You turn and stare at him."
            hide deceased
            n "It's only a matter of time, right? Sooner or later, he has got to leave for a meeting or something."
            show ryz pensive
            n "Look, he's checking his watch right now."
            show caffi pensive at appear(x_align = 1.0)
            n "You notice someone else also staring at Dr. Ryz. It's Caffi with a devious smile."
            n "You follow her gaze...she's readding his bingo sheet."
            show caffi happy
            n "Caffi stands up, and her smile grows bigger. "
            show uriel pensive:
                xzoom -1.0
            show ryz surprise:
                xzoom -1.0
            n "Caffi hops over to the kitchenette, and promptly grabs the pot of coffee."
            n "She downs it in one giant gulp. Then the room eruptes."
            show uriel upset
            show ryz fury
            show layer master:
                shake(persist=15.0, preset="rumble")
            ethy "{sc}{size=+3}{b}AAAAAAAAAA!!!{/b}{/size}{sc}"
            show layer master
            n "You hear a big sigh amongst everyone. Caffi have sabotaged almost everyone, including you."
            show censor zorder 50: #will prob have to reanimate this once we get permenant sprites
                zoom 0.25
                yalign 0.4
                xalign 0.51
            ryz surprise "THERE WAS ONE MINUTE LEFT. ONE MINUTE!!! CAFFI!!!"
            n "Ohhh wait a minute."
            # show bingo card
            n "Ethy screams...someone get flipped off...You win!!!"
            # hide bingo card
            hide censor
            show ryz unique:
                xzoom 1.0
            show uriel:
                xzoom 1.0
            player "BINGO!!!"
            show ryz unique at disappear
            show uriel at disappear
            show caffi at disappear
            n "You make your way over to the prize and pick it up. The Miku's eyes glitter at you."
            n "See, you can win morally!"
            $ update_character_points({"uriel": 1, "helco": -1})
            return
        
        label bingo2_cheat:
            n "You push back against your conscience. You really want to win this bingo."
            show deceased pensive at disappear 
            show ryz at disappear
            show uriel pensive at disappear
            n "You stand up and walk towards the vents. You pull out the loot from within."
            hide deceased
            hide ryz
            hide uriel
            n "4 pieces of chewed on wires. Perfect."
            show layer master:
                shake(persist=15.0, preset="rumble")
            ethy "{sc}{size=+3}{b}AAAAAAAAAA!!!{/b}{/size}{sc}"
            show layer master
            n "You ignore Ethy. What does he know about bingo anyways?"
            n "You make your way towards the exit with the wires. You have one foot out the door when someone grabs your shoulder."
            show deceased fury at appear
            deceased "[player], you can't do that!"
            player "Do what?"
            deceased "You are going to show the wires to that wal, aren't you? To blow him up!"
            deceased "We can't have you do that, for that breaks the foundation safety code!"
            n "Safety code? Since when have anyone in this room followed the safety code?"
            show ryz at appear(x_align = 0.9)
            show uriel at appear(x_align = 0.1)
            deceased happy "I'm reporting [player_name] for cheating! Who else agrees that they should be disqualified?"
            n "The others nod. Dr. Deceased rips apart your bingo sheet."
            ryz sad "Sorry, [player_name]. I'm not about to write an incident report for this."
            show ryz neutral
            n "You see a Dr. Deceased and Dr. Ryz cross out a square on their sheet. {i}Someone gets reported for cheating.{/i}"
            n "A strong feeling of spite emerges within you. What's the difference between what Dr. Deceased did and what you were going to do?"
            n "Your gaze fall on the innocent Miku keychain lying on the table. You recall that Dr. Deceased has an unmatched foundness to Miku."
            n "You spontaneously grab it off the table and dash out of the lounge."
            scene bg room hall
            deceased "HOW DARE YOU GET YOUR GRUBBY HANDS ON MIKU!!! GET [player_obj!u]!!!" #####################
            n "You run down the hallway and realize what you've done to a bunch of department heads. Your spite is immediately replaced by fear."
            n "You can hear Dr. Deceased's furious steps getting closer."
            n "Too late for regrets now. You continue running forwards-"
            show layer master:
                shake
            n "-crashing into a dense black ball on four legs."
            n "The prized Miku flies through the air and is caught in Pochi's huge mouth. Then he runs off."
            deceased "YES! BINGO! {i}Pochi commits thievery{/i}!"
            show deceased happy at appear(x_align = 0.5)
            n "You turn around and see Dr. Deceased marking off their bingo card."
            deceased "HA! You loser!"
            show deceased at disappear
            n "They skip away, following Pochi's trail. You're just glad that Dr. Deceased seems to have forgotten about your earlier action."
            $ update_character_points ({"deceased": 1, "helco": 1})
            return

    label bingo2_dont_help_helco:
        n "You keep your mouth shut. Perhaps Dr. Helco is doing it on purpose to fish out those that break rule #2."
        n "The room remains silent and tense. No one is doing anything, just observing each other."
        with default_fade
        n "It's been...an hour. Your breaktime is definitely over."
        n "You should get back to work. You still have some tasks to complete today, and you don't want to stay overtime."
        # turn around
        player "I forfit. I have to get back to work."
        ryz happy "Yes! {i}Someone forfits.{/i} Thank you [player_name], you have severed your purpose."
        player "...You're welcome?"
        show ryz at disappear
        show uriel at disappear
        n "You go over to the coffee machine and make yourself a hot, bitter cup of coffee. This should power you through the rest of the day."
        hide ryz
        hide uriel
        deceased "Pspsps. Hey, [player_name]."
        show deceased at appear(x_align = 0.5)
        n "You turn around to see Dr. Deceased waving you over."
        player "What is it?"
        deceased "I need you to do something for me. When you're leaving, go trigger the anomaly outbreak alarm."
        player "Huh!? Why? Is there an anomaly outbreak?"
        deceased "Shush! Just do as I say!"
        n "You look down at Dr. Deceased's hand. They are holding their bingo card against their chest. Upon seeing your gaze, they hold it closer, as if trying to cover what's on it."
        n "What Dr. Deceased doesn't seems to realize is the side with the bingo grid is facing outwards. Meaning, you can see everything on it."
        n "You very clearly see that they are one away from a bingo. The last square reads {i}\"anomaly outbreak\"{/i}."
        n "Dr. Deceased must really want that keychain."
        show ryz pensive at appear(x_align = 0.1)
        show uriel pensive at appear(x_align = 0.9)
        n "You look at the other participants. Dr. Helco has achived a bingo with his empty squares. Dr. Uriel remains in deep focus. Caffi has fallen asleep. Dr. Ryz is staring at you, with a hint of suspicion in his eyes."
        menu:
            n "What do you do?"
            "Help Dr. Deceased win.":
                jump bingo2_help_deceased
            "Report Dr. Deceased for cheating.":
                jump bingo2_dont_help_deceased

        label bingo2_help_deceased:
            n "dnkjs"
            return

        label bingo2_dont_help_deceased:
            n "bahaahhaa"
            return






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
