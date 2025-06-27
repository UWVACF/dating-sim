image escape_it = "images/cgs/escape it.png"
image escape_blue_sticky = "images/cgs/escape blue sticky.png"
image escape_peculiar_paper = "images/cgs/escape peculiar paper.png"

# TODO
# make cgs
#   morse
#   page 810
# minigame at very end, reverse pandemonium, keep mouse out of button in middle while it slowly gets dragged in
# inventory

init python:
    def escape_check_drag_positions():
        if not escape_left_wall_blue_sticky_completed:
            threshold = 1.5
            
            sticky_props = renpy.get_placement(renpy.get_displayable("escape_blue_sticky_screen", "sticky"))
            paper_props = renpy.get_placement(renpy.get_displayable("escape_blue_sticky_screen", "paper"))

            if abs(sticky_props.xpos + 17 - paper_props.xpos) < threshold and abs(sticky_props.ypos - paper_props.ypos - 15) < threshold:
                renpy.jump("escape_left_wall_blue_sticky_end")

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
        escape_blue_sticky_read = False

        escape_left_wall_blue_sticky_completed = False

        escape_passcode_attempts_remaining = 5
        escape_inventory = ["Peculiar Paper", "Blue Sticky", "Page 524", "Page 621", "Purple Light", "Slip of Paper"]
        escape_item_labels = {
            "Peculiar Paper": "escape_item_peculiar_paper",
            "Blue Sticky": "escape_item_blue_sticky",
            "Page 524": "escape_item_page_524",
            "Page 621": "escape_item_page_621",
            "Purple Light": "escape_item_purple_light",
            "Slip of Paper": "escape_item_slip_of_paper",
        }

        escape_inventory_page = 0
        escape_inventory_display_per_page = 3

    return

screen escape_inventory_screen:

    vbox:
        xalign 0.5
        yalign 0.5
        spacing gui.choice_spacing

        text "Your Inventory":
            size 50
            xalign 0.13

        $ escape_inventory_screen_start = escape_inventory_page * escape_inventory_display_per_page
        $ escape_inventory_screen_end = escape_inventory_screen_start + escape_inventory_display_per_page
        $ escape_inventory_displayed_items = escape_inventory[escape_inventory_screen_start:escape_inventory_screen_end] 
        for i in escape_inventory_displayed_items:
            textbutton i:
                xalign 0.5
                style "choice_button"
                action Call(escape_item_labels[i])
    
        textbutton "Go back.":
            xalign 0.5
            style "choice_button"
            action Jump("escape_main_menu")

        hbox:
            xalign 0.5
            spacing 800

            textbutton "<":
                xsize 78
                ysize 78
                xalign 0.0

                text_xalign 0.5
                action SetVariable("escape_inventory_page", escape_inventory_page - 1)
                sensitive escape_inventory_page != 0
                idle_background "gui/button/choice_small_idle_background.png"
                hover_background "gui/button/choice_small_hover_background.png"
                insensitive_background "gui/button/choice_small_insensitive_background.png"


            textbutton ">":
                xsize 78
                ysize 78
                xalign 1.0
                text_xalign 0.5
                action SetVariable("escape_inventory_page", escape_inventory_page + 1)
                sensitive escape_inventory_page != int(len(escape_inventory) / escape_inventory_display_per_page) - 1
                idle_background "gui/button/choice_small_idle_background.png"
                hover_background "gui/button/choice_small_hover_background.png"
                insensitive_background "gui/button/choice_small_insensitive_background.png"

screen escape_blue_sticky_screen:
    drag:

        id "sticky"
        xalign 0.2
        yalign 0.5
        draggable not escape_left_wall_blue_sticky_completed
        add "images/cgs/escape blue sticky.png"
    drag:
        id "paper"
        xalign 0.8
        yalign 0.5
        draggable not escape_left_wall_blue_sticky_completed
        add "images/cgs/escape peculiar paper.png"
    timer 0.1 repeat True action Function(escape_check_drag_positions)

