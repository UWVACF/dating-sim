image overlay_ai_1 = Image("images/day events/overlay ai 1.png", xpos = -100, ypos = -100, xanchor = 0.0, yanchor = 0.0)
image aikha flairup1 = Image("images/personnel/aikha/aikha flairup1.png", sprite_highlight("aikha"))
image aikha flairup2 = Image("images/personnel/aikha/aikha flairup2.png", sprite_highlight("aikha"))

label day_event_aikha_flair:

    transform bobbing(duration = 0.1):
        block:
            easein duration xalign 0.495
            pause 0.02
            easein duration xalign 0.5
            pause 0.02
            repeat

    scene bg hallway
    n "You've just finished your last errand of the day and are very excited to go home."
    n "You skip down to the Path-Para office to report task completion."
    n "Unfortunately, your intern ID doesn't cover any of the doors in Path-Para..."
    n "Wouldn't want to risk a zombie apocalypse I guess."
    n "You knock on the door to Dr. Aikha's office."
    n "..."
    n "You knock again, this time more impatiently. You really want to finish this and go home."
    show plutoes at appear(x_align = 1.0)
    n "Plutoes comes out of the office. Clearly not to answer your knocking."
    player "Is Dr. Aikha in?"
    show plutoes at move_to(x_align = -0.5)
    n "Plutoes ignores you and shrooms away."
    n "You catch the door just as it closes and piggyback in."

    scene bg office
    show aikha flairup1
    show aikha flairup1 at bobbing()
    pause 0.5
    # dark filter
    player "I've delivered the old Path-Para cases to the archives, Dr. Aikha."
    player "Here are the trial records you wanted."
    player "Can I go home now?"
    aikha "..."
    player "Dr. Aikha?"
    aikha "..."
    show aikha flairup1 at bobbing(duration = 0.3)
    player "Helloooo?"
    aikha "..."
    # slightly darker
    n "You suddenly remember an old entry you read at the archives earlier about an anomaly that impersonates foundation personnel and eats unsuspecting coworkers."
    n "The defining traits are that it can't speak and show odd behavior patterns."
    # EVEN darker
    show aikha:
        xalign 0.5
    show aikha flairup2
    n "Uh oh, it must have spotted you."
    show aikha flairup2:
        linear 5 zoom 1.3
    n "It gets up from the seat and makes its ways towards you."
    n "You see your life flash before your eyes. Tomorrow, you'll just be a statistic on the {i}Monthly Foundation Casualty Report{/i}."

    menu:
        n "You pull out your company issued gun."
        "Shoot":
            jump ahoot
        "Shoot":
            jump ahoot
        "Shoot":
            jump ahoot
        "Shoot":
            jump ahoot 

    label ahoot:
        show layer master:
            shake
        n "You shoot without hesitation."
        # STOP SHOOTING WHY IS IT CONTINUING
        show overlay_ai_2 onlayer top:
            alpha 0.0
            linear 0.4 alpha 1.0
        n "..."
        n "The entity stumbles back and writhes in pain." 
        n "Haha! You've survived another day at the foundation!"
        n "Dr. Aikha jolts awake, suddenly gaining life in their eyes."
        aikha "{sc}Wh-... new recruit...?{/sc}"
        n "Wait... Did it just talk?"
        aikha "{sc}W...hy... auuughh...im...destabilizin...g...{/sc}"
        n "... This might have been {i}actually{/i} Dr. Aikha."
        aikha "Hur...ry..."
        aikha "{sc}AH-IIEIAAIII{/sc}"
        hide overlay_ai_2
        #show aikha unique:
        n "Uh oh. You are about to actually get eaten! Not by a Mimimic, but Dr. Aikha!"
        n "You backup against the door and try to open it. The door won't budge without an Path-Para ID."
        n "Out of the corner of your eye, you see Dr. Aikha's wallet on the desk behind {i}it{/i}."
        #show aikha unique:
        menu:
            n "Quick! What to do!?"
            "Attempt to take Dr. Aikha's wallet on the desk. Hopefully their employee badge is in there and you can use it to escape the room... or at least get some cash.":
                jump swipe_id
            "Apologise and try to reason with Dr. Aikha. Surely they're in there somewhere, right?":
                jump reason

        label swipe_id:
            show aikha unique: 
                linear 0 zoom 1
                move_to(x_align = 0.2)
            n "You lunge to the side and barely dodge Dr. Aikha's teeth."
            hide aikha
            n "Scrambling to your feet, you run towards the desk with all the might you can muster."
            n "{sc}You can hear screeching behind you.{/sc}"
            n "You reach the wallet and grab it, knocking over seven pill bottles in the process."
            n "The mass of eyes and teeth quickly approaches. In a panic, you roll the chair into it and run back towards the door."
            n "The anomaly is barely slowed by your desperate attack. It slinks past the office chair, reaching its sharp teeth towards you."
            n "Oh god. You really are gonna make it onto that Casualty Report..."
            # ENTER POCKET WAL
            n "You accept your fate... this is what you get for wrecklessly shooting a department head..."
            n "When suddenly..."
            firewal "{size=-10}WEEWOOWEEWOO!!! THIEF! THIEF! THIEF ALERT!{/size}"
            n "A small Wal pops out of Dr. Aikha's discarded lab coat."
            n "A... Smal?..."
            n "A Smal if you will."
            n "The Smal pushes past the fabric and marches towards you."
            firewal "{size=-10}Don't worry, Ai! I, Pocket Wal! will defeat this poacher!{/size}"
            firewal "{size=-10}HAAAAAAA!!!{/size}"
            n "Pocket Wal charges up and bursts into flames. Slightly calming down the mess of Dr. Aikha."
            aikha "nnnghnnn..."
            player "Wait, wait! I'm no poacher!"
            firewal "{size=-10}Oh. It's just you, intern.{/size}"
            firewal "{size=-10}You really shouldn't steal! What's wrong with you! I'm gonna have to report this to THE WAL! I mean this is just ridiculous... breaking into a Path-Para office and stealing Dr. Aikha's wallet! A DEPARTMENT HEAD TOO! The audacity! THE WAL has set me, WAL NO.2 in charge of protecting and keeping Ai company and the last thing I would expect to encounter is the INTERN stealing!{/size}"
            n "The Pocket Wal's lecturing is interrupted by a very damaged Dr. Aikha. Who screeches before trying to engulf you."
            n "This is really a horrific way to go..."
            # shake! or soundwave overlay?
            n "The Pocket Wal springs into action! Emitting a high pitch frequency to stun Dr. Aikha."
            firewal "Ah, I see the issue."
            
            ####### eol filler starts here

            firewal "Dr. Aikha is destablizied right now and require substance input. I will occupy them while you will go retrive their emergency snack."
            #shake/soundwave overlay again
            # maybe have wal open his mouth (like the epic violin noise doodle)...sorry cg assets team...
            firewal "{i}{sc}*************{/sc}{/i}"
            firewal "It's in the cabinet to the right of the door, open the third cupboard down and you will see a safe." 
            hide firewal
            #shake/soundwave overlay again again
            n "You run amidst Dr. Aikha's growls and Smal's screeches."
            # safe gc here
            n "Thankfully you find the safe. Now you just have to open it."
            # uh discuss and design minigame? like asking you silly foundation lore questions? or solving actual puzzles?
            menu:
                n "uh discuss and design minigame? like asking you silly foundation lore questions? or solving actual puzzles?"
                "i haven't planed the minigame yet so this is the only choice you get":
                    jump open_safe

            label open_safe:
                # jar of eyeballs cg
                n "The safe pops open. It is a clear jar of...eyeballs. Fresh, hydrous white spheres of various colors of iris."
                n "You are what you eat, I guess."
                n "You decide not to ponder about the origins of the eyeballs."
                player "Dr. Firewal, I got the...substances!"
                #shake/overlay
                firewal "{b}{sc}Good, now throw it over!{/sc}{/b}"

                scene bg hallway
                #bg should be back towards the office where dr ai and smal are
                n "You throw the jar and the glass shatters upon hitting the ground." 
                n "As if sensing the scent of bloody organics, what became of Dr. Aikha spreads over the scattered balls and glass shards, infusing it with their own mass."
                n "You watch in awe as the purple blob reforms into the familiar shape of Dr. Aikha."
                show aikha upset at appear(x_align = 0.5) 
                aikha "Ughhh. Wh..what happened..?"
                n "They spits out some glass shards. You also notice some more shards embedded on their forhead."
                aikha "Oh right. I got shot. Again."
                n "You feel a little bad. Okay, very bad."
                aikha neutral "[player_name]. It would be preferred if you...don't do that again."
                aikha "Violence is not the answer. Towards me, at least."
                n "They pick up the report you delivered and dismisses you."
                hide aikha
                n "You have a feeling you won't be coming back here anytime soon."

            return

        label reason:
            player "Dr. Aikha! I'm so sorry! Please wake up!"
            player "I didn't mean to, I thought you were a man-eating anomaly..."
            aikha "{sc}IIEIAAIIIEEEAAAAAAAAA{/sc}"
            n "Their 'arm' suddenly extends and latches onto your left hand."
            n "For a moment, you believe that this is a handshake of forgiveness."
            n "...then they rip your arm off."
            # blurry vision, blood red? filter
            n "The pain reach your brain before the realization of what have just occurred does."
            n "You feel yourself begin hyperventilating as every muscle in your body seemingly begin to throb."
            n "You watch in horror as Dr. Aikha infuses the arm into their purple mass."
            n "...surely this is covered in the employee insurance plan, right?"
            n "After the arm completely dissolves, the purple blob rapidly reforms into the familiar shape of Dr. Aikha."
            show aikha sad
            aikha "Ughhh. Wh..what happened..?"
            aikha "Oh right. I got shot. Again."
            aikha "[player_name], you-"
            aikha surprise "Oh."
            aikha "Ah. I must have...attacked you during the flair up."
            aikha happy "Don't worry! I can fix your arm!"
            hide aikha
            n "In your progressively blurring vision, you see Dr. Aikha shuffles over to a cabinet to take something out and begin munching."
            n "Guess this isn't considered an emergency."
            show aikha neutral
            aikha "Sorry, I had to...recharge for a bit."
            aikha "But I'll fix you up now!"
            show aikha flairup2
            n "They hold your shoulder that is now dirpping red. You feel viscous material encasing the wound and a tickish feeling extends to your fingertips."
            n "...wait, fingertips?"
            # possible, completely optional cg of an omni arm!
            n "You look down to find you now have two arms again. However, your left arm is an unusual shade of violet with seams. "
            #hide cg
            aikha happy "There, all fixed! Don't worry about the purple, it'll turn 'normal' in a few days!"
            aikha "...but if you like the purple, I can also keep it for you."
            aikha "Anyways, I was going to reprimand you for shooting me, but it seems you already learnt you lessson, eh?"
            aikha "Just don't do it again!"
            hide aikha

            scene hallway
            n "You re-emerge into the hallway with your brand new arm."
            n "You don't think you would ever use your company issued gun ever again."
            return

            ####### eol filler ends here


