label day_event_didnt_do_it:
    scene bg lounge
    n "It's lunch break and you're hungry."
    n "You march into the lounge kitchenette. Today you even brough a whole lettuce to include in your sandwich. Healthy!"
    n "You realizes that you've forgotten to bring your own knife today."

    label choice_loop:
        menu:
            n "There has to be a knife here somewhere, right? Your mouth isn't as big as Pochi's so you can't bite into a sandwich as big as your head."
            "Check cabinet":
                jump cabinet
            "Check the fridge":
                jump open_fridge
            "Check the drawers":
                jump drawers
            "Check the microwave":
                jump microwave
            
        label cabinet:
            n "You open the cabinet above your head."
            n "A gun falls out and hits you on the head. Ouch."
            n "As it hit the ground, it misfires, shooting a hole in your lab coat."
            n "Who left their company gun here??? How irrisponsible."
            n "You shove it back into the cabinet for it to hit the next unfortunate person who opens it."
            jump choice_loop

        label drawers:
            n "You try to slide open the drawers. It won't budge."
            n "You pull on the handle harder. It still won't budge."
            n "Something tells you that this is a sign for you to not open it. However, your stomache disagrees and yearns for that healthy sandwich."
            n "You pull on the handle with all your strength. The handle pops off."
            n "You stare into the drawers through the handle holes, and realize that it's a false drawer that hides the sink."
            jump choice_loop

        label microwave:
            n "Why would a knife be in a microwave?"
            n "Anyways, you open the microwave. There is no knife."
            n "But there is a Hampter."
            show hampter happy
            hampter "Oh hey [player_name]! Are you getting lunch?"
            player "...Yes."
            hampter "Don't mind me and use the microwave! I'm just taking a nap!"
            hampter "Do close the door when you leave, please!"
            hide hampter
            n "Hampter turns around and begins shoo mimimiming."
            n "You shut the door gently."
            jump choice_loop

        label open_fridge:
            n "Did you pick this place because you're out of options?"
            n "You pull open the fridge and are hit with a wave of chill air."
            n "You look around the compartments."
            n "There's someone's half eaten ramen, four vials of red liquid, a slice of molded cheese, and...a knife!"
            n "You gleefully take out the knife. It's slightly stained in red. You make a mental note to submit a complaint to HR later for kitchenette hygiene."

    n "You rinse the knife in the sink. The stains remain."
    n "Huh. It must be rusted. But you won't die from a little bit of rust on your lettuce, surely?"
    n "You turn back towards your sandwich workshop when you hear footsteps behind you."
    deceased "AH!!!!! DR. RALEX!!!!"
    n "You drop the knife and almost stabbed your toe. You turn around, slighly pissed off."
    show deceased surprise 
    deceased "YOU MURDERER!"
    n "Murderer? What are they talking about?"
    n "You bend down to pick up the knife when you saw it. A dead woman right next to your feet, bleeding out a pool of red the same color as the stains on the knife." 
    # more lines here about deceased yelling
    # and more lines here about people gathering and deceased accursing you

    menu:
        n"How do you defend yourself?"
        "Tell the truth":
            jump ddi_truth
        "Lie your way out of this":
            jump ddi_lie
        "Deflect the accusation onto Dr. Deceased":
            jump ddi_deflect

    label ddi_truth:
        n "pspspspsps I'm still working on it..."

    label ddi_lie:
        n "still working on it"

    label ddi_deflect:
        player "No, you were probably the one who killed her!"
        player "I bet you came back to clean up, but then ran into me here, so now you're trying to blame me!"
        deceased "Huh." 
        deceased "{i}{size=10}I did forget what I came here for…unless{/size}{i}"
        n "Dr. Deceased stares down at their own hands. Seemingly considering it." 
        jessie surprise "Dr. Deceased, did you really?"
    menu: 
        n "this is a good chance to prove your innocence! (by blaming it on someone else!)"
        "ouble down on deceased":
            jump ddi_decease_murderer
        "uhhhhh":
            jump ddi_still_screwed_up

    label ddi_decase_murderer:
        player "double down statement"
        all "gasps"
        deceased "nuh uh"
        player "yuh uh"
        deceased "NUH UH!!"
        player "YUH UH!!"
        firewal "Affirmative. Security did show Dr. Deceased entering the lounge 5 minutes earlier."
        someone else "Dr. Deceased, I can't believe you would do this!"
        deceased "But I didn't! This...you bastard!"
        alex "Take them away to the confinement room! We shall hold a fair trial later to bring justice to my dear twin sister!"
        n "Two wals come into the room and start to drag Dr. Deceased away by their arm."
        n "Dr. Deceased tries to put up a fight. They swing their arms at the wals and kick them."
    n "Unfortunately, the wals are made of hard metals."
        n "Dr. Deceased's arms and legs break off from the impact. The wals carry their scattered remains away, while Dr. Deceased's head curses them with the curse of the nile."
        someone "What a tragedy this is. I'm sorry you have to witness this, [player_name]."
        player "...Yea, I was so startled."
        n "The crowd disperses and you decide to go back to prepping your sandwich. To your dismay, the wals has confiscated the knife as evidence for the murder."
        n "Guess you're not getting your greens in today."
        return


    label ddi_still_screwed_up:
        player "lame uncredible statement"
        deceased "HA! NUH UH"
        crowd "Nuh uh..."
        deceased "smug statement"
        firewal "Affirmative. My memory module shows that Dr. Ralex specifically stated that the intern [player_name] has asked to meet them here to discuss matters concerning a potential full time offer."


#### CRIME SCENE ####
# victim is beloved co-founder dr ralex

# Co - founder (not real, anti cameo)
    # lore accurate 
    # dr alex's twin, who also has immortality, and the immortal snail


# reason to pick up knife
# making sandwich for lunch? picks up knife from counter
# Dr. deceased walks in (witness), triggers anomaly effect to show corpse///
# Dr. deceased yell and a crowd gathers
# choice: 
    # truth - idk what is going on
    # lie - make up excuses
    # deflect - no YOU killed the co founder 

    # truth chan +1
        # overexplains, seems even more suspecious. no one believes you 
        # you are dragged away into confinments by wal bots

    # lie - chan -1
        # "he ran into my knife volunterrily"
        # "I was just testing how sharp it was"
        # you are dragged away into confinments by wal bots

    # deflect
        # dr deceased "..."
        # "Oh shit did i?"
        # choice: 
            # good argument -> dr deceased as the defendent in trial and error, deceased -1
            # bad argument -> you are on trial, dr deceased +1

# visitors during confinement - chan, uriel, syg (only truth or lie)
    # uriel: do you need a lawer to represent you (foundation's right to appoint on, uriel is hence obligated to ask as the legal head) 
    # syg: if you get death-rowed can i feed you to the demons (will avocate for death row)
