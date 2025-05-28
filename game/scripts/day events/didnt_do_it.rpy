label day_event_didnt_do_it:
    $ tne_defendant = True
    $ tne_chan_backup = False
    $ hampeter_witness = False
    $ plague_mask = False
    $ tne_syg_backup = False
    scene bg lounge
    n "It's lunch break and you're hungry."
    n "You march into the lounge kitchenette. Today you even brough a whole lettuce to include in your sandwich. Healthy!"
    n "You realize that you've forgotten to bring your own knife today."

    label choice_loop:
        menu:
            n "There has to be a knife here somewhere, right? Your mouth isn't as big as Pochi's so you can't bite into a sandwich as big as your head."
            "Check the drawers":
                jump drawers
            "Check the fridge":
                jump open_fridge
            "Check cabinet":
                jump cabinet
            "Check the microwave":
                jump microwave
            
        label cabinet:
            n "You open the cabinet above your head."
            n "A plague doctor mask falls out and its beak stabs you on the head. Ouch."
            n "Who left their hat here??? How irrisponsible."
            n "You shove it back into the cabinet for it to hit the next unfortunate person who opens it."
            $ plague_mask = True
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
            $ hampeter_witness = True
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
    n "You drop the knife and almost stabbed your toe. You turn around, slighly annoyed."
    show deceased surprise 
    deceased "YOU MURDERER!"
    n "Murderer? What are they talking about?"
    # optoinal dead dr. ralex cg
    n "You bend down to pick up your knife when you saw it. A dead woman right next to your feet, bleeding out a pool of red the same color as the stains on the knife."
    n "You were wondering who she is and how can an unauthorize person get in here when Dr. Deceased interuptes your thought." 
    deceased panic "{size=+10}{sc}{b}THERE'S A MURDER!!!{/b}{/sc}{/size}"
    player "Wait, Dr. Deceased-"
    n "Your voice is cut off by the swarm of people now stuck stomping in the doorway, all trying to get a closer look at the crime scene."
    deceased fury "Everyone look! [player_name] murdered Dr. Ralex!"

    menu:
        n"How do you defend yourself?"
        "Tell the truth":
            jump ddi_truth
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
        alex fury "Take the culprit away, security!"
        hide alex 
        hide deceased
        n "Two wals come forward and take you by the arms."
        n "You cast a resentful glare at the bystanders as you are dragged out of the lounge."
        n "Out of the corner of your eye, you see Dr. Chan and Ethy amongst the crowd of people."
        n "Dr. Chan looks deep in thought, while Ethy gives you a thumbs up with a wide grin."
        $ update_character_points({"chan": 1})
        $ tne_defendant = True
        $ tne_chan_backup = True
        jump ddi_jail
        return

    label ddi_deflect:
        player "No, you were the one who killed her!"
        ethy "{sc}{size=+10}{b}AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!!!{/b}{/size}{/sc}"
        n "You fight the instinct to cover your ears from the piercing scream you hear in your head."
        player "I bet you came back to clean up, but then ran into me here, so now you're trying to blame me!"
        deceased pensive "Huh." 
        deceased "{i}{size=25}I did forget what I came here for...unless...{/size}{i}"
        n "Dr. Deceased stares down at their own hands. Seemingly considering it." 
        show jessie surprise at appear (x_align = 0.2)
        jessie surprise "Dr. Deceased, did you really?"
        n "The crowd begin mumbling ans discussing amongst themselves."
        hide jessie
        $ update_character_points({"chan": -1})

        if plague_mask == True:            
            menu: 
                n "This is a good chance to prove your innocence!" 
                "Bring up the plague doctor mask you found.": # secret deceased trial ending
                    jump ddi_decease_murderer
                "Bring up the high casualty rate of Dr. Deceased's department.": # bad argumment, jail ending, deceased is unhappy because you brought up their sore spot
                    jump ddi_bad_argument
                "Make up a motive for Dr. Deceased to kill.": #also bad argument jail ending, but gain a point because deceased is happy with winning
                    jump ddi_poor_argument
        elif plague_mask == False:
            menu:
                n "This is a good chance to prove your innocence!" 
                "Bring up the high casualty rate of Dr. Deceased's department.": # bad argumment, jail ending, deceased is unhappy because you brought up their sore spot
                    jump ddi_bad_argument
                "Make up a motive for Dr. Deceased to kill.": #also bad argument jail ending, but gain a point because deceased is happy with winning
                    jump ddi_poor_argument

        label ddi_decease_murderer:
            player "In fact, I have evidence that you've been here!"
            ethy "{sc}{size=+3}{b}aaaa...?{/b}{/size}{/sc}"
            n "Despite Ethy's scream trailing off, you can tell that you're not clear of suspicion yet."
            n "You step over the pool of blood and open the cabinet. The plague mask falls out once again, stabbing you on the head."
            # make "all" gasps here
            n "{i}{size=25}*gasps*{/size}{i}"
            n "All eyes gaze towards Dr. Deceased."
            deceased surprise "{i}{size=25}Oh. So that's what I came into the lounge for.{/size}{i}"
            deceased panic "S- So what? It can belong to anyone!"
            player "It looks identical to the one you're wearing, Dr. Deceased."
            deceased "Nuh uh."
            player "Yuh uh."
            deceased fury "{sc}NUH UH!!{/sc}"
            player "{sc}YUH UH!!{sc}"
            show firewal at appear(x_align = 0.3)
            firewal "Affirmative. Security did show Dr. Deceased entering the lounge 5 minutes earlier. That lines up with [player_name]'s hypothesis."
            hide firewal
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
            player "...?"
            n "Dr. Helco simply stares into your eyes. Then he seems to remembered something."
            helco surprise "Ah. What I mean is, you must be shocked."
            player "...Yea, I was so startled."
            hide helco
            n "The crowd disperses and you decide to go back to prepping your sandwich. To your dismay, the wals have confiscated the knife as evidence for the murder."
            n "Guess you're not getting your greens in today."
            $ tne_defendant = False
            $ tne_chan_backup = False
            return

            label ddi_bad_argument: 
            player "How cold-blooded! And you've already forgotten about it this quickly, huh? You must be plenty used to commiting manslaughter!"
            # make "all" gasps here
            n "{i}{size=25}*gasps*{/size}{i}"
            deceased fury "What utter bullshit are you spilling now??"
            player "There's a reason why your department has one of the highest employee casualties, doesn't it?"
            show chan pensive at appear(x_align=0.8 )
            chan "I must say, [player_name], that doesn't have much to do with the current situation."
            chan "It is also inappropriate to base one's character on groundless spectulations."
            deceased happy "Thank you! Dr. Chan."
            deceased fury "So you are the bitching type, huh?" #there a word for this but I cannot remember, basically refering to player as a person who makes up/exaggerates rumors 
            deceased "I'll have you know that unlike you, I speak based on facts and evidence!"
            deceased "And I have evidence on why you would kill Dr. Ralex!"
            # make "all" gasps here
            n "{i}*loud gasps*{/i}"
            deceased "You wanted to be promoted to a fulltime employee, but Dr. Ralex rejected you!"
            player "Wha-"
            deceased "Which is why in desperation, you took a knife to threaten her! But you're so emotional and not in controled that you accidentally stabbed her and she died!"
            show firewal at appear(x_align = 0.2)
            firewal "Affirmative. My memory module shows that Dr. Ralex specifically stated that the intern [player_name] has asked to meet them here to discuss matters concerning a potential full time offer. This aligns with Dr. Deceased's hypothesis."
            player "That's bullshit! I have never even seen Dr. Ralex before!!!"
            deceased neutral "Tsk tsk, just look at you now. You're clearly emotionally unstable and you're still trying to lie your way out of this."
            hide deceased
            hide chan
            firewal "INSTRUCTION RECIEVED. THE WAL and the Founder Alex have issued an order: arrest the suspect and prep for a trial immediatly. Executing now."
            n "The wal come forward and take you by the arms. You try your best to shove him away from you, but you're no match against the ingenious creations of Dr. Firewal."
            n "He picks you up and throws you over his metallic shoulders an carry you off like a stack of potatoes."
            hide firewal
            $ update_character_points({"deceased": -1})
            $ tne_defendant = True
            $ tne_chan_backup = False
            jump ddi_jailtwo
            return

        label ddi_poor_argument:
            n "You side eye the unfamiliar, cold body on the ground. You have no idea who she is, or her relationship with anyone in the room."
            n "What would Dr. Deceased gain from this? That's when you notice the keychain peeking out of the soaked lab coat."
            n "You knee down and pick it up. Its iconic blue twintails look awfully similar. An idea clickes in your head."
            player "You must've done it because of this!"
            deceased surprise "Huh??"
            player "Dr. Ralex stole your prized keychain, so you confronted her for it! But you accidentally killed her during a struggle!"
            n "You can see a few of the audiance nodding. Wow, you didn't actually think Dr. Deceased would give people this impression."
            deceased pensive "..."
            show deceased happy
            n "To your surprise, Dr. Deceased starts cackling like a crow. Like many crows."
            deceased "I see what you're trying to get at. Unfrotunetly for you, I gave this to Dr. Ralex myself!"
            deceased "{i}{size=25}After losing a bet, that is.{/size}{i}"
            n "Dr. Deceased snatchs the keychain out of your hand."
            deceased neutral "I think it's pretty obvious who the murderer is now, right?"
            hide deceased
            n "You look around the room desperately. No one meets you eyes."
            show firewal at appear(x_align = 0.2)
            firewal "CONCLUSION: Arrest the suspect and prep for a trial immediatly. Executing now."
            hide firewal
            n "Two wals come forward and take you by the arms. You try your best to fight them off, but you're no match against the ingenious creations of Dr. Firewal."
            n "They pick you up easily by your arms and legs and carry you out while swinging you like a hammock."
            n "On the way out of the lounge, you stare resentfully Dr. Deceased, who looks satisfied with winning this debate and getting an addition to their collection."
            $ update_character_points({"deceased": 1})
            $ tne_defendant = True
            $ tne_chan_backup = False
            jump ddi_jailtwo
            return

        
    label ddi_jail:
        scene bg containment
        n "You stare out the thick, anomaly-secured glass. Is this what anomalies feel like when contained?"
        n "It's not too bad. You wager this containment room is larger than any jail cell."
        n "You were about to gaslight yourself into acceptance when the door opens and Dr. Syg walks in. Your first prison visit!"
        show syg at appear
        n "You feel like Dr. Syg looks a little more content than usual. You wishfully hope that he's happy to deliver good news, rather than happy that you're in containment."
        syg "Hello, [player_name]."
        player "Dr. Syg, am I free?"
        syg "Oh no. I'm here to ask if you would like to contribute to the Demonic Studies Department in the event that you are found convicted."
        player "...?"
        syg "We have been running low on demon feed. They're usually death row immates convicted of crimes such as murder or worse."
        syg "Ex-Foundation employees however are have the employment benefit to choose the method of execution. But I would really appreciate it if you would like to chip in."
        n "He pulls out a contract and questionable red ink."
        menu:
            syg "It's for a great cause. I'll make sure it's painless."
            "Sign it, for science.":
                n "You pick up the quill and sign your name. You hope Dr. Syg can keep his words."
                n "Dr. Syg looks very content. In fact, you can {i}almost{/i} say he's smiling."
                syg "I will do my best to avocate for a {i}desirable{/i} outcome on your trial."
                hide syg
                n "You're unsure if he meant desirable for him or you. You decide not to ask."
                $ tne_chan_backup = True
                $ update_character_points({"syg": 1})
                n "You lie down on the cold floor and wonder will this truly spell the end of your career. And your life."
                return

            "Don't sign it. Surely you won't be found guilty.":
                syg "That's a shame."
                syg pensive "Let me know if you change your mind later."
                hide syg
                syg "He leaves, significantly less content."
                $ tne_syg_backup = False
                $ update_character_points({"syg": -1})
                n "You lie down on the cold floor and wonder will this truly spell the end of your career. And your life."
                return
        
        label ddi_jailtwo:
            #can we make the fade in a bit slower
            scene bg containment
            n "You stare out the thick, anomaly-secured glass. Is this what anomalies feel like when contained?"
            n "It's not too bad. You wager this containment room is larger than any jail cell."
            n "You lie down on the cold floor and wonder will this truly spell the end of your career. And your life."
            return





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
