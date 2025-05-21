image overlay_ai_1 = Image("images/day events/overlay ai 1.png", xpos = -100, ypos = -100, xanchor = 0.0, yanchor = 0.0)
image aikha flairup1 = Image("images/personnel/aikha/aikha flairup1.png", sprite_highlight("aikha"))
image aikha flairup2 = Image("images/personnel/aikha/aikha flairup2.png", sprite_highlight("aikha"))
image haze black= Image("images/day events/red blur.png", xpos = -100, ypos = -100, xanchor = 0.0, yanchor = 0.0)
image soundwave = Image("images/day events/soundwave overlay.png", xpos = -100, ypos = -100, xanchor = 0.0, yanchor = 0.0)

transform dummy:
    alpha 1.0

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
    n "Wouldn't want to risk a zombie apocalypse, I guess."
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
    show haze black onlayer top:
        alpha 0.0
        linear 1.5 alpha 0.2
    player "I've delivered the old Path-Para cases to the archives, Dr. Aikha."
    player "Here are the trial records you wanted."
    player "Can I go home now?"
    aikha "..."
    player "Dr. Aikha?"
    aikha "..."
    show aikha flairup1 at bobbing(duration = 0.3)
    player "Helloooo?"
    aikha "..."
    show haze black onlayer top:
        linear 1.5 alpha 0.5
    n "You suddenly remember an old entry you read at the archives."
    n "{sc}It was about an anomaly that impersonates foundation personnel and eats\nunsuspecting coworkers.{/sc}"
    n "The defining traits are that it can't speak and shows odd behavior patterns."
    show haze black onlayer top:
        linear 1.5 alpha 0.8
    show aikha:
        xalign 0.5
    show aikha flairup2
    n "Uh oh, it must have spotted you."
    show aikha flairup2:
        linear 5 zoom 1.3
    n "It gets up from the seat and makes its ways towards you."
    n "You see your life flash before your eyes. Tomorrow, you'll just be a statistic on the {i}Monthly Foundation Casualty Report{/i}."

    show screen qte (act=Jump("ahoot"), time=5.0, hidden=True)

    menu:
        n "You pull out your company issued gun."
        "Shoot":
            hide screen qte
            jump ahoot
        "Shoot":
            hide screen qte
            jump ahoot
        "Shoot" (on_hover = "Wait"):
            hide screen qte
            jump ahoot
        "Shoot":
            hide screen qte
            jump ahoot 

    label ahoot:
        show layer master:
            shake
        n "You shoot without hesitation."
        show overlay_ai_2 onlayer top:
            alpha 0.0
            linear 0.4 alpha 1.0
        n "..."
        show aikha flairup1:
            zoom 1.3
            easein 0.05 zoom 1
        n "The entity stumbles back and writhes in pain." 
        n "Haha! You've survived another day at the foundation!"
        n "Dr. Aikha jolts awake, suddenly gaining life in their eyes."
        aikha "{sc}Wh-... new recruit...?{/sc}"
        n "Wait... Did it just talk?"
        aikha "{sc}My... Head... auuughh...im...destabilizin...g...{/sc}"
        n "... This might have {i}actually{/i} been Dr. Aikha."
        aikha "{sc}Hur...ry...{/sc}"
        aikha "{sc}AH-IIEIAAIII{/sc}"
        hide overlay_ai_2 onlayer top
        #show aikha unique:
        n "Uh oh. Getting eaten by Dr. Aikha is definitely worse than that old Mimimic thing!"
        n "You back up against the door and try to open it. The door won't budge without a Path-Para ID."
        n "Out of the corner of your eye, you see Dr. Aikha's wallet on the desk behind {i}it{/i}."
        #show aikha unique:
        menu:
            n "Quick! What to do!?"
            "Steal the wallet":
                jump swipe_id
            "Try to reason":
                jump reason

        label swipe_id:
            "You instinctly decide to steal the wallet in hopes that their path-para badge is in there and you can use it to escape the room... or at least get some cash. "
            show aikha unique: 
                linear 0 zoom 1
                move_to(x_align = 0.2)
            n "You lunge to the side and barely dodge Dr. Aikha's teeth."
            hide aikha
            n "Scrambling to your feet, you run towards the desk with all the might you can muster."
            n "{sc}You can hear screeching behind you.{/sc}"
            n "You reach the wallet and grab it, knocking over seven pill bottles in the process."
            n "The mass of eyes and teeth quickly approaches. In a panic, you roll the chair into it and run back towards the door."
            n "The anomaly is barely slowed by your desperate attack. It slinks past the office chair, reaching its sharp teeth and tendrils towards you."
            n "Oh god. You really {i}are{/i} gonna make it onto that Casualty Report..."
            # ENTER POCKET WAL
            n "You accept your fate... this is what you get for recklessly shooting a department head..."
            n "When suddenly..."
            show haze black strong onlayer top:
                alpha 0.8
                linear 1 alpha 0
            firewal_unknown "WEEWOOWEEWOO!!! THIEF! THIEF! THIEF ALERT!"
            hide haze black strong onlayer top
            n "A small Wal pops out of Dr. Aikha's discarded lab coat."
            n "A... Smal?..."
            n "A Smal if you will."
            n "The Smal pushes past the fabric and marches towards you."
            pocket_wal "Don't worry, Ai! I, Pocket Wal! will defeat this poacher!"
            pocket_wal "HAAAAAAA!!!"
            n "Pocket Wal charges up and bursts into flames. Slightly calming down the mess of Dr. Aikha."
            aikha "nnnghnnn..."
            player "Wait, wait! I'm no poacher!"
            pocket_wal "Oh. It's just you, intern."
            pocket_wal "You really shouldn't steal! What's wrong with you! I'm gonna have to report this to THE WAL! I mean this is just ridiculous... breaking into a Path-Para office and stealing Dr. Aikha's wallet! A DEPARTMENT HEAD TOO! The audacity! THE WAL has set me, WAL NO.2 in charge of protecting and keeping Ai company and the last thing I would expect to encounter is the INTERN stealing!"
            n "The Pocket Wal's lecturing is interrupted by a very damaged Dr. Aikha. Who screeches before trying to engulf you."
            n "This is really a horrific way to go..."
            show soundwave onlayer top
            show layer master:
                shake(persist=15.0, preset="rumble")
            n "The Pocket Wal springs into action! Emitting a high pitch frequency to stun Dr. Aikha."
            show layer master # reset shake
            show soundwave onlayer top:
                alpha 1.0
                linear 0.3 alpha 0
            pocket_wal "Ah, I see the issue. Ai, spaighettied."
            show soundwave onlayer top:
                alpha 1.0
            show layer master:
                shake(persist=15.0, preset="rumble")
            n "The Pocket Wal opens its mouth to emit another frequency."
            show soundwave onlayer top:
                alpha 1.0
                linear 0.3 alpha 0
            show layer master
            pocket_wal "I will occupy them while you will go retrieve an emergency snack."
            pocket_wal "It's in the cabinet to the right of the door, open the third cupboard down and you will see a safe." 
            hide pocket_wal
            show soundwave onlayer top:
                alpha 1.0
            show layer master:
                shake(persist=15.0, preset="rumble")
            n "You run amidst Dr. Aikha and Pocket Wal's screeching match."
            # safe cg here
            n "Thankfully you find the safe. Now you just have to open it."
            # uh discuss and design minigame? like asking you silly foundation lore questions? or solving actual puzzles?
            show layer master
            show soundwave onlayer top:
                alpha 1.0
                linear 0.3 alpha 0
            menu:
                n "uh discuss and design minigame? like asking you silly foundation lore questions? or solving actual puzzles?"
                "i haven't planed the minigame yet so this is the only choice you get":
                    jump open_safe

            label open_safe:
                # cg of open safe with biomass
                n "The safe pops open and out spills a mess of eyeballs, teeth, and flesh."
                n "You are what you eat, I guess."
                n "You decide not to ponder about the origins of the biomass."
                player "Pocket Wal! I got the... biohazards?"
                show soundwave onlayer top:
                    alpha 1.0
                show layer master:
                    shake(persist=15.0, preset="rumble")
                show soundwave onlayer top
                firewal "{b}{sc}Good, now throw it over!{/sc}{/b}"

                #idk should we bother swapping backgrounds
                #bg should be back towards the office where dr ai and smal are
                n "You scoop up the pile of... stuff and toss it onto the freshly vacuumed carpet... sorry janitors!" 
                show soundwave onlayer top:
                    alpha 1.0
                    linear 0.3 alpha 0
                hide soundwave onlayer top
                n "As if sensing the readily available organics, what became of Dr. Aikha spreads over the biomass, assuming it into their own mass."
                n "You watch in awe as the spaighetti reforms into the familiar shape of Dr. Aikha."
                show layer master
                show aikha upset at appear(x_align = 0.5) 
                aikha "Ughhh. Wh..what happened...?"
                n "The hole in their head remains intact."
                aikha "Right."
                aikha "I got shot."
                aikha "Again."
                n "This is definitely gonna jeopardize your internship, isn't it... Not to mention the guilt creeping in from shooting a person(?)."
                n "The Pocket Wal hops onto Dr. Aikha's desk, knocking over an empty pill bottle."
                pocket_wal "Don't think I forgot your attempts to poach from Ai!"
                aikha "..."
                n "Oh, come on!"
                aikha neutral "[player_name]. I advise you don't attempt such a stunt again."
                aikha "That will be all. Leave."
                n "The Pocket Wal hops down and shoves you out of the door with surprising strength."
                hide aikha
                n "You have a feeling you won't be coming back here anytime soon."

            return

        label reason:
            n "You should probably apologise. Although that won't get rid of the role in their head."
            player "Dr. Aikha! I'm so sorry! Please wake up!"
            player "I didn't mean to, I thought you were a man-eating anomaly..."
            aikha "{sc}IIEIAAIIIEEEAAAAAAAAA{/sc}"
            n "Their 'arm' suddenly extends and latches onto your left hand."
            n "For a moment, you believe it's the handshake of forgiveness."
            n "...then they rip your arm off."
            show haze red strong zorder 50 onlayer top:
                alpha 0.25
                block:
                    ease 0.75 alpha 0.5
                    ease 0.75 alpha 0.7
                    repeat
            show layer master:
                blur 30
            n "The pain reaches your brain before the realization does."
            n "You feel yourself hyperventilating as every muscle in your body seemingly begins to throb."
            n "You watch in horror as Dr. Aikha assimilates the arm into their mass."
            n "...surely this is covered in the employee insurance plan, right?"
            n "After the arm completely dissolves, the mass rapidly reforms into the familiar shape of Dr. Aikha."
            show aikha sad
            aikha "Ughhh. My... head..."
            aikha "Right."
            aikha "I got shot."
            aikha "Again."
            aikha "New recruit, you-"
            aikha surprise "Hm."
            aikha "Did you lose an arm on the job?"
            aikha happy "Don't worry! I can fix it!"
            hide aikha
            n "In your progressively blurring vision, you see Dr. Aikha shuffling over to a cabinet."
            n "After fiddling for a bit, they shove something into their mouth and begin munching."
            n "Guess this isn't considered an emergency."
            show aikha neutral
            aikha "Sorry, I had to...recharge."
            aikha "One moment."
            show aikha flairup2
            n "They hold onto your stub of a forearm. You close your eyes unable to stomach what will happen next."
            # black screen cg
            show haze red onlayer top:
                alpha 0.5
                linear 1 alpha 0
            show layer master:
                blur 30
                linear 1.5 blur 0
            hide haze red onlayer top
            n "You hear squelching noises, as if something is being grown right in front of you."
            # slight shake of text box temp?
            n "Something is jammed into your stub and you feel all the vicera and nerves connect to something."
            n "You desperately clench your left hand to comfort yourself."
            n "Wait. Left hand?"
            n "You look down to find you now have two arms again. However, your left arm is scarred with purple, root-like structures. "
            aikha "There, all fixed! Don't worry about the artifacts, it'll turn 'normal' in a few days!"
            aikha "I don't blame you too too much, I guess."
            aikha happy "Was gonna reprimand you for entering my office without permission and shooting me, but it seems you already learnt you lessson, eh?"
            aikha "Heheh."
            aikha "..."
            aikha "I advise you refrain from that."
            hide aikha

            scene hallway
            n "You re-emerge into the hallway with your brand new arm."
            n "Maybe you should refrain from playing with guns in the future."
            return



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

