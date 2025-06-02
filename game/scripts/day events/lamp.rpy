label day_event_lamp:
    scene bg cubicle
    n "You return to your desk after a small walk."
    n "Time to get back to work!"
    n "You notice a new addition to your cubicle. A tall lamp stands in the corner of your already cramped cubicle."
    n "Must be the part of the new egonomic assessment. It's just a bit too clunky to your liking."
    n "Still, it's better than nothing."
    n "You plug its cord into the outlet, then turn the switch on."
    
    show black_screen onlayer top
    with default_fade
    show black_screen as black_bg
    hide black_screen onlayer top
    show black_screen as black_between zorder 3:
        alpha 0.0
        block:
            linear 2.5 alpha 0.8
            linear 2.5 alpha 0.5
            repeat

    n "Huh. Why are even the office lights out?"
    n "You click on the switch again. But you can't feel the switch."
    n "In fact, you can't even {i}feel{/i} your fingers. Or your arm. Or yourself. Or anything."
    player "   "
    player "   "
    player "   "
    n "You can't even hear your own voice. This is kind of bad, isn't it?"
    n "You have a meeting in 20 minutes and you haven't finished preparing for it. You really can't afford to be stuck in perpetual darkness."
    n "Actually, how long has it been? You can't even count your own heartbeat to detemine this."
    n "Just as you are about to start panicking, you make out a faint...image of someone."
    show layer master:
        blur 30
    show alex pensive
    n "Is that...Founder Alex?"
    n "Oh right. You have a meeting with the Founder."
    alex "{color=#8eabbf}{size=-15}Hm. Is intern [player_name] not here?{/size}{/color}"
    player "    "
    n "Oh right. You don't have a vocal cord anymore."
    alex "{color=#8eabbf}{size=-15}Oh. He left his phone here.{/size}{/color}"
    alex "{color=#8eabbf}{size=-15}More break time!{/size}{/color}"
    show alex pensive at disappear
    n "Oh. He's gone."
    n "Well, at least you don't have to worry about the meeting."
    hide alex
    with default_fade
    n "You don't know how long it's been. An hour? A day? A week?"
    n "Time seems to have stopped in the enternal darkness."
    n "You try to recall the emergency protocol trainings you did during onboarding for anomalous situations."
    n "1. Distant yourself from the anomaly. Can't really do that."
    n "2. Seek help from the Wal security team. Can't really do that."
    n "3. Report to respective supervisor. You don't really know what department this falls under."
    n "4. ...What was it again?"
    n "Just as you try to scrape your brain for step 4, another...image come into existance."
    show firewal pensive
    unknown "{color=#8eabbf}{size=-15}This is all we found at [player_pos_adj] cubicle.{/size}{/color}"
    wal1 "{color=#8eabbf}{size=-10}I see. That should rule out murder by robbery, since their device is here.{/size}{/color}"
    n "It's a Wal! The security team! You're saved!"
    wal1 "{color=#8eabbf}{size=-5}Hm. The device seems normal.{/size}{/color}"
    wal1 "{color=#8eabbf}{size=-5}We'll put it in the evidence archive, then.{/size}{/color}"
    n "You can feel the Wal No.1's image getting more distant. "




