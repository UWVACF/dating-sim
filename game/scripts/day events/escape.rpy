image escape_it = "images/cgs/escape it.png"
image escape_blue_sticky = "images/cgs/escape blue sticky.png"
image escape_peculiar_paper = "images/cgs/escape peculiar paper.png"

# TODO
# make cgs
#   morse (cipher + code)
#   page 810
# dialogue
# hint + solution system

# trickster colour is #095a10 (ctrl f to replace)

init python:
    def escape_check_drag_positions():
        if not escape_left_wall_blue_sticky_completed:
            threshold = 1.5
            
            sticky_props = renpy.get_placement(renpy.get_displayable("escape_blue_sticky_screen", "sticky"))
            paper_props = renpy.get_placement(renpy.get_displayable("escape_blue_sticky_screen", "paper"))

            if abs(sticky_props.xpos + 17 - paper_props.xpos) < threshold and abs(sticky_props.ypos - paper_props.ypos - 15) < threshold:
                renpy.jump("escape_left_wall_blue_sticky_end")
    
    def escape_lose_life(label):
        global escape_end_lives
        escape_end_lives -= 1
        print("escape end lives is ", escape_end_lives)
        print("label is ", label)
        renpy.jump("escape_lose_life_animations", lab=label)
    
    def escape_drag_mouse():
        import math
        mx, my = renpy.get_mouse_pos()
        cx, cy = config.screen_width / 2, config.screen_height / 2
        d = escape_final_minigame_pull_strength
        dx = cx - mx
        dy = cy - my
        length = math.hypot(dx, dy)
        if length <= d:
            new_x, new_y = cx, cy  # already at center
        else:
            # normalize
            move_x = dx / length * d
            move_y = dy / length * d

            # find updated position
            new_x = mx + move_x
            new_y = my + move_y
        
        renpy.run(MouseMove(new_x, new_y))
    
    def escape_final_minigame_disable():
        if not escape_final_minigame_is_hovering:
            renpy.run(SetVariable("qte_paused", True))
    
    def escape_final_minigame_enable():
        if not escape_final_minigame_is_hovering:
            renpy.run(SetVariable("qte_paused", False))
        

        
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

        escape_aikha_solved_morse = False

        escape_passcode_attempts_remaining = 5
        escape_inventory = ["Peculiar Paper", "Blue Sticky", "Page 524", "Page 621", "Purple Light", "Slip of Paper"]
        escape_item_labels = {
            "Peculiar Paper": "escape_item_peculiar_paper",
            "Blue Sticky": "escape_item_blue_sticky",
            "Page 524": "escape_item_page_524",
            "Page 621": "escape_item_page_621",
            "Page 810 (Puzzles)": "escape_item_page_810",
            "Purple Light": "escape_item_purple_light",
            "Slip of Paper": "escape_item_slip_of_paper",
        }

        escape_inventory_page = 0
        escape_inventory_display_per_page = 3

        escape_end_lives = 3

        escape_moving_minigame_phase = 0
        escape_moving_minigame_max_phase = 3
        escape_moving_minigame_delays = [0.6, 0.4, 0.15]
        escape_moving_minigame_dialogue = ["Turn around!", "You think you're funny?", "Stop disobeying me."]

        escape_inventory_current_item = ""

        escape_talk_shown_item = ""

        escape_inventory_screen_is_talking = False
        escape_inventory_talking_to = ""

        escape_talked = False

        escape_talk_items = {
            "aikha":
            {
                "Peculiar Paper": False,
                "Blue Sticky": False,
                "Page 524": False,
                "Page 621": False,
                "Page 810": False,
                "Purple Light": False,
                "Slip of Paper": False,
            },
            "ryz":
            {
                "Peculiar Paper": False,
                "Blue Sticky": False,
                "Page 524": False,
                "Page 621": False,
                "Page 810": False,
                "Purple Light": False,
                "Slip of Paper": False,
                "Escaping": False,
            },
            "firewal":
            {
                "Peculiar Paper": False,
                "Blue Sticky": False,
                "Page 524": False,
                "Page 621": False,
                "Page 810": False,
                "Purple Light": False,
                "Slip of Paper": False,
            }
        }

        escape_talk_chats_aikha = 0
        escape_talk_chats_ryz = 0
        escape_talk_chats_firewal = 0

    return

screen escape_inventory_screen:
    vbox:
        xalign 0.5
        yalign 0.5
        spacing gui.choice_spacing


        hbox:
            xalign 0.5
            spacing 300
            text "Your Inventory":
                size 50
                xalign 0.0
                yalign 0.5
            textbutton "Go back.":
                style "choice_button"
                xalign 1.0
                xsize 230
                action If(escape_inventory_screen_is_talking,
                        true=If(escape_inventory_talking_to == "aikha",
                                true=Jump("escape_talk_aikha"),
                                false=If(escape_inventory_talking_to == "ryz",
                                        true=Jump("escape_talk_ryz"),
                                        false=Jump("escape_talk_firewal"))),
                        false=Jump("escape_main_menu"))

        $ escape_inventory_screen_start = escape_inventory_page * escape_inventory_display_per_page
        $ escape_inventory_screen_end = escape_inventory_screen_start + escape_inventory_display_per_page
        $ escape_inventory_displayed_items = escape_inventory[escape_inventory_screen_start:escape_inventory_screen_end] 
        for i in escape_inventory_displayed_items:
            textbutton i:
                xalign 0.5
                style "choice_button"
                action If(escape_inventory_screen_is_talking, true=[SetVariable("escape_talk_shown_item", i), Return()], false=[SetVariable("escape_inventory_current_item", escape_item_labels[i]), Jump("escape_call_item_label")])

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

label escape_call_item_label:
    $ renpy.call(escape_inventory_current_item)
    jump escape_inventory_menu

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

screen escape_blue_sticky_screen_answer:
    drag:
        id "sticky"
        xalign 710
        yalign 290
        draggable False
        add "images/cgs/escape blue sticky.png"
    drag:
        id "paper"
        xalign 727
        yalign 275
        draggable False
        add "images/cgs/escape peculiar paper.png"

default escape_final_minigame_hp = 100
default escape_final_minigame_is_hovering = False
default escape_final_minigame_pull_strength = 10

