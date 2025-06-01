label day_event_fin:
    image overlay_ai_1 = At("images/day events/overlay ai 1.png", base_overlay_transform)
    
    scene bg cubicle
    n "You take a long yawn. Today is one of those few uneventful and slow day at work."
    n "Really, you should appreciate such peaceful days."
    n "But all you feel is mind-numbing boredom as you comb through the old files and type them into the system."
    n "Perhaps you've gotten too used to the constant chaos that usually occur."
    n "You stand up to take a strech and glance around the office room. It seems like today is a slow day for everyone else too."
    n "You reach your arm into your backpocket and slowly pull out your phone. Surely you can take a short break, right?"
    n "Your finger follows your muscle memory and opens the app. Just one reel."
    with default_fade
    n "..."
    n "So it's been a little bit more than one reel."
    n "Just one more..."
    n "A loud {i}thump{/i} startles you and make you drop your phone. Someone must have fallen asleep on their keyboard."
    n "You look up from your desk and see...a shark fin peeking over the cubicle wall."
    n "You drop your phone a second time. The fin rises above the wall and you see that it's Dr. Aikha."
    show aikha 
    aikha happy "Working hard, aren't we, intern?"
    n "You nervously break a sweat."
    aikha "So how's it going so far?"
    player "It's alrgiht...just a slow day."
    n "You avoid Dr. Aikha's main pair of eyes. Your eyes land on their fin, which also has an eye. It stares at you and blinks."
    player "Dr. Aikha, have you...always had a shark fin?"
    aikha neutral "Hm? Oh. Yes. It just comes out sometimes."
    n "Huh. Guess you learn something new every day at the foundation."
    n "You stare intensely at the shark fin. It has greatly evoked your curiousity. Especially comparing to the monotonus archive files you still have to go through."
    player "If I may ask, why {i}do{/i} you have a shark fin, Dr. Aikha?"
    aikha happy "To better swim with, of course!"
    show aikha neutral
    n "Swim..?"
    n "Well, you suppose that it'll make it easier for them to collect anomaly samples in aquatic environments."
    n "Some of Dr. Aikha's eyes begin to twich and survey the office. Looks like they're about to leave."
    n "But you really don't want to get back to work. You pounder for things to say that'll keep Dr. Aikha here to entertain your boredom."
    player "Dr. Aikha, why do you have so many eyes?"
    n "All the eyes on Dr. Aikha turn to focus on you."
    aikha happy "To better to see you guys with, of course!"
    n "Some of the eyes blink in agreement."
    aikha neutral "I must say, [player_name], you're particularly curious today."
    player "Haha. Well, I've always been curious."
    n "You can't help but feel that Dr. Aikha has been giving you very vague answers."
    aikha happy "So, anything else you want to know?"
    n "You think for a bit. Actually, your brain has given up on thinking."
    n "You despertely scan Dr. Aikha for any other talking points. They grin at you."
    player "Dr. Aikha, why do you have sharp teeth?"
    aikha neutral "..."
    show overlay_ai_1 onlayer top:
        alpha 0.0
        linear 0.5 alpha 1.0
    aikha unique "{sc}{b}To better eat you with, of course!{b}{/sc}"
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
    n "You take out your phone and open the camera to admire your grided forhead."
    n "Then you see Dr. Aikha peeking at you over the cubicle wall from behind."
    show aikha
    n "You drop your phone for the third time. No, first time?"
    player "Hello, Dr. Aikha."
    aikha happy "Working hard, aren't we, intern?"
    n "You {i}very{/i} nervously break a sweat."
    aikha "So how's it going so far?"
    player "..."
    player "It's alrgiht...just a slow day."
    n "You glance on the top of Dr. Aikha's head. There is no fin. Just an ahoge."
    aikha neutral "You look a little pale, [player_name]. Is something the matter?"
    player "Oh no. Just...tired."
    aikha happy "Well then, keep it up!"
    aikha neutral "Anyways, I was here to look for Plutoes. Have you seen Plutoes around here, [player_name]?"
    player "No, can't say I have."
    aikha "I see. Thank you."
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
        aikha "I must say, [player_name], you're particularly curious today."
        player "Haha. Well...it's a slow day."
        n "Dr. Aikha glances at your file of archive entries. They give you a nod in pity."
        aikha "Well, good luck with that!"
        hide aikha 
        n "Dr. Aikha turns around and leaves. Likely to continue their search for Plutoes."
        n "You turn your attention back to the stack of dull files. You reach over to turn on your computer when you noticed a long row of faint teeth-marks on your arm."
        n "...Wait, teeth-marks?"
        $ update_character_points({"aikha": +1})
        return

    label fin_nope:
        n "You don't say anything. Remember, curiousity killed the cat."
        n "You slump back down onto your chair. Maybe you should go to the psychology department sometime to get a check-in on your mental health."
        n "You turn your attention back to the stack of dull files. You can't decide whether you prefer this or the life-threatening situation."
        n "...Maybe you really should go get an assessment with Dr. Chan."
        $ update_character_points({"aikha": -1})
        return