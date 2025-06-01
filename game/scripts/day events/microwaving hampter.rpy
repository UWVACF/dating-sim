label day_event_microwaving_hampter:
    scene bg office
    n "57...58...59..."
    n "The clock strikes noon. Hell yeah! It's coffee time!!"
    show bg hallway
    n "You eagerly jog over to the lounge to help yourself to a cup of that delicious black nectar."

    show bg lounge
    show jessie at appear(x_align = 0.1)
    show hampter happy at appear
    show helco at appear(x_align = 0.9)

    n "As you enter the lounge, you see Dr. Jessie and Dr. Helco gathered around Hampter next to the microwave."
    hampter "In! In!"
    n "Dr. Jessie scoops up Hampter and places her into the microwave...?"
    n "She sets the timer to a minute and presses Start."
    n "The microwave hums."

    # do we want hampter to rotate along the x axis or would that be janky
    hampter "Wee!!!"
    n "Hampter starts to slowly rotate. She seems awfully excited."
    helco "Oh, hello! I didn't see you there."
    jessie "Hi [player_name]! We're microwaving Hampter. Do you wanna join?"
    n "...Guess you're not getting your coffee for a while."
    n "The microwave lets out its signature jingle, signalling its completion. Dr. Jessie brings Hampter out of the microwave."
    hampter "Again! Again!"
    jessie "What do you want next?"
    hampter "Hmmm... There's too many options. I can't choose!"
    jessie "Maybe [player_name] can choose instead?"
    hampter "Oh, sure! [player_name], choose for me!"
    player "What am I choosing?"
    hampter "Put me back in the microwave with something!"
    $ microwaving_hampter_first_choice = ""
    label microwaving_hampter_choice:
        menu:
            n "What do you put Hampter in with?"
            "A bowl of hard-boiled eggs.":
                jump microwaving_hampter_eggs
            "A packet of frozen Tater Tots.":
                jump microwaving_hampter_tots
            "A dozen pieces of string cheese.":
                jump microwaving_hampter_string_cheese
            "Yourself.":
                n "..."
                n "...What?"
                jump microwaving_hampter_choice
    label microwaving_hampter_eggs:
        $ microwaving_hampter_first_choice = "eggs"
        n "Wasn't there something about not putting eggs in the microwave? Something about pressure and causing an explosion..."
        n "Eh, if you forgot it, it probably wasn't important."
        n "You find a plate of about a half dozen hard-boiled eggs sitting conveniently next to the microwave."
        jessie panic "...Eggs?"
        player "What's up?"
        jessie panic "Oh, nothing!"
        n "You put Hamp in the middle and make sure she's snug."
        hampter "Oooh! So warm!"
        n "You place the plate into the microwave. You decide 5 minutes is a reasonable amount of time and set the microwave to that long."
        hampter "Wee!!"
        n "The microwave hums, spinning both the eggs and Hampter."
        hampter "This is so fun! This is so-"
        show layer master:
            shake
            0.8
            repeat 6
        n "Suddenly, the eggs explode. One by one, they pop like balloons, spewing scalding hot yolk all around the microwave."
        hampter "AHHH!!"
        n "Now you remember: eggs explode in the microwave!"
        n "You quickly stop the microwave to rescue Hampter from the onslaught of egg-grenades."
        n "You grab the plate-"
        player "SHIT! That's hot!"
        n "The scalding eggs covering the plate burn your hands as you try to grab it, and you drop the plate."
        hampter "NOOO!"
        show layer master:
            shake
        n "...And Hampter."
        jessie panic "HAMPTER!"
        n "Dr. Jessie rushes to Hampter and scoops her up from the mess, ignoring the "


    label microwaving_hampter_tots:
        $ microwaving_hampter_first_choice = "tots"
        n "But microwaving tater tots makes them soggy..."
        n "Despite that, you find a packet of frozen Tater Tots from the freezer and unload the contents onto a plate."
        helco "Interesting. What are those?"
        player "Tater Tots! They're like potato cubes."
        helco "Oh!"
        helco "...What are potatoes?"
        n "As Dr. Jessie explains what potatoes are, you make a little divet in the middle of the Tater Tot pile and place Hampter there."
        hampter "Ah! Cold!"
        n "The packet says to bake at 425F for 30 minutes, so you set the microwave to 30 minutes."

    label microwaving_hampter_string_cheese:
        $ microwaving_hampter_first_choice = "cheese"
        n "...String cheese. Sure. I guess there are worse options."
        n "You find a packet of string cheese in the fridge and take about a dozen or so."
        n "You unwrap them and line a plate neatly with them, placing Hampter onto what looks like a makeshift cheese raft."
        hampter "Ooh! Cheese!"




    