label escape_initialize:
    python:
        # viewed
        escape_left_wall_password_viewed = False
        escape_back_wall_viewed = False
        escape_back_wall_notebook_viewed = False
        escape_back_wall_notebook_ciphers_viewed = False
        escape_back_wall_notebook_invalid_viewed_times = 0
        escape_back_wall_notebook_gullible_marked = False
        escape_back_wall_notebook_gullible_viewed = False # unused
        escape_right_wall_briefcase_viewed = False
        escape_right_wall_computer_viewed = False
        escape_right_wall_footage_viewed = False
        escape_right_wall_briefcase_opened = False

        escape_passcode_attempts_remaining = 3
        escape_inventory = ["Phone (Dead)"]
        escape_item_labels = {
            "Phone (Dead)": "escape_item_phone_dead",
            "Phone (Charged)": "escape_item_phone_charged",
            "Testimony (Blue Sticky)": "escape_item_testimony",
            "Page 140 (Spawn Rate)": "escape_item_page_140",
            "Purple Light": "escape_item_purple_light",
            "Slip of Paper": "escape_item_slip_of_paper",
        }
        escape_checked_phone = False
        escape_testimony_read = False
    return

screen escape_inventory_screen:
    style_prefix "choice"
    
    vbox:
        for i in escape_inventory:
            button:
                style "choice_button"
                child Text(i, style="choice_button_text")
                action Call("[escape_item_labels[i]]")
        button:
            style "choice_button"
            child Text("Go back.")
            action Jump("escape_main_menu")

label day_event_escape:
    call escape_initialize
    scene bg hallway
    player "Yeah!!! It's coffee time!!"
    n "You excitedly hurry over to the lounge to indulge in your coffee addiction when-"
    show black_screen
    with hpunch
    scene bg room containment
    with Fade(0.0, 1.0, 1.0)
    player "Huh? What?"
    n "You suddenly wake up and find yourself sprawled on the floor of a containment room."
    aikha "Oh, look who the cat dragged in."
    show aikha at appear(x_align = 0.2)
    show ryz at appear(x_align = 0.5)
    show firewal at appear(x_align = 0.8)
    ryz "Morning, [player_name]."
    player "Where the hell are we?"
    firewal "No clue. Think we're in some containment room."
    aikha "We all just kind of woke up here."
    n "You look at the door to the room and see a torn scrap of paper next to it. You make your way over to it and read it:"
    n "\"..And for those who forgot, the password is simply the anomaly's name and V.A.C. number.\""
    n "\"Signed, #######\""
    n "The name is blacked out."
    aikha "Ooh, this could be fun. New recruit, there should be hints scattered around the room. Try to piece together the puzzle and get us out of here!"
    show aikha at disappear
    show ryz at disappear
    show firewal at disappear
    jump escape_main_menu

label escape_main_menu:
    menu:
        n "What do you do?"
        "Look around.":
            jump escape_look_around
        "Talk.":
            jump escape_talk
        "Check inventory.":
            jump escape_inventory_menu
        "Submit the passcode.":
            jump escape_passcode

# ------------------------------ LOOK ------------------------------
label escape_look_around:
    menu:
        n "Where do you look?"
        "Left wall.":
            jump escape_left_wall
        "Back wall.":
            jump escape_back_wall
        "Right wall.":
            jump escape_right_wall
        "Go back.":
            jump escape_main_menu

