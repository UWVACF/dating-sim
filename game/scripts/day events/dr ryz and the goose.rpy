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
    n "You decide punch a random code in."
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
        if code != correct_code:
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
            elif times_tried == 5:
                n "It looks like it's commenting on when you get a letter right or wrong."
            elif times_tried == 10:
                n "Maybe a \"honk\" is a correct letter and a \"hiss\" is an incorrect one."
            elif times_tried >= 15:
                n "..."
                n "Surely you have enough information to solve it by now."
            $ times_tried += 1

            jump enter_passcode
        else:
            n "The door unlocks!"
    
    n "You follow the goose into the room."
    scene bg secret_room
    show roose at center
    n "It begins to devour the loaves of bread sitting in the corner."
    n "You look around the room. It doesn't look like Dr. Ryz is here."
    show roose at disappear
    n "You do, however, find various sticky notes pinned to a bulletin board."
    hide roose
    n "They read:"
    n "\"It looks like the others are unable to understand Roose. Interesting.\""
    n "\"In any case, the goose is intelligent enough to recognize whenever this is the case and react accordingly.\""
    n "\"He will keep his responses as simple as possible. If he must convey more complicated messages, he will use human-known ciphers, such as Morse.\""
    n "\"A Roose translator is currently being developed to facilitate communication.\""
    n "The notes end there."
    show roose at appear
    n "You glance back at the goose just as he finishes his fourteenth loaf of bread."
    n "He glances at you and honks."
    roose "Honk! Honk!"
    show roose at disappear
    n "He runs out of the room, and you quickly follow him."
    scene bg hallway
    show roose at center
    with default_fade
