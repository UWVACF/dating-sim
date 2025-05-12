# define wal387 = get_wal_num(387)

label day_event_the_bingo_card_1:
    scene bg lounge
    with default_fade
    n "As you walk into the lounge for your break, you notice that the vibe feels...off."
    # have characters not facing the player (center)
    show aikha panic at appear(x_align = 0.8)
    show alex pensive at appear(x_align = 0.5)
    show ryz pensive at appear(x_align = 0.2)
    n "Everyone in the room is speaking in hushed voices and carrying around a small sheet of paper."
    # all character turn and face you (center)
    aikha "Hold on, [player_name]."
    aikha "We're playing Ryz's bingo. Everyone's... uh... really into it, heh..."
    aikha "One wrong move could result in mass pandemonium among the players."
    n "You spare a glance at Founder Alex's bingo sheet. The sheet is filled with goals like...\"Someone downs a pot of coffee\" and \"Someone does a backflip.\""
    n "...How often does someone do a backflip here?"
    n "You see Founder Alex's eyes fixated on a mug in the corner that reads, \"#1 BINGO Player.\" So that's why he's in this."
    n "You decide to act nonchanlant and carry on with what you were doing. Everyone's eyes follow you as you make your way across the room."
    menu:
        n "...What exactly were you up to again?"
        "Check the fridge for lunch":
            jump fridge
        "Power nap":
            jump power_nap
    
    label fridge:
        n "You make your way towards the fridge and hear someone inhale sharply."
        n "You decide to ignore it. Lunch time waits for nobody!"
        n "You open the fridge door...and are greeted by Pochi."
        n "He's napping on a plate like a basted turkey."
        n "His face is covered with crumbs of the sandwich you were just about to eat...His greed knows no bounds."
        n "Startled by the sound of the fridge door opening, Pochi wakes up. He takes one look at you before bouncing out of the fridge into Plutoes' arms."
        n "Just as he does that, you hear the room erupt behind you."
        ryz "YES! \"Pochi escapes from fridge,\" check that off!"
        wal387 "Objective [[Pochi escapes from fridge] has been completed. Column 2 has achieved {b}80%%{/b} completion."
        alex upset "...Damnit."
        jump middle
    
    label power_nap:
        n "That's right! You were going to take a power nap. It's been a long morning, after all."
        n "You make your way towards the couch, pushing through the small crowd of people watching your every move."
        n "In spite of the 5 pairs of eyes on you, you lie down comfortably and start napping."
        show black_screen zorder 50:
            alpha 0.0
            linear 0.5 alpha 1.0
        n "Hoooooooonk shoooooooooooo mimimimimi"
        n "Hoooooooonk shoooooo- you hear the sound of a marker scribbling."
        n "Surely that doesn't-"
        hide black_screen
        alex "HAHA!"
        # plutoes does his thing
        ryz "Shit..."
        wal387 "Objective [[Mustache drawn on Employee] has been completed. Outcome undesirable."
        jump middle


    label middle:
        aikha "Bastard! What's wrong with you?!"
        player "I was just minding my own business. What's the big deal?"
        aikha "You don't underst-"
        wal387 "REMINDER:\nIn the event that {i}Wal NO.387{/i} fails to complete mission \"Win Bingo Game,\" it will initiate {b}SELF_DESTRUCT_SEQUENCE{/b}."
        player "...Oh."
        aikha "...And now everyone's one away..."
        n "You decide that it's probably best to get out of the room before the bingo game ends."
        n "You walk briskly over to the door but are stopped by Wal No.387."
        n "You sneak a glance at his bingo sheet. The last goal he needs is...\"Someone gets punched in the face.\""
        n "As he towers over you, you see flames begin swirling around his fist."
        n "...Is the fire really necessary??"
        wal387 "Please remain still. I can assure you that there will be no lasting consequences."
        wal387 "REMINDER:\nIn the event that {i}Wal No.387{/i} fails-"
        ryz "Don't listen to him! Here, you gotta do a backflip. I can give you...4 dollars and 35 cents."
        alex "[player_name], I will kindly tell you this: if you don't down this pot of coffee, I will revoke your position at this company, effective immediately."
        n "Plutoes throws a sign at you that reads:"
        plutoes "Eat your walet nd i will give you a skatboard - signed plutoes{fast}"
        n "Five people are watching you intensely. Two are threatening you, two are bribing you, and one just wants peace."
        
        menu:
            n "Tread carefully."
            "Get punched by Wal No.387.":
                jump punch
            "Do a backflip.":
                jump backflip
            "Down a pot of coffee.":
                jump coffee
            "Eat your wallet.":
                jump wallet
        
    label punch:
        n "Well, your top priority is probably not dying to a kamikaze bingo robot."
        n "Wal No.387 cracks his robotic knuckles, the fire around his fist turning blue."
        wal387 "Your cooperation is greatly apprec-"
        n "He doesn't have time to finish his sentence before Founder Alex throws a sofa at him."
        n "The sofa knocks him over and spontaneously combusts."
        n "As the fire alarm blares, you see Plutoes check his card and grin happily."
        n "He makes his way over to Dr. Aikha, who sighs and says something you can't quite make out."
        n "Still grinning ear to ear, Plutoes makes his way over to the \"#1 BINGO\" mug."
        n "Meanwhile, Dr. Ryz has gotten a fire extinguisher and put out the sofa fire."
        ryz "Are we all good?"
        n "You glance around the room. Your eyes lock onto Founder Alex, who's on his hands and knees in the floor."
        alex "...My...mug..."
        n "He looks at Plutoes and Pochi, who are both happily chewing on the mug. Tears start to stream from behind his goggles."
        n "While that's going on, you see Wal No.387 glitching off to the side. Dr. Aikha is frantically trying to fix him."
        wal387 "CRITICAL MALFUNCTION. INTERFERENCE DETECTED. AWAITING FURTHER ORDERS."
        n "...Bingo's over! You'd better leave before the Founder fulfills his promise."
        $ update_character_points({"firewal": 1, "plutoes": 1})
        return

    label backflip:
        n "...Do you really value your life and job at $4.35??"
        n "Well, rent {i}is{/i} due soon, I guess..."
        ryz "Yes! Okay, so what you want to do is swing your arms upwards when you jump. It helps give you momentum. Like this!"
        n "Dr. Ryz does a radical backflip..."
        show black_screen zorder 50
        with vpunch
        n "...and promptly kicks you in the face."
        hide black_screen
        show black_screen onlayer top:
            alpha 1.0
            linear 2.0 alpha 0.0
        aikha "Wakey wakey, new recruit!"
        n "You wake up to find yourself amidst mass pandemonium."
        wal387 "Objective complete. Delivering goods to THE WAL."
        n "Wal No.387 grabs the mug, crushing it in the process. He then blasts a hole in the wall and leaves."
        n "Dr. Ryz is curled up in a ball under a table, muttering to himself."
        ryz sad "I threw. I threw. I threw."
        n "After witnessing the shattering of his prized mug, Founder Alex is completely shellshocked."
        alex surprise "..."
        n "And Plutoes is nowhere to be seen."
        aikha "Well, new recruit..."
        aikha "Told ya!"
        $ update_character_points({"ryz": 1, "firewal": 1})
        return
    label coffee:
        n "I mean, your job is pretty important. Rent's due soon, anyways."
        alex "Huzzah!"
        n "You grab the pot of coffee from Founder Alex's hands and start chu-"
        player "FUCK THAT'S HOT-"
        n "You spill scalding-hot coffee all over the floor. As you stumble around, dazed by the first degree burns on your face, you slip."
        n "Not just any kind of slip. You do a whole cartoon-banana-peel kind of slip, tumbling gracelessly through the air."
        n "After 2.75 rotations, you land face-first onto the floor."
        ryz "That was a backflip! That counts! THAT COUNTS!!!"

    label wallet:
        n "...In a situation as dire as this, you were won over by...a skateboard."
        n "You take your wallet out of your pocket and empty it. It has nothing noteworthy inside: just a couple of maxed-out credit cards and a handful of loose change."
        n "The wallet itself, though, was an heirloom from your late grandfather. You admire the antique, faded brown leather one last time..."
        n "The thought of the...skateboard...pushes aside all doubts."
        n "Plutoes flashes you an encouraging smile. You brace yourself and shove the wallet in your mouth."
        n "As you attempt to unhinge your jaw to fit it in, you feel something slide down your throat. Something remarkably...coin-shaped."
        n "It looks like you missed a coin. Oh, no, wait, three coins. Three coins that are now jammed in your esophagus."
        n "You begin to choke and flail around, searching for something to remove the $1.15 stuck in your throat."
        n "Luckily, your seeking hands stumble upon Founder Alex's coffee pot. Out of the corner of your eye, you see him tense, but you have more pressing issues right now."
        n "It's a little awkward, given the wallet stuck in your mouth, but you manage to down the entire thing."
        n "It's hot. Scalding hot. But it's better to burn your insides than to die of asphyxiation."
        n "It takes the entire pot, but you manage to dislodge the coins. They'll come out the other end soon enough."
        n "You decide that enough is enough and spit the wallet out. Or, attempt to spit the wallet out. It actually takes you another full minute of grasping, trying to pull it out of your mouth."
        n "When"