label escape_left_wall:
    if not escape_testimony_read:
        menu:
            n "The left wall features three coloured sticky notes."
            "Look at the yellow one.":
                jump escape_left_wall_yellow
            "Look at the blue one.":
                jump escape_left_wall_blue
            "Look at the orange one.":
                jump escape_left_wall_orange
            "Go back.":
                jump escape_look_around
    else:
        menu:
            n "The left wall now features two coloured sticky notes."
            "Look at the yellow one.":
                jump escape_left_wall_yellow
            "Look at the orange one.":
                jump escape_left_wall_orange
            "Go back.":
                jump escape_look_around

    label escape_left_wall_yellow:
        if escape_left_wall_password_viewed:
            n "The purple light revealed that the computer's password is 'beans1247'."
            jump escape_left_wall
        else:
            n "You read the yellow sticky note."
            n "\"...The first sighting of the anomaly was on September 23. Since then, there have been 683 more reported appearances.\""
            n "\"Note to personnel:\""
            n "...The rest is cut off."
            if "Purple Light" in escape_inventory:
                n "Hang on, isn't purple the complementary colour of yellow?"
                n "You pull out the little flashlight and shine it on the sticky note."
                n "Under the light, more text becomes visible."
                n "\"Note to personnel: the passcode to the computer is 'beans1247'.\""
                n "You make a mental note of this."
                $ escape_left_wall_password_viewed = True
            jump escape_left_wall
    

    label escape_left_wall_blue:
        n "You read the blue sticky note."
        n "It's labelled, \"Witness Testimony.\""
        n "..."
        n "It's in Swedish. You can't read Swedish, unfortunately."
        if "Phone (Charged)" in escape_inventory:
            n "You do, however, have a translator on your phone."
            n "You open Guugle Trunslate and snap a photo of the sticky note."
            n "It reads:"
            n "\"I just suddenly woke up on the floor of my living room. I- I couldn't remember how I got there, but someone had attached some kind of lock to my front door? They locked me in my own house!\""
            n "\"On top of that, they had rearranged all my belongings and made some kind of escape room. It was so weird. My-\""
            n "The middle part of the testimony is scribbled out."
            n "\"-ckily, I managed to piece together to code, but just as I inputted the code to the front door, the lights went out.\""
            n "\"I could see - no, {i}sense{/i} some kind of figure in the shadows standing right behind me. I didn't dare move.\""
            n "\"After what felt like forever, it introduced itself as:\""

            show black_screen zorder 50
            # stop music
            show layer screens:
                shake
            n "{sc}{color=#ff0000}The Trickster.{/color}{/sc}"
            
            show screen qte(act=Jump("escape_trickster_game_1_fail"), time=6)
            menu:
                n "{sc}{color=#ff0000}Shall we play a game?{/color}{/sc}"
                "Don't turn around." (on_hover = "Turn around."):
                    jump escape_trickster_game_1_fail
                "Don't turn around." (on_hover = "Turn around."): 
                    jump escape_trickster_game_1_fail
                "Don't turn around.": 
                    jump escape_trickster_game_1_2
                "Don't turn around." (on_hover = "Turn around."):
                    jump escape_trickster_game_1_fail
            
            label escape_trickster_game_1_2:
                hide screen qte
                show screen qte(act=Jump("escape_trickster_game_1_fail"), time=4)
                menu:
                    n "{sc}{color=#ff0000}Turn around.{/color}{/sc}"
                    "Don't turn around.": 
                        jump escape_trickster_game_1_3
                    "Don't turn around." (on_hover = "Turn around."):
                        jump escape_trickster_game_1_fail
                    "Don't turn around." (on_hover = "Turn around."): 
                        jump escape_trickster_game_1_fail
                    "Don't turn around." (on_hover = "Turn around."):
                        jump escape_trickster_game_1_fail
                
            label escape_trickster_game_1_3:
                hide screen qte
                show screen qte(act=Jump("escape_trickster_game_1_fail"), time=3)
                menu:
                    n "{sc}{b}{color=#ff0000}FACE ME.{/color}{/b}{/sc}"
                    "Don't turn around." (on_hover = "Turn around."):
                        jump escape_trickster_game_1_fail
                    "Don't turn around." (on_hover = "Turn around."): 
                        jump escape_trickster_game_1_fail
                    "Don't turn around." (on_hover = "Turn around."):
                        jump escape_trickster_game_1_fail
                    "Don't turn around.": 
                        hide screen qte
                        jump escape_trickster_game_1_end
                    
            label escape_trickster_game_1_fail:
                hide screen qte
                n "Your attempts of resistance are futile."
                n "You feel your body turn around, against your will."
                n "You look upwards, {color=#ff0000}against your will.{/color}"
                n "{color=#ff0000}You reach your arm out, {/color}{sc}{color=#ff0000}against your will.{/color}{/sc}"
                n "{cps=*0.35}{sc}{color=#ff0000}You are but a puppet.{/color}{/sc}{/cps}"
                

            label escape_trickster_game_1_end:
                hide black_screen
                n "Suddenly, the lights turn back on."
                n "Your heart is pounding. Your palms are sweaty."
                n "But whatever was behind you is gone."
                n "...Was it ever there to begin with? You don't know."
                n "The blue sticky note is still on the wall in front of you."
                n "You decide to keep it for safekeeping."
                n "Witness Testimony has been added to your inventory."
                $ escape_inventory.append("Testimony (Blue Sticky)")
                $ escape_testimony_read = True
                jump escape_left_wall
    
    label escape_left_wall_orange:
        n "You read the orange sticky note. All it says is:"
        n "\"610: ? + ?? + ???\""
        n "So concise."
        jump escape_left_wall