screen escape_final_minigame:
    button:
        background None
        xsize 1920
        ysize 1080
        xpos 0
        ypos 0
        hovered Function(escape_final_minigame_enable)
        unhovered Function(escape_final_minigame_disable)
        action NullAction()

    vbox:
        xalign 0.5
        yalign 0.5
        textbutton "Turn around.":
            xalign 0.5
            yalign 0.5
            text_xalign 0.5
            text_yalign 0.5
            xsize 417
            ysize 87
            hovered SetVariable("escape_final_minigame_is_hovering", True)
            unhovered SetVariable("escape_final_minigame_is_hovering", False)
            idle_background "gui/button/choice_idle_background.png"
            hover_background "gui/button/choice_red_hover_background.png"
            action NullAction()
    
    timer 0.1:
        repeat True
        action If(escape_final_minigame_is_hovering, true=SetVariable("escape_final_minigame_hp", escape_final_minigame_hp - 10))
    timer 0.1:
        repeat True
        action If(escape_final_minigame_hp < 0, true=Jump("escape_bad_end"))
    
    timer 0.05:
        repeat True
        action Function(escape_drag_mouse)
    
    timer 2.0:
        action SetVariable("escape_final_minigame_pull_strength", 20)
    timer 4.0:
        action SetVariable("escape_final_minigame_pull_strength", 30)
    timer 6.0:
        action SetVariable("escape_final_minigame_pull_strength", 40)
    timer 8.0:
        action SetVariable("escape_final_minigame_pull_strength", 50)
        
screen escape_unwinnable:
    vbox:
        xalign 0.5
        yalign 0.5
        textbutton "TURN AROUND.":
            xalign 0.5
            yalign 0.5
            text_xalign 0.5
            text_yalign 0.5
            xsize 417
            ysize 87
            idle_background "gui/button/choice_idle_background.png"
            hover_background "gui/button/choice_red_hover_background.png"
            action Return()
    
    timer 0.05:
        repeat True
        action Function(escape_drag_mouse)
    
    timer 1.0:
        action SetVariable("escape_final_minigame_pull_strength", 100)
    timer 2.0:
        action SetVariable("escape_final_minigame_pull_strength", 200)
    timer 3.0:
        action SetVariable("escape_final_minigame_pull_strength", 400)
    timer 4.0:
        action SetVariable("escape_final_minigame_pull_strength", 800)
    timer 5.0:
        action SetVariable("escape_final_minigame_pull_strength", 1600)
    timer 6.0:
        action SetVariable("escape_final_minigame_pull_strength", 3200)
    timer 7.0:
        action SetVariable("escape_final_minigame_pull_strength", 999999)
    timer 10.0:
        action Jump("escape_unwinnable_end")

screen escape_force_to_middle:
    timer 0.05:
        repeat True
        action Function(escape_drag_mouse)

screen escape_comply_1:
    vbox:
        xalign 0.5
        yalign 0.5
        textbutton "Comply.":
            xalign 0.5
            yalign 0.5
            style "choice_button"
            action Return()
            unhovered MouseMove(config.screen_width / 2, config.screen_height / 2)

screen escape_comply_2:
    style_prefix "choice"
    vbox:
        xalign 0.5
        yalign 0.5

        textbutton "":
            xalign 0.5
            style "choice_button"
            background None
            sensitive False
        
        textbutton "Comply.":
            xalign 0.5
            style "choice_button"
            action NullAction()
            unhovered MouseMove(config.screen_width / 2, config.screen_height / 2)
        
        textbutton "Grab the gun.":
            xalign 0.5
            style "choice_button"
            action Jump("escape_good_end")
    

label escape_lose_life_animations(lab):
    if escape_end_lives == 2:
        show haze white zorder 50 onlayer top:
            matrixcolor ColorizeMatrix("#000000", "#095a10")
            alpha 0.4
    elif escape_end_lives == 1:
        show haze white zorder 50 onlayer top:
            matrixcolor ColorizeMatrix("#000000", "#095a10")
            alpha 1.0
        
    show white_screen zorder 50 onlayer top:
        matrixcolor ColorizeMatrix("#000000", "#095a10")
        alpha 0.0
        linear 0.1 alpha 0.6
        linear 0.3 alpha 0.0
    
    $ shake_screen(layers="all")
    
    if escape_end_lives <= 0:
        $ print("you died")
        $ renpy.jump("escape_bad_end")
    else:
        $ print("jumping")
        $ renpy.jump(lab)

    return

