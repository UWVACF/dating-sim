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
    deceased "I love Miku."
    




label trial_deceased_as_defendant:
    scene bg court main
    $ trial_credibility_deceased = 0