label escape_back_wall:
    $ escape_back_wall_flavour_text = "The notebook is here."
    if not escape_back_wall_viewed:
        n "There's a countertop on the back wall, on which a notebook rests. Most of the pages are burnt, bloodstained or otherwise vandalized."
        $ escape_back_wall_viewed = True
        $ escape_back_wall_flavour_text = "What do you do?"
    else:
        n "[escape_back_wall_flavour_text]"
    
    menu:
        n "What do you do?"
        "Open notebook.":
            jump escape_back_wall_notebook
        "Go back.":
            jump escape_look_around

    label escape_back_wall_notebook:
        if not escape_back_wall_notebook_viewed:
            n "There's some writing on the back of the notebook's cover."
            n "\"This notebook contains information paramount to the containment of this anomaly. What follows is a brief table of contents.\""
            
        n "\"Page 1: About the anomaly system.\""
        n "\"Page 67: Ciphers and translating them.\""

        if not escape_back_wall_notebook_viewed:
            n "\"Page 193: Tax fraud and illegal immigration.\""
            n "...Maybe the rest isn't so important."
            $ escape_back_wall_notebook_viewed = True

        label escape_back_wall_notebook_flip:
            python:
                escape_flip_to_page = renpy.input("What page do you go to? (\"Back\" to go back.)", default=1)
                if escape_flip_to_page.lower() == "back":
                    Jump("escape_back_wall")
                elif not escape_flip_to_page.isdigit():
                    renpy.notify("Choose a page from 1 to 999.")
                    escape_flip_to_page = renpy.input("What page do you go to? (\"Back\" to go back.)", default=1)
                escape_flip_to_page = int(escape_flip_to_page)
            if escape_flip_to_page == 1:
                n "The page reads:"
                n "\"All anomalies are given a unique identification code comprised of six digits separated three-and-three by a hyphen.\""
                n "\"The first number is the anomaly's {b}threat level{/b} from 1-10, which indicates how dangerous the anomaly is to the general public.\""
                n "\"Following this number is the {b}spawn rate{/b} from 1-100 (with 00 being 100), which is often the anomaly has been encountered."
                n "\"This three-digit number is followed by a hyphen and the anomaly's {b}globalization{/b}, which indicates how widespread the anomaly's presence is.\""
                n "\"Finally, the last digit is the {b}authorization level{/b} required to know about this anomaly from 1-10."
                n "\"For instance, VACF 505-102, nicknamed 'Smiling Marshmallow' is relatively dangerous, found rarely, appears only in specific areas and can be found on the information with some digging.\""
                n "The explanation ends with various doodles of Pochi eating a grinning marshmallow."
            elif escape_flip_tp_page == 50:
                n "Oh! There's something on this page. It appears to be a transcript between two people."
                n "\"{i}*inaudible*{/i}\""
                n "\"{i}...Here? Like, here here?{/i}\""
                n "\"{i}Yeah, I got ... to perform an analysis.{/i}\""
                n "\"{i}Well, shit, where is it?{/i}\""
                n "\"{i}{/i}\""
            elif escape_flip_to_page == 67:
                if not escape_back_wall_notebook_ciphers_viewed:
                    n "The notebook reads:"
                    n "\"Many ciphers exist for a variety of different reasons and are applicable to a wide range of use cases.\""
                    n "\"For instance, Morse code assigns each letter and number a unique combination of short and long pulses, with characters separated by short pauses and words by long pauses.\""
                    n "\"Alternatively, it can be conveyed in written form, where dots and dashes represent short and long pulses respectively, and with letters separated by spaces and words separated by slashes.\""
                    n "\"This allows communication when tools are limited. For example, Morse can be communicated via beeping noises picked up over a radio or lights shone from a mirror.\""
                
                n "\"Below is a chart for translating Morse code.\""
                # show morse CG

                if "Slip of Paper" in escape_inventory:
                    n "You suddenly recall that slip of paper you found in the briefcase. You pull it out, and sure enough, the dots and dashes resemble those on the chart."
                    n "Now's your time to shine. Translate this!"
                    $ escape_morse_attempts = 0
                    
                    label escape_back_wall_notebook_morse_game:
                        $ escape_morse_input = renpy.input("What's the answer?")
                        if escape_morse_input.lower() != "page 140":
                            if escape_morse_attempts == 0:
                                n "..."
                                n "No, that doesn't seem right. Try again."
                                $ escape_morse_attempts += 1
                                jump escape_back_wall_notebook_morse_game
                            elif escape_morse_attempts == 1:
                                n "..."
                                n "Nope. Doesn't seem right. Once more."
                                jump escape_back_wall_notebook_morse_game
                            else:
                                n "..."
                                n "That's probably wrong."
                                player "RAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH{nw}"
                                show aikha at appear
                                aikha "Hey, newbie, what's up?"
                                player "I can't solve this fricking-"
                                aikha happy "Ooh, is that Morse? Give me!"
                                n "Dr. Aikha snatches the paper out of your hand, and without even looking at the cipher, decodes it effortlessly."
                                aikha "Page...140! That's what it says."

                                # TODO: give less points to aikha if you fail this
                                aikha "Hehe, thank me later!"
                        
                        n "\"Page 140\"... You have a feeling you know what this means."

                if not escape_back_wall_notebook_ciphers_viewed:
                    n "\"\"The Vigenere cipher, on the other hand...\""
                    n "You can almost feel the condescending nerd voice emanating from the words on the page and decide to stop before you get infected."
                    $ escape_back_wall_notebook_ciphers_viewed = True
            
            elif escape_flip_to_page == 193:
                n "\"A Guide to Committing Tax Fraud.\""
                n "Unfortunately for you, the guide to illegal immigration seems to be missing."
                n "...You probably have better things to be looking at."

            # elif escape_flip_to_page == 140:
            #     # TODO: UPDATE
            #     $ NullAction()

            elif escape_flip_to_page == 610:
                n "Oh, there's some stuff on this page."
                # show cg
                # 3, 4, 4, 5, 6, 8, ?, 16, 24, 37
                # ARTISAN + GLOBE = BEAR , ELEGANT + STRIFE = FEEL, NEANDERTHAL + ALUMNI = ??
                # T T T T T T T
                #     ^ what is this???
                #  11, 9, 30 TODO: UPDATE ANSWERS
                n "There's a lot going on here. Wonder what any of this means."
                n "You tear the page out for safekeeping."
                $ escape_inventory.append("Page 810 (Numbers)")
            elif escape_flip_to_page == 887:
                n "There's nothing here."
                if escape_back_wall_notebook_gullible_marked:
                    n "...aside from a massive \"L\" written in the middle of the page."

            else:
                if escape_back_wall_notebook_invalid_viewed_times == 0:
                    n "It's impressive how the author managed to use so many words to make so little sense."

                elif escape_back_wall_notebook_invalid_viewed_times == 1:
                    n "The handwriting is atrocious. You can't read any of this."

                elif escape_back_wall_notebook_invalid_viewed_times == 2:
                    n "...That letter's probably an F. No, wait, why does it have a line sticking out from the top? Is this even English?"

                elif escape_back_wall_notebook_invalid_viewed_times == 3:
                    n "The entire page is black...aside from a small, red {color=#ff0000}=){/color} in the corner."

                elif escape_back_wall_notebook_invalid_viewed_times == 4:
                    n "The page reads:"
                    n "\"Did you know it says 'gullible' on page 887?\""
                    $ escape_back_wall_notebook_gullible_marked = True

                elif escape_back_wall_notebook_invalid_viewed_times == 5:
                    n "Oh, the page reads:"
                    n "\"Hahaha, haha, haha haha{i}ha{/i}ha.\""
                    n "\"Haha-\" wait, no, sorry. That should be \"Hehe.\""
                    n "\"Hehe, heheheha.\""
                    n "Oh, it says more at the very bottom of the page:"
                    n "{size=-10}\"Ha\".{/size}"
                    
                else:
                    n "Nothing here is useful."
                $ escape_back_wall_notebook_invalid_viewed_times += 1
            
            jump escape_back_wall_notebook_flip
        