label day_event_escape:
    call escape_initialize
    scene bg hallway
    player "Yeah!!! It's coffee time!!"
    n "You excitedly hurry over to the lounge to indulge in your coffee addiction when-"
    show escape_it
    with hpunch
    scene bg room containment
    with Fade(0.0, 1.0, 1.0)
    player "Huh? What?"
    n "You suddenly wake up and find yourself sprawled on the floor of some room."
    aikha "Oh, look who the cat dragged in."
    show aikha at appear(x_align = 0.2)
    show ryz at appear(x_align = 0.5)
    show firewal at appear(x_align = 0.8)
    ryz "Morning, [player_name]."
    player "Where the hell are we?"
    firewal "No clue. Think we're in some containment room."
    aikha "We all just kind of woke up here."
    n "You look at the door to the room and see a tablet attached to it. Lying beside it is a torn scrap of paper. It reads;"
    n "\"..And for those who forgot, the password is simply the anomaly's name, V.A.C. number and appearance.\""
    n "\"Signed, #######\""
    n "The name is blacked out."
    ryz "This is actually quite convenient. Matter of fact, I was just doing some research into this anomaly."
    aikha "Oh, this is fun!. Newbie, there should be hints scattered around the room. Try to piece together the puzzle and get us out of here!"
    show aikha at disappear
    show ryz at disappear
    show firewal at disappear
    jump escape_main_menu

label escape_main_menu:
    if "Page 524" in escape_inventory and "Page 621" in escape_inventory and "Blue Sticky" in escape_inventory and escape_right_wall_footage_viewed:
        menu:
            n "You have everything you need to submit the passcode."
            "Look around.":
                jump escape_look_around
            "Talk.":
                jump escape_talk
            "Check inventory.":
                jump escape_inventory_menu
            "Submit the passcode.":
                jump escape_passcode
    else:
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
    if not escape_blue_sticky_read:
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
            n "\"Note to personnel:\""
            n "...The message cuts off there."
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
        n "It's a garbled mess of random letters."
        n "Notably, on the top left of the sticky note is a cane symbol."
        if "Peculiar Paper" in escape_inventory:
            n "Wait. A cane symbol?"
            n "You take the peculiar piece of paper that you found in the drawer out, and, sure enough, the cane symbols are exactly the same."

            show screen escape_blue_sticky_screen
            n "You know what to do. Probably."
            while True:
                $ ui.interact()

            # minigame
            label escape_left_wall_blue_sticky_end:
                $ escape_left_wall_blue_sticky_completed = True
                n "When you aligned the symbols together, the holes in the paper revealed a message."
                n "\"It introduced itself as{w=0.5}{nw}"

                hide screen escape_blue_sticky_screen

                show black_screen zorder 50
                # stop music
                show layer screens:
                    shake(preset="rumble")
                n "{sc}{color=#ffffff}The Trickster.{/color}{/sc}"
                
                show screen qte(act=Jump("escape_trickster_game_1_fail"), time=6)
                menu:
                    n "{sc}{color=#ffffff}Shall we play a game?{/color}{/sc}"
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
                        n "{sc}{color=#ffffff}Turn around.{/color}{/sc}"
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
                        n "{sc}{b}{color=#ffffff}Face me.{/color}{/b}{/sc}"
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
                    hide black_screen
                    show escape_it zorder 50
                    n "Your attempts of resistance are futile."
                    n "You feel your body turn around, against your will."
                    n "You look upwards, {color=#ffffff}against your will.{/color}"
                    n "{color=#ffffff}You reach your arm out, {/color}{sc}{color=#ffffff}against your will.{/color}{/sc}"
                    n "{cps=*0.35}{sc}{color=#ffffff}You are but a puppet.{/color}{/sc}{/cps}"
                    

                label escape_trickster_game_1_end:
                    hide black_screen
                    hide escape_it
                    n "Suddenly, the lights turn back on."
                    n "Your heart is pounding. Your palms are sweaty."
                    n "But whatever was behind you is gone."
                    n "...Was it ever there to begin with?"
                    n "The blue sticky note is still on the wall in front of you."
                    n "You decide to keep it for safekeeping."
                    n "Blue Sticky has been added to your inventory."
                    $ escape_inventory.append("Blue Sticky")
                    $ escape_blue_sticky_read = True
                    jump escape_left_wall
    
    label escape_left_wall_orange:
        n "You read the orange sticky note. All it says is:"
        n "\"810: ? x ??? - ??\""
        n "So concise."
        jump escape_left_wall

