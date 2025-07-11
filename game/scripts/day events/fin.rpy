label day_event_fin:
    image overlay_ai_1 = At("images/day events/overlay ai 1.png", base_overlay_transform)
    
    scene bg cubicle
    n "You let out a long yawn. Today is one of those few uneventful and slow days at work."
    n "Really, you should appreciate such peaceful days."
    n "But all you feel is mind-numbing boredom as you comb through the old files and type them into the system."
    n "Perhaps you've gotten too used to the constant chaos that usually occurs."
    n "You stand up to take a strech and glance around the office room. It seems like today is a slow day for everyone else too."
    n "You reach your arm into your back pocket and slowly pull out your phone. Surely you can take a short break, right?"
    n "Your finger follows your muscle memory and opens the app. Just one reel."
    with default_fade
    n "..."
    n "So it's been a little bit more than one reel."
    n "Just one more..."
    n "A loud {i}thump{/i} startles you and makes you drop your phone. Someone must have fallen asleep on their keyboard."
    n "You look up from your desk and see...a shark fin peeking over the cubicle wall."
    n "You drop your phone a second time. The fin rises above the wall and you see that it's Dr. Aikha."
    show aikha 
    aikha happy "Working hard, aren't we, new recruit?"
    n "You nervously break a into sweat."
    aikha "So how's it going so far?"
    player "It's alright...just a slow day."
    n "You avoid Dr. Aikha's main pair of eyes. Your eyes land on their fin, which also has an eye. It stares at you and blinks."
    player "Dr. Aikha, have you...always had a shark fin?"
    aikha neutral "Hm? Oh. Yes. It just comes out sometimes."
    n "Huh. Guess you learn something new every day at the foundation."
    n "You stare intensely at the shark fin. It has greatly evoked your curiousity. Especially compared to the monotonous archive files you still have to go through."
    player "If I may ask, why {i}do{/i} you have a shark fin, Dr. Aikha?"
    aikha happy "The better to swim with, of course!"
    show aikha neutral
    n "Swim..?"
    n "Well, you suppose that it'll make it easier for them to collect anomaly samples in aquatic environments."
    n "Some of Dr. Aikha's eyes begin to twich and survey the office. Looks like they're about to leave."
    n "But you really don't want to get back to work. You ponder for things to say that'll keep Dr. Aikha here to lessen your boredom."
    player "Dr. Aikha, why do you have so many eyes?"
    n "All the eyes on Dr. Aikha turn to focus on you."
    aikha happy "The better to see you guys with, of course!"
    n "Some of the eyes blink in agreement."
    aikha neutral "I must say, [player_name], you're particularly curious today."
    player "Haha. Well, I've always been curious."
    n "You can't help but feel that Dr. Aikha has been giving you very vague answers."
    aikha happy "So, anything else you want to know?"
    n "You think for a bit. Actually, your brain has given up on thinking."
    n "You desperately scan Dr. Aikha for any other talking points. They grin at you."
    player "Dr. Aikha, why do you have sharp teeth?"
    aikha neutral "..."
    show overlay_ai_1 onlayer top:
        alpha 0.0
        linear 0.5 alpha 1.0
    aikha unique "{sc}{b}The better to eat you with, of course!{b}{/sc}"
    hide aikha 

    show black_screen:
        alpha 0.0
        linear 0.5 alpha 1.0

    show overlay_ai_1 onlayer top:
        alpha 1.0
        linear 0.2 alpha 0.0

    pause 2

    n "You feel sharp, hard pieces against your face."
    hide overlay_ai_1 onlayer top
    n "This must be the end..."
    n "..."
    n "Curiousity kills the cat."
    n "..."
    n "Huh. The end sure is taking a while."
    hide black_screen
    n "You open your eyes to take a peek. There is no Dr. Aikha, no shark fin, no eyes, no teeth."
    n "There is however, a [player_name] who is currently lying face first on [player_pos_adj] keyboard."
    n "You take out your phone and open the camera to admire your gridded forehead."
    n "Then you see Dr. Aikha peeking at you over the cubicle wall from behind."
    show aikha
    n "You drop your phone for the third time. No, first time?"
    player "Hello, Dr. Aikha."
    aikha happy "Working hard, aren't we, new recruit?"
    n "You {i}very{/i} nervously break into a sweat."
    aikha "So how's it going so far?"
    player "..."
    player "It's alright...just a slow day."
    n "You glance at the top of Dr. Aikha's head. There is no fin. Just an ahoge."
    aikha neutral "Your heartrate is a little higher than usual, [player_name]. Is something the matter?"
    player "Oh no. Just...tired."
    aikha happy "Well then, keep it up!"
    aikha neutral "Anyways, I was here to check in on everyone. Oh, what's that on your phone?"
    aikha "I didn't think that dancing rats was part of your assignment."
    n "You force a smile and shove your phone deep into your back pocket."
    aikha "As long as work's getting done, I don't mind."
    aikha "So I advise you get back to it."
    hide aikha
    n "Dr. Aikha turns around to leave. You stand up to walk them out of your tiny cubicle."
    n "And on the back of Dr. Aikha's head, you see...a shark fin."
    menu:
        "Ask about the shark fin.":
            jump fin_ask
        "Don't ask.":
            jump fin_nope

    label fin_ask:
        n "You muster up the courage to speak the words."
        player "Dr. Aikha, have you...always had a shark fin?"
        show aikha 
        aikha surprise "Hm? Oh. Yes. It just comes out sometimes."
        aikha neutral "I didn't realize it had popped out again. Huh."
        player "...If I may ask, why {i}do{/i} you have a shark fin, Dr. Aikha?"
        aikha neutral "Oh. It's just something I have. Just like you have two eyes and a nose, yea?"
        player "...I see."
        aikha "I must say, you're particularly curious today."
        player "Haha. Well...it's a slow day."
        n "Dr. Aikha glances at your file of archive entries. They give you a nod in pity."
        aikha "Well, good luck with that!"
        hide aikha 
        n "Dr. Aikha turns around and leaves. Likely to continue their micromanaging."
        n "You turn your attention back to the stack of dull files. You reach over to turn on your computer when you notice a long row of faint teeth-marks on your arm."
        n "...Wait, teeth-marks?"
        $ update_character_points({"aikha": 3})
        return

    label fin_nope:
        n "You don't say anything. Remember, curiousity killed the cat."
        n "You pull your phone back out. Your butt has swiped the screen for you and you are now the rats are no longer dancing kpop, but pole dancing."
        n "You quickly turn your screen brightness down and look up to see if anyone has seen your screen."
        n "Out of the corner of your eye, you see Dr. Aikha walks through the exit to the office, some of their eyes still on you."
        $ shake_screen()(0.2,0.4)
        n "Their fin slams against the doorframe. Ouch."
        n "Dr. Aikha usually wouldn't make this kind of mistake, given their very hightened perception."
        n "Unless, of course, they were very distracted."
        n "You slump back down onto your chair to avoid the few eyes glaring at you on Dr. Aikha's neck."
        n "You turn your attention back to the stack of dull files. You can't decide whether you prefer this or the life-threatening situation."
        n "...Maybe you should go get a mental health check with Dr. Chan. For your reel addiction, too."
        $ update_character_points({"aikha": -3})
        return