label escape_right_wall:
    menu:
        n "On the right wall, there's a desk and a lounge chair. On the desk is a computer, and underneath lies a briefcase."
        "Check the computer.":
            jump escape_right_wall_computer
        "Check the lounge chair.":
            jump escape_right_wall_lounge_chair
        "Check the briefcase.":
            jump escape_right_wall_briefcase
        "Go back.":
            jump escape_look_around

    label escape_right_wall_computer:
        if escape_right_wall_footage_viewed:
            n "The computer is no longer of use. You know that Uriel was the last person in the room before you."
            jump escape_right_wall
        elif not escape_right_wall_computer_viewed:
            n "You inspect the computer and notice that a few of the cables plugged into it run up the wall."
            n "After following the wires, you notice that they're connected to a security camera sitting in a corner on the ceiling."
            n "You can use this to find out who the last person in this room was! Excitedly, you boot up the computer."
            n "However, your plans come to a halt when the screen asks for a password."
            $ escape_right_wall_computer_viewed = True
        
        menu:
            n "What do you do?"
            "Enter the password.":
                jump escape_right_wall_computer_password
            "Go back.":
                jump escape_right_wall

        label escape_right_wall_computer_password:
            if not escape_left_wall_password_viewed:
                n "...You don't have the password. There's no point in trying to guess it."
                jump escape_right_wall_right_wall
            else:
                n "That's right! You found the password on the back of that sticky note."
                n "You confidently enter..."
                jump escape_right_wall_computer_password_enter
            
            label escape_right_wall_computer_password_enter:
                menu:
                    n "...What was the password again?"
                    "peas1247":
                        n "..."
                        n "Wrong password."
                        jump escape_right_wall_computer_password_enter
                    "peas1274":
                        n "..."
                        n "Wrong password."
                        jump escape_right_wall_computer_password_enter
                    "beans1247":
                        n "You enter the password...and the computer opens! Yippee!!"
                        n "You find the security program and search through the past few days' worth of footage."
                        n "After reversing for a while, you stumble upon the most recent instance of people being in the room."

                        # animate this
                        n "You see Dr. Jessie and Uriel talking in the room before Dr. Jessie turns around and leaves."
                        n "Uriel paces around the room for a while before Dr. Jessie returns with Dr. Ryz."
                        n "Uriel and Dr. Ryz start talking animatedly. After a little bit, he sighs and exits."
                        n "Dr. Jessie waves at Uriel and leaves once more."
                        n "Uriel starts going through the items in the room. They flip through the notebook, inspect the sticky notes and try to open the computer."
                        n "Dr. Ryz appears a few minutes later, holding a comically large stack of paper and a pen."
                        n "Uriel points to outside the room, and Dr. Ryz sighs dramatically before leaving for a third time."
                        n "Uriel also sighs, taps something on the keypad next to the door and leaves."

                        n "...Well, there's your answer."
                        $ escape_right_wall_footage_viewed = True
                        jump escape_right_wall

                    "beans1274":
                        n "..."
                        n "Wrong password."
                        jump escape_right_wall_computer_password_enter
    
    label escape_right_wall_lounge_chair:
        if "Phone (Charged)" in escape_inventory:
            n "No time for breaks."
            jump escape_right_wall
        
        n "You inspect the lounge chair. It looks very comfy."
        menu:
            n "Take a seat?"
            "Yes.":
                jump escape_right_wall_lounge_chair_sit
            "No.":
                jump escape_right_wall

        label escape_right_wall_lounge_chair_sit:
            n "You plop yourself happily on the lounge chair."
            n "..?"
            n "There's something under the cushion."
            n "You found a phone charger."
            if not escape_checked_phone:
                n "That reminds you. You rummage your pockets and pull out your phone."
                n "You tap the screen, but it doesn't power on. How convenient of the phone charger to make its presence known."

            n "You find the nearest outlet and start charging your phone."
            n "After a little bit, the screen turns on. Nice!"
            $ escape_inventory.remove("Phone (Dead)")
            $ escape_inventory.append("Phone (Charged)")
            jump escape_right_wall


    label escape_right_wall_briefcase:
        if escape_right_wall_briefcase_opened:
            n "The briefcase is now empty."
            jump escape_right_wall
        elif not escape_right_wall_briefcase_viewed:
            n "You check the briefcase. Embedded on the front of it is what appears to be a small square with a corner folded in."
            n "You try to open it, but it's locked with a colour code."
            $ escape_right_wall_briefcase_viewed = True
        else:
            n "Embedded on the front of the briefcase is what appears to be a small square with a corner folded in."
        
        menu: 
            n "What do you do?"
            "Open the briefcase.":
                jump escape_right_wall_open_briefcase
            "Go back.":
                jump escape_right_wall

        label escape_right_wall_open_briefcase:
            $ escape_right_wall_briefcase_code_correct = True
            menu:
                n "What's the first colour?"
                "Red.":
                    $ escape_right_wall_briefcase_code_correct = False
                "Pink.":
                    $ escape_left_wall_briefcase_code_correct = False
                "Yellow.":
                    $ NullAction()
                "Crimson.":
                    $ escape_right_wall_briefcase_code_correct = False
            menu:
                n "What's the second colour?"
                "Green.":
                    $ escape_right_wall_briefcase_code_correct = False
                "Teal.":
                    $ escape_right_wall_briefcase_code_correct = False
                "Purple.":
                    $ escape_right_wall_briefcase_code_correct = False
                "Blue.":
                    $ NullAction()
            
            menu:
                n "What's the third colour?"
                "Orange.":
                    $ NullAction()
                "Brown.":
                    $ escape_right_wall_briefcase_code_correct = False
                "White.":
                    $ escape_right_wall_briefcase_code_correct = False
                "Black.":
                    $ escape_right_wall_briefcase_code_correct = False
                
            if escape_right_wall_briefcase_code_correct:
                n "You hear a click. The briefcase opens!"
                n "Within the briefcase, you find a small slip of paper and a tiny flashlight."
                n "The slip of paper is filled with dots, dashes and slashes."
                if escape_back_wall_notebook_ciphers_viewed:
                    n "Seems awfully familiar..."
                else:
                    n "You don't know what to make of it."
                
                n "You play with the flashlight a bit. It emits a purple light."
                n "After turning it around in your hands, you notice a small note attached to it that reads:"
                n "\"Find my complement.\""
                n "There doesn't seem to be anything else in the briefcase."
                n "Both items have been added to your inventory."
                $ escape_inventory.append("Slip of Paper")
                $ escape_inventory.append("Purple Light")
                jump escape_right_wall
            else:
                n "The briefcase doesn't open."
                jump escape_right_wall_briefcase