label day_event_escape:
    call escape_initialize
    scene bg ryz office
    ryz "...which is exactly why we can't just {i}shoot{/i} it. We'll probably need nukes, at the very least."
    n "You come to after zoning out and find yourself in Dr. Ryz's office."
    player "Ohhhh, I think I understand now."
    n "You completely forgot what you were talking about."
    ryz "Yeah, it's probably not a big deal. Won't be the first time, anyway."
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
    n "You look at the door to the room and see a tablet attached to it. Taped beside it is a torn scrap of paper. It reads:"
    n "{color=#095a10}\"And all you have to do is find my anomaly's name, V.A.C. number and what I look like!\"{/color}"
    n "\"Good luck!\""
    n "The name is blacked out."
    ryz "I feel like I recognize this anomaly..."
    aikha "Oh, this is fun! Newbie, take a look around the room. Try to piece together the puzzle and get us out of here!"
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
                jump escape_search_minigame_1
                # jump escape_passcode

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
        n "You look at the blue sticky note."
        show escape_blue_sticky:
            xalign 0.5
            yalign 0.5
        n "..."
        n "It's a garbled mess of random letters."
        n "Notably, on the top left of the sticky note is a cane symbol."
        if "Peculiar Paper" in escape_inventory:
            n "Wait. A cane symbol?"
            hide escape_blue_sticky
            $ escape_left_wall_blue_sticky_completed = True
            show screen escape_blue_sticky_screen
            n "You take the peculiar piece of paper that you found in the drawer out, and, sure enough, the cane symbols are exactly the same."
            
            $ escape_left_wall_blue_sticky_completed = False
            show screen qte(time = 60, act = Jump(escape_left_wall_blue_sticky_timeout), hidden=True)
            n "Uncover the code. You know how to. Probably."
            while True:
                n "Uncover the code. You know how to. Probably.{fast}"

            label escape_left_wall_blue_sticky_timeout:
                n "Okay, well, nevermind. Seems you don't know what to do."
                hide screen escape_blue_sticky_screen
                show screen escape_blue_sticky_screen_answer
                n "Here. You put the cane symbol here onto the cane symbol here, and voila!"
                jump escape_left_wall_blue_sticky_end

            # minigame
            label escape_left_wall_blue_sticky_end:
                hide screen qte
                $ escape_left_wall_blue_sticky_completed = True
                n "When you aligned the symbols together, the holes in the paper revealed a message."
                n "\"It introduced itself as{w=0.5}{nw}"

                hide screen escape_blue_sticky_screen
                hide screen escape_blue_sticky_screen_answer

                show black_screen zorder 50
                # stop music
                $ shake_screen()
                trickster "{sc=3}{color=#095a10}The TRICKSTER!!!{/color}{/sc}"
                
                trickster "{sc=3}{color=#095a10}Oh, yes! Yes! YES!{/color}{/sc}"
                menu:
                    trickster "{sc=3}{color=#095a10}Welcome, [player_name]! How has your time here been?{/color}{/sc}"
                    "Splendid.":
                        trickster "{sc=3}{color=#095a10}Delightful! Just delightful! I'm SO glad to hear that!{/color}{/sc}"
                    "Splendid.":
                        trickster "{sc=3}{color=#095a10}Delightful! Just delightful! I'm SO glad to hear that!{/color}{/sc}"
                    "Splendid." (on_hover = "Terrible."):
                        trickster "Oh dear oh dear, I'm so very sorry to hear that!"
                    "Splendid.":
                        trickster "{sc=3}{color=#095a10}Delightful! Just delightful! I'm SO glad to hear that!{/color}{/sc}"

                trickster "{sc=3}{color=#095a10}Now then, [player_name], my little intern, shall we play a game?{/color}{/sc}"
                trickster "{sc=3}{color=#095a10}All you have to do is TURN AROUND and FACE ME, eh?{/color}{/sc}"
                n "You have a very bad feeling about this...!"

                show screen qte(act=Jump("escape_trickster_game_1_fail"), time=8)
                menu:
                    trickster "{sc=3}{color=#095a10}Turn around!{/color}{/sc}"
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
                    show screen qte(act=Jump("escape_trickster_game_1_fail"), time=7)
                    menu:
                        trickster "{sc=3}{color=#095a10}C'mon, turn around!{/color}{/sc}"
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
                    show screen qte(act=Jump("escape_trickster_game_1_fail"), time=6)
                    menu:
                        trickster "{sc=3}{b}{color=#095a10}Face me! Face the lights! Face the music!{/color}{/b}{/sc}"
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
                    hide black_screen
                    show escape_it zorder 50
                    n "You feel your body turn around, against your will."
                    n "You look upwards, {color=#095a10}against your will.{/color}"
                    n "{color=#095a10}You reach your arm out, {/color}{sc=3}{color=#095a10}against your will.{/color}{/sc}"
                    n "{cps=*0.35}{sc=3}{color=#095a10}You are but a puppet.{/color}{/sc}{/cps}"
                    trickster "{sc=3}{color=#095a10}Oh, yes! Yes! YES! Delightful! Just delightful!{/color}{/sc}"
                    trickster "{sc=3}{color=#095a10}[player_name], my little intern, have you not yet realized?{/color}{/sc}{/cps}"
                    trickster "{cps=*0.35}{color=#095a10}You are not the one in control here.{/color}{/cps}{w=0.5}{nw}"
                    jump escape_tricker_game_1_end

                label escape_trickster_game_1_end:
                    hide black_screen
                    hide escape_it
                    n "Suddenly, the lights turn back on."
                    n "Your heart is pounding. Your palms are sweaty."
                    n "But it looks like the anomaly behind you is gone."
                    n "Heart still racing, you decide it's best to escape as fast as possible."
                    n "You decide to take the blue sticky note for safekeeping."
                    n "Blue Sticky has been added to your inventory."
                    $ escape_inventory.append("Blue Sticky")
                    $ escape_blue_sticky_read = True
        
        jump escape_left_wall
    
    label escape_left_wall_orange:
        n "You read the orange sticky note. All it says is:"
        n "\"810: ? x ??? - ??\""
        n "You have no clue what this means. Or do you?"
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
            n "...Maybe the rest isn't that important."
            $ escape_back_wall_notebook_viewed = True

        python:
            escape_flip_to_page = renpy.input("What page do you go to? (1-999, \"back\" to go back.)", default=1)
            if escape_flip_to_page.lower() == "back":
                renpy.jump("escape_back_wall")
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
            n "\"For instance, VAC 505-102, nicknamed 'Smiling Marshmallow' has a danger level of 5, a spawn rate of 5, a globalization value of 10 and an authorization level of 2.\""
            n "\"Of course, none of this information is actually important to solving this escape room.\""
            n "\"Escape room? What escape room?\""
            n "The explanation ends with various doodles of Pochi eating marshmallows."
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
                            $ escape_aikha_solved_morse = True
                    
                    n "\"Page 524\"... You have a feeling you know what this means."

            if not escape_back_wall_notebook_ciphers_viewed:
                n "\"\"The Vigenere cipher, on the other hand...\""
                n "You can almost feel the condescending voice emanating from the words on the page and decide to stop before you develop a savior complex."
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
            if "Page 810 (Puzzles)" in escape_inventory:
                $ NullAction()
                # show cg
            else:
                n "Oh, there's some stuff on this page."
                # show cg
                # 1, 3, 6, 10, 15, ?, 28, 35... (21)
                # ARTISAN + GLOBE = BEAR , ELEGANT + STRIFE = FEEL, NEANDERTHAL + ALUMNI = ?? (9)
                # T T T T T T T (30)
                #     ^ what is this???
                #  11, 9, 30 TODO: UPDATE ANSWERS TO 621
                n "There's a lot going on here. Wonder what any of this means."
                n "You tear the page out for safekeeping."
                $ escape_inventory.append("Page 810 (Puzzles)")
        elif escape_flip_to_page == 887:
            n "There's nothing here."
            if escape_back_wall_notebook_gullible_marked:
                n "...aside from a massive \"L\" written in the middle of the page."
                $ escape_back_wall_notebook_gullible_viewed = True
        else:
            if escape_back_wall_notebook_invalid_viewed_times == 0:
                n "It's impressive how the author managed to use so many words to make so little sense."

            elif escape_back_wall_notebook_invalid_viewed_times == 1:
                n "The handwriting is atrocious. You can't read any of this."

            elif escape_back_wall_notebook_invalid_viewed_times == 2:
                n "...That letter's probably an F. No, wait, why does it have a line sticking out from the top? Is this even English?"

            elif escape_back_wall_notebook_invalid_viewed_times == 3:
                n "The entire page is illegible...aside from a small, green {color=#095a10}:D{/color} in the corner."

            elif escape_back_wall_notebook_invalid_viewed_times == 4:
                n "Oh, hey. You see a small note on the corner of the page:"
                n "\"Did you know it says 'gullible' on page 887?\""
                $ escape_back_wall_notebook_gullible_marked = True

            elif escape_back_wall_notebook_invalid_viewed_times == 5:
                n "In the margins, there's a small bit of text."
                n "\"Hahaha, haha, haha haha{i}ha{/i}ha.\""
                n "\"Haha-\" wait, no, sorry. That should be \"Hehe.\""
                n "\"Hehe, heheheha.\""
                n "Oh, it says more at the very bottom of the page:"
                n "{size=-10}\"Ha.\"{/size}"
                
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
            show escape_peculiar_paper:
                xalign 0.5
                yalign 0.5
            n "Notably, on the top left of the paper is the cut-out symbol of a cane."
            n "This feels important. You take the piece of paper for safekeeping."
            hide escape_peculiar_paper
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
    $ appear_if_absent("aikha", x_align = 0.25)
    $ appear_if_absent("ryz", x_align = 0.5)
    $ appear_if_absent("firewal", x_align = 0.75)
    $ escape_talked = False
    menu:
        n "Who do you talk to?"
        "Dr. Aikha.":
            jump escape_talk_aikha
        "Dr. Ryz.":
            jump escape_talk_ryz
        "Dr. Firewal.":
            jump escape_talk_firewal
        "Go back.":
            jump escape_main_menu

    label escape_talk_aikha:
        $ disappear_if_present("ryz")
        $ disappear_if_present("firewal")
        $ escape_inventory_talking_to = "aikha"
        $ escape_talk_message = "Need something else?" if escape_talked else "Hi [player_name]!"
        $ escape_talked = True
        show aikha:
            linear 1.0 xalign 0.5

        menu:
            aikha "[escape_talk_message]"
            "Ask about an item.":
                call screen escape_inventory_screen
                if escape_talk_shown_item == "Blue Sticky" or ("Blue Sticky" in escape_inventory and escape_talk_shown_item == "Peculiar Paper"):
                    if not escape_talk_items["aikha"]["Blue Sticky"]:
                        $ escape_talk_items["aikha"]["Blue Sticky"] = True
                        aikha "Ah! You solved the puzzle! Excellent!"
                        aikha "What did it say?"
                        player "\"It introduced itself as 'The Trickster.'\""
                        player "Do you have any idea what that means?"
                        aikha pensive "Hmm... "
                        aikha neutral "Nah. No clue."
                        aikha "But that's one piece of the door code, right? You're one step closer!"
                    else:
                        aikha "You got this, intern!"

                elif escape_talk_shown_item == "Peculiar Paper":
                    if not escape_talk_items["aikha"]["Peculiar Paper"]:
                        $ escape_talk_items["aikha"]["Peculiar Paper"] = True
                        player "Dr. Aikha, could you take a look at this?"
                        show escape_peculiar_paper:
                            xalign 0.5
                            yalign 0.5
                        aikha pensive "Hmm..."
                        hide escape_peculiar_paper
                    aikha "Not sure. Maybe keep looking around?"

                elif escape_talk_shown_item == "Page 524" or escape_talk_shown_item == "Page 621":
                    n "Dr. Aikha probably wouldn't be interested in this."

                elif escape_talk_shown_item == "Page 810":
                    if "Page 621" in escape_inventory:
                        n "You already solved this. No point in discussing it further."
                    elif not escape_talk_items["aikha"]["Page 621"]:
                        $ escape_talk_items["aikha"]["Page 621"] = True
                        player "Dr. Aikha, could you take a look at this?"
                        # show cg
                        aikha pensive "Hmm..."
                        aikha "The second one looks an awful lot like"
                        # TODO: FINISH 

                elif escape_talk_shown_item == "Purple Light":
                    if not escape_talk_items["aikha"]["Purple Light"]:
                        $ escape_talk_items["aikha"]["Purple Light"] = True
                        player "Dr. Aikha, what do you think of this flashlight?"
                        aikha "Oh?"
                        n "You give the purple flashlight to Dr. Aikha, who turns it around in their hands."
                        aikha pensive "\"Find my complement...\""
                        aikha neutral "Hmm... maybe it has something to do with the colour?"
                    else:
                        aikha "It probably has something to do with the colour!"

                elif escape_talk_shown_item == "Slip of Paper":
                    if "Page 524" in escape_inventory:
                        if not escape_talk_items["aikha"]["Slip of Paper"]:
                            n "You already solved this. There's no point discussing it further."
                        elif escape_aikha_solved_morse:
                            aikha "Oh? Did you come to thank me?"
                            aikha happy "You're welcome!"
                            show aikha neutral
                        else:
                            aikha happy "Hey, you solved it! Nice job!"
                    else:
                        if not escape_talk_items["aikha"]["Slip of Paper"]:
                            $ escape_talk_items["aikha"]["Slip of Paper"] = True
                            player "Dr. Aikha, do you know what this is?"
                            n "You hand over the slip of paper with dots and dashes on it."
                            aikha "Oh yeah. It's morse."
                            player "What does it say?"
                            aikha "Haha, that's for you to figure out!"
                            player "..."
                        aikha "I reckon there's a cipher somewhere around here. Just keep looking."
                else:
                    n "aikha talk shown item broke bruh wtf"
            "Chat.":
                if escape_talk_chats_aikha == 0:
                    aikha "Hey! How's it going, newbie?"
                    player "Not bad, I suppose. Figuring things out slowly."
                    aikha happy "That's good! Come to me if you need any help, yeah?"
                elif escape_talk_chats_aikha == 1:
                    aikha "Hey, newbie."
                    player "Yeah?"
                    menu:
                        aikha "Waffles or pancakes?"
                        "Waffles.":
                            player "Waffles."
                        "Pancakes.":
                            player "Pancakes!"
                    player "What about you?"
                    aikha "Eh. I'm indifferent."
                    player "..."
                    aikha "Fuck whipped cream though. Hate that."
                    player "Is this relevant to the escape room?"
                    aikha "Nope!"
                elif escape_talk_chats_aikha == 2:
                    aikha "You know, I had a really weird dream last night."
                    player "Uh huh."
                    aikha "In it, I was some chess grandmaster playing Magnus Carlsen."
                    aikha panic "I was completely winning, but just before I delivered checkmate, he grabbed a shotgun from under the table and blasted my head clean off."
                    aikha "What a sore loser, right?"
                elif escape_talk_chats_aikha == 3:
                    aikha "Remember to stay hydrated!"
                    aikha "Also, remember to check your posture. Can't be getting osteoporosis, can we now?"
                elif escape_talk_chats_aikha == 4:
                    aikha "There's this one light novel that I enjoy, but I can't out myself by telling you."
                    aikha happy "So I'm gonna keep it a secret! Hehe."
                elif escape_talk_chats_aikha == 5:
                    aikha "Wow. Are things really going so well that you can sit around and talk to me all day?"
                    aikha "I mean, I'm all for it, but, shouldn't you be doing something else?"
                else:
                    aikha "Don't you have anything better to do?"
                show aikha neutral
                $ escape_talk_chats_aikha += 1
            "Go back.":
                jump escape_talk
        jump escape_talk_aikha

    label escape_talk_ryz:
        $ disappear_if_present("aikha")
        $ disappear_if_present("firewal")
        $ escape_inventory_talking_to = "ryz"
        $ escape_talk_message = "Still need something?" if escape_talked else "Hmm?"
        $ escape_talked = True

        show ryz:
            linear 1.0 xalign 0.5
        
        menu:
            ryz "[escape_talk_message]"
            "Ask about an item.":
                if escape_talk_shown_item == "Blue Sticky" or ("Blue Sticky" in escape_inventory and escape_talk_shown_item == "Peculiar Paper"):
                    if not escape_talk_items["ryz"]["Blue Sticky"]:
                        $ escape_talk_items["ryz"]["Blue Sticky"] = True
                        ryz "yap yap"
                    else:
                        ryz "yap yap"

                elif escape_talk_shown_item == "Peculiar Paper":
                    if not escape_talk_items["ryz"]["Peculiar Paper"]:
                        $ escape_talk_items["ryz"]["Peculiar Paper"] = True
                        ryz "yap yap"
                    else:
                        ryz "yap yap"


                elif escape_talk_shown_item == "Page 524" or escape_talk_shown_item == "Page 621":
                    n "Dr. ryz probably wouldn't be interested in this."

                elif escape_talk_shown_item == "Page 810":
                    if "Page 621" in escape_inventory:
                        ryz "yap yap"
                        
                    elif not escape_talk_items["ryz"]["Page 621"]:
                        $ escape_talk_items["ryz"]["Page 621"] = True
                        ryz "yap yap"
                        
                        # TODO: FINISH 

                elif escape_talk_shown_item == "Purple Light":
                    if not escape_talk_items["ryz"]["Purple Light"]:
                        $ escape_talk_items["ryz"]["Purple Light"] = True
                        ryz "yap yap"
                        
                    else:
                        ryz "yap yap"

                elif escape_talk_shown_item == "Slip of Paper":
                    if "Page 524" in escape_inventory:
                        if not escape_talk_items["ryz"]["Slip of Paper"]:
                            ryz "yap yap"
                        else:
                            ryz "yap yap"
                    else:
                        if not escape_talk_items["ryz"]["Slip of Paper"]:
                            $ escape_talk_items["ryz"]["Slip of Paper"] = True
                            ryz "yap yap"
                else:
                    n "ryz talk shown item broke bruh wtf"
            "Chat.":
                if escape_talk_chats_ryz == 0:
                    ryz "Hey. How's it going?"
                    player "Pretty alright. You?"
                    ryz "Not bad. Are the puzzles hard?"
                    player "They're fine. Probably. Wanna help?"
                    ryz happy "Hmm. Nah."
                    ryz "I'll be here if you need me, though. Just hit me up."
                elif escape_talk_chats_ryz == 1:
                    player "Nice day out, isn't it?"
                    ryz "I wouldn't know. I don't go outside."
                    player "..."
                    ryz pensive "I think it's been...let's see..."
                    ryz "3? No, 4 days since I went out."
                    player "..."
                    ryz neutral "What?"
                elif escape_talk_chats_ryz == 2:
                    player "Say, Dr. Ryz, can't you just like...phase through the wall and free us?"
                    ryz "Hm? Well, I guess, but I spent {i}way{/i} too long coding this."
                    player "What?"
                    ryz "What?"
                elif escape_talk_chats_ryz == 3:
                    # TODO: change this if lore demands it
                    ryz pensive "..."
                    player "What are you thinking of?"
                    ryz "All of these puzzles are really off-putting."
                    ryz "First the passcode on that door, now this?"
                    ryz "Makes you really wonder who - or what - is behind all of this."
                elif escape_talk_chats_ryz == 4:
                    ryz "Are you just overly talkative today, or do you really not want to do the escape room?"
                    ryz "If you {i}really{/i} want to give up, you can just get the passcode wrong 5 times, you know?"
                else:
                    ryz "Go do something else, please."
                show ryz neutral
                $ escape_talk_chats_ryz += 1
            "Go back.":
                jump escape_talk
        jump escape_talk_ryz

    label escape_talk_firewal:
        $ escape_inventory_talking_to = "firewal"
        $ disappear_if_present("ryz")
        $ disappear_if_present("aikha")
        $ escape_talk_message = "Anything else?" if escape_talked else "What's up?"
        $ escape_talked = True

        show firewal:
            linear 1.0 xalign 0.5

        menu:
            firewal "[escape_talk_message]"
            "Ask about an item.":
                if escape_talk_shown_item == "Blue Sticky" or ("Blue Sticky" in escape_inventory and escape_talk_shown_item == "Peculiar Paper"):
                    if not escape_talk_items["firewal"]["Blue Sticky"]:
                        $ escape_talk_items["firewal"]["Blue Sticky"] = True
                        firewal "yap yap"
                    else:
                        firewal "yap yap"
                        

                elif escape_talk_shown_item == "Peculiar Paper":
                    if not escape_talk_items["firewal"]["Peculiar Paper"]:
                        $ escape_talk_items["firewal"]["Peculiar Paper"] = True
                        firewal "yap yap"
                    else:
                        firewal "yap yap"


                elif escape_talk_shown_item == "Page 524" or escape_talk_shown_item == "Page 621":
                    n "Dr. firewal probably wouldn't be interested in this."

                elif escape_talk_shown_item == "Page 810":
                    if "Page 621" in escape_inventory:
                        firewal "yap yap"
                        
                    elif not escape_talk_items["firewal"]["Page 621"]:
                        $ escape_talk_items["firewal"]["Page 621"] = True
                        firewal "yap yap"
                        # TODO: FINISH 

                elif escape_talk_shown_item == "Purple Light":
                    if not escape_talk_items["firewal"]["Purple Light"]:
                        $ escape_talk_items["firewal"]["Purple Light"] = True
                        firewal "yap yap"
                    else:
                        firewal "yap yap"

                elif escape_talk_shown_item == "Slip of Paper":
                    if "Page 524" in escape_inventory:
                        if not escape_talk_items["firewal"]["Slip of Paper"]:
                            firewal "yap yap"
                        else:
                            firewal "yap yap"
                    else:
                        if not escape_talk_items["firewal"]["Slip of Paper"]:
                            $ escape_talk_items["firewal"]["Slip of Paper"] = True
                else:
                    n "firewal talk shown item broke bruh wtf"
            "Chat.":
                if escape_talk_chats_firewal == 0:
                    player "Hey, Dr. Firewal. Rare to see you outside of your office."
                    firewal "Yeah, true. How's the escape room?"
                    player "It's going, it's going."
                    firewal "That's good. Let me know if you need help with anything."
                elif escape_talk_chats_firewal == 1:
                    
                elif escape_talk_chats_firewal == 2:
                    
                elif escape_talk_chats_firewal == 3:
                    
                elif escape_talk_chats_firewal == 4:
                    
                else:
                    
                show firewal neutral
                $ escape_talk_chats_firewal += 1
            "Go back.":
                jump escape_talk
        
        jump escape_talk_firewal


