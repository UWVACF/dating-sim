label start:
    if debug_mode:
        jump day_init
    
    scene bg room
    n "As I walk past the..."
    n "Dancing...rainbow mushroom...?"
    n "I hear a girl's voice behind me."

    show jessie neutral at appear

    jessie_unknown "Oh, hey!"
    jessie_unknown "The Founder told me you were coming today."
    jessie "I'm Dr. Jessie. What's your name?"
    jessie "{nw}" (cb_name = None) # force unhighlight jessie
    python:
        player_name = renpy.input("My name is...", default=default_name)
        while len(player_name) > 15 or len(player_name) < 1 or not player_name.strip():
            renpy.notify("Invalid name: must be between 1-15 characters")
            player_name = renpy.input("My name is...", default=player_name)
        player_name = player_name.strip() or default_name
    # 
    menu:
        player "My pronouns are..."
        "He, him":
            $ player_sub = "he"
            $ player_sub_be = "he's"
            $ player_obj = "him"
            $ player_pos_adj = "his"
            $ player_pos_pro = "his"
            $ player_ref = "himself"
        "She, her":
            $ player_sub = "she"
            $ player_sub_be = "she's"
            $ player_obj = "her"
            $ player_pos_adj = "her"
            $ player_pos_pro = "hers"
            $ player_ref = "herself"
        "They, them":
            # assignments technically redundant since they/them is the default
            $ player_sub = "they"
            $ player_sub_be = "they're"
            $ player_obj = "them"
            $ player_pos_adj = "their"
            $ player_pos_pro = "theirs"
            $ player_ref = "themself"

    jessie "Nice to meet you, [player_name]!"
    jessie "Let me just call the founder to let him know you've come!"
    
    show jessie neutral at move_to(x_align = 0.0)
    jessie "Hello, Mr. Founder?"
    jessie "The new recruit..."
    jessie "Yup, I've met up with [player_obj]."
    jessie "[cap_first(player_sub_be)] right here!"
    jessie "Of course! I'll do that right away."

    show jessie neutral at move_to(0.5)
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

    python: 
        returned_answer = 0
        questions_answered = 0
        remaining_honing_survey_questions = copy.deepcopy(honing_suvey_questions)

    while questions_answered < honing_survey_questions_threshold:
        $ question_index = random.randint(0, len(remaining_honing_survey_questions) - 1)
        show screen honing_survey(
            question=remaining_honing_survey_questions[question_index]["question"],
            answers_and_actions=remaining_honing_survey_questions[question_index]["answers"]
        )

        # TODO: increment honing points depending on the question

        python:
            returned_answer = ui.interact()
            reply = remaining_honing_survey_questions[question_index]["answers"][returned_answer]["reply"]
            if reply == "":
                reply = random.choice(default_jessie_replies)
        
        jessie "[reply]"

        $ remaining_honing_survey_questions.pop(question_index)
        $ questions_answered += 1

    window show

    jessie "Great job!"

    hide screen honing_survey

    show jessie neutral:
        linear default_move_time xalign 0.5

    # toggleable option
    jessie "Congrats on finishing the survey!"

    if honing_points["bad end"] > 10:
        jessie "..."
        jessie "Uh, one second..."
        show jessie neutral at left
        with move
        jessie "..."
        jessie "...okay..."
        show jessie neutral:
            linear default_move_time xalign 0.5
        jessie "..."
        jessie "So, um..."
        jessie "According to the founder, your results were..."
        jessie "\"Abysmal. Appalling. Inhumane.\""
        jessie "He said he would \"recommend you to see a therapist,\" but he'd be \"scared for the therapist.\""
        jessie "He said you \"somehow chose the very obviously worst answer over 90%% of the time.\""
        jessie "So we're revoking your position at the company."
        jessie "Sorry about that..."
        return


    menu:
        jessie "Are you satisfied with your results?"
        "Yes":
            jessie "Excellent!"
        "No":
            jessie sad "womp womp go reload your save"
    
    jessie neutral "Now that the survey's out of the way, let me introduce you to the personnel at VACF!"
    n "And thus began my journey at VACF."
    jump day_init


