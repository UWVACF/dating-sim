image red_blur_1= Image("images/day events/red blur.png", xpos = -100, ypos = -100, xanchor = 0.0, yanchor = 0.0)
image red_blur_2 = Image("images/day events/red blur 2.png", xpos = -100, ypos = -100, xanchor = 0.0, yanchor = 0.0)
image overlay_ai_1 = Image("images/day events/overlay ai 1.png", xpos = -100, ypos = -100, xanchor = 0.0, yanchor = 0.0)
image overlay_ai_2 = Image("images/day events/overlay ai 2.png", xpos = -100, ypos = -100, xanchor = 0.0, yanchor = 0.0)

label day_event_staring_contest:
    scene bg lounge
    with default_fade
    player "Ugh, I need a coffee."
    show aikha at appear(x_align = 0.33)
    n "You open the door to the lounge and see Dr. Aikha staring intensely at a wall."

    if characters["aikha"]["points"] > 2:
        n "You don't really pay them any mind. You're used to this kind of stuff by now."
    else:
        n "Looks like the 9-5 got to them."

    n "You make your way over to the coffee machine."
    aikha "Do it. You won't."
    lee_unknown "Not happening. You first."
    n "A talking wall. Huh."
    n "You decide it's best for your sanity to ignore it. You continue pouring your coffee."
    lee_unknown "Oh hey! Is that the intern?"
    aikha "Hm? Oh, yeah! Recruit, would you like to join us?"
    player "\"Us\" being...you and the wall?"
    aikha "Not just any wall! Dr. Lee's behind this one. We're having a staring contest!"
    player "...Through the wall?"
    lee "Through the wall! Come!"
    n "You make your way over to the wall and admire its...wall-like qualities."
    player "Am I supposed to be seeing them, or..."
    aikha "Shh! I'm about to win..."
    aikha "..."
    lee "..."
    player "..."
    n "You calmly take a sip of coffee- "
    lee "YOU BLINKED! I SAW THAT!"
    aikha "NUH UH!"
    lee "YUH HUH!"
    player "...So I should go-"
    aikha "No no, join!"
    lee "Yessss! Join us!"
    player "But I can't just...see through walls."
    aikha "Not a problem. I'll just give you some eyes!"
    player "\"Give me some eyes\"...?"
    lee "I can help too! I could make your eyes like mine!"
    player "...Or I could leave-"
    aikha "So what will it be?"
    n "...It really doesn't seem like you have a choice in the matter."
    menu:
        n "Well?"
        "Let Dr. Aikha grow you a fresh pair of eyes.":
            jump grow_more
        "Let Dr. Lee douse your eyes in radiation.":
            jump irradiate
        "Ask to judge.":
            jump judge
    
    label grow_more:
        n "Surely having more eyes is always a good thing."
        aikha "Ready? Here goes!"
        n "Dr. Aikha holds out their hand and conjures a pair of grotesque eyes."
        n "Before you can react, they slaps you."
        show overlay_ai_1 onlayer top:
            alpha 0.6
            blur 2
        show layer master:
            blur 2
        with hpunch
        pause 0.5
        n "Twice."
        show overlay_ai_1 onlayer top:
            alpha 1.0
        show layer master:
            block:
                linear 2.0 blur 6
                linear 2.0 blur 0
                repeat
        with hpunch
        pause 0.5
        aikha "How is it?"
        n "Your head is pounding. Shivers run through your body, and you resist the urge to throw up."
        show overlay_ai_1 onlayer top:
            linear 0.5 alpha 0.0
        show overlay_ai_2 onlayer top:
            blur 6
            alpha 0.0
            linear 0.5 alpha 1.0
        show lee at appear(x_align = 0.66):
            alpha 0.5
            matrixcolor TintMatrix("#ff000088")
        n "But..."
        hide overlay_ai_1 onlayer top
        n "You can faintly see Dr. Lee through the wall."
        lee "Heya! Can you see me?"
        player "Yeah..."
        aikha "How you feelin'?"
        player "Just peachy..."
        n "You throw up onto the floor."
        aikha "Disregard any adverse side effects. Go! Staring contest!"
        player "..."
        $ battle_fiercely = False
        menu:
            n "What's your game plan?"
            "Battle valiantly for honour, with no regard for your personal wellbeing.":
                $ battle_fiercely = True
                n "You stare fiercely at Dr. Lee."
                n "Fueled by the insurmountable desire to win..."
            "Pretend to put up a fight but lose so you can get these eyes out faster.":
                n "You stare half-heartedly at Dr. Lee."
                n "They stare back through the wall, smiling."
                lee "I'm gonna- "

        show layer master:
            blur 0.0
        hide overlay_ai_2 onlayer top
        show black_screen zorder 50
        with hpunch
        show aikha neutral at center
        hide lee
        window hide
        pause 2.0 
        
        if battle_fiercely:
            n "..."
            n "You collapse."
        
        show black_screen zorder 50:
            alpha 1.0
            delay 2.0
            linear 5.0 alpha 0.0
        aikha "You awake yet?"
        aikha "Hello? [player_name]?"
        n "You wake up and find yourself sprawled on the floor. Your head is pounding, but it seems your vision is back to normal."
        aikha "Oh, you're up!"
        show aikha at move_to(x_align = 0.33)
        show lee at appear(x_align = 0.66)
        lee "How are you feeling?"
        aikha "[player_sub!c]'ll be fine. [player_sub!c] shouldn't suffer any lasting damage."
        n "You throw up over yourself."
        aikha "I said lasting."
        n "You try to play it off but end up in a coughing fit."
        lee "Uh oh."
        n "You should probably head to the infirmary."
        $ update_character_points({"aikha": 2, "lee": 1})
        return

    label irradiate:
        n "Surely blasting your eyes with a lethal dose of radiation won't be detrimental to your health."
        n "Wait. Lethal?{w=0.2}"
        lee "Here goes!"
        n "..."

        show aikha:
            matrixcolor TintMatrix("#ff000000")
            linear 0.6 matrixcolor TintMatrix("#ff00000f")
        show red_blur_1 zorder 50 onlayer top:
            alpha 0.0
            linear 0.6 alpha 0.3
        
        n "It doesn't seem like anything's ha- "
        
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
            "Battle valiantly for honour, with no regard for your personal wellbeing.":
                jump fight
            "Pretend to put up a fight but lose so you can go back to normal faster.":
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
            aikha "Wow, [player_name]. You're good!"
            n "Dr. Lee just keeps smiling, unwavering."
            n "Your eyes beg for mercy, but your hubris drowns out their cries."
            n "And finally..."
            hide red_blur_1 onlayer top
            hide red_blur_2 onlayer top
            hide aikha
            hide lee
            show black_screen zorder 50:
                matrixcolor ColorizeMatrix("#ff0000",   "#000000")
                linear 2.0 matrixcolor ColorizeMatrix("#000000", "#ff0000")
            with hpunch
            n "You succumb to the pain and collapse."
            n "Oops!"
            show black_screen zorder 50:
                alpha 1.0
                linear 2.0 alpha 0.0
            jump lee_conclusion
            
        label give_up:
            n "You gaze halfheartedly at Dr. Lee through the wall. They do the same back."
            lee "Heya!"
            n "After a minute passes, you decide it's about time to call it and blink."
            show black_screen zorder 50:
                matrixcolor ColorizeMatrix("#ff0000",   "#000000")
                linear 5.0 matrixcolor ColorizeMatrix("#000000", "#ff0000")
            hide red_blur_1 onlayer top
            n "Terrible idea."
            n "The burning feeling in your eyes spreads throughout your body, and you succumb to the pain."
            show black_screen zorder 50:
                matrixcolor ColorizeMatrix("#000000",   "#ff0000")
                alpha 1.0
                linear 2.0 alpha 0.0
            hide aikha
            hide lee

        label lee_conclusion:
            show aikha neutral:
                xalign 0.33
                yalign 1.0
            show lee neutral:
                xalign 0.66
                yalign 1.0
            lee "Hey, I think [player_sub_be] up!"
            n "You find yourself sprawled on the floor. Aside from slightly swollen eyes, you feel surprisingly normal."
            aikha "How you doing?"
            player "Better. A lot better. What did you guys do?"
            aikha "Heh."
            lee "..."
            aikha "That's classified."
            n "You decide it's not worth questioning further. At least you lived."
            lee "By the way, [player_name]!"
            player "Hm?"
            lee "I won!"
            $ update_character_points({"lee": 2, "aikha": 1})
            return

    label judge:
        player "What if I just judged?"
        aikha "Mmmmmmmmm FIIIIIIIIINE."
        aikha "'Alright with you, CT?"
        lee "Yep! Ready?"
        aikha "Mm!"
        n "Dr. Aikha goes back to gazing intensely at the wall. It only just hits you that you can't actually see Dr. Lee behind it."
        player "..."
        aikha "..."
        lee "..."
        with default_fade
        n "It's been 4 hours."
        n "Your coffee has long since gone cold."
        player "Don't you two have anything else to do?"
        n "An eye on Dr. Aikha's neck turns to stare at you."
        aikha "Nope!"
        lee "There aren't a lot of radiological entities that need to be taken care of, anyway."
        aikha "I can monitor my staff from here anyways!"
        n "The eye goes back staring at the wall."
        n "You reckon it's about time to leave, when Dr. Chan walks into the room."
        show chan fury at appear(x_align = 0.66)
        chan "What the fuck are you guys doing."
        aikha "Hi Chan!"
        lee "We're having a staring contest!"
        chan "..."
        show chan fury at disappear
        chan "My colleagues are all idiots."
        hide chan
        with default_fade
        n "Another 3 hours pass."
        n "You wonder what you're doing with your life when you hear the door open behind you."
        show alex at appear(x_align = 0.66)
        n "Founder Alex barely even glances in your direction as he fills his \"#1 BOSS\" mug with coffee."
        aikha "Hiya Mr. Founder!"
        alex happy "Hello!"
        n "He walks away nonchalantly."
        show alex happy at disappear
        n "Does he not... forget it."
        
        n "You should really be heading home. You don't get paid for overtime."
        n "Do you even get paid at all...?"
        menu:
            n "How do you break out of this stalemate?"
            "Persuade them they both blinked at the same time.":
                jump persuasion_check
            "Try to leave.":
                jump try_to_leave
        
        label persuasion_check:
            n "You pull out your trusty d20 to do a persuasion check."
            n "You roll a Nat 1. Oops."
            player "Wait, hang on. You both just blinked."
            aikha "Pardon?"
            n "Shocked by your sudden comment, you see Dr. Aikha's eyes blink. All 23 of them."
            lee "Oops. I just blinked."
            n "Somehow, by sheer dumb luck, they both just blinked simultaneously."
            aikha "Shit. Guess we tied."
            n "You're free. You're finally free- "
            lee "We can have a rematch tomorrow!"
            aikha "Sure! Same time?"
            lee "Yesss! [player_name], join us tomorrow!"
            n "NONONONONONONONONONO"
            player "Sure!"
            show black_screen onlayer top:
                alpha 0.0
                linear 1.0 alpha 1.0
                pause 2.0
                alpha 0.0
            n "{cps=24}NONONONONONONONONONONONONONONO{nw}{/cps}"
            $ update_character_points({"aikha": 2, "lee": 2})
            return
        
        label try_to_leave:
            player "So I should really get going now..."
            aikha "..."
            lee "..."
            n "They're too invested in their staring contest to notice, so you turn to leave."
            n "...Was it that easy the entire time?"
            show aikha unique
            show overlay_ai_1 onlayer top:
                alpha 0.0
                linear 0.4 alpha 1.0
            n "Dr. Aikha starts splitting open by {i}its{/i} seams, revealing an amalgamation of eyes and teeth."
            show lee at appear(x_align = 0.66):
                alpha 0.5
                matrixcolor TintMatrix("#ff000088")
            show red_blur_2 onlayer top:
                alpha 0.0
                block:
                    linear 0.4 alpha 1.0
                    linear 0.4 alpha 0.7
                    repeat
            n "At the same time, you feel an overwhelming amount of radiation emanating from the wall."
            n "{cps=12}{sc}{color=#ff0000}{b}Looks like they want you to stay. :){b}{/color}{/sc}{/cps}"
            show black_screen zorder 50
            hide red_blur_2 onlayer top
            hide overlay_ai_1 onlayer top
            n "Your body decides that's enough for today and black out."
            window hide
            hide aikha
            hide lee
            pause 2.0
            show black_screen zorder 50:
                alpha 1.0
                linear 2.0 alpha 0.0
            window auto
            n "You wake up and find yourself lying on the floor of the lounge."
            n "The events of the staring contest slowly come back to you."
            n "Maybe you should avoid Dr. Aikha and Dr. Lee for the time being..."
            $ update_character_points({"aikha": -1, "lee": -1})
            return
