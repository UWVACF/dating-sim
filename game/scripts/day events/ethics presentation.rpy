image ethics_slide 1 = "images/day events/ethics slide 1.png"    
image ethics_slide 2 = "images/day events/ethics slide 2.png" 
image ethics_slide 3 = "images/day events/ethics slide 3.png" 
image ethics_slide 4 = "images/day events/ethics slide 4.png" 
image ethics_slide 5 = "images/day events/ethics slide 5.png" 
image ethics_slide 6 = "images/day events/ethics slide 6.png" 

transform run_left(duration = 1.1):
    xzoom 1.0
    move_to(-0.5, duration)

transform run_right(duration = 1.1):
    xzoom -1.0
    move_to(1.5, duration)

label day_event_ethics_presentation:
    scene bg venue
    with default_fade
    chan "Quiet down, everyone!"
    show chan neutral at appear
    chan "Thank you all for coming to the presentation."
    show chan neutral at move_to(x_align = 1.0)
    chan "Today, we will be discussing \"The Importance of Ethics in Everyday Life.\""
    show ethics_slide 1 behind chan:
        xalign 0.5
        yalign 0.2
        alpha 0.0
        linear 0.5 alpha 1.0
    chan "The information in this presentation is of utmost importance. As such, I expect you all to give 100%% of your attention."
    chan "Please ensure your cellphones are either on silent or turned off."
    chan "Firstly, let us define \"ethics.\""
    show black_screen zorder 50:
        alpha 0.0
        linear 4.0 alpha 1.0
    chan "Ethics is..."
    n "You feel your eyelids drooping."
    n "It hasn't even been a minute yet."
    
    show ethics_slide 2
    show black_screen:
        linear 2.0 alpha 0.0
    chan "...this includes not shooting your fellow coworkers. As well..."
    n "You hear someone furiously scribbling behind you."
    show helco at appear(x_align = 0.0)
    helco "{size=[helco_text_downsize]}(Do not...shoot...coworkers...I wonder why?){/size}"
    show helco at disappear
    show black_screen:
        alpha 0.0
        linear 4.0 alpha 1.0
    n "You're losing your fight for consciousness."
    hide helco
    n "Just as you're about to give in, you hear a panicked voice and the sound of running."
    show black_screen:
        linear 0.7 alpha 0.0
    aikha "Hey! Pochi! Stop!"
    show aikha:
        xalign -0.5
        yalign 1.0
    show aikha at run_right
    show ethics_slide 3
    
    chan "It is also paramount that you make every effort to pay your taxes."
    
    show aikha:
        xalign 1.5
    show aikha at run_left
    
    chan "Not only is it your moral obligation as a citizen, taxes help pay for government programs and services, such as infrastructure and health care."
   
    show aikha:
        xalign -0.5
    show aikha at run_right
    
    aikha "Stawp! STAWP!!!"
    chan "Furthermore- Dr. Aikha, do you mind?"
    
    show aikha:
        xalign 1.5
    show aikha at run_left

    aikha "Sure. One moment. POCHIIIIIIIIIIIIIIIII!!!"

    show aikha:
        xalign -0.5
    show aikha at run_right

    chan "On that note, the IRS have{nw}"

    show aikha:
        xzoom 1.0
        xalign 1.5
    show aikha at move_to(x_align = 0.5, duration = 0.5)

    extend " contacted us about- {nw}"

    show aikha:
        xzoom -1.0
    aikha "GOTCHA! FINALLY!"
    aikha "Heh, {nw}"

    show aikha at run_left(duration = 2.0)

    extend "sorry Chan!"
    hide aikha
    chan "..."
    chan "As I was saying, one of our units is under investigation by the IRS due to-"
    aikha "POCHI! AA- {nw}"
    hide ethics_slide 
    with hpunch
    n "You hear the sound of a projector crashing onto the floor."
    chan "..."
    chan "/no_pause.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}"
    show chan at run_right(duration = 5.0)
    chan "I'm going to get a new projector."
    n "You can't help but feel a bit bad. Just a little."
    n "You decide to try helping Dr. Chan out by becoming an exemplary audience member."
    $ ethics_presentation_correct_answers = 0

    show ethics_slide 3:
        xalign 0.5
        yalign 0.2
        alpha 0.0
        linear 0.5 alpha 1.0
    n "You move yourself to the front row."
    show chan:
        xzoom 1.0
    show chan at move_to(x_align = 1.0, duration = 1.4)
        
    n "As he sets up the new projector, you decide to ask:"
    player "Dr. Chan, what were you saying about the IRS?"
    n "You see his eyes light up slightly."
    chan "That's right. The IRS..."
    show black_screen:
        alpha 0.0
        linear 3.0 alpha 1.0
    n "Despite your efforts, you feel yourself dozing off yet again."
    n "\"Exemplary\", you said..."
    show ethics_slide 4
    show black_screen:
        alpha 1.0
        linear 3.0 alpha 0.0
    chan "...violation of the Geneva convention."
    
    show helco at appear(x_align = 0.0)
    helco "{size=[helco_text_downsize]}(Violate...the Geneva...convention...){/size}"
    show helco at disappear
    
    chan "On that note, can anybody tell me what the IRS stands for?"
    n "You remember the decision you made 40 seconds ago and meekly raise your hand."
    n "Dr. Chan's eyes light up a bit more."
    chan "Yes, [player_name]?"
    menu:
        chan "What does the IRS stand for?"
        "International Revenue Service":
            chan "Not quite."
        "Internal Returns System":
            chan "Not quite."
        "Internal Revenue Service":
            chan "Correct."
            $ ethics_presentation_correct_answers += 1
        "I'm Really Sleepy":
            chan "..."
            chan "Please try to pay attention."
    chan "The IRS - Internal Revenue Service - is responsible for collecting..."

    show black_screen:
        alpha 0.0
        linear 4.0 alpha 1.0
    
    n "The sound of his voice has yet to fail at putting you to sleep."
    chan "...deductibles...insurance...Ponzi scheme..."

    show ethics_slide 5
    show black_screen:
        alpha 1.0
        linear 4.0 alpha 0.0
    
    chan "...which, naturally, brings us to the Declaration of Independence. Who can tell me which US president first drafted this document?"
    menu:
        n "You don't want to question the line of reasoning that brought him here. Who drafted the Declaration of Independence?"
        "Thomas Edison":
            chan "Not exactly."
        "Abraham Lincoln":
            chan "Not exactly."
        "Thomas Jefferson":
            chan "Perfect."
            $ ethics_presentation_correct_answers += 1
        "Al Capone":
            chan "..."
    chan "It was Thomas Jefferson who initially drafted the Declaration of Independence on July 4th, 1776."

    show black_screen:
        alpha 0.0
        linear 4.0 alpha 1.0
    
    chan "This was a pivotal point in United States history. The document discusses..."
    n "Maybe you should go to bed earlier."

    show ethics_slide 6
    show black_screen:
        alpha 1.0
        linear 4.0 alpha 0.0
    
    chan "...to quote Hamlet, \"To be or not to be? That is the question.\""
    chan "Speaking of Hamlet, many misremember a crucial part of the play. Can somebody tell me what it is?"
    menu:
        n "How did we get here? Anyways, which of the following is a common misconception about the play, \"Hamlet\"?"
        "That Yorick is the court jester - the court jester's name is actually Horatio":
            chan "Wrong."
        "That Hamlet holds a skull during his \"To be or not to be\" soliloquy - he does not":
            chan "Excellent."
            $ ethics_presentation_correct_answers += 1
        "That Hamlet is the Prince of Denmark - he's actually the Prince of Norway":
            chan "Wrong."
        "That Hamlet's father was poisoned in his garden - he was actually poisoned in his bed":
            chan "Wrong."
    chan "Hamlet is often believed to be holding a skull during his famous soliloquy in Act III, Scene I. This is incorrect: he holds a skull during his soliloquy in Act V, Scene I, \"Alas, Poor Yorick!\""
    chan "Please do not forget this when the IRS investigation occurs later tonight."
    show ethics_slide 6:
        alpha 1.0
        linear 1.0 alpha 0.0
    chan "That concludes the presentation for today."

    hide ethics_slide
    chan "If you have any questions, please send me an email and I will reply promptly."
    show chan at move_to(x_align = 0.5)
    chan "[player_name], I would like a word, please."

    if ethics_presentation_correct_answers < 2:
        chan "I appreciate that you...attempted to answer my questions."
    else:
        chan "I appreciate that you answered my questions."
    
    if ethics_presentation_correct_answers >= 2:
        chan "It's a breath of fresh air to see someone actually realize the importance of ethics."
    
    chan "I hope you found something useful from the presentation today."

    if ethics_presentation_correct_answers == 0:
        n "You feel closer with Dr. Chan...is what you would say if you'd gotten a single one of his questions correct."
        $ update_character_points({"chan": -1})
    elif ethics_presentation_correct_answers < 3:
        n "For someone dozing off during the presentation, you feel like you didn't do too bad on the questions."
    else:
        n "Despite being half awake during the presentation, you managed to answer his questions flawlessly. What a prodigy you are!"
        $ update_character_points({"chan": 1})
    return