label escape_back_wall:
    $ escape_back_wall_flavour_text = "The notebook is here."
    if not escape_back_wall_viewed:
        n "There's a countertop on the back wall, on which a notebook rests. Most of the pages are burnt, bloodstained or otherwise vandalized."
        $ escape_back_wall_viewed = True
        $ escape_back_wall_flavour_text = "What do you do?"
    
    menu:
        n "[escape_back_wall_flavour_text]"
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

        python:
            escape_flip_to_page = renpy.input("What page do you go to? (1-999, \"back\" to go back.)", default=1)
            if escape_flip_to_page.lower() == "back":
                Jump("escape_back_wall")
            while not escape_flip_to_page.isdigit():
                renpy.notify("Invalid input.")
                escape_flip_to_page = renpy.input("What page do you go to? (1-999, \"back\" to go back.)", default=1)
            
            escape_flip_to_page = int(escape_flip_to_page)
        
        if escape_flip_to_page == 1:
            n "The page reads:"
            n "\"All anomalies are given a unique identification code comprised of six digits separated three-and-three by a hyphen.\""
            n "\"The first number is the anomaly's {b}threat level{/b} from 1-10 (with 0 being 10), which indicates how dangerous the anomaly is to the general public.\""
            n "\"Following this number is the {b}spawn rate{/b} from 1-100 (with 00 being 100), which is often the anomaly has been encountered."
            n "\"This three-digit number is followed by a hyphen and the anomaly's {b}globalization{/b} from 1-100 (with 00 being 100), which indicates how widespread the anomaly's presence is.\""
            n "\"Finally, the last digit is the {b}authorization level{/b} required to know about this anomaly from 1-10 (with 0 being 10)."
            n "\"For instance, VAC 505-102, nicknamed 'Smiling Marshmallow' is relatively dangerous, found rarely, appears only in specific areas and can be found on the information with some digging.\""
            n "The explanation ends with various doodles of Pochi eating a grinning marshmallow."
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
                n "Now's your time to shine. Decipher this!"
                $ escape_morse_attempts = 0
                
                label escape_back_wall_notebook_morse_game:
                    $ escape_morse_input = renpy.input("What's the answer?")
                    if escape_morse_input.lower() != "page 524":
                        if escape_morse_attempts == 0:
                            n "..."
                            n "No, that doesn't seem right. Try again."
                            $ escape_morse_attempts += 1
                            jump escape_back_wall_notebook_morse_game
                        elif escape_morse_attempts == 1:
                            n "..."
                            n "Nope. Doesn't seem right. Once more."
                            $ escape_morse_attempts += 1
                            jump escape_back_wall_notebook_morse_game
                        else:
                            n "..."
                            n "That's probably wrong."
                            player "RAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH{nw}"
                            show aikha at appear
                            aikha "Hey newbie, what's going on?"
                            player "I can't solve this fricking-"
                            aikha happy "Ooh, is that Morse? Gimme!"
                            n "Dr. Aikha snatches the paper out of your hand, and without even looking at the cipher, decodes it effortlessly."
                            aikha "Page...524! That's what it says."

                            # TODO: give less points to aikha if you fail this
                            aikha "Haha, you can thank me later!"
                    
                    n "\"Page 524\"... You have a feeling you know what this means."

            if not escape_back_wall_notebook_ciphers_viewed:
                n "\"\"The Vigenere cipher, on the other hand...\""
                n "You can almost feel the condescending nerd voice emanating from the words on the page and decide to stop before you get infected."
                $ escape_back_wall_notebook_ciphers_viewed = True
        
        elif escape_flip_to_page == 193:
            n "\"A Guide to Committing Tax Fraud.\""
            n "Unfortunately for you, the guide to illegal immigration seems to be missing."
            n "...Actually, you probably have better things to be looking at."
        elif escape_flip_tp_page == 524:
            if "Page 524" not in escape_inventory:
                n "Oh! There's something on this page. It reads:"

            call escape_item_page_524

            if "Page 524" not in escape_inventory:
                n "You tear the page out for safekeeping."
                $ escape_inventory.append("Page 524")
        elif escape_flip_to_page == 621:
            if "Page 621" not in escape_inventory:
                n "There's some writing on the page. It reads:"

            call escape_item_page_621

            if "Page 621" not in escape_inventory:
                n "You tear the page out for safekeeping."
                $ escape_inventory.append("Page 621")

        elif escape_flip_to_page == 810:
            if "Page 810 (Numbers)" in escape_inventory:
                $ NullAction()
                # show cg
            else:
                n "Oh, there's some stuff on this page."
                # show cg
                # 1, 3, 6, 10, 15, ?, 28, 35... (21)
                # ARTISAN + GLOBE = BEAR , ELEGANT + STRIFE = FEEL, NEANDERTHAL + ALUMNI = ?? (9)
                # T T T T T T T (30)
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
                n "The entire page is black...aside from a small, red {color=#ffffff}=){/color} in the corner."

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
        n "On the right wall, there's a desk with a drawer. On the desk is a computer, and underneath lies a briefcase."
        "Check the computer.":
            jump escape_right_wall_computer
        "Check the drawer.":
            jump escape_right_wall_drawer
        "Check the briefcase.":
            jump escape_right_wall_briefcase
        "Go back.":
            jump escape_look_around

    label escape_right_wall_computer:
        if escape_right_wall_footage_viewed:
            n "The computer is no longer of use. You know that the anomaly is a tall figure in a trench coat that dons a wide-brimmed hat."
            jump escape_right_wall
        elif not escape_right_wall_computer_viewed:
            n "You inspect the computer and notice that a few of the cables plugged into it run up the wall."
            n "After following the wires, you notice that they're connected to a security camera sitting in a corner on the ceiling."
            n "You realize you can use this to find out more about the anomaly. Excitedly, you boot up the computer."
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
                        $ escape_right_wall_footage_viewed = True
                        n "You enter the password and unlock the computer."
                        n "You navigate over to the security camera program to review the footage from the past few days."
                        n "Nothing of note happens until you look at the footage from earlier today."
                        n "You see a tall figure in a trench coat and wide-brimmed hat enter the room. Despite the room being alit, the figure is but a silhouette."
                        n "You watch as it moves around the room, placing various objects in certain locations: the sticky notes, the briefcase, the computer, et cetera."
                        n "Once it's done, it turns to face the camera {nw}"

                        show escape_it zorder 50
                        extend "before the entire room goes dark."
                        n "{cps=*0.5}You can almost feel {/cps}"
                        n "{cps=*0.5}a presence {/cps}"
                        n "{cps=*0.5}standing right in front you.{/cps}"

                        hide escape_it
                        n "Suddenly, the power comes back."
                        n "However, the computer in front of you stays off. You inspect it, but you can't find the reason why."
                        n "No matter. You got what you needed."
                        jump escape_right_wall

                    "beans1274":
                        n "..."
                        n "Wrong password."
                        jump escape_right_wall_computer_password_enter
    
    label escape_right_wall_drawer:
        if "Peculiar Paper" not in escape_inventory:
            n "You open the drawer and find a peculiar looking piece of paper. It's entirely black, with numerous small, square holes cut into it."
            # show cg
            n "Notably, on the top left of the paper is a cut-out cane."
            n "This feels important. You take the piece of paper for safekeeping."
            $ escape_inventory.append("Peculiar Paper")
        else:
            n "The drawer is now empty."
        jump escape_right_wall


    label escape_right_wall_briefcase:
        if escape_right_wall_briefcase_opened:
            n "The briefcase is now empty."
            jump escape_right_wall
        elif not escape_right_wall_briefcase_viewed:
            n "You check the briefcase. Embedded on the front of it is what appears to be a small square with a corner folded in."
            n "You try to open it, but it's locked. It looks like its code consists of three colours."
            $ escape_right_wall_briefcase_viewed = True
        else:
            n "Embedded on the front of the briefcase is what appears to be a small square with a corner folded in."
        
        menu: 
            n "What do you do?"
            "Enter the briefcase code.":
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

    label escape_talk_aikha:
        player "A"

    label escape_talk_ryz:
        player "Say, Dr. Ryz, can't you just like...walk through the wall and free us?"
        ryz "Hm? Well, I guess, but I spent {i}way{/i} too long coding this."
        player "What?"
        ryz "What?"

    label escape_talk_firewal:
        player "A"


