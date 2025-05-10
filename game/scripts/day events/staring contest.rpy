image red_blur_1= Image("images/day events/red blur.png", xpos = -100, ypos = -100, xanchor = 0.0, yanchor = 0.0)
image red_blur_2 = Image("images/day events/red blur 2.png", xpos = -100, ypos = -100, xanchor = 0.0, yanchor = 0.0)

label day_event_staring_contest:
    scene bg lounge
    player "Ugh, I need a coffee."
    show aikha at appear(x_align = 0.33)
    n "You open the door to the lounge and see Dr. Aikha staring intensely at a wall."

    if characters["aikha"]["points"] > 2:
        n "You don't really pay her any mind. You're used to this kind of stuff by now."
    else:
        n "Looks like the 9-5 got to her."

    n "You make your way over to the coffee machine."
    aikha "Do it. You won't."
    lee_unknown "Not happening. You first."
    n "A talking wall. Huh."
    n "You decide it's best for your sanity to ignore it. You continue pouring your coffee."
    lee_unknown "Oh hey! Is that the intern?"
    aikha "Hm? Oh, yeah! [player_name], wanna join us?"
    player "\"Us\" being...you and the wall?"
    aikha "Not just any wall! Dr. Lee's behind this one. We're having a staring contest!"
    player "...through the wall?"
    lee "Through the wall! Come!"
    n "You make your way over to the wall and admire its...wall-like qualities."
    player "Am I supposed to be seeing them, or..."
    aikha "Shh! I'm about to win..."
    n "..."
    n "..."
    n "/no_pause.{w=0.5}.{w=0.5}.{w=0.5}"
    n "You calmly take a sip of coffee- {nw}"
    lee "YOU BLINKED! I SAW THAT!"
    aikha "NOPE! DID NOT!"
    player "...so I should go-"
    aikha "Wait, no, join us!"
    lee "Yessss! Join us!"
    player "But I can't just see through walls."
    aikha "Not a problem. I can give you some eyes to do just that!"
    player "\"Give me eyes\"...?"
    lee "I can help too! I could make your eyes like mine!"
    player "...or I could leave-"
    aikha "What will it be?"
    n "...it really doesn't seem like you have a choice in the matter."
    menu:
        n "Well?"
        "Let Dr. Aikha grow you a fresh pair of eyes":
            jump grow_more
        "Let Dr. Lee douse your eyes in radiation":
            jump irradiate
        "Ask to just be the judge":
            jump judge
    
    label grow_more:
        n "Surely having more eyes is always a good thing."
        aikha "Ready? Here goes!"
        n "Dr. Aikha stretches out her hand and conjures a pair of grotesque eyes."
        n "Before you can react, she slaps you."
        show aikha neutral:
            blur 2
        with hpunch
        pause 0.5
        n "Twice."
        show aikha neutral:
            linear 2.0 blur 4
            linear 2.0 blur 0
            repeat
        with hpunch
        pause 0.5
        aikha "How is it?"
        n "Your head is pounding. Shivers run through your body, and you resist the urge to throw up."
        show lee at appear(x_align = 0.66):
            alpha 0.5
            matrixcolor TintMatrix("#ff000088")
            block:
                linear 2.0 blur 4
                linear 2.0 blur 0
                repeat
        n "But..."
        n "You can faintly see Dr. Lee through the wall."
        lee "Heya! Can you see me?"
        player "Yeah..."
        aikha "How do you feel?"
        player "Just peachy..."
        n "You throw up onto the floor."
        aikha "Don't mind the adverse side effects. Go! Staring contest!"
        player "..."
        show aikha at move_to(x_align = 0.0)
        show lee at move_to(x_align = 0.5)
        $ battle_fiercely = False
        menu:
            n "What's your game plan?"
            "Battle valiantly for honour, with no regard for your personal wellbeing":
                $ battle_fiercely = True
                n "You stare fiercely- {nw}"
            "Pretend to put up a fight but lose so you can get these eyes out faster":
                n "You stare half-heartedly at Dr. Lee."
                n "They stare back through the wall, smiling."
                lee "I'm gonna- {nw}"

        show black_screen zorder 50
        with hpunch
        hide lee
        window hide
        pause 2.0 
        
        if battle_fiercely:
            n "..."
            n "That was pathetic."
        
        show black_screen zorder 50:
            alpha 1.0
            delay 2.0
            linear 5.0 alpha 0.0
        show aikha at center:
            blur 0.0
        aikha "Hey, wake up!"
        aikha "Wake up! [cap_first(player_name)]!"
        n "Your head is pounding, but it seems like you're back to having only two eyes."
        aikha "Oh, you're up!"
        show aikha at move_to(x_align = 0.33)
        show lee at appear(x_align = 0.66)
        lee "How are you feeling?"
        aikha "[cap_first(player_sub)]'ll be fine. [player_sub] won't suffer any lasting damage."
        aikha "Or at least  shouldn't..."
        n "You try to laugh it off but end up in a coughing fit."
        lee "Uh oh."
        
        $ update_character_points({"aikha": 2, "lee": 1})
        return

    label irradiate:
        n "Surely blasting your eyes with a lethal dose of radiation won't be detrimental to your health."
        n "Wait. Lethal?{w=0.2}{nw}"
        lee "Here goes!"
        n "..."

        show aikha:
            matrixcolor TintMatrix("#ff000000")
            linear 0.6 matrixcolor TintMatrix("#ff00000f")
        show red_blur_1 zorder 50 onlayer top:
            alpha 0.0
            linear 0.6 alpha 0.3
        
        n "It doesn't seem like anything's ha- {nw}"
        
        show aikha:
            linear 0.3 matrixcolor TintMatrix("#ff000033")
        show red_blur_1 zorder 50 onlayer top:
            linear 0.3 alpha 1.0
            block:
                linear 1.0 alpha 0.7
                linear 1.0 alpha 1.0
                repeat
        with hpunch
        
        n "A burning sensation hits your eyes."
        show lee at appear(x_align = 0.66):
            matrixcolor TintMatrix("#ff000088")
            alpha 0.0
            linear 0.5 alpha 0.5
        lee "How is it?"
        n "Through the pain, you can see Dr. Lee grinning behind the wall."
        lee "You can see me now!"
        aikha "Staring contest! Staring contest!"
        n "You don't feel great, but the sooner you finish this, the sooner you can return to normal."
        lee "Ready up!"
        menu:
            n "What's your game plan?"
            "Battle valiantly for honour, with no regard for your personal wellbeing":
                jump fight
            "Pretend to put up a fight but lose so you can get these eyes out faster":
                jump give_up
        
        label fight:
            n "You gaze intensely at Dr. Lee through the wall. They do the same back."
            n "A minute passes. You can feel your eyes straining, while Dr. Lee shows no signs of faltering."
            show red_blur_1 zorder 50 onlayer top:
                linear 0.5 alpha 0.7
                linear 0.5 alpha 1.0
                repeat
            n "Another minute passes. Your eyes start tearing up. Dr. Lee continues to stare at you, smiling all the same."
            show red_blur_2 zorder 50 onlayer top:
                alpha 0.0
                linear 1.0 alpha 0.25
            n "You don't give up. You can't. Sunk cost fallacy dictates you keep fighting."
            show red_blur_1 zorder 49 onlayer top:
                alpha 1.0
            show red_blur_2 zorder 50 onlayer top:
                alpha 0.25
                block:
                    linear 0.5 alpha 0.7
                    linear 0.5 alpha 1.0
                    repeat
            n "The both of you reach the four minute mark."
            aikha "Woah, [player_name]'s a prodigy at this!"
            n "Dr. Lee just keeps smiling, unwavering."
            n "Your eyes beg for mercy, but your hubris drowns out their cries."
            n "And finally..."
            hide red_blur_1 onlayer top
            hide red_blur_2 onlayer top
            show black_screen zorder 50:
                matrixcolor ColorizeMatrix("#ff0000",   "#000000")
                linear 2.0 matrixcolor ColorizeMatrix("#000000", "#ff0000")
            with hpunch
            n "You succumb to the pain and collapse."
            n "Oops!"
            return

    label judge:
        n "yip"
        return


