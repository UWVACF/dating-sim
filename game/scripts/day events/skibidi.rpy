label day_event_skibidi:
    scene bg hallway
    if day_number > 5:
        n "Take a wild guess as to what you're doing."
        n "Yep. Coffee. It's your only defining trait, at this point."
        n "You should go on a character arc sometime soon. You know, find some new motivations."
    else:
        n "You're on your way to the lounge to fuel your coffee addiction."
        n "This will be a recurring trend. Get comfy with it."
    n "You open the door to the lounge and are greeted by three other personnel, chatting away happily."
    n "You pay them no mind, until Dr. Helco approaches you."
    show helco happy at appear
    helco happy "Hello, [player_name]. What the skibidi is going on?"
    show caffi at appear(x_align = 0.25)
    show meem at appear(x_align = 0.75)
    caffi "Helco! It doesn't work like that!"
    helco neutral "Huh? Did I use it incorrectly?"
    caffi "Yeah! It's like, \"What the hell\" or \"What the fuck,\" you know?"
    helco "Oh."
    helco happy "Hello, [player_name]. What the fuck is going on?"
    show helco scared
    n "Caffi drags Dr. Helco by the sleeve to the back of the room, while Meme, chuckling, follows behind."
    show helco scared at disappear
    show caffi at disappear
    show meme at disappear
    caffi "You know what? Let's move on. I'll teach you the word \"gyatt\" instead." # im in so much pain
    menu:
        n "...Do you intervene?"
        "Save Dr. Helco from brainrot.":
            jump skibidi_helco
        "Save yourself.":
            jump skidibi_yourself
    
    label skibidi_helco:
        n "Well, nobody else is gonna save Dr. Helco from this disaster."
        n "You sigh to yourself and make your way to the back of the room."
        show helco pensive at appear
        show caffi happy at appear(x_align = 0.25)
        show meme at appear(x_align = 0.75)
        caffi happy "You say \"gyatt\" whenever you're really surprised, or when something's really cool."
        caffi "Then we have \"sus\", which means suspicious, \"cap\" which means lie, \"aura\" which means..."
        n "You can feel your brain shrinking as Caffi continues talking. You mourn the loss of thousands of years of societal development."
        n "About 14 and a half minutes later, Dr. Helco walks up to you with renewed confidence. You brace yourself for impact."
        helco happy "Hey [player_name], you rizzler " # i literally died writing this somebody else can take over

    label skibidi_yourself:
        n "a"