# ------------------------------ TALK ------------------------------
label escape_talk:
    # implement current_task sorted list being the most recent puzzles (e.g. swedish, having a charged phone, briefcase)
        # each item should be task name (string), aikha_seen (bool), ryz_seen (bool), wal_seen (bool)
    # go down the list for each personnel and trigger dialogue about them
    # once list is exhausted, have list of generic dialogue event labels and trigger them sequentially (or random if not too hard)
    menu:
        n "To who?"
        "Dr. Aikha.":
            jump escape_talk_aikha
        "Dr. Ryz.":
            jump escape_talk_ryz
        "Dr. Firewal.":
            jump escape_talk_firewal
        "Go back.":
            jump escape_main_menu

# ------------------------------ INVENTORY ------------------------------

label escape_inventory_menu:
    call escape_inventory_screen
    n "You check your inventory."
    $ ui.interact()
    # jump escape_inventory_menu


label escape_item_testimony:
    n "{color=#ff0000}The Trickster.{/color}"
    # add rest of testimony to locked app in phone
    return


# ------------------------------ PASSCODE ------------------------------
label escape_passcode:
    $ escape_plural = "" if escape_passcode_attempts_remaining == 1 else "s"
    menu:
        n "You have [escape_passcode_attempts_remaining] attempt[escape_plural] remaining. Are you sure you would like to submit the code?"
        "Yes.":
            jump escape_submit_passcode_1
        "Go back.":
            jump escape_main_menu