# bingo card 1 
# player walks into room, everyone is stressed
# asks what's going on, no one replies
# 
# characterization:
# Dr. Ryz - bingo card creator, moral competitive
# Dr. Aikha - auditor, casual player. stress about the competitive players
# Dr. wal387 387 - immoral competitive game winner
# Founder Alex - immoral compettitve for the #1 bingo winner mug, 
# Plutoes - wild card, spontaneous 
# player - not playing 
# 
# intro:
# extreme tension
# everyone stares at you
# aikha "please stop moving" with all eyes closed. "everyone's really closed to getting bingo"
# you see the #1 bingo player mug. Ah, so that's why. 
# ... x3
# 
# you coninue to do your own thing, although a bit uncomfortable 
# choice:
# - open the fridge and pochi is inside, Dr Ryz yells "yes!", plutoes does plutoes thing, wal387 "80% completion"
# - (attempt to) take a power nap on the couch, Founder Alex pushes you off the couch then cross off grid (employee unsuccessfully take nap and gives up within 15 minutes), Dr wal387 is pissed
# 
# quiet gasping, aikha wisphers "oh gosh everyone's one away now"
# competitive players shout for final
# choice: +1 for intended winner, +1 for accidental winner, -1 for losers
# DR. RYZ - do a backflip
    # - in the attempt, knowck youself out (wal387). wake up in the infirmary w dr ryz and dr ai standing over you. at least it's over now.
# FOUNDER - keep drinking! (your coffee) it's almost done (it's completely full), might as well finish it! (pours you more coffee)
    # - chucks coffee, drips on the floor, backsteps and accidentally do a backflip, Ryz yells bingo 
    # 387 self destruct, ai -1
# PLUTOES - consult pluto for what he wants to make the player do (no even on the bingo card) eat your own wallet, you struggle to swallow it, so you wash it down with all the coffee (Founder Alex wins)
    # - aikha "that wasn't even on his bingo card..."
    # - 387 self destruct, ai -1
# DR wal387 387 - my initiative is to win bingo, i will be terminated if i fail to complete my objective; please move 2 steps forward (holds out fist on fire), you will be fine. There will be no lasting consequences
    # - take the punch. what's one punch to save one wal. but founder alex tackles 387 before the fire could reach you. 
    # - the wal did not self-destruct due to interferrence, sends appreciation email: feed wall corp will remember this (positive)
    # - plutoes win (alex tackles wal), plutoes/pochi eats the mug
# 
#
#
# 
# 
# 
# 
# 
# 