# ------------------------------ INVENTORY ------------------------------

label escape_inventory_menu:
    if not escape_inventory:
        n "Your inventory is empty."
    else:
        $ escape_inventory_page = 0
        $ escape_inventory_screen_is_talking = False
        call screen escape_inventory_screen
    jump escape_main_menu

label escape_item_blue_sticky:
    n "{color=#095a10}The Trickster.{/color}"
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
            trickster "{sc=3}{color=#095a10}Oh dear oh dear! [player_name], my little intern, how could you fail this?{/color}{/sc}"
            trickster "{sc=3}{color=#095a10}A shame. Truly a shame!{/color}{/sc}"
            trickster "{sc=3}{color=#095a10}Well now. Your actions have consequences, you know!{/color}{/sc}"
            trickster "{cps=*0.35}{color=#095a10}You are no longer of use.{/color}{/cps}"

            n "You notice"
            n "a presence"
            n "right"
            n "in front"
            n "of yo{nw}"
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
        # add firewal and aikha transform into shadows, ryz is the only real one
        # ryz tells you what to do  

        if escape_back_wall_notebook_gullible_viewed:
            trickster "You even fell for that \"gullible\" joke!"
            trickster "Come on, what year is it? You can't be falling for that anymore!"

        $ renpy.notify("Fullscreen is recommended for this segment of the game.")

