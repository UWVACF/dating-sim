label ending_event_aikha_1:
    scene bg office
    with default_fade
    show aikha neutral at appear
    aikha "Yippee! aikha ending 1"
    aikha "Anyway here's some {sc=2}shaky text{/sc}"
    aikha "And here's some {bt=4}wavy text{/bt}"
    aikha "The {bt=7}power of friendship!{/bt}"
    menu:
        aikha "Now choose the right choice to get the ending"
        "Right choice":
            aikha "Yippee!!"
            $ current_ending = "aikha_2"
        "Wrong choice":
            aikha "Bruh!"
            $ current_ending = None

