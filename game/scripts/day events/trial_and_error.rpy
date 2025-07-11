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
    chan "Ethy will help me determin if the Plaintiff or the defendant are lying."
    uriel "The court session will now start."
    # insert start cg or something
    uriel sad "Our co-founder, Dr. Ralex was found dead earlier during lunch in the lounge."
    uriel upset "After {i}through{/i} investigation, the security department has determined that the intern, [player_name] is the most likely suspect to this crime."
    uriel "Evidence suggested that [player_name] likely called Dr. Ralex out to meet in order to discuss a full time position offer, and resorted to murder when [player_sub] were rejected."
    uriel neutral "Hence, it is concluded that [player_name] shall be charged with first degree murder. [player_name], do you plead guilty to these charges?"
    menu:
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
        deceased happy "I KNEW IT!"
        uriel panic "Well, case close, I supposed."
        uriel neutral "So, [player_name], you're officially convicted of the murder of Dr. Ralex. We will now decide on your sentence-"
        chan "Hold on!"
        chan "...[player_sub_be] lying."
        show uriel:
            xzoom -1
        uriel "Lying at what?"
        chan "Ethy screamed softly in my ears when [player_sub] said yes to the crime."
        chan pensive "That means that statement was said with a deceitful intend."
        show uriel:
            xzoom -1
        show chan neutral
        uriel upset "Did you lie, [player_name]?"
        uriel "Perjury is a serious crime. So answer truthfully, {i}do you plead guilty to the charges of planning and murdering Dr. Ralex?{/i}"
        menu:
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
        n "...So did you do something while I wasn't here?"
        player "Yes, I do."
        $ trial_credibility_you += -1
        chan "...he's still lying."
        deceased "What tricks are you pulling here!!"
        deceased "Aha! I get it! You saying yes to pleading guilty is a lie beacuse you {i}don't feel guilty!{/i} What a cold-hearted criminal!"
        deceased "Judge {i}Urinal{/i}, I say we should just throw [player_obj]-"
        uriel fury "{size=+10}Perjury! I will not have this in my courtroom!{/size}"
        uriel ""

    




label trial_deceased_as_defendant:
    scene bg court main
    $ trial_credibility_deceased = 0