label escape_search_minigame_1:
    show screen qte(time=6, act=Function(escape_lose_life, "escape_search_minigame_2"))
    menu:
        trickster "{sc=3}{color=#095a10}Just turn around!{/color}{sc=3}"
        "Don't turn around.":
            jump escape_search_minigame_2
        "Don't turn around." (on_hover = "Turn around"):
            $ escape_lose_life("escape_search_minigame_2")
        "Don't turn around." (on_hover = "Turn around"):
            $ escape_lose_life("escape_search_minigame_2")
        "Don't turn around." (on_hover = "Turn around"):
            $ escape_lose_life("escape_search_minigame_2")
    
label escape_search_minigame_2:
    hide screen qte
    show screen qte(time=5, act=Function(escape_lose_life, "escape_search_minigame_3"))

    menu:
        trickster "{sc=3}{color=#095a10}You'll be so much happier!{/color}{sc=3}"
        "Don't turn around." (on_hover = "Turn around"):
            $ escape_lose_life("escape_search_minigame_3")
        "Don't turn around." (on_hover = "Turn around"):
            $ escape_lose_life("escape_search_minigame_3")
        "Don't turn around." (on_hover = "Turn around"):
            $ escape_lose_life("escape_search_minigame_3")
        "Don't turn around.":
            jump escape_search_minigame_3        

