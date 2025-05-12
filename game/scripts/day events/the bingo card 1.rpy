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
    n "You pass a glance at Founder Alex's bingo sheet. The sheet is filled with random objectives, such as \"Someone downs a pot of coffee\" and \"Someone does a backflip.\""
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
        n "You open the fridge door...are greeted by Pochi."
        n "He's napping on a plate like a basted turkey."
        n "His face is covered with crumbs of the sandwich you were just about to eat...His gluttony knows no bounds."
        n "Startled by the sound of the fridge door opening, Pochi wakes up. He takes one look at you before bouncing out of the fridge."
        n "Just as he does that, you hear the room erupt from behind you."
        ryz "YES! \"Pochi escapes from fridge\", check that off!"
        firewal "Objective [[Pochi escapes from fridge] has been completed. Column 2 now has 4/5 boxes checked."
        # plutoes does his thing
        jump middle
    
    label power_nap:
        n "That's right! You were going to take a power nap. It's been a long day, after all."
        n "You make your way towards the couch, pushing through the small crowd of people watching your every move."
        n ""

    label middle:
        aikha "What's wrong with you?!"
        player "I was just trying to get my lunch. What's the big deal?"
        aikha "Have you not been listeni-"
        firewal "Reminder: in the event that Wal NO.387 fails to complete mission \"Win Bingo Game,\" it will initiate SELF_DESTRUCT_SEQUENCE."
        player "...Oh."
        n ""Oh" indeed."
        n "Despite the initial stakes of upsetting the founder himself, the edition of a self-destructing Wal has definitely upped the ante."


# bingo card 1 
# player walks into room, everyone is stressed
# asks what's going on, no one replies
# 
# characterization:
# Dr. Ryz - bingo card creator, moral competitive
# Dr. Aikha - auditor, casual player. stress about the competitive players
# Dr. Firewal 387 - immoral competitive game winner
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
# - open the fridge and pochi is inside, Dr Ryz yells "yes!", plutoes does plutoes thing, firewal "80% completion"
# - (attempt to) take a power nap on the couch, Founder Alex pushes you off the couch then cross off grid (employee unsuccessfully take nap and gives up within 15 minutes), Dr firewal is pissed
# 
# quiet gasping, aikha wisphers "oh gosh everyone's one away now"
# competitive players shout for final
# choice: +1 for intended winner, +1 for accidental winner, -1 for losers
# DR. RYZ - do a backflip
    # - in the attempt, knowck youself out (firewal). wake up in the infirmary w dr ryz and dr ai standing over you. at least it's over now.
# FOUNDER - keep drinking! (your coffee) it's almost done (it's completely full), might as well finish it! (pours you more coffee)
    # - chucks coffee, drips on the floor, backsteps and accidentally do a backflip, Ryz yells bingo 
    # 387 self destruct, ai -1
# PLUTOES - consult pluto for what he wants to make the player do (no even on the bingo card) eat your own wallet, you struggle to swallow it, so you wash it down with all the coffee (Founder Alex wins)
    # - aikha "that wasn't even on his bingo card..."
    # - 387 self destruct, ai -1
# DR FIREWAL 387 - my initiative is to win bingo, i will be terminated if i fail to complete my objective; please move 2 steps forward (holds out fist on fire), you will be fine. There will be no lasting consequences
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