# end of day -> player excited to go home
# report errand at path-para
# run into weird dr ai
# plutoes leave and you entered the door that only path-para personnel badges can open - forced proximity
# finds dr aikha, who seems out of it (relaxed, auto-pilot), who doesn't respond to player
# player remember report of a "missing" anomaly that was reported to shapeshift into personnels, trick their unsuspecting coworkers and kill them. just as you think of that, dr aikha spots you and starts walking towards you, some of their eyes and seams opening
# choice:
# shoot
# shoot
# shoot (wait)
# shoot

#(wait)
#dr aikha snaps out of it and you have a nice convo and then they dismiss you. You feel closer to dr. Aikha. [+1]


#shoot
#you shoot and dr aikha doesn't go down. In fact, they are more aggravated. the seams open fully and the flesh slides across the office floor towards you.

#choice to escape:
#grab dr ai’s badge that is on the ground
#try to reason with dr ai

#grab_badge -> activates pocket wal as id leaves pocket wal’s proximity, sees what's happening, directs you to the safe, open the safe (puzzle) to find aikha’s stash of emergency eyeballs [net -1]

#try_reason -> eats your arm??? recovers??? blocks out? Eats emergency eyeballs while you bleed with a missing arm. makes you a new arm? "If you want your memory wiped, you can ask the ethic department?" [net 0]

