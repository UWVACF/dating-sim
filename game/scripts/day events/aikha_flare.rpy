image overlay_ai_1 = At("images/day events/overlay ai 1.png", base_overlay_transform)
image haze black= At("images/day events/red blur.png", base_overlay_transform)
image soundwave = At("images/day events/soundwave overlay.png", base_overlay_transform)
image black screen = "images/day events/black screen.png"

transform dummy:
    alpha 1.0

label day_event_aikha_flare:

    transform bobbing(duration = 0.5):
        block:
            easein duration xalign 0.495
            pause 0.02
            easein duration xalign 0.5
            pause 0.02
            repeat

    scene bg hallway
    n "You've just finished your last errand of the day."
    n "Home time is so close..."
    n "You skip down to the Path-Para office to do the final check-in."
    scene bg door
    n "Right..."
    n "Unfortunately, your intern ID doesn't cover any of the doors in Path-Para..."
    n "Wouldn't want to risk a zombie apocalypse, I guess."
    n "You knock on the door to Dr. Aikha's office."
    n "..."
    n "You knock again, this time more impatiently. You really want to finish this and go home."
    show plutoes at appear(x_align = 0.5)
    n "Plutoes comes out of the office. Clearly not to answer your knocking."
    player "Is Dr. Aikha in?"
    show plutoes at move_to(x_align = -0.5)
    n "Plutoes ignores you and shrooms away."
    n "You catch the door just as it closes and piggyback in."

    scene bg aikha office leave
    show haze black onlayer top:
        alpha 0.0
        linear 1.5 alpha 0.2
    player "I've delivered the old cases to the archives as you've asked, Dr. Aikha."
    scene bg aikha office dark
    show aikha sad
    show aikha sad at bobbing()
    pause 0.5
    player "Here are the trial records you wanted."
    player "Can I go home now?"
    scene bg aikha office dark close
    show aikha sad
    show aikha sad at bobbing()
    aikha "..."
    player "Dr. Aikha?"
    aikha "..."
    show aikha sad at bobbing(1)
    player "Helloooo?"
    aikha "..."
    show haze black onlayer top:
        linear 1.5 alpha 0.5
    n "You suddenly remember an old entry you read at the archives."
    n "{sc}An anomaly that impersonates foundation personnel and eats unsuspecting \ncoworkers.{/sc}"
    n "Its defining traits?" 
    n "It can't speak and shows odd behavior patterns."
    scene bg aikha office dark
    show aikha sad
    show aikha sad at bobbing(1)
    show haze black onlayer top:
        linear 1.5 alpha 0.8
    show aikha sad:
        xalign 0.5
    n "I mean... It could just be paranoia..."
    n "But... it did inexplicably go missing."
    n "And from what you've heard, Dr. Aikha is pretty injury prone."
    show aikha unique
    n "Huh. It's looking right at you, isn't it?"
    show aikha unique:
        linear 5 zoom 1.3
    n "It approaches."
    n "You see your life flash before your eyes. Tomorrow, you'll just be a statistic on the {i}Monthly Foundation Casualty Report{/i}."

    show screen qte (act=Jump("af_shoot"), time=5.0, hidden=True)

    menu:
        n "You pull out your company issued gun."
        "Shoot":
            hide screen qte
            jump af_shoot
        "Shoot":
            hide screen qte
            jump af_shoot
        "Shoot" (on_hover = "Wait"):
            hide screen qte
            jump af_wait
        "Shoot":
            hide screen qte
            jump af_shoot 

    label af_wait:
        n "You fight your trigger finger, deciding to exercise restraint."
        n "I mean, if your judgement is wrong then you'd be shooting a department head."
        n "What you hope is Dr. Aikha stops in place and reaches a tendril towards you."