label escape_search_minigame_3:
    hide screen qte
    show screen qte(time=4, act=Function(escape_lose_life, "escape_moving_minigame_1"))

    menu:
        trickster "{sc=3}{color=#095a10}All you need to do is...!{/color}{sc=3}"
        "Turn around.":
            $ escape_lose_life("escape_moving_minigame_1")
        "Turn around.":
            $ escape_lose_life("escape_moving_minigame_1")
        "Turn around." (on_hover = "Don't turn around."):
            jump escape_moving_minigame_1
        "Turn around.":
            $ escape_lose_life("escape_moving_minigame_1")

label escape_moving_minigame_1:
    hide screen qte
    show screen qte(time=escape_moving_minigame_delays[escape_moving_minigame_phase], act=Jump("escape_moving_minigame_2"), hidden=True)
    menu:
        n "{sc=3}{color=#095a10}[escape_moving_minigame_dialogue[escape_moving_minigame_phase]]{/color}{sc=3}{fast}"
        "Don't turn around.":
            jump escape_moving_minigame_end
        "Turn around.":
            $ escape_lose_life("escape_moving_minigame_end")
        "Turn around.":
            $ escape_lose_life("escape_moving_minigame_end")
        "Turn around.":
            $ escape_lose_life("escape_moving_minigame_end")