init python:
    default_jessie_replies = [
        "Mhm!",
        "Yup!",
        "Nice!",
        "Yep!",
        "Great!"
    ]


    # if you guys REALLY want to add onto the reply system, i can add support for multiple lines and characters speaking in each reply

    # array of honing survey questions
    # the format is as such:
    # - array
    #   - dictionary
    #       - "question": string
    #       - "answers": list
    #           - dictionary
    #               - "answer": string
    #               - "personnel": dictionary
    #                       - "person name": num of points (int)
    #               - "reply": string
    honing_suvey_questions = [
        {
            "question": "What do you do on a typical Friday night?",
            "answers": [
                {
                    "answer": "Partying! Clubbing! Drinking!",
                    "personnel": {"plutoes": 1, "aikha": -1},
                    "reply": ""
                },
                {
                    "answer": "Snuggle in a blanket and binge three seasons of House MD",
                    "personnel": {"helco": 1},
                    "reply": "Real!"
                },
                {
                    "answer": "Accidentally doomscroll for seven hours",
                    "personnel": {"aikha": 1},
                    "reply": "REAL!"
                },
                {
                    "answer": "Stay at the office until dawn: there's always more to be done",
                    "personnel": {"aikha": 1},
                    "reply": "Oh my..."
                }
            ]
        },
        {
            "question": "In the event of a containment breach...",
            "answers": [
                {
                    "answer": "Carry on as usual",
                    "personnel": {"firewal": 1},
                    "reply": "Sure!"
                },
                {
                    "answer": "Look to Section J-3: Handing Anomaly Breaches",
                    "personnel": {"firewal": 1},
                    "reply": ""
                },
                {
                    "answer": "Sleep",
                    "personnel": {"firewal": 1},
                    "reply": "Sure..."
                },
                {
                    "answer": "Destroy all evidence of personal involvement",
                    "personnel": {"bad end": 1},
                    "reply": "Oh..."
                }
            ]
        },
        {
            "question": "How would you resolve a conflict with a coworker?",
            "answers": [
                {
                    "answer": "Wait until both sides have cooled down before hosting a mature and respectful discussion with them",
                    "personnel": {"firewal": 1},
                    "reply": ""
                },
                {
                    "answer": "Separate their body from their head",
                    "personnel": {"bad end": 1},
                    "reply": "Huh??"
                },
                {
                    "answer": "Run to HR",
                    "personnel": {"firewal": 1},
                    "reply": ""
                },
                {
                    "answer": "Calmly threaten them with eternal damnation should they disrespect you again",
                    "personnel": {"firewal": 1},
                    "reply": "Huh??"
                }
            ]
        },
        {
            "question": "Which of the following is an appropriate employee interaction?",
            "answers": [
                {
                    "answer": "Prolonged eye contact",
                    "personnel": {"firewal": 1},
                    "reply": ""
                },
                {
                    "answer": "Ankle biting! (consensual or otherwise)",
                    "personnel": {"firewal": 1},
                    "reply": ""
                },
                {
                    "answer": "Spew brainrot",
                    "personnel": {"firewal": 1},
                    "reply": "Yippee!!"
                },
                {
                    "answer": "Opioid shot",
                    "personnel": {"bad end": 1},
                    "reply": "..."
                }
            ]
        },
        {
            "question": "Where would you go on vacation with your coworkers?",
            "answers": [
                {
                    "answer": "Somewhere in Europe! Barcelona? Or maybe Paris...",
                    "personnel": {"firewal": 1},
                    "reply": "Ooh! Classic!"
                },
                {
                    "answer": "Anomaly reconnaissance with the gang!!!",
                    "personnel": {"firewal": 1},
                    "reply": ""
                },
                {
                    "answer": "Hell",
                    "personnel": {"bad end": 1},
                    "reply": "Whuh-"
                },
                {
                    "answer": "Do I really have to go...?",
                    "personnel": {"firewal": 1},
                    "reply": "Yes..."
                }
            ]
        },
        {
            "question": "You have a meeting at 7 am. When do you show up?",
            "answers": [
                {
                    "answer": "6:45 should be good!",
                    "personnel": {"firewal": 1},
                    "reply": ""
                },
                {
                    "answer": "Accounting for my morning routine, traffic and miscellaneous catastrophic anomalies, I'll aim for 4:15",
                    "personnel": {"firewal": 1},
                    "reply": ""
                },
                {
                    "answer": "Set an alarm for 6 but snooze it until 10",
                    "personnel": {"firewal": 1},
                    "reply": ""
                },
                {
                    "answer": "Show up?",
                    "personnel": {"bad end": 1},
                    "reply": "..."
                }
            ]
        },
        {
            "question": "What do you do when an employee takes your lunch?",
            "answers": [
                {
                    "answer": "It's fine! I'll just starve :'D",
                    "personnel": {"firewal": 1}, 
                    "reply": ":'D"
                },
                {
                    "answer": "Challenge them to a duel at high noon",
                    "personnel": {"bad end": 1},
                    "reply": "Hmm..."
                },
                {
                    "answer": "Steal theirs back",
                    "personnel": {"firewal": 1},
                    "reply": ""
                },
                {
                    "answer": "Fall into a state of depression",
                    "personnel": {"firewal": 1},
                    "reply": ""
                }
            ]
        },
        {
            "question": "Live, laugh and...",
            "answers": [
                {
                    "answer": "Love",
                    "personnel": {"firewal": 1},
                    "reply": "Yay!"
                },
                {
                    "answer": "Lacerate",
                    "personnel": {"bad end": 1},
                    "reply": "...huh???"
                },
                {
                    "answer": "Lament",
                    "personnel": {"firewal": 1},
                    "reply": "Oh."
                },
                {
                    "answer": "Leave",
                    "personnel": {"firewal": 1},
                    "reply": ""
                }
            ]
        },
        {
            "question": "How well can you cook?",
            "answers": [
                {
                    "answer": "I mean, I'm okay",
                    "personnel": {"firewal": 1},
                    "reply": ""
                },
                {
                    "answer": "They call me Gordon Ramsay",
                    "personnel": {"firewal": 1},
                    "reply": "Ooh!"
                },
                {
                    "answer": "I starve",
                    "personnel": {"firewal": 1},
                    "reply": ""
                },
                {
                    "answer": "Where do you think my fingers went?",
                    "personnel": {"firewal": 1},
                    "reply": "God, are you okay?"
                }
            ]
        },
        {
            "question": "What's your favourite thing to do with friends?",
            "answers": [
                {
                    "answer": "Chill on the couch with snacks and tea",
                    "personnel": {"firewal": 1},
                    "reply": ""
                },
                {
                    "answer": "Hold a meeting to discuss our budget and future prospects",
                    "personnel": {"firewal": 1},
                    "reply": "Yay..."
                },
                {
                    "answer": "Plan a heist and/or murder",
                    "personnel": {"bad end": 1},
                    "reply": "..."
                },
                {
                    "answer": "I have no friends. I'm so alone.",
                    "personnel": {"bad end": 1},
                    "reply": "Oh..."
                }
            ]
        },
        {
            "question": "How's your work life balance?",
            "answers": [
                {
                    "answer": "Pretty solid!",
                    "personnel": {"firewal": 1},
                    "reply": ""
                },
                {
                    "answer": "I'm a bit of a workaholic",
                    "personnel": {"firewal": 1},
                    "reply": ""
                },
                {
                    "answer": "Work?",
                    "personnel": {"bad end": 1},
                    "reply": ""
                },
                {
                    "answer": "Life?",
                    "personnel": {"firewal": 1},
                    "reply": ""
                }
            ]
        },
        {
            "question": "What traits in other people are important to you?",
            "answers": [
                {
                    "answer": "Confidence and respect",
                    "personnel": {"firewal": 1},
                    "reply": ""
                },
                {
                    "answer": "Compassion and generosity",
                    "personnel": {"firewal": 1},
                    "reply": ""
                },
                {
                    "answer": "Ambition and open-mindedness",
                    "personnel": {"firewal": 1},
                    "reply": ""
                },
                {
                    "answer": "Evident lack of moral compass",
                    "personnel": {"bad end": 1},
                    "reply": "..."
                }
            ]
        },
        # {
        #     "question": "",
        #     "answers": [
        #         {
        #             "answer": "",
        #             "personnel": {"firewal": 1},
        #             "reply": ""
        #         },
        #         {
        #             "answer": "Empathy",
        #             "personnel": {"firewal": 1},
        #             "reply": ""
        #         },
        #         {
        #             "answer": "Ambition",
        #             "personnel": {"firewal": 1},
        #             "reply": ""
        #         },
        #         {
        #             "answer": "Evident lack of moral compass",
        #             "personnel": {"bad end": 1},
        #             "reply": "..."
        #         }
        #     ]
        # }
    ]