label escape_submit_passcode_1:
    menu:
        n "What does the anomaly look like?"
        "An amorphous blob.":
            jump escape_submit_passcode_2
        "A smiling marshmallow.":
            jump escape_submit_passcode_2
        "An invisible entity.":
            jump escape_submit_passcode_2
        "A human-like creature.":
            jump escape_submit_passcode_2

label escape_submit_passcode_2:
    menu:
        n "What's its spawn rate value?"
        "Low (001-333).":
            jump escape_submit_passcode_3
        "Medium (334-666).":
            jump escape_submit_passcode_3
        "High (667-999).":
            jump escape_submit_passcode_3

label escape_submit_passcode_3:
    menu:
        n "What's its globalization value?"
        "Low (001-333).":
            jump escape_submit_passcode_4
        "Medium (334-666).":
            jump escape_submit_passcode_4
        "High (667-999).":
            jump escape_submit_passcode_4

label escape_submit_passcode_4:
    menu:
        n "Who was last in the room?"
        "Dr. Ryz.":
            jump escape_submit_passcode_end
        "Uriel.":
            jump escape_submit_passcode_end
        "Dr. Deceased.":
            jump escape_submit_passcode_end
        "Dr. Jessie.":
            jump escape_submit_passcode_end

label escape_submit_passcode_end:
    n "blegh"

    player "Say, Dr. Ryz, can't you just like...walk through the wall and free us?"
    ryz "Hm? Well, I guess, but I spent {i}way{/i} too long coding this."
    player "What?"
    ryz "What?"



# setting: trapped in the containment room
# need the code for the front door
# the code is based off the anomaly that was initially contained in here
# split into three parts:
# anomaly name + VACF foundation number + personnel who contained it