# ------------------------------ INVENTORY ------------------------------

label escape_inventory_menu:
    if not escape_inventory:
        n "Your inventory is empty."
    else:
        $ escape_inventory_page = 0
        call screen escape_inventory_screen
    jump escape_main_menu
    


label escape_item_blue_sticky:
    n "{color=#ffffff}The Trickster.{/color}"
    # add rest of testimony to locked app in phone
    return

label escape_item_page_524:
    n "\"VAC 524-### is an entity of unknown origin that appears all around the world. It will choose and trap victims seemingly at random before using nearby objects to form puzzles and riddles to form something akin to an escape room.\""
    n "\"Victims have described the anomaly as having...\""
    n "The rest is crossed out."
    return

label escape_item_page_621:
    n "\"...a 'booming voice [[that] inflicts fear with every syllable.' VAC ###-621 seems to enjoy the suffering of its victims, as it frequently sabotages escape attempts by laying red herrings or by appearing behind the victim and coercing them to 'turn around.'\""
    n "In the event that a victim complies and turns around, it will..."
    n "The rest is crossed out."
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
    $ escape_submit_passcode_correct = True
    menu:
        n "What does the anomaly look like?"
        "An massive, amorphous blob.":
            $ escape_submit_passcode_correct = False
            jump escape_submit_passcode_2
        "A figure with a blood-red hood and cloak.":
            $ escape_submit_passcode_correct = False
            jump escape_submit_passcode_2
        "A silhouette with a trench coat and a hat.":
            jump escape_submit_passcode_2
        "It's invisible.":
            $ escape_submit_passcode_correct = False
            jump escape_submit_passcode_2

