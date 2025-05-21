label day_event_dr_ryz_and_the_goose:
    scene bg office
    with default_fade
    player "So I just need to deliver this box of samples to Dr. Ryz? Should be simple."
    n "As you approach the door to Dr. Ryz's office, you hear the sounds of shouting and furious honking."
    show caffi at appear(x_align = 0.33)
    show roose upset at appear(x_align = 0.66)
    caffi "RIZZ!"
    roose "HISSSSS!"
    caffi "IT'S DR. \"RIZZ\"!"
    roose "HONK HONK! HONK HONK!"
    caffi "I'M RIGHT! I'M LITERALLY RIGHT!"
    n "This wasn't in the job description. You decide to ignore...whatever is going on and follow your objective."
    player "Have you seen Dr. Ryz?"
    n "Your question was directed at Caffi, but for some reason, the goose turns to you. His beady eyes lock onto the box in your hands, and he starts flapping his wings in excitement."
    roose talk "Honk! Honk!"
    n "He runs out the door and pulls you out towards the hallway. Seems like he's trying to lead you to Dr. Ryz."
    player "Well, see you then, Caffi."
    caffi "IT'S PRONOUNCED RIZZ! IT'S PRONOUNCED- "
    hide caffi
    n "You calmly shut the door and leave."
    
    scene bg hallway
    show roose at center
    with default_fade
    n "You follow the goose down a dimly lit hallway. He leads you to a metal door with a keypad beside it."
    n "The keypad has four buttons arranged in a diamond shape."
    roose "Honk! Honk!"
    n "You're not sure how you're supposed to open the door. You don't exactly have the passcode."
    roose "Honk honk hooonk! Honk! Honk!"
    n "...Seems like the goose doesn't care. Might as well punch a random code in."
    $ times_tried = 0
    label enter_passcode:
        $ numbers_entered = 0
        $ code = ""
        while numbers_entered < 5:
            menu:
                n "You've entered: [code]{fast}"
                "Up":
                    $ numbers_entered += 1
                    $ code += "U"
                "Left":
                    $ numbers_entered += 1
                    $ code += "L"
                "Down":
                    $ numbers_entered += 1
                    $ code += "D"
                "Right":
                    $ numbers_entered += 1
                    $ code += "R"
        
        n "You enter [code]."
        
        $ correct_code = "DLRUD"
        if code != correct_code and times_tried < 20:
            n "The door doesn't open."
            python:
                goose_reply = ""
                for i, letter in enumerate(code):
                    if letter == correct_code[i]:
                        goose_reply += "Honk! "
                    else:
                        goose_reply += "Hiss! "
            
            roose "[goose_reply]"

            if times_tried == 0:
                n "Is the goose giving you feedback on your guess?"
            elif times_tried == 7:
                n "It looks like it's commenting on when you get a letter right or wrong."
            elif times_tried >= 15:
                n "Seems like a \"honk\" is a correct letter and a \"hiss\" is an incorrect one."
            $ times_tried += 1
            jump enter_passcode

        else:
            if times_tried >= 20:
                n "The door doesn't open."
                n "The goose, fed up with your incompetence, angrily jumps onto your shoulder."
                n "Its nails dig into your collarbone as it frustratedly types in the combination \"[correct_code]\"."

            n "The door unlocks!"

            if times_tried >= 20:
                n "...No thanks to you."
                
    
    n "You follow the goose into the room."
    scene bg secret_room
    show roose at center
    n "It begins to devour the loaves of bread sitting in the corner."
    n "You glance around but see no sign of Dr. Ryz. Maybe he's out."
    show roose at disappear
    n "You do, however, find various sticky notes pinned to a bulletin board."
    hide roose
    n "They read:"
    n "\"It looks like the others are unable to understand Pebbles. Interesting.\""
    n "\"In any case, the goose is intelligent enough to recognize whenever this is the case and react accordingly.\""
    n "\"He will keep his responses as simple as possible. If he must convey more complicated messages, he will often resort to human-known ciphers, such as Morse code.\""
    n "\"A translating device is currently being developed to facilitate communication.\""
    n "Just as you finish reading the notes, you hear a voice behind you."
    show ryz at appear(x_align = 0.33)
    ryz "Oh, hey. What are you doing in here?"
    n "You quickly explain the situation and pass him the samples. You'd really rather not get a complaint filed against you for breaking and entering."
    n "As you finish, the goose honks in affirmation of your story."
    show roose at appear(x_align = 0.66)
    roose "Honk! Honk!"
    ryz happy "As expected. Pebbles is a smart one."
    roose "Honk! Honk!"
    n "Dr. Ryz tosses a cracker at the goose, who catches it mid-air and gobbles it up."
    player "I'll be off, then."
    n "As you turn to leave, Dr. Ryz calls you once more."
    ryz "Say, what was the combination to the door?"
    if times_tried < 20:
        $ numbers_entered = 0
        $ code = ""
        while numbers_entered < 5:
            menu:
                n "The door combination was: [code]{fast}"
                "Up":
                    $ numbers_entered += 1
                    $ code += "U"
                "Left":
                    $ numbers_entered += 1
                    $ code += "L"
                "Down":
                    $ numbers_entered += 1
                    $ code += "D"
                "Right":
                    $ numbers_entered += 1
                    $ code += "R"
        
        player "It was [code]."
        if code == correct_code:
            ryz "Oh, nice. You remembered."
            ryz "I've been meaning to change it, but I forgot the old code. I owe you one."
            roose "Honk!!"
            ryz "Yeah, yeah, I know you know it. You're free to leave, intern."
            $ update_character_points({"ryz": 2})
        else:
            ryz "That doesn't sound right."
            ryz "No matter, I'll remember it eventually. You're free to leave, intern."
            $ update_character_points({"ryz": 1})
        
        ryz "...Nope. You've had enough bread already."
        roose angry "HONK HONK!"
        n "You decide to leave before the argument gets too intense."
        n "As you close the door, you hear Dr. Ryz and the goose arguing through the wall."
        ryz "...Was that Shakespeare? Don't you quote Shakespeare at me."
        return

    else:
        n "Before you can answer, the goose looks at Dr. Ryz and honks a few times."
        ryz "...I see."
        n "He turns to look at you. You can almost feel the contempt radiating from his stare."
        ryz "Nevermind. I'll remember it eventually."
        ryz "...Twenty tries???"
        $ update_character_points({"ryz": -1})
        return
