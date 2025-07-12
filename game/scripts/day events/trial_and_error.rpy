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

    # to remove when not testing
    $ tne_defendant = renpy.input("Ture for defendant, or False for Deceased being the defendant.")
    $ tne_defendant = tne_defendant.strip()

    $ tne_chan_backup = renpy.input("Ture or False for Chan on your side")
    $ tne_chan_backup = tne_chan_backup.strip()
    
    $ hampter_witness = renpy.input("Ture or False for hampt witness")
    $ hampter_witness = hampter_witness.strip()
    
    $ tne_syg_backup = renpy.input("Ture or False for syg back you up")
    $ tne_syg_backup = tne_syg_backup.strip()
    # btw for the showcase we're going defendant route

    if tne_defendant == True:
        jump trial_you_as_defendant
    elif tne_defendant == False:
        jump trial_deceased_as_defendant

label trial_you_as_defendant:
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
    uriel "The accused, [player_name], was found to be the prime suspect to this murder, with Dr. Deceased being the Plaintiff."
    uriel "I would like to introduce Dr. Chan as the jury."
    show chan onlayer master at appear(x_align = 1.0)
    chan "Thank you, Uriel. I swear that I will remain fair."
    show chan unique
    ethy "AA."
    chan "Ethy will help me determine if the plaintiff or the defendant are lying."
    uriel "The court session will now start."
    # insert start cg or something
    show chan neutral
    uriel sad "Our co-founder, Dr. Ralex was found dead earlier during lunch in the lounge."
    uriel upset "After {i}through{/i} investigation, the security department has determined that the intern, [player_name] is the most likely suspect to this crime."
    uriel "Evidence suggested that [player_name] likely called Dr. Ralex out to meet in order to discuss a full time position offer, and resorted to murder when [player_sub] got rejected."
    uriel neutral "Hence, it is concluded that [player_name] shall be charged with first degree murder. [player_name], do you plead guilty to these charges?"
    menu:
        uriel "/no_pause{cps=1000}Hence, it is concluded that [player_name] shall be charged with first degree murder. [player_name], do you plead guilty to these charges?{/cps}"
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
            player "/no_pause{cps=1000}No, I don't. Because...{/cps}"
            "Dr. Deceased is the real murderer!":
                player "bla bla bla"
            "I don't know Dr. Ralex!":
                player "blu blu blu"
            
    label tne_yes:
        n "...Why would you admit guilt to something you didn't do?"
        player "Yes, I do."
        $ trial_credibility_you += -1
        show deceased happy onlayer master2
        deceased happy "I KNEW IT!"
        show deceased neutral onlayer master2
        uriel panic "Well, case close, I suppose."
        uriel neutral "So, [player_name], you're officially convicted of the murder of Dr. Ralex. We will now decide on your sentence-"
        chan "Hold on!"
        chan "...[player_sub_be] lying."
        show uriel:
            xzoom -1
        uriel "Lying about what?"
        chan "Ethy screamed softly in my ears when [player_sub] said yes to the crime."
        chan pensive "Which means that statement was said with a deceitful intent."
        show uriel:
            xzoom 1
        show chan neutral
        pause 0.5
        uriel upset "Did you lie, [player_name]?"
        uriel "Perjury is a serious crime. So answer truthfully, {i}do you plead guilty to the charges of planning and murdering Dr. Ralex?{/i}"
        menu:
            uriel "/no_pause{cps=1000}Perjury is a serious crime. So answer truthfully, {i}do you plead guilty to the charges of planning and murdering Dr. Ralex?{/i}{/cps}"
            "No":
                jump tne_yes_no
            "No":
                jump tne_yes_no
            "No":
                jump tne_yes_no
            "Yes":
                jump tne_yes_yes

    label tne_yes_no:
        n "okay back to the trial"
    
    label tne_yes_yes:
        player "Yes, I do."
        n "Hey, this isn't a marriage proposal."
        $ trial_credibility_you += -1
        chan "...[player_sub_be] still lying."
        deceased "What tricks are you pulling here!!" #fury or something
        deceased "Aha! I get it! You saying yes to pleading guilty is a lie beacuse you {i}don't feel guilty!{/i} What a cold-hearted criminal!"
        deceased "Judge {i}Urinal{/i}, I say we should just throw [player_obj]-"
        uriel fury "{size=+10}Such contempt! I will not have this in my courtroom!{/size}"
        uriel "You will be charged with the crimes of contemning the court!"
        show uriel upset
        chan "Uh, Uriel, we should probably conclude the murder charge first."
        if tne_chan_backup == "True" or True:
            chan "So [player_name], I recall you had previously denied the murder at the crime scene. Is there a reason why you're lying now?"
            chan unique "I totally understand if it is out of spite, but please rest assure that we are fair and just here at the court."
        elif tne_chan_backup == False or "False":
            chan unique "[player_name], you are legally obligated to answer truthfully in court."
            chan "It gains you no benefit to not do so."
        chan "So let me ask you again, did you kill Dr. Ralex?"
        menu:
            chan "/no_pause{cps=1000}So let me ask you again, did you kill Dr. Ralex?{/cps}"
            "No":
                jump tne_yes_yes_no
            "No":
                jump tne_yes_yes_no
            "No":
                jump tne_yes_yes_no
            "Yes":
                jump tne_yes_yes_yes

        label tne_yes_yes_no:


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
            deceased "What if you're lying?"
            chan surprise "Excuse me?"
            show uriel neutral
            deceased "How do I know if you're telling the truth? What if you're helping [player_name]? What if Ethy is helping [player_name]?"
            chan upset "That's ridiculous! Dr. Deceased, this is slander!"
            show uriel:
                xzoom -1
                pause 0.3
            show chan surprise
            uriel upset "...Are you lying, Dr. Chan?"
            chan fury "You can't be serious! Uriel, Deceased's is talking nonsense!"
            show uriel fury
            n "You watch as the room erupts into chaos. The trial is surely not proceeding at this state."
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
            n "You've escaped! Though you probably lost the job."
            n "From the [day_number - 1] days here, you can confidently assume that this incident will be forgotten within the matter of days."
            n "In other words, you're basically free as long as you make it out of the building and don't come back."
            n "Seems all clear. Now run for it-"
            venture_unknown "[player_name]!"
            n "OH FUCK-"
            show venture at appear
            ##idk what to write here##

            


    




label trial_deceased_as_defendant:
    scene bg court main
    $ trial_credibility_deceased = 0