label escape_moving_minigame_2:
    show screen qte(time=escape_moving_minigame_delays[escape_moving_minigame_phase], act=Jump("escape_moving_minigame_3"), hidden=True)
    menu:
        n "{sc=3}{color=#095a10}[escape_moving_minigame_dialogue[escape_moving_minigame_phase]]{/color}{sc=3}{fast}"
        "Turn around.":
            $ escape_lose_life("escape_moving_minigame_end")
        "Don't turn around.":
            jump escape_moving_minigame_end
        "Turn around.":
            $ escape_lose_life("escape_moving_minigame_end")
        "Turn around.":
            $ escape_lose_life("escape_moving_minigame_end")

label escape_moving_minigame_3:
    show screen qte(time=escape_moving_minigame_delays[escape_moving_minigame_phase], act=Jump("escape_moving_minigame_4"), hidden=True)
    menu:
        n "{sc=3}{color=#095a10}[escape_moving_minigame_dialogue[escape_moving_minigame_phase]]{/color}{sc=3}{fast}"
        "Turn around.":
            $ escape_lose_life("escape_moving_minigame_end")
        "Turn around.":
            $ escape_lose_life("escape_moving_minigame_end")
        "Don't turn around.":
            jump escape_moving_minigame_end
        "Turn around.":
            $ escape_lose_life("escape_moving_minigame_end")

label escape_moving_minigame_4:
    show screen qte(time=escape_moving_minigame_delays[escape_moving_minigame_phase], act=Jump("escape_moving_minigame_1"), hidden=True)
    menu:
        n "{sc=3}{color=#095a10}[escape_moving_minigame_dialogue[escape_moving_minigame_phase]]{/color}{sc=3}{fast}"
        "Turn around.":
            $ escape_lose_life("escape_moving_minigame_end")
        "Turn around.":
            $ escape_lose_life("escape_moving_minigame_end")
        "Turn around.":
            $ escape_lose_life("escape_moving_minigame_end")
        "Don't turn around.":
            jump escape_moving_minigame_end

label escape_moving_minigame_end:
    $ escape_moving_minigame_phase += 1
    if escape_moving_minigame_phase >= escape_moving_minigame_max_phase:
        hide screen qte
        $ renpy.run(MouseMove(100, 100, 0))
        show screen qte(time = 10.0, act=Jump("escape_final_minigame_success"))
        show screen escape_final_minigame
        n "{sc=3}{color=#095a10}[player_name], my little intern! Come on!{/color}{sc=3}"
        while True:
            n "{sc=3}{color=#095a10}[player_name], my little intern! Come on!{/color}{sc=3}{fast}"
    else:
        jump escape_moving_minigame_1
    
label escape_final_minigame_success:
    hide screen qte
    hide screen escape_final_minigame
    trickster "{sc=3}{color=#095a10}Fine. Fine! FINE!{/color}{/sc}"
    trickster "{sc=3}{color=#095a10}You wanna play like that? You wanna see where your insubordination gets you?{/color}{/sc}"
    show screen escape_unwinnable
    show white_screen zorder 50 onlayer top:
        matrixcolor ColorizeMatrix("#000000", "#095a10")
        alpha 0.0
        linear 0.1 alpha 0.6
        linear 0.3 alpha 0.0
    
    show haze white strong zorder 50 onlayer top:
        matrixcolor ColorizeMatrix("#000000", "#095a10")
        alpha 1.0
        block:
            ease 0.3 alpha 0.7
            ease 0.3 alpha 1.0
    
    $ shake_screen(layers="all")
    trickster "{sc=3}{color=#095a10}TURN. AROUND.{/color}{/sc}"
    while True:
        trickster "{sc=3}{color=#095a10}TURN. AROUND.{/color}{/sc}{fast}"
        # TODO: add jumpscare if they alt tab out