# add spoopy ooOOooO overlay
        n "And grabs the papers from you."
        show aikha unique:
            zoom 1.3
            easein 0.5 zoom 1
        n "Huh. That wasn't too bad."
        n "It's not doing anything though..."
        n "You decide to sit down on the couch. Waiting to either be taken out by the Mimimic thing or dismissed."
        player "..."
        aikha "..."
        player "..."
        player "Dr. Aikha?"
        aikha "..."
        aikha "nnngn..."
        n "The life returns in Dr. Aikha's eyes."
        aikha panic "Hm? How'd you get in here, new recruit?"
        scene bg aikha office
        show haze black onlayer top:
            alpha 0.8
            linear 0.4 alpha 0.0
        show aikha
        n "Dr. Aikha turns on the lights."
        n "A Plut Shroom spurts spores in the corner of the room."
        aikha pensive "Ah, I must have blanked out. For..."
        n "Dr. Aikha pulls out a small Wal... a Smal."
        n "A Smal if you will."
        aikha "Pocket Wal?"
        show pocketwal at appear(x_align = 0.4)
        pocketwal "Good morning!"
        pocketwal "You've been dissociating for 58 minutes, 59 seconds."
        aikha pensive "I see... thanks Pocket Wal."
        pocketwal "Yippiee!"
        n "The Pocket Wal hops down and crawls back into Dr. Aikha's labcoat pocket."
        n "Seems like an awfully advanced pocket watch..."
        aikha upset "Sorry, [player_name]. I was supposed to meet you a while ago."
        aikha "Did you finish everything I ask-"
        n "Dr. Aikha stops mid-question after noticing the papers in their hand."
        aikha pensive "Mmm."
        n "They also notice the gun in your hand."
        aikha upset "Hm."
        player "Ah- uh I was just uh... practicing open-carry..."
        n "Their eyes stare through you."
        aikha "Well, your heart rate looks pretty high."
        aikha "I'm... sorry you had to see me like that."
        player "I'm sorry for almost shooting you!"
        aikha "It's understandable. I look a little... off when I'm relaxing my form."
        player "Relaxing?"
        n "Wow. You were going to shoot someone leisuring."
        aikha upset "Mm. Maintaining appearances is straining is all."
        aikha happy "Sometimes it's good to kinda melt in private."
        n "Relatable."
        aikha sad "And sometimes you melt so much you end up completely losing shape and giving full control to muscle memory."
        n "Slightly less so..."
        aikha "Regardless, thanks for giving it a second thought before shooting me."
        aikha happy "I'll drop off a gift to you later as compensation for your time. Next time just give the papers to one of my assistants, personnel, or just leave it at my door."
        n "Huh, you were so excited to leave, you forgot those were all options."
        hide aikha
        scene hallway
        # idk about this part bc if each event is a day we shouldn't have an event jump to the next day
        # we can keep the joke with a different delivery
        n "The next day you find a gold bar at your desk." #later in the day maybe?
        n "There seems to be a clear disparity between how you're paid and how heads are paid..."
        n "Not that you're complaining at this moment!"
        n "You can pay rent!"
        $ update_character_points ({"aikha": 3})
        return

    label af_shoot:
        $ shake_screen()
        n "You shoot without hesitation."
        show overlay_ai_2 onlayer top:
            alpha 0.0
            linear 0.4 alpha 1.0
        n "..."
        show bg aikha office dark close
        show aikha fury:
            zoom 1.3
            easein 0.05 zoom 1
        n "The entity stumbles back and writhes in pain." 
        n "Haha! You've survived another day at the foundation!"
        n "Dr. Aikha jolts awake, suddenly gaining life in their eyes."
        aikha "{sc}Wh-... new recruit...?{/sc}"
        n "Wait... Did it just talk?"
        aikha unique "{sc}My... Head... auuughh...im...destabilizin...g...{/sc}"
        n "... This might have {i}actually{/i} been Dr. Aikha."
        aikha unique "{sc}Hur...ry...{/sc}"
        aikha unique "{sc}AH-IIEIAAIII{/sc}"
        hide overlay_ai_2 onlayer top
        show bg aikha office dark
        show aikha unique
        n "Uh oh. Getting eaten by Dr. Aikha is definitely worse than that old Mimimic thing!"
        show bg aikha office leave
        n "You back up against the door, fumbling with the knob."
        n "Right, that Path-Para access."
        n "Out of the corner of your eye, you see Dr. Aikha's wallet on the desk behind {i}it{/i}."
        show aikha unique
        menu:
            n "Quick! What to do!?"
            "Steal the wallet.":
                jump af_swipe_id
            "Try to reason.":
                jump af_reason

        label af_swipe_id:
            "You instinctively steal the wallet in hopes that their Path-Para ID is in there and you can use it to escape the room... or at least get some cash. "
            show aikha unique: 
                linear 0 zoom 1
                move_to(x_align = 0.2)
            show bg aikha office dark close
            n "You lunge to the side and barely dodge Dr. Aikha's maws."
            hide aikha
            n "Scrambling to your feet, you dive towards the desk."
            n "{sc}You can hear screeching behind you.{/sc}"
            n "You grab the wallet, knocking over seven pill bottles in the process."
            n "Is... Dr. Aikha alright?"
            show bg aikha office leave
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
            show bg aikha office dark
            show pocketwal at appear()
            n "A small Wal pops out of Dr. Aikha's discarded lab coat."
            n "A... Smal?..."
            n "A Smal if you will."
            n "The Smal pushes past the fabric and marches towards you."
            pocketwal upset "Don't worry, Ai! I, Pocket Wal! will defeat this poacher!"
            pocketwal upset "HAAAAAAA!!!"
            n "Pocket Wal charges up and bursts into flames. Slightly calming down the mess of Dr. Aikha."
            aikha "nnnghnnn..."
            player "Wait, wait! I'm no poacher!"
            pocketwal "Oh. It's just you, intern."
            pocketwal upset "{cps=*2}You really shouldn't steal! What's wrong with you! I'm gonna have to report this to THE WAL! I mean this is just ridiculous... breaking into a Path-Para office and stealing Dr. Aikha's wallet! A DEPARTMENT HEAD TOO! The audacity!{/cps} {cps=*3}THE WAL has set me, WAL NO.2 in charge of protecting and keeping Ai company and the last thing I would expect to encounter is the INTERN stealing! What kind of fiend are you! {/cps} {cps=*5}Why I should just blast you right here. I mean if I protect Ai then THE WAL will be even happier with my operations! This is such a great opportunity! Usually I'm just hanging out in their pocket on stand-by but now is my chance! I can use all that dangerous tech that THE WAL graciously and benevolently gifted me!{/cps}"
            show aikha unique:
                alpha 0.0
                alpha 1.0
                appear(x_align = 1.3)
                move_to(x_align = 0.6, duration = 3)
            n "The Pocket Wal's lecturing is interrupted by a very damaged Dr. Aikha. Who screeches before trying to engulf you."
            n "This is really a horrific way to go..."
            n "You can't even squeak out your last words because Wal NO.2 the yapper is drowning you out."
            show soundwave onlayer top
            $ shake_screen(persist=15.0, preset="rumble")
            show aikha fury:
                move_to(x_align = 0.9, duration = 0.7)
            n "The Pocket Wal springs into action! Emitting a high pitch frequency to stun Dr. Aikha."
            show soundwave onlayer top:
                alpha 1.0
                linear 0.3 alpha 0
            pocketwal upset "Ah, I see the issue. Ai, spaighettied."
            show soundwave onlayer top:
                alpha 1.0
            $ shake_screen(persist=15.0, preset="rumble")
            n "The Pocket Wal opens its mouth to emit another frequency."
            show soundwave onlayer top:
                alpha 1.0
                linear 0.3 alpha 0
            show layer master
            pocketwal "I will occupy them while you will go retrieve an emergency snack."
            pocketwal "It's behind the mirror, push past it and you'll see a safe." 
            hide pocketwal
            hide aikha
            show bg aikha office leave
            show soundwave onlayer top:
                alpha 1.0
            $ shake_screen(persist=15.0, preset="rumble")
            n "You run amidst Dr. Aikha and Pocket Wal's screeching match."
            show bg aikha office leave:
                zoom 2.0
            # safe cg here
            n "Thankfully you find the safe. Now you just have to open it."
            show layer master
            show soundwave onlayer top:
                alpha 1.0
                linear 0.3 alpha 0
            $ flare_pin_tries = 0
            $ flare_actual_pin = renpy.random.randint(1000,9999)
            $ flarepin_attempts = 'You\'ve already tried:'
            jump flare_enter_pin

        label flare_enter_pin:
            while flare_pin_tries < 3:
                n "You see the display only allows for a 4-digits code. A label has been stuck above it. It reads: {i}How many eyes does Dr. Aikha usually have?{/i}"
                $ renpy.notify([flarepin_attempts])
                $ flare_pin = renpy.input("Enter a 4-digits pin:")
                $ flare_pin = flare_pin.strip()
                if flarepin_attempts == 'You\'ve already tried:':
                    $ flarepin_attempts = f"{flarepin_attempts} {flare_pin}"
                else:
                    $ flarepin_attempts = f"{flarepin_attempts} ', ' {flare_pin}"
                python:
                    try: 
                        flare_pin_int = int(flare_pin)
                        if flare_pin_int < flare_actual_pin:
                            if len(str(flare_pin)) != 4:
                                renpy.say(n, "{b}4-digits{/b}. Do you not know how to count?")
                            else:
                                renpy.say(n, "WHOMP WHOMP. THAT'S TOO LITTLE. TRY AGAIN.")
                        elif flare_pin_int > flare_actual_pin:
                            if len(str(flare_pin_int)) != 4:
                                renpy.say(n, "{b}4-digits{/b}. Do you not know how to count?")
                            else:
                                renpy.say(n, "WHOMP WHOMP. NOT THAT MANY. TRY AGAIN.")
                        elif flare_pin_int == flare_actual_pin:
                            renpy.say(n, "DING!")
                            renpy.say(n, "What the fu-")
                            renpy.say(n, "How did you even know that???")
                            renpy.jump("open_safe")
                    except:
                        renpy.say(n, "That is not a number. How did you even enter this?")
                    flare_pin_tries += 1
                    renpy.jump("flare_enter_pin")
            label flare_enter_pin_answer:
                if flare_pin_tries >= 3:
                    pocketwal "IT'S [flare_actual_pin]!!!!!"
                    $ renpy.notify([flarepin_attempts])
                    $ flare_pin = renpy.input("Enter a 4-digits pin:")
                    $ flare_pin = flare_pin.strip()
                    if flare_pin == str(flare_actual_pin):
                        n "DING!"
                        n "Wow. Finally. That only took like what, [flare_pin_tries] times?"
                        jump open_safe
                    elif flare_pin != flare_actual_pin:
                        if flare_pin_tries == 4:
                            n "Do you prefer the omni version of Dr. Aikha, perhaps?"
                        elif flare_pin_tries == 5:
                            n "Come on, this is getting old."
                        elif flare_pin_tries == 6:
                            n "I'm starting to question how you got this intern position."
                        elif flare_pin_tries == 7:
                            n "Is it your life's dream to be eaten? What is this, reverse cannibalism?"
                        elif flare_pin_tries == 8:
                            n "Okay, I'll fullfill your wish."
                            n "You frantically attempt to enter the wrong passwords, unaware that the screeching has gotten closer."
                            show overlay_ai_1 zorder 49:
                                alpha 0.0
                                linear 0.5 alpha 1.0
                            n "Uh oh."
                            show black screen zorder 50:
                                alpha 0.0
                                easeout 0.2 alpha 1.0
                            hide overlay_ai_1 zorder 49
                            n ""
                            pocketwal "{sc}ARE YOU NOT DONE YET???? IT'S [flare_actual_pin]!!!!!{/sc}"
                            hide black screen zorder 50
                            n "You jolt back awake."
                            n "Wow, you really must be tired, to be able to fall asleep in a situation like this."
                        elif flare_pin_tries %3 == 0:
                            n "Do you prefer the omni version of Dr. Aikha, perhaps?"
                        elif flare_pin_tries %5 == 0: 
                            n "Come on, this is getting old."
                        elif flare_pin_tries %2 == 0:
                            n "I'm starting to question how you got this intern position."
                        else:
                            n "Is it your life's dream to be eaten? What is this, reverse cannibalism?"

                        $ flarepin_attempts = f"{flarepin_attempts} ', ' {flare_pin}"
                        $ flare_pin_tries += 1
                        jump flare_enter_pin_answer



            label open_safe:
                # cg of open safe with biomass
                n "You could've swore this was different from the last time you counted."
                n "The safe pops open and out spills a mess of eyeballs, teeth, and flesh."
                n "You are what you eat, I guess."
                n "You decide not to ponder about the origins of the biomass."
                player "Pocket Wal! I got the... biohazards?"
                show soundwave onlayer top:
                    alpha 1.0
                $ shake_screen()
                show soundwave onlayer top
                pocketwal "{b}{sc}Good, now throw it over!{/sc}{/b}"

                show bg aikha office dark close:
                    zoom 1.0
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
                pocketwal upset "Don't think I forgot your attempts to poach from Ai!"
                aikha fury "..."
                n "Oh, come on!"
                aikha happy "[player_name]. I advise you don't attempt such a stunt again."
                aikha fury "That will be all. Leave."
                n "The Pocket Wal hops down and shoves you out of the door with surprising strength."
                hide aikha
                n "You have a feeling you won't be coming back here anytime soon."
                $ update_character_points({"aikha": -3})

            return

        label af_reason:
            n "You should probably apologise. Although that won't get rid of the hole in their head."
            show bg aikha office dark close
            player "Dr. Aikha! I'm so sorry! Please wake up!"
            player "I didn't mean to, I thought you were a man-eating anomaly..."
            aikha unique "{sc}IIEIAAIIIEEEAAAAAAAAA{/sc}"
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
            n "You feel yourself hyperventilating as every muscle in your body begins to throb."
            n "You watch in horror as Dr. Aikha assimilates the arm into their mass."
            n "...Surely this is covered in the employee insurance plan, right?"
            n "After the arm completely dissolves, the mass rapidly reforms into the familiar shape of Dr. Aikha."
            show aikha upset
            aikha "Ughhh. My... head..."
            aikha "Right."
            aikha "I got shot."
            aikha "Again."
            aikha "New recruit, you-"
            aikha surprise "Hm."
            aikha "Did you lose an arm on the job?"
            aikha happy "Don't worry! I can fix it!"
            hide aikha
            n "In your progressively blurring vision, you see Dr. Aikha looking behind a mirror."
            n "After fiddling for a bit, they shove something into their mouth and begin munching."
            n "Guess this isn't considered an emergency."
            show aikha neutral
            aikha "Can't do this on an empty 'stomach'."
            aikha "One moment."
            show aikha unique
            n "They hold onto your stub of a forearm. You close your eyes, unable to stomach what will happen next."
            # black screen cg
            show haze red onlayer top:
                alpha 0.5
                linear 1.5 alpha 0
            show layer master:
                blur 30
                linear 1.5 blur 0
            n "You hear squelching noises, as if something is being grown right in front of you."
            hide haze red onlayer top
            # slight shake of text box temp?
            n "Something is jammed into your stub and you feel all the vicera and nerves connect to something."
            n "You desperately clench your left hand to comfort yourself."
            n "Wait. Left hand?"
            n "You look down and find that you now have two arms again. However, your left arm is scarred with purple, root-like structures. "
            aikha happy "There, all fixed! Don't worry about the artifacts, it'll turn 'normal' in a few days!"
            aikha "I don't blame you {i}too{/i} too much, I guess."
            aikha happy "Was gonna reprimand you for entering my office without permission and shooting me, but it seems you already learned you lessson, eh?"
            aikha "Heheh."
            aikha upset "..."
            aikha fury "I advise you refrain from doing that again."
            hide aikha
            $ update_character_points({"aikha": 0})

            scene bg hallway
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

