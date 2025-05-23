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
            n "You gleefully take out the knife. It's slightly stained in red. You make a mental note to submit a complaint to HR later on the kitchenette hygiene."

    n "You rinse the knife in the sink. The stains remain."
    n "Huh. It must be rusted. But you won't die from a little bit of rust on your lettuce, surely?"
    n "You turn back towards your sandwich workshop when you hear footsteps behind you."
    deceased "AH!!!!! DR. RALEX!!!!"
    n "You drop the knife and almost stabbed your toe. You turn around, slighly pissed off."
    show deceased surprise 
    deceased "YOU MURDERER!"
    n "Murderer? What are they talking about?"
    # optoinal dead dr. ralex cg
    n "You bend down to pick up the knife when you saw it. A dead woman right next to your feet, bleeding out a pool of red the same color as the stains on the knife."
    n "You were wondering who she is and how can an unauthorize person get in here when Dr. Deceased interuptes your thought." 
    deceased panic "{size=+10}{sc}{b}THERE'S A MURDER!!!{/b}{/sc}{/size}"
    player "Wait, Dr. Deceased-"
    n "Your voice is cut off by the swarm of people now stuck stomping in the doorway, all trying to get a closer look at the crime scene."
    deceased fury "Everyone look! [player_name] murdered Dr. Ralex!"

    menu:
        n"How do you defend yourself?"
        "Tell the truth":
            jump ddi_truth
        "Lie your way out of this":
            jump ddi_lie
        "Deflect the accusation onto Dr. Deceased":
            jump ddi_deflect

    label ddi_truth:
        player "No I did not! I was just preping my lunch when Dr. Deceased came in and started accusing me!"
        show syg at appear(x_align = 0.8)
        syg "How do you explain the body then?"
        player "I don't know! It was just there when I turned around after hearing Dr. Deceased!"
        hide syg
        n "You see a few in the crowd shake their heads."
        show aikha at appear(x_align = 0.2)
        aikha pensive "That was an unconvincing excuse, [player_name]. Did you not pay attention during my presentation?"
        player "It's not an excuse! I'm telling the truth! I don't even know who she is!"
        hide aikha
        n "Nobody dares to meet your gaze. The silence is telling of how little they believe you."
        n "A recognizable figure squeezes through the crowd. It's Dr. Alex."
        show deceased at move_to(x_align = 0.8)
        pause 0.5
        show alex
        n "You look towards him hopefully. Surely the Great Founder would remain calm and collected in the face of hysteria."
        player "Dr. Alex, you must-"
        alex sad "That's enough."
        alex "You've murdered my twin sister, [player_name]. (insert deep regret dialogues)"
        alex sad "Take the culprit away, security!"
        hide alex 
        hide deceased
        n "Two wals come forward and take you by the arms."
        n "You cast a resentful glare at the bystanders as you are dragged out of the lounge."
        n "Out of the corner of your eye, you see Dr. Chan and Ethy amongst the crowd of people."
        n "Dr. Chan looks deep in thought, while Ethy gives you a thumbs up with a wide grin."
        $ update_character_points({"chan": 1})
        #define variable here that lets chan defend you in court
        jump ddi_jail
        return


    label ddi_lie:
        n "still working on it"
        $ update_character_points({"chan": -1})
        # chan will not defend you in court, may or may not testify against you
        return

    label ddi_deflect:
        player "No, you were probably the one who killed her!"
        player "I bet you came back to clean up, but then ran into me here, so now you're trying to blame me!"
        deceased pensive "Huh." 
        deceased "{i}{size=25}I did forget what I came here for...unless...{/size}{i}"
        n "Dr. Deceased stares down at their own hands. Seemingly considering it." 
        show jessie surprise at appear (x_align = 0.2)
        jessie surprise "Dr. Deceased, did you really?"
        n "The crowd begin mumbling ans discussing amongst themselves."
        hide jessie
        menu: 
            n "This is a good chance to prove your innocence! (by blaming it on someone else!)"
            "Double down on Dr. Deceased":
                jump ddi_decease_murderer
            "insert some bad statement here":
                jump ddi_still_screwed_up

        label ddi_decease_murderer:
            player "How cold-blooded! And you've already forgotten about it this quickly, huh? You must be plenty used to commiting manslaughter!"
            # make "all" gasps here
            n "{i}{size=25}*gasps*{/size}{i}"
            deceased fury "What utter bullshit are you spilling now??"
            player "There's a reason why your department has one of the highest employee casualties, doesn't it?"
            # make "all" gasps here
            n "{i}*loud gasps*{/i}"
            deceased panic "nuh uh"
            player "yuh uh"
            deceased fury "{sc}NUH UH!!{/sc}"
            player "{sc}YUH UH!!{sc}"
            firewal "Affirmative. Security did show Dr. Deceased entering the lounge 5 minutes earlier. That lines up with [player_name]'s hypothesis."
            show aikha at appear(x_align = 0.8)
            aikha surprise "Dr. Deceased, I can't believe you would do this!"
            deceased "But I didn't! This...you bastard!"
            show alex at appear(x_align = 0.2)
            alex upset "Take them away to the confinement room! We shall hold a fair trial later to bring justice to my dear twin sister!"
            hide deceased
            hide alex
            hide aikha
            n "Two wals come into the room and start to drag Dr. Deceased away by their arm."
            n "Dr. Deceased tries to put up a fight. They swing their arms at the wals and kick them."
            n "Unfortunately, the wals are made of hard metals."
            n "Dr. Deceased's arms and legs break off from the impact. The wals carry their scattered remains away, while Dr. Deceased's head curses them with the curse of the nile."
            show helco at appear(x_align = 0.4)
            helco "What a tragedy this is. I'm sorry for your loss, [player_name]."
            player "..?"
            n "Dr. Helco simply stares into your eyes. Then he seems to remembered something."
            helco surprise "Ah. What I mean is, you must be shocked."
            player "...Yea, I was so startled."
            hide helco
            n "The crowd disperses and you decide to go back to prepping your sandwich. To your dismay, the wals has confiscated the knife as evidence for the murder."
            n "Guess you're not getting your greens in today."
            # define variable here for dr deceased to be the defendant
            $ update_character_points({"deceased": -1})
            return


        label ddi_still_screwed_up: #working on this
            player "lame uncredible statement"
            deceased "HA! NUH UH"
            # make the crowd say this
            n "Nuh uh..."
            deceased "smug statement"
            firewal "Affirmative. My memory module shows that Dr. Ralex specifically stated that the intern [player_name] has asked to meet them here to discuss matters concerning a potential full time offer."
            n "more dialogues"
            $ update_character_points({"deceased": 1}) 
            return

        
    label ddi_jail:
        n "hehehehehehehehehehe"


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