label escape_unwinnable_end:
    show layer master
    show layer screens
    show layer top
    hide screen escape_unwinnable
    show screen escape_force_to_middle
    n "Despite every fibre of your being protesting otherwise..."
    n "You slowly turn around."
    trickster "{sc=3}{color=#095a10}Haha, YES, YES, YES!{/color}{/sc}"
    trickster "{sc=3}{color=#095a10}Delightful! Just delightful!{/color}{/sc}"
    trickster "{sc=3}{color=#095a10}See, my little intern? See, [player_name]? Isn't it just so much easier?{/color}{/sc}"
    n "Your eyes are immovably attached to the green figure in the darkness."

    hide screen escape_force_to_middle
    show screen escape_comply_1
    $ renpy.run(MouseMove(960, 540, 0))
    trickster "{sc=3}{color=#095a10}Life is so much easier if you just comply, comply, comply!{/color}{/sc}"
    trickster "{sc=3}{color=#095a10}See? No fuss at all!{/color}{/sc}"
    n "You slowly nod, against your will."
    n "Your body disobeys every command you try to give it."
    n "You "
    n "are not"
    n "{color=#095a10}the one{/color}"
    n "{sc=3}{color=#095a10}in control here.{/color}{/sc}"
    n "...?"
    n "But..."
    n "Through the faint glow in the darkness, you can just barely see a gun lying on the table  your right."
    n "That's your last hope."
    hide screen escape_comply_1
    show screen escape_comply_2
    n "Break free.{w=1.5}{nw}"
    trickster "{sc=3}{color=#095a10}[player_name]! [player_name], [player_name], [player_name].{w=3.0}{nw}{/color}{/sc}"
    trickster "{sc=3}{color=#095a10}Oh, I'm so excited! I didn't plan this far ahead!{w=3.0}{nw}{/color}{/sc}"
    trickster "{sc=3}{color=#095a10}You'll be happy, [player_name]. You'll be so happy.{w=3.0}{nw}{/color}{/sc}"

    show aikha at appear(x_align = 0.3, final_brightness = -1.0)
    show firewal at appear(x_align = 0.7, final_brightness = -1.0)
    trickster "{sc=3}{color=#095a10}Nevermind these \"department heads!\"{w=3.0}{nw}{/color}{/sc}"
    trickster "{sc=3}{color=#095a10}They talk so much, but have they ever {i}actually{/i} done anything for you?{w=3.0}{nw}{/color}{/sc}"
    trickster "{sc=3}{color=#095a10}wait where'd the third guy go{w=3.0}{nw}{/color}{/sc}"
    trickster "{sc=3}{color=#095a10}My little intern, with me, you can do so much more! {i}Be{/i} so much more!{w=3.0}{nw}{/color}{/sc}"
    trickster "{sc=3}{color=#095a10}Oh! By the way! How did you like the escape room?{w=3.0}{nw}{/color}{/sc}"
    trickster "{sc=3}{color=#095a10}Haha, I spent so long on it. I would literally break down and cry if you told me you hated it.{w=3.0}{nw}{/color}{/sc}"
    trickster "{sc=3}{color=#095a10}You loved it?{w=2.0}{nw}{/color}{/sc}"
    trickster "{sc=3}{color=#095a10}Delightful! Just delightful! I'm so glad to hear that!{w=3.0}{nw}{/color}{/sc}"
    trickster "{sc=3}{color=#095a10}I'll make another one, just for you, eh? Eh?{w=3.0}{nw}{/color}{/sc}"
    trickster "{sc=3}{color=#095a10}You'd love that? But of course!{w=3.0}{nw}{/color}{/sc}"
    trickster "{sc=3}{color=#095a10}Anything for you! Anything for you.{w=3.0}{nw}{/color}{/sc}"
    

    trickster "{sc=3}{color=#095a10}Don't worry, [player_name]. You're with me.{w=3.0}{nw}{/color}{/sc}"
    while True:
        trickster "{sc=3}{color=#095a10}Don't worry, [player_name]. You're with me.{w=3.0}{nw}{/color}{/sc}{fast}"    

label escape_good_end:
    hide screen escape_comply_2
    n "YIPPEE"

label escape_bad_end:
    hide screen qte
    hide screen escape_final_minigame
    hide haze
    hide white_screen

    $ shake_screen(layers="all")

    show white_screen zorder 50 onlayer top:
        matrixcolor ColorizeMatrix("#000000", "#095a10")
        alpha 0.0
        linear 0.1 alpha 0.8
        linear 0.5 alpha 0.05
    show haze white strong zorder 50 onlayer top:
        matrixcolor ColorizeMatrix("#000000", "#095a10")
        alpha 1.0
        block:
            ease 0.3 alpha 0.7
            ease 0.3 alpha 1.0
    show white_screen
    n "You succumb. Your body turns around "
    trickster "{sc=3}{color=#095a10}Oh, yes! Yes! YES!{/color}{/sc}"
    trickster "{sc=3}{color=#095a10}Delightful! Just delightful!{/color}{/sc}"
    trickster "{sc=3}{color=#095a10}See, my little intern? See, [player_name]? Isn't it just so much easier?{/color}{/sc}"
    trickster "{sc=3}{color=#095a10}Life is so much easier if you just comply, comply, comply!{/color}{/sc}"
    n "You try {nw}"
    $ shake_screen(layers="all")
    trickster "{sc=3}{color=#095a10}Oh, shut it! You're not welcome here.{/color}{/sc}"
    trickster "{sc=3}{color=#095a10}[player_name], [player_name], [player_name]...{/color}{/sc}"
    trickster "{sc=3}{color=#095a10}This is so delightful! Just delightful! I don't know what to do! I didn't plan this far ahead!{/color}{/sc}"
    menu:
        trickster "{sc=3}{color=#095a10}Did you like my escape room? Was it fun?{/color}{/sc}"
        "YES!":
            $ NullAction()
        "YES!":
            $ NullAction()
        "YES!":
            $ NullAction()
        "YES!":
            $ NullAction()
    
    trickster "{sc=3}{color=#095a10}I'm SO glad to hear that!{/color}{/sc}"

    menu:
        trickster "{sc=3}{color=#095a10}Did you want me to make another one? Did you?{/color}{/sc}"
        "YES!":
            $ NullAction()
        "YES!":
            $ NullAction()
        "YES!":
            $ NullAction()
        "YES!":
            $ NullAction()
    trickster "{sc=3}{color=#095a10}Of course! I'll get on that right now, just you w- {nw}{/color}{/sc}"
    $ shake_screen(layers="all")
    
    n "The sound of a gunshot causes your ears to ring."
    trickster "{sc=3}{color=#095a10}Y-You!{/color}{/sc}"
    $ shake_screen(layers="all")
    n "You hear a second gunshot."
    trickster "{sc=3}{color=#095a10}Okay, OKAY! You win, you w-{/color}{/sc}"
    $ shake_screen(layers="all")
    n "Then a third."
    trickster "{sc=3}{color=#095a10}I'LL BE TAKING MY LEAVE NOW THANK YOU VERY MUCH{/color}{/sc}"
    show haze white strong zorder 50 onlayer top:
        matrixcolor ColorizeMatrix("#000000", "#095a10")
        alpha 0.7
        linear 5 alpha 0.0
    show white_screen zorder 50 onlayer top:
        matrixcolor ColorizeMatrix("#000000", "#095a10")
        alpha 0.05
        linear 3 alpha 0.0

    show ryz at appear
    ryz fury "That was MY escape room, by the way! MINE! 1500 LINES OF CODE!"
    player "What?"
    ryz neutral "What?"
    player "...Thanks, Dr. Ryz."
    ryz "Don't mention it. You alright?"
    player "Yeah, I think."