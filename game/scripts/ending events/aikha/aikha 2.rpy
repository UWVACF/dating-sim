label ending_event_aikha_2:
    scene bg office
    with default_fade
    show aikha neutral at appear    
    aikha "Woohoo! ending event 2"
    menu:
        aikha "Now choose the right choice to get the ending"
        "Right choice":
            aikha "Yippee!!"
            $ current_ending = "aikha_3"
        "Wrong choice":
            aikha "Bruh!"
            $ current_ending = None