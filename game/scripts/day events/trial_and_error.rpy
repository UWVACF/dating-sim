label day_event_trial_and_error:
#    For court main:
#        master:
#            uriel (don't specify zorder)
#            judge's table (zorder 90)
#        master2:
#            stage (zorder -1)
#            defendant (don't specify zorder)
#            side wall of stage (zorder 90)
#    For court side:
#        master:
#            person
#            stage (zorder 90)
    
    image judge overlay = "images/cgs/court_main_overlay.png"
    image defendant overlay= "images/cgs/court_main_overlay2.png"
    image front defendant overlay = "images/cgs/court_main_overlay3.png"
    image side overlay = "images/cgs/court_side_overlay.png"
    image shock = "images/cgs/shock effect.png"

    # to remove when not testing
    #$ tne_chan_backup = renpy.input("Ture or False for Chan on your side (did not lie in I didn't do it)")
    #$ tne_chan_backup = tne_chan_backup.strip()=="True"
    #
    #$ hampter_witness = renpy.input("Ture or False for hampt witness (found hampter in the vents)")
    #$ hampter_witness = hampter_witness.strip()=="True"
    #
    #$ tne_syg_backup = renpy.input("Ture or False for syg back you up (agreed to become demon food if you're on death row)")
    #$ tne_syg_backup = tne_syg_backup.strip()=="True"

    # for showcase
    $ tne_chan_backup = True
    $ tne_syg_backup = False
    $ hampter_witness = True

    scene bg court main
    $ trial_credibility_you = 0
    show judge overlay onlayer master zorder 90
    show defendant overlay onlayer master2 zorder -1
    show front defendant overlay onlayer master2 zorder 90
    show uriel onlayer master:
        appear(0.5, y_align = 0.0)
    pause 1
    uriel "Today we are here for the trial of the murder of Dr. Ralex. I will be your judge, and will oversee this procedure."
    n "Huh. You didn't know that Uriel has a side gig as a judge outside of being the head of legal."
    show deceased onlayer master2:
        alpha 0 
        xzoom -1.0
        alpha 1.0
        appear(-0.1, y_align = 1.3)
    uriel "The accused, [player_name], was found to be the prime suspect of this murder, with Dr. Deceased being the prosecutor."
    uriel "I would like to introduce Dr. Chan as the jury."
    show chan onlayer master at appear(x_align = 1.0)
    n "One singular person as the jury. What an official trial."
    chan "Thank you, Uriel. I swear that I will remain fair."
    show chan unique
    ethy "AA."
    chan "Ethy will help me determine if the prosecutor or the defendant are lying."
    uriel "The court session will now start."
    # insert trial start cg or something
    show chan neutral
    uriel sad "Our co-founder, Dr. Ralex was found dead earlier during lunch in the lounge."
    uriel upset "After {i}thorough{/i} investigation, the security department has determined that the intern, [player_name] is the most likely suspect to this crime."
    uriel "Evidence suggests that [player_name] met with Dr. Ralex to discuss a full time position offer, and resorted to murder when [player_sub] got rejected."
    uriel neutral "Hence, it is concluded that [player_name] shall be charged with first degree murder. [player_name], do you plead guilty to these charges?"
    menu:
        uriel "Hence, it is concluded that [player_name] shall be charged with first degree murder. [player_name], do you plead guilty to these charges?{fast}"
        "No":
            jump tne_no
        "No":
            jump tne_no
        "No":
            jump tne_no
        "Yes":
            jump tne_yes
    
    label tne_no:
        player "No, I don't. Because..."
        menu:
            player "No, I don't. Because...{fast}"
            "Dr. Deceased is the real murderer!":
                $ trial_credibility_you += -1
                player "As I've said before, I think Dr. Deceased is the real murderer!"
                deceased "OBJECTION!"
                deceased "SPECULATION! Do you have evidence?"
                uriel pensive "It is not your turn to speak, Dr. Deceased."
                uriel neutral "The defendant's statement is rejected due to lack of evidence. Also, for being irrelevant to my question."
                deceased "{size=3}Yadayada.{/size}"
                uriel "We will proceed with presenting evidence. Dr. Deceased, you may speak."
                jump objection_time

            "I don't know Dr. Ralex!":
                $ trial_credibility_you += 1
                player "I don't know Dr. Ralex! I've never seen her before!"
                chan "...No reaction from Ethy."
                deceased "So? Are you telling me that I'm supposed to remember everyone that I've killed?"
                player "?"
                uriel upset "...Silence, Dr. Deceased. It is not your turn to speak."
                deceased "..." #angry
                uriel neutral "Since the defendant does not plead guilty, we will proceed with presenting evidence. Dr. Deceased, {i}now{/i} you may speak."
                jump objection_time

    label objection_time:
        scene bg court side

        hide deceased onlayer master2
        hide defendant overlay onlayer master2
        hide front defendant overlay onlayer master2
        
        show side overlay zorder 90
        show deceased objection as dece_point:
            xalign 0.4
            yalign 1.3
            xzoom 1.4
            zoom 1.3
        show shock onlayer master2
        $ shake_screen(layers="master2", duration=0.1, strength=4, repeat=True)
        deceased "OBJECTION!"
        show shock onlayer master2:
            alpha 0.0
        uriel "Nevermind. I suppose Dr. Deceased will not be speaking."
        deceased "Wait no! I have a point I promise!"
        show shock onlayer master2:
            alpha 1.0
        deceased "I have evidence that this is an orchestrated murder!"
        deceased "The fact that [player_name] had a knife is solid proof!"
        show deceased objection as dece_point:
            alpha 0.0
        show deceased: 
            alpha 0.0
            xalign 0.2
            yalign 0.3
            xzoom -1.0
            alpha 1.0
        show shock onlayer master2:
            alpha 0.0
        deceased happy "According to foundation protocols, the kitchenette cannot be used to store dangerous objects such as knives!" #pensive
        deceased neutral "Hence, the knife was brought in by [player_name] [player_ref]."
        show deceased:
            alpha 0.0
        show deceased objection as dece_point:
            alpha 1.0
        show shock onlayer master2:
            alpha 1.0
        deceased "Which could only mean that Dr. Ralex's murder was planned!"
        n "You see a few in the audience nodding their heads. This isn't looking good for you."
        menu:
            n "Object to Dr. Deceased!"
            "The knife doesn't belong to you - you found it in the fridge.":
                $ trial_credibility_you += 1
                show shock onlayer master2:
                    alpha 0.0
                show deceased:
                    alpha 1.0
                show deceased objection as dece_point:
                    alpha 0.0
                player "I found the knife in the fridge! It's not mine!"
                chan "...No reaction from Ethy."
                deceased "Consider this: [player] simply forgot [player_sub] put it there! This happens all the time to me!"
                uriel "...Dr. Deceased, how mnay knives have you left around foundation grounds?"
                deceased "How am I supposed to remember all that?"
            "The protocol Dr. Deceased mentioned must be false - here are other dangerous weapons.":
                $ trial_credibility_you += -1
                show shock onlayer master2:
                    alpha 0.0
                show deceased:
                    alpha 1.0
                show deceased objection as dece_point:
                    alpha 0.0
                player "There are other dangerous weapons at the foundation! A knife is nothing!"
                n "To prove your point, you pull out from your pockets: a ceremonial dagger from the demonics department, radioactive materials from Dr. Lee, six brass knuckles for spider legs-"
                n "-a nuclear warhead from a Wal, two taser traps from the Extraterrestial department, a blend of fifteen espresso shots and ten Red Bulls (not exactly a weapon but should be considered one)-"
                roose "HONK HONK HONK??? HONK HONK HONK!??"
                n "Oh, and that goose. That one in particular. I'm most scared of that one."
                n "{i}How{/i} did you get all that???"
                show shock onlayer master2:
                    alpha 1.0
                show deceased:
                    alpha 0.0
                show deceased objection as dece_point:
                    alpha 1.0
                deceased "OBJECTION! Irrelevance!"
                deceased "What matters is that you were in possession of the murder weapon which is clear contraband!"

        show shock onlayer master2:
            alpha 0.0
        show deceased:
            alpha 1.0
        show deceased objection as dece_point:
            alpha 0.0
        deceased "And another thing! Why were you even in the lounge?"
        deceased "It wasn't lunch time yet! Dr. Ralex shouldn't have been there either."
        show shock onlayer master2:
            alpha 1.0
        show deceased:
            alpha 0.0
        show deceased objection as dece_point:
            alpha 1.0
        deceased "You had absolutely no reason to be there. Hence, the only logical deduction is that you were planning to murder Dr. Ralex in the lounge!"
        menu:
            n "Object Dr. Deceased's accusations!"
            "You finished your work and were craving an early lunch.":
                $ trial_credibility_you += 1
                show shock onlayer master2:
                    alpha 0.0
                show deceased:
                    alpha 1.0
                show deceased objection as dece_point:
                    alpha 0.0
                player "No, I finished my work, so I just wanted to have lunch early!"
                chan "Ethy says that the first half of the statement does not seem truthful."
                player "...Fine, but I was only there to make my sandwich! You all saw my sandwich ingredients!"
                deceased "Malarkey! If they were in the fridge I would've eaten them."
                player "..."
                show shock onlayer master2:
                    alpha 1.0
                show deceased:
                    alpha 0.0
                show deceased objection as dece_point:
                    alpha 1.0
                
            "Nobody follows strict work schedules - Dr. Deceased themselves were also there.":
                show shock onlayer master2:
                    alpha 0.0
                show deceased:
                    alpha 1.0
                show deceased objection as dece_point:
                    alpha 0.0
                $ trial_credibility_you += -1
                player "I could say the same for you, and everyone else who was there!"
                deceased "I'm a department head! I set my own work schedule!"
                chan "Actually, you don't."
                deceased "..."
                show shock onlayer master2:
                    alpha 1.0
                show deceased:
                    alpha 0.0
                show deceased objection as dece_point:
                    alpha 1.0
                deceased "Regardless! In that case we both didn't have valid reasons to be there! But, all the other evidence points to you!"

        show shock onlayer master2:
            alpha 0.0
        show deceased:
            alpha 1.0
        show deceased objection as dece_point:
            alpha 0.0
        deceased "I have no further questions."
        hide shock onlyer master2
        hide deceased objection as dece_point
        show layer master2

        scene bg court main
        show judge overlay onlayer master zorder 90
        show defendant overlay onlayer master2 zorder -1
        show front defendant overlay onlayer master2 zorder 90
        show uriel onlayer master:
            xalign 0.5
            yalign 0.0

        show deceased onlayer master2:
            alpha 0 
            xzoom -1.0
            alpha 1.0
            xalign -0.1
            yalign 1.3

        show chan onlayer master:
            xalign 1.0
            yalign 1.0

        uriel "In that case, let us hear from the character witnesses."
        if tne_chan_backup or hampter_witness or tne_syg_backup:
            if tne_chan_backup == True or "True":
                uriel pensive "First, Dr. Chan."
                show uriel neutral:
                    xzoom -1.0
                uriel neutral "You said you wanted to make a statement, right?"
                show uriel neutral
                $ trial_credibility_you += 0.5
                chan unique "Yes. I can attest that [player_name] was not lying when they said [player_sub_be] not the murderer at the crime scene. Ethy can back me up."
                n "Ethy gives you two thumbs up."
                if trial_credibility_you <= 0:
                    chan "I'm cannot say the same about [player_pos_adj] statements today, but I swear that me and Ethy are reporting truthfully."
                uriel "Thank you, Dr. Chan."
                ethy "AAA."
                uriel "And Ethy."
            if tne_syg_backup == True or "True":
                show uriel neutral:
                    xzoom -1.0
                if tne_chan_backup == True or "True":
                    uriel pensive "Next, Dr. Syg."
                else:
                    uriel pensive "You may make your testimony, Dr. Syg."
                uriel neutral "Would you like to make a statement?"
                $ trial_credibility_you += 0.5
                show syg onlayer master2:
                    alpha 0
                    alpha 1.0
                    appear(1.0, y_align = 1.3) 
                syg "I believe in [player_name]."
                uriel neutral "Based on..?"
                syg "..."
                n "Dr. Syg gives you an affirming nod before shadows envelop him."
                show syg onlayer master2 at disappear
                uriel "Well, alright then."
            if hampter_witness == True or "True":
                if tne_chan_backup == False or "False" and tne_syg_backup == False or "Flase":
                    uriel "We have a witness. Hampter, you may come in and make your testimony."
                else:
                    uriel pensive "We also have a witness. Hampter, you can come in."
                $ trial_credibility_you += 1
                show hampter panic onlayer master2:
                    alpha 0
                    alpha 1.0
                    appear(1.0, y_align = 1.3)
                hampter "Uh. Hello."
                deceased "Hampter, you said that you were at the crime scene. Can you describe what you were doing?"
                show hampter happy onlayer master2
                hampter happy "Oh, yes. I was napping in the vents when [player_name] woke me up."
                deceased pensive "And what was [player_name] doing?"
                hampter "[player_be!c] [player_sub] looking for something, I think. After that, I went back to napping." 
                show hampter panic onlayer master2
                hampter panic "Then five minutes later, I heard Dr. Deceased scream."
                deceased "I did NOT scream! It was an exclamation!"
                deceased "*ahem* So you didn't hear any struggling?"
                hampter "No, I didn't."
                deceased "Hampter, you mentioned that you were napping. Are you 100\% certain that no struggling occurred?"
                hampter panic "Uh...I..."
                deceased "Are you 100\% certain that that was [player_name]? Could it be possible that you were, quote, 'tweaking'?"
                hampter "Uh...uh...uh"
                show hampter panic onlayer master2 at disappear
                n "Hampter disappears in a blink of an eye."
                chan neutral "I believe the witness is too stressed to continue. But I think we have enough statements."
        else:
            show uriel pensive
            n "..."
            uriel happy "It seems that you do not have any of those. That is tragic."
        
        uriel neutral "We shall decide on the verdict now, then."
        if trial_credibility_you > 2:
            uriel "[player_name], you are found..."
            uriel "Not guilty. Congratulations."
            n "Two Wals come up to you and free you from your handcuffs."
            uriel "There is insufficient evidence to prove [player_name] as the murderer."
            uriel "The case will be given to the Walbots security team to investigate further."
            uriel "Court dismissed."
            jump after_court_innocent
        else:
            uriel neutral "[player_name], you are found..."
            uriel fury "Guilty!"
            uriel "For your crimes of murdering our great co-founder, I sentence you to-"
            venture_unknown "Wait! Wait!"
            show chan surprise
            uriel upset "Who dares to interrupt!"
            show venture onlayer master2 zorder 91:
                appear(0.7, y_align = 2.0)
            venture "There has been a great misunderstanding!"
            uriel "Misunderstanding?"
            venture "Yes, yes. This was all caused by an anomaly!"
            venture "The knife that was suspected as the murder weapon was an anomalous knife that creates illusions of murder scenes with false victims!"
            show venture onlayer master2:
                xzoom -1.0
            chan pensive "Hmm. Now that you speak of it, I do vaguely remember such an anomaly in containment."
            chan neutral "But, I recall that individuals with high ONERIO such as Founder Alex and I should be immune to its effects. So it cannot be that anomaly, can it now?"
            show uriel neutral
            venture "About that...I was working with the anomaly for an alchemical experiment."
            chan pensive "...What was your experiment about, Dr. Venture?"
            venture "To amplify its cognitive effects, and investigate the material origin of the corpse it manifests."
            chan fury "..."
            chan "We will have a meeting {i}soon{/i} about practicing ethics and responsibilities when choosing research topics, Dr. Venture."
            show venture onlayer master2:
                xzoom 1.0
            uriel "Hold on, Dr. Venture. Do you have evidence to back up your claim?"
            chan pensive "I believe that a thorough investigation into Dr. Ralex should reveal some inconsistencies in our knowledge of her, as well as a lack of actual record of her work."
            uriel "If you say so, Dr. Chan."
            uriel pensive "In that case, the trial shall be put on hold until further investigation is complete."
            uriel neutral "[player_name], you will remain in custody for the time being."
            show uriel pensive
            show chan upset
            n "Dr. Venture gives you a wink of reassurance."
            n "Two Wals come up to you and drag you back into the containment room."

            show black_screen onlayer top:
                alpha 0.0
                linear 1.0 alpha 0.1
            scene bg containment
            hide venture onlayer master2
            hide deceased onlayer master2
            hide defendant overlay onlayer master2
            hide front defendant overlay onlayer master2
            hide black_screen onlayer top
            
            n "You're back in the fucking building again."
            n "I mean, the containment room."
            n "You have no idea how long you'll be here this time."
            n "Given what you know about the efficiency of the Wals security team, this investigation might take longer than your internship."
            n "Meaning, the only thing you will be putting on your resume for this internship is \'jail time\'."
            n "Perhaps, \'experience in containment\' will sound better."
            n "You begin drafting your resume update with the fog you breathe on the glass wall when Dr. Venture walks in."
            show venture at appear
            venture "...Are you kissing the glass?"
            venture "Sorry, I didn't expect this incident to cause you this much...distress."
            venture "Anyways, good news!"
            venture "You're free!"
            player "...That was quick."
            venture "Well, yes. Since Dr. Chan was familiar with the anomaly, he aided in the investigation process."
            venture "However, as personnel who were involved in, ahem, \'a misconducted experiment\', both you and I are to each write 5 incident reports, complete 3 ethic courses, and commit to 7 hours of community services."
            player "Why am I involved???"
            venture "Well, while I could explain that you {i}didn't{/i} commit murder, I have no idea how you came into contact with the knife."
            venture "They probably wouldn't let it go so easily if the story isn't complete. You catch my drift?"
            venture "So I just said you were assigined as my temporary assistant for this experiment."
            player "...So, why was the knife there?"
            venture "...Haha."
            n "You stare Dr. Venture right in the eye. If looks could kill, you would've committed your first murder right here."
            venture "...I forgot it in the fridge while I was getting a snack."
            $ update_character_points({"alex": -1, "aikha": -1, "ryz": -1, "helco": -1, "uriel": -1, "firewal": -1, "chan": -1, "hamp": -1, "deceased": -1, "syg": -1})
            return

    label tne_yes:
        n "...Why would you admit guilt to something you didn't do?"
        player "Yes, I do."
        $ trial_credibility_you += -0.5
        show deceased happy onlayer master2
        deceased happy "AHA!!! I KNEW IT!"
        show deceased neutral onlayer master2
        uriel panic "Well, case closed, I suppose."
        uriel neutral "So, [player_name], you are officially convicted of the murder of Dr. Ralex. We will now decide on your sentence-"
        chan "Hold on!"
        chan "...[player_sub_be!c] lying."
        show uriel:
            xzoom -1
        uriel "Lying about what?"
        chan "Ethy screamed in my ears when [player_sub] said yes to the crime. "
        chan pensive "Which means that that statement was said with a deceitful intent."
        show uriel:
            xzoom 1
        show chan neutral
        pause 0.5
        uriel upset "Did you lie, [player_name]?"
        uriel "Perjury is a serious crime. So answer truthfully, {i}do you plead guilty to the charges of planning and murdering Dr. Ralex?{/i}"
        menu:
            uriel "Perjury is a serious crime. So answer truthfully, {i}do you plead guilty to the charges of planning the murder of Dr. Ralex?{/i}{fast}"
            "No":
                jump tne_yes_no
            "No":
                jump tne_yes_no
            "No":
                jump tne_yes_no
            "Yes":
                jump tne_yes_yes

    label tne_yes_no:
        chan "In that case, let us return to normal procedures."
        uriel neutral "Since the defendant does not plead guilty, we will proceed with presenting evidence. Dr. Deceased, {i}now{/i} you may speak."
        jump objection_time
        
    
    label tne_yes_yes:
        player "Yes, I do."
        n "Hey, this isn't a marriage proposal."
        $ trial_credibility_you += -0.5
        chan "...[player_sub_be!c] still lying."
        deceased "Yo what is this intern doing!?" #fury or something
        deceased "Aha! I get it! I get it! Ethy sensed dishonestly because you {i}don't feel guilty at all!{/i} What a cold-hearted criminal!"
        deceased "Judge {i}Urinal{/i}, I say we should just throw [player_obj] into the dungeons-"
        uriel fury "{size=+10}Such contempt! I will not have this in my courtroom!{/size}"
        uriel "You will be charged with the crimes of contemning the court!"
        show uriel upset
        chan "Uh, Uriel, we should probably conclude the murder charge first."
        if tne_chan_backup == "True" or True:
            chan "So [player_name], I recall you had previously denied the murder at the crime scene. Is there a reason why you're lying now?"
            chan unique "I totally understand if it is out of spite, but please rest assured that we are fair and just here at the court."
        elif tne_chan_backup == False or "False":
            chan unique "[player_name], you are legally obligated to answer truthfully in court."
            chan "It gains you no benefit to not do so."
        chan "So let me ask you again, did you kill Dr. Ralex?"
        menu:
            chan "So let me ask you again, did you kill Dr. Ralex?{fast}"
            "No":
                jump tne_yes_yes_no
            "No":
                jump tne_yes_yes_no
            "No":
                jump tne_yes_yes_no
            "Yes":
                jump tne_yes_yes_yes

        label tne_yes_yes_no:
            chan "In that case, let us return to normal procedures."
            uriel neutral "Since the defendant does not plead guilty, we will proceed with presenting evidence. Dr. Deceased, {i}now{/i} you may speak."
            jump objection_time


        label tne_yes_yes_yes:
            n "Did you forget how to say no? It's N-O. NO."
            $ trial_credibility_you += -1
            if "anendophasia" in seen_events:
                n "If you really want to go to jail, I'm leaving again. I don't want to be stuck narrating for you in a 20ft cell for the rest of time."
            show chan surprise
            player "Yes, I did."
            deceased "Hey, is this neccesary? [player_name] already admitted guilt. We should just chuck [player_obj] in jail and get it over with."
            show uriel upset:
                xzoom -1
            chan unique "But [player_sub_be] lying, which means [player_sub_be] not responsible for the murder."
            show uriel upset:
                xzoom 1
            deceased "What reason would [player_sub] have to lie???"
            show uriel upset:
                xzoom -1
            chan upset "We don't know!"
            show chan neutral
            show uriel upset:
                xzoom 1
            deceased "What if {i}you're{/i} lying?"
            chan surprise "Excuse me?"
            show uriel neutral
            deceased "How would I know if you're telling the truth? What if you're helping [player_name]? What if {i}Ethy{/i} is helping [player_name]?"
            chan upset "That's ridiculous! Dr. Deceased, this is slander!"
            show uriel:
                xzoom -1
                pause 0.3
            show chan surprise
            uriel upset "...Are you lying, Dr. Chan?"
            chan fury "You can't be serious! Uriel, Deceased is talking nonsense!"
            show uriel fury
            n "You watch as the room erupts into chaos. The trial is surely not proceeding in this state."
            show uriel sad:
                xzoom 1
            show chan sad
            n "Was this your plan all along? You're smarter than I thought."
            if "anendophasia" in seen_events:
                n "...You ask why I haven't left yet?"
                show uriel upset
                show chan upset
                n "As much as I don't want to spend the rest of time in jail with you, I have less desire to narrate for these people."
            show uriel fury
            show chan fury
            n "You look around the room. The three personnel in front of you are engaged in a heated argument. The audience members are also discussing amongst themselves. Walbot security is nowhere to be seen."
            show uriel upset:
                xzoom -1
            show chan surprise
            n "This would be the perfect chance to sneak out. You silently take a step back. Then two. Then three."
            show uriel pensive
            show chan unique
            n "You turn around to see that the exit is unguarded, and decide to make a break for it."
            show uriel upset:
                xzoom 1
            show chan neutral
            
            scene bg room hall
            scene onlayer master2
            with default_fade
            n "You've escaped! Though you've probably lost your job."
            n "From the [day_number - 1] days you've been here, you can confidently assume that this incident will be forgotten within a matter of days."
            n "In other words, you're basically free as long as you make it out of the building and don't come back."
            n "Seems all clear. Now run for it-"
            venture_unknown "[player_name]!"
            n "OH FUCK-"
            n "Quick! Commit a real murder!"
            n "You've already been charged for one murder, might as well make it count!"
            show venture at appear
            pause 0.5
            show venture at move_to(x_align = 0.6, duration = 0.1)
            $ shake_screen()
            n "You pull the trigger before you even take a proper look at who you're shooting."
            n "Unfortunately, not looking at your target makes it really easy to miss a shot."
            venture "Woah woah woah. Woah there buddy."
            venture "Let's calm down, shall we?"
            n "Before you can shoot another shot, Dr. Venture quickly pulls a flask out from his pocket and throws it at you. The glass shatters on your forehead, drenching you in unknown liquid."
            n "You feel your limbs go numb as you drop your gun on the ground."
            venture "That was dangerous. Now, are we calm enough to have a civil conversation?"
            n "You stare daggers at Dr. Venture as you slump against the wall."
            venture "I don't know why you're so on edge, but I won't do anything to you. I just want to ask about something."
            player "You're not here to arrest me?"
            venture "Huh? Arrest you?"
            show venture #pensive
            venture "Aha. I see what's going on."
            venture "No, I'm not here to arrest you. In fact, I'm here to help you."
            venture "But for me to help you, I'll need you to answer some questions."
            n "You reluctantly nod your head. You don't really have another choice right now, do you?"
            n "You hear rapid footsteps from the direction of the multi-purpose room-turned-courtroom. Dr. Venture seems to have heard it too."
            n "He pulls out a scroll with a complex rune on it and slaps it onto you."
            hide venture
            scene bg lab
            show black_screen onlayer master zorder 0:
                alpha 0.75
            n "You're immediately warped to an unknown space."

            show venture at appear
            n "Dr. Venture reappears in front of you a few moments later."
            venture "Damn, you really got yourself into some big trouble, huh?"
            venture "So I take it that you touched the knife?"
            player "Knife?"
            venture "An anomalous knife I was conducting research on. Touching it frames you for murder."
            n "You think back to what you were doing when it all happened." 
            n "You were in the lounge preparing your lunch. Then, you wanted to cut your lettuce, but you had forgotten your own knife."
            n "So you tried looking for one in the kitchenette. Then-"
            player "Right, I found a knife in the fridge."
            n "Dr. Venture lets out a sigh. Then, he pats your shoulders."
            venture "Looks like we're stuck in the same boat, then."
            player "What do you mean?"
            venture "Well, that anomaly escaped containment from my lab due to some...accidents. So it's, supposedly, under my responsibility."
            venture "But, if we can retrieve it without getting caught, I have a way to resolve this situation."
            venture "You'll be proven innocent, and I won't get in trouble for the \'accidents\'. It's a win-win."
            n "You nod. Although Dr. Venture doesn't seem entirely reliable, you see no other way out of this situation that involves keeping your job."
            venture "Great!" 
            venture "So, I've already located the knife. It's currently being kept in the evidence room of the security department."
            venture "But, with you currently on the run, all the Walbots have been deployed to search for you. That means that there should only be one Walbot looking after the storage."
            venture "I'll go distract the others to make sure they don't go near that area. You only have to get through the one Walbot and get the knife."
            player "But I'm wanted right now. Why can't you go instead, Dr. Venture?"
            if "lamp" in seen_events:
                venture "I've been banned from being within 10-foot radius of a Walbot since the lamp incident last time."
            else:
                venture "...It's far, and my body is frail."
                n "He bends down slowly and slumps down on his chair like an old man. His bandages ruffle in agreement."
                n "A pretty convincing act, if it weren't for the fact that you saw him dodged your shot nimbly before throwing a flask at your face with full force."
            venture "So it has to be you, [player_name]." #smile

            show bg room hall
            hide black_screen onlayer master
            hide venture
            n "He shakes your hand, and you're transported once again back to the corridor near the temporary court room."
            scene bg room hall
            with default_fade
            n "You make your way towards the security department."
            n "Dr. Venture seems to have kept his word. You haven't seen a single person or Walbot on your way here."

            scene bg cubicle
            n "You open the door to the evidence storage section quietly. You see only a single Walbot at the work desk with his back against you."
            $ tne_sneak_v = False
            $ tne_sneak_w = False
        label tne_convince_wal:
            show firewal at appear
            wal1986 "Hello (^O^)/ how (?_?) may ^_^ I (>_<)> help L(^w^ ) you ( ^o^)-->(oOo) !"
            if tne_sneak_v == False and tne_sneak_w == False:
                player "...How are you saying that?"
                wal1986 "I (>_<)> installed \\(^0^) an (owo)1!! emoticon (^.^) virus (@_@) ! Everything \\(+w+)/ I (>_<)> say ( oDo) and (IvI)/\\(IvI) see (O-O) is (~w~) emoticon (^.^) !"
                wal1986 "I (>_<)> have (UAU) no (-=-)X idea (*o*)! who (p_-) you ( ^o^)-->(oOo) are (~w~) !"
            show shock onlayer master2
            $ shake_screen(layers="master2", duration=0.1, strength=4, repeat=True)
            show firewal fury
            wal1986 fury "{size=+10}{b}WHO ARE YOU. {/b}{/size}"
            wal1986 fury "{size=+10}{b}...{/b}{/size}"
            show shock onlayer master2:
                alpha 0.0
            wal1986 fury "{size=+10}{b}<(`O_O`)>{/b}{/size}"
            jump tne_convince_wal_menu

        label tne_convince_wal_menu:
            menu:
                n "Uh oh, the Walbot is charging up his fist."
                "I'm Dr. Venture":
                    if not tne_sneak_v:
                        player "I'm Dr. Venture."
                        if "lamp" in seen_events:
                            show firewal
                            wal1986 "I (>_<)> see (O-O) !"
                            wal1986 "..."
                            show shock onlayer master2:
                                alpha 1.0
                            show firewal fury
                            wal1986 fury "{size=+10}{b}WARNING! WARNING! DR. VENTURE IS WITHIN DANGEROUS PROXIMITY!{/b}{/size}"
                            n "The flames turn blue as he aims his fire cannon at you."
                            wal1986 "{size=+10}{b}LEAVE RIGHT THIS INSTANT OR BE OBLITERATED!!!!!!{/b}{/size}"
                            n "You quickly dash out of the room."
                            show shock onlayer master2:
                                alpha 0.0
                            show firewal
                            wal1986 "I (>_<)> cannot (-=-)X see (O-O) IMPOSTER ?!(@-@) ?"
                            n "The emoticon virus seems to have lost him his object permanence."
                            n "Perhaps you can re-enter and retry."
                            jump tne_convince_wal
                        else:
                            show firewal
                            wal1986 "I (>_<)> see (O-O) !"
                            wal1986 "..."
                            wal1986 "Can ^_^ you -->(oOo) show (owo)/ your -->(oOo) department head (O/\O) ID (-o-)*+ ?"
                            n "Oh shit."
                            wal1986 "..."
                            show shock onlayer master2:
                                alpha 1.0
                            show firewal fury
                            wal1986 fury "{size=+10}{b}WARNING! WARNING! DETECTING IMPOSTER!{/b}{/size}"
                            n "The flames turn blue as he aims his fire cannon at you."
                            wal1986 "{size=+10}{b}ELIMINATING THREAT!!!!{/b}{/size}"
                        $ tne_sneak_v = True
                    else:
                        n "Do you want to get burned for real??"
                        jump tne_convince_wal_menu
                "I'm Wal No.283":
                    if not tne_sneak_w:
                        player "I'm Wal No.283."
                        show firewal
                        wal1986 "I (>_<)> see (O-O) !"
                        wal1986 "..."
                        show firewal fury
                        wal1986 fury "{size=+10}{b}NO YOU ARE NOT.{/b}{/size}"
                        show shock onlayer master2:
                            alpha 1.0
                        wal1986 "{size=+10}{b}I (>_<)> installed \\(^0^) the <--(OAO) virus (@_@) on ^(1-1)^ every \\(+A+)/ Wal <(>_<)> !{/b}{/size}"
                        wal1986 "{size=+10}{b}YOU -->(oOo) DO <(o-o) NOT (-=-)X SPEAK ( oDo) EMOTICON (^.^). YOU -->(oOo) ARE (~w~) AN (owo)1!! IMPOSTER ?!(@-@) !!!{/b}{/size}"
                        wal1986 "{size=+10}{b}OBLITERATE (`O`)// IMPOSTER ?!(@-@) !!!{/b}{/size}"
                        $ tne_sneak_w = True
                    else:
                        n "Do you want to get blasted for real??"
                        jump tne_convince_wal_menu
                "(>_<)>":
                    player "(>_<)>"
                    show firewal
                    wal1986 "I (>_<)> see (O-O) !"
                    wal1986 "How (?_?) may ^_^ I (>_<)> serve (^w^ )> you ( ^o^)-->(oOo) ?"
                    jump tne_con_success
            n "Uh oh, you messed up."
            hide firewal
            n "You duck behind the corner as the Walbot releases a fireball."
            show shock onlayer master2:
                alpha 0.0
            n "..."
            n "Why is it so quiet?"
            show firewal
            wal1986 "I (>_<)> cannot (-=-)X see (O-O) IMPOSTER ?!(@-@) ?"
            n "The emoticon virus seems to have lost him his object permanence."
            n "Perhaps you can re-enter and retry."
            jump tne_convince_wal

        label tne_con_success:
            player "I need the knife from [player_name]'s trial."
            wal1986 "I (>_<)> see (O-O) !"
            wal1986 "..."
            show firewal fury
            wal1986 "{size=+10}{b}WHERE IS YOUR EMOTICON.{/b}{/size}"
            n "Shit."
            player "...(O-O)>"
            show firewal
            wal1986 "{size=+10}{b}Hm.{/b}{/size}"
            wal1986 "I (>_<)> will v( owo)/ get (u-u)/ it (i-i)."    
            show firewal talk at disappear
            n "The Walbot goes up and goes up to the nearest wall."
            $ shake_screen()
            n "He punches the wall with a fully-charged fire fist. The wall crumbles under the impact, revealing four more walls behind it, all of which have been destroyed as well."
            n "The Walbot digs through the rubble and retrieves an object."           
            show firewal at appear
            wal1986 "Mission (>_<)> completed (>_<)> !"
            n "You let out a sigh of relief. The Walbot hands you the knife that started all of this."
            n "You quickly leave the security department."

            scene bg room hall
            show venture 
            n "To your surprise, Dr. Venture is already here, waiting for you."
            venture "Great! You got the knife!"
            n "You hand him the knife. Then, he stabs you."
            n "The moment the tip of the knife touches your skin, someone identical to you appears out of nowhere at your feet."
            n "Dr. Venture kneels down and shoves another knife in the hands of your doppelganger."
            venture "Ta-da! I've made it so that the knife frames you for your own murder!"
            n "Before you can ask any questions, Dr. Venture sounds the emergency alarm on the wall. Immediately, rapid footsteps can be heard closing in from both ends of the corridor."
            show deceased:
                alpha 0.0
                xzoom -1.0
            show deceased at appear(x_align = 0.2)
            show venture at move_to(x_align = 0.8)
            deceased "Aha! Found you..! And you've already murdered another victim!!!"
            deceased "Huh."
            deceased "Why are there two of you?? And why are you dead??? And why are you also alive???"
            deceased "Only I am allowed to be dead! You can't be Deceased too!!"
            venture "It appears {b}[player_name]{/b} has an evil twin!"
            venture "I was strolling down the hall when I saw {b}[player_name]{/b} here being chased by {b}[player_name]{/b}."
            venture "Naturally, as a department head, I have to make sure our employees were safe."
            venture "So, I attempted to apprehend {b}[player_name]{/b} so that {b}[player_name]{/b} couldn't harm {b}[player_name]{/b}."
            venture "But, there was an accident, and now {b}[player_name]{/b} is dead."
            deceased "..."
            n "Dr. Deceased looks back and forth between you and your corpse."
            deceased "So is [player_name] deceased?"
            venture "[player_name] is, but {i}[player_name]{/i} isn't."
            deceased "..."
            deceased happy "Okay then! As long as [player_name] doesn't take my identity."
            show deceased happy at disappear
            n "Dr. Deceased happily skips away. "
            venture "See? Problem solved!"
            venture "I'll get the Wal inside to frame your \'evil\' twin for the murder of Dr. Ralex. You should be off the hook."
            venture "Just keep the knife thing a secret between you and me, yea? I don't want to write another five reports for \'letting an anomaly escape containment\'."
            show venture at disappear
            n "You watch as Dr. Venture drags your dead doppelganger into the security department." 
            n "You're never going to forget your own knife, ever again."
            $ update_character_points({"venture":1})
            return

    label after_court_innocent:
        scene bg room hall

        hide deceased onlayer master2
        hide defendant overlay onlayer master2
        hide front defendant overlay onlayer master2

        n "You walk out of the multi-purpose room, and the reality of what just happened finally hit you."
        n "You were accused of murder. Almost sent to jail."
        n "You begin to question whether this job is really worth it."
        n "You feel a light tap on the back of your shoulder."
        show venture at appear
        venture "Hey, [player_name]!"
        player "Hello, Dr. Venture."
        venture "Woah, what's going on? Why are so many people coming out of the multi-purpose room?"
        venture "Did we have a foundation-wide event? Without me?"
        player "It was a trial, actually-"
        venture "Oh. Nah. That's boring. Glad I sat that one out."
        venture "Anyways, I pulled you over 'cause I want to ask if you've seen something I've lost."
        venture "I've applied an alchemical scent onto it and you seem to have picked up on some of it."
        venture "It's an anomalous knife! I must have misplaced it, silly me!"
        venture "It's quite dangerous though; it's capable of affecting the mind and creating illusions of a murder of a fake person."
        player "..."
        player "{nw}ARE YOU FUCKING KIDDING ME-"
        $ update_character_points({"alex": 1, "aikha": 1, "ryz": 1, "helco": 1, "uriel": 1, "firewal": 1, "chan": 1, "hamp": 1, "deceased": 1, "syg": 1})
        return

