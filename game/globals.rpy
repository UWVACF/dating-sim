# This file will contain global variables and constants

# Constants

init python:
    import copy
    import random
    random.seed()

    # the pause times after certain punctuation marks
    comma_pause = 0.2
    period_pause = 0.4
    elipsis_pause = 0.133
    exclamation_pause = period_pause
    question_pause = period_pause
    colon_pause = comma_pause
    semicolon_pause = colon_pause
    quotation_pause = comma_pause

    # the default time for a standard sprite movement
    default_move_time = 0.7

    # the amount helco's text size will decrease when he's thinking
    # must be <= 0
    helco_text_downsize = -15

    # variables

    intimacy_points = {
        "helco": 0,
        "aikha": 0,
        "firewal": 0,
        "jessie": 0,
        "plutoes": 0,
        "alex": 0,
        "chan": 0,
        "paul": 0
    }

    # should include only who's romanceable/has a route
    honing_points = {
        "syg": 0,
        "alex": 0,
        "helco": 0,
        "aikha": 0,
        "firewal": 0,
        "venture": 0,
        "uriel": 0,
        "ryz": 0,
        "deceased": 0,
        "chan": 0,
        "bad end": 0
    }

    # TODO: determine this value procedurally
    # array of top three personnel from honing survey, in no particular order
    top_three_honed = [
        "aikha",
        "firewal",
        "plutoes"
    ]

    # TBD: determine if we just want a fixed chance of having an event with one of the three (e.g. 75% the event guaranteed has one of them)
    # the multiplier of weight given to events with the top three
    top_three_weight_factor = 2

    day_number = 1
    day_threshold = 7 # max number of days

    honing_survey_questions_threshold = 7 # number of honing survey questions that need to be taken


# Player pronouns and names
define default_name = "Jakob"
define player_name = ""
define player_sub = "they" # subject pronoun (he, she, they)
define player_sub_be = "they're" # subject pronoun + to be (he's, she's, they're)
define player_obj = "them" # object pronoun (him, her, them)
define player_pos_adj = "their" # possessive adjective  (his, her, their)
define player_pos_pro = "theirs" # possessive pronoun (his, hers, theirs)
define player_ref = "themself" # reflexive pronoun (himself, herself, themself)

# Personnel images

image jessie neutral = At("images/jessie neutral.png", sprite_highlight("jessie"))
image jessie sad = At("images/jessie sad.png", sprite_highlight("jessie"))
image jessie upset = At("images/jessie upset.png", sprite_highlight("jessie"))

image firewal neutral = At("images/firewal neutral.png", sprite_highlight("firewal"))

image helco neutral = At("images/helco neutral.png", sprite_highlight("helco"))

image aikha neutral = At("images/aikha neutral.png", sprite_highlight("aikha"))

image plutoes neutral = At("images/plutoes neutral.png", sprite_highlight("plutoes"))



# Characters

define base_char = Character("", callback=name_callback)

define jessie = Character("Dr. Jessie", kind=base_char, color="#ff6dcf", cb_name="jessie", image="jessie")
define jessie_unknown = Character("???", kind=jessie)

define firewal = Character("Dr. Firewal", kind=base_char, color="#961e44", cb_name="firewal", image="firewal")

define helco = Character("Dr. Helco", kind=base_char, color="#fffda1", cb_name="helco", image="helco")

define aikha = Character("Dr. Aikha", kind=base_char, color="#8f76ff", cb_name="aikha", image="aikha")

define plutoes = Character("Plutoes", kind=base_char, color="#62ff58", cb_name="plutoes", image="plutoes")

define player = Character("[player_name]", kind=base_char, color="#c9c9c9", cb_name="player")

# Transitions and transformations

transform appear(y_offset = 70, duration = 0.5, x_align = 0.5, y_align = 1.0):
    xalign x_align
    yalign y_align
    yoffset y_offset
    matrixcolor BrightnessMatrix(-1.0)
    # alpha 0.0

    parallel:
        easein duration yoffset 0
    parallel:
        linear duration matrixcolor BrightnessMatrix(0.0)

define default_fade = Fade(1.0, 1.0, 1.0)