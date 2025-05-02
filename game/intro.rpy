# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# The game starts here.

label start:
    scene bg room
    "As I walk past the..."
    "Dancing...rainbow mushroom...?"
    "I hear a girl's voice behind me."

    show jessie neutral at appear

    jessie_unknown "Oh, hey!"
    jessie_unknown "The Founder told me you were coming today."
    jessie "I'm Dr. Jessie. What's your name?"

    python:
        player_name = renpy.input("My name is...", default=default_name)
        while len(player_name) > 15 or len(player_name) < 1 or not player_name.strip():
            renpy.notify("Invalid name: must be between 1-15 characters")
            player_name = renpy.input("My name is...", default=player_name)
        player_name = player_name.strip() or default_name
    
    menu:
        player "My pronouns are..."
        "He/him":
            $ player_sub = "he"
            $ player_sub_be = "he's"
            $ player_obj = "him"
            $ player_pos_adj = "his"
            $ player_pos_pro = "his"
            $ player_ref = "himself"
        "She/her":
            $ player_sub = "she"
            $ player_sub_be = "she's"
            $ player_obj = "her"
            $ player_pos_adj = "her"
            $ player_pos_pro = "hers"
            $ player_ref = "herself"
        "They/them":
            # assignments technically redundant since they/them is the default
            $ player_sub = "they"
            $ player_sub_be = "they're"
            $ player_obj = "them"
            $ player_pos_adj = "their"
            $ player_pos_pro = "theirs"
            $ player_ref = "themself"

    jessie "Nice to meet you, [player_name]!"
    jessie "Let me just call the founder to let him know you've come!"
    
    show jessie neutral:
        linear default_move_time xalign 0.0
    jessie "Hello, Mr. Founder?"
    jessie "The new recruit..."
    jessie "Yup, I've met up with [player_obj]."
    jessie "[cap_first(player_sub_be)] right here!"
    jessie "Of course! I'll do that right away."

    show jessie neutral:
        linear default_move_time xalign 0.5
    jessie "The founder has prepared a quick onboarding survey to determine the most suitable department for you to join!"
    jessie "Follow me into Plutoes' backyard!"

    
    jump honing_survey

label honing_survey:
    scene bg room
    show jessie neutral at center
    with default_fade

    jessie "Just answer these questions honestly!"
    jessie "Your responses will determine who you'll be spending the majority of your first week with."

    window hide # hide the say window when dialogue is not being shown
    show jessie neutral at right
    with move

    # TODO - if we want a pool of honing questions, expand this into a while loop and throw question-answer tuples into a list 

    $ returned_answer = 0

    show screen honing_survey(
        question="What do you do on a typical Friday night?",
        answer1="Partying! Clubbing! Drinking!", action1=Function(update_closeness, [("firewal", 1)]),
        answer2="Snuggle in a blanket and binge three seasons of House MD", action2=Function(update_closeness, [("firewal", 1)]),
        answer3="Accidentally doomscroll for seven hours", action3=Function(update_closeness, [("firewal", 1)]),
        answer4="Stay at the office until dawn, because there's always more to be done", action4=Function(update_closeness, [("firewal", 1)])
    )

    $ returned_answer = ui.interact() # force a ui interaction (that being an interaction with the screen) in order to proceed

    if returned_answer == 2:
        jessie "Cozy!"
    else:
        jessie "Okay!"

    show screen honing_survey(
        question="In the event of a containment breach...",
        answer1="Carry on as usual", action1=Function(update_closeness, [("firewal", 1)]),
        answer2="Look to Section J-3: Handing Anomaly Breaches", action2=Function(update_closeness, [("firewal", 1)]),
        answer3="Sleep", action3=Function(update_closeness, [("firewal", 1)]),
        answer4="Destroy all evidence of personal involvement", action4=Function(update_closeness, [("firewal", 1)])
    )

    $ returned_answer = ui.interact()

    if returned_answer == 3:
        jessie "Sure..."
    elif returned_answer == 4:
        jessie "Oh..."
    else:
        jessie "Sure!"

    show screen honing_survey(
        question="How would you resolve a conflict with a coworker?",
        answer1="Wait until both sides have cooled down before hosting a mature and respectful discussion with them", action1=Function(update_closeness, [("firewal", 1)]),
        answer2="Separate their body from their head", action2=Function(update_closeness, [("firewal", 1)]),
        answer3="Run to HR", action3=Function(update_closeness, [("firewal", 1)]),
        answer4="Calmly threaten them with eternal damnation should they disrespect you again", action4=Function(update_closeness, [("firewal", 1)])
    )

    $ returned_answer = ui.interact()

    if returned_answer == 2 or returned_answer == 4:
        show jessie sad
        jessie "Huh??"
        show jessie neutral
    else:
        jessie "Mhm!"

    show screen honing_survey(
        question="Which of the following is an appropriate employee interaction?",
        answer1="Prolonged eye contact", action1=Function(update_closeness, [("firewal", 1)]),
        answer2="Ankle biting! (consensual or otherwise)", action2=Function(update_closeness, [("firewal", 1)]),
        answer3="Group brainrot session!", action3=Function(update_closeness, [("firewal", 1)]),
        answer4="Opioid shot", action4=Function(update_closeness, [("firewal", 1)])
    )

    $ returned_answer = ui.interact()

    "The pulsating rainbow mushroom cheers."
    jessie "Don't mind Plutoes!"

    show screen honing_survey(
        question="Where would you go on vacation with your coworkers?",
        answer1="Somewhere in Europe! Barcelona? Or maybe Paris...", action1=Function(update_closeness, [("firewal", 1)]),
        answer2="Anomaly reconnaissance with the gang!!!", action2=Function(update_closeness, [("firewal", 1)]),
        answer3="Hell", action3=Function(update_closeness, [("firewal", 1)]),
        answer4="Do I really have to go...?", action4=Function(update_closeness, [("firewal", 1)])
    )

    $ returned_answer = ui.interact()

    jessie "Last question!"

    show screen honing_survey(
        question="You have a meeting at 7 am. When do you show up?",
        answer1="6:45 should be good!", action1=Function(update_closeness, [("firewal", 1)]),
        answer2="Accounting for my morning routine, traffic and miscellaneous catastrophic anomalies, I'll aim for 5:15", action2=Function(update_closeness, [("firewal", 1)]),
        answer3="Set an alarm for 6 but snooze it until 10", action3=Function(update_closeness, [("firewal", 1)]),
        answer4="Show up?", action4=Function(update_closeness, [("firewal", 1)])
    )

    $ returned_answer = ui.interact()

    window show

    jessie "Great job!"

    hide screen honing_survey

    show jessie neutral:
        linear default_move_time xalign 0.5

    # toggleable option
    jessie "According to the survey, the personnel you would get along with the best are:"
    

    menu:
        jessie "Are you satisfied with your results?"
        "Yes":
            jessie "Excellent!"
        "No":
            show jessie sad
            jessie "womp womp go reload your save" # add loop back to beginning of survey
            show jessie neutral
    
    jessie "Now that the survey's out of the way, let me introduce you to the personnel at VACF!"
    "And thus began my journey at VACF."
    "lItTlE dId I kNoW wHaT wAs WaItInG fOr Me In ThE cOmInG wEeK..."
    jump day_init