label escape_submit_passcode_2:
    python:
        escape_submit_passcode_2_input = renpy.input("What's the anomaly's VAC number?")
        while len(escape_submit_passcode_2_input) != 7 or escape_submit_passcode_2_input[3] != "-" or not escape_submit_passcode_2_input[:3].isdigit() or not escape_submit_passcode_2_input[4:].isdigit():
            renpy.notify("Invalid input. Make sure you input two three-digit numbers separated by a hyphen.")
            escape_submit_passcode_2_input = renpy.input("What's the anomaly's VAC number?")
    
    if escape_submit_passcode_2_input != "524-621":
        $ escape_submit_passcode_correct = False
    jump escape_submit_passcode_3
    

label escape_submit_passcode_3:
    menu:
        n "What's the anomaly's name?"
        "The Jester.":
            $ escape_submit_passcode_correct = False
            jump escape_submit_passcode_end
        "The Trickster.":
            jump escape_submit_passcode_end
        "The Fool.":
            $ escape_submit_passcode_correct = False
            jump escape_submit_passcode_end
        "The Reaper.":
            $ escape_submit_passcode_correct = False
            jump escape_submit_passcode_end

label escape_submit_passcode_end:
    if not escape_submit_passcode_correct:
        n "The tablet beeps, and the screen flashes red."
        if escape_passcode_attempts_remaining == 5:
            n "No worries. One mistake isn't the end of the world."
        elif escape_passcode_attempts_remaining == 4:
            n "Be a little more careful next time."
        elif escape_passcode_attempts_remaining == 3:
            n "You should really confirm your answers before entering them."
        elif escape_passcode_attempts_remaining == 2:
            n "It's about to be the end of the world."
            n "Your world, at least."
        elif escape_passcode_attempts_remaining == 1:
            n "The tablet lets out a ear-piercing screech before the screen shatters."
            show escape_it zorder 50:
                alpha 1.0
                0.3 
                alpha 0.0
                0.4
                alpha 1.0
            n "The lights flicker and go out."
            n "{color=#ffffff}I thought there was more to you than this.{/color}"
            n "{color=#ffffff}A shame. It really is a shame.{/color}"
            n "{color=#ffffff}Well now. You have served your purpose.{/color}"
            n "{color=#ffffff}You are no longer of use.{/color}"

            n "You notice"
            n "a presence"
            n "right"
            n "in front"
            n "of you.{nw}"
            # jumpscare
            return
            
        $ escape_passcode_attempts_remaining -= 1
    else:
        n "The tablet lets out a jingle, and the screen flashes green!"
        n "You hear the door click."
        show aikha happy at appear
        aikha "Newbie! You solved it!"
        show ryz at appear(x_align = 0.8)
        ryz "Oh hey, you got it."
        show firewal happy at appear(x_align = 0.2)
        firewal "Congrats! Let's go."
        n "Dr. Aikha and Dr. Firewal make their way out the door. You're about to follow them when you get a weird feeling."
        n "Something's...off."
        


    



# setting: trapped in the containment room
# need the code for the front door
# the code is based off the anomaly that was initially contained in here
# split into three parts:
# anomaly name + VACF foundation number + personnel who contained it
