label day_event_pokanom:
    scene bg hallway
    n "The workday is over, but you're still here. That would be admirable if you were actually working. Instead you're just looking around for your phone."
    n "Maybe it's in the lounge. You definitely had it on your lunch break."
    scene bg lounge
    n "You walk into the sounds of ripping plastic and shuffling cards."
    n "You see Dr. Chan, Dr. Lee, B6, Egg, and Uriel around a table covered in cards and torn wrappings."
    n "Looking at one mostly intact wrapper, it says \"Pokanom\"."
    show uriel talk
    uriel "They ordered a box of cards that came today. Unfortunately, until they are done with the pack opening, Dr. Chan and Egg are functionally inaccessible."
    show uriel neutral
    n "Egg is just eating the tops of the card wrappers off with concerning speed, and Dr. Chan tearing into the packs at a similar rate."
    n "B6 and Lee are having a comparatively calmer game on the other end of the table."
    n "Suddenly, you hear loud screeching from something that looks like a buff demon with a scale for a head that's hovering over Dr. Chan's shoulder."
    show chan happy
    chan "Yes! A CeleMeme! My demonics deck is finally complete."
    n "Well, at least they're having fun, right?"
    egg " Dr. Chan, have you gotten the full-art shiny card from the pack yet?"
    chan "No, have you?"
    n "Uh oh, looks like there's only one pack left. Well they're both reasonable people, you're sure they can just talk this out."
    n "Nope. Egg has just lunged on to Dr. Chan and Dr. Chan is pulling out a gun."

    menu: 
        n "Quick! Find a way to resolve this without your two most responsible department heads coming to blows."
        "Settle this the proper way: with a Pokanom battle.":
            jump pokanom_battle
        "A full-art card? Those are worth quite a bit. Take it for yourself.":
            jump grab_and_run

    label pokanom_battle:
        chan "Fine. We'll settle this properly."
        chan "Hey Uriel, we're going to need a moderator."
        uriel "...Fine."
        egg ""
    
    label grab_and_run: