# This file will contain global variables and constants

# Constants

init python:
    # ----- STATEMENTS -----
    import copy
    import random
    random.seed() # makes a new seed to ensure randomness

    # disables the option of moving back in text
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! SET TO FALSE WHEN SHIPPING !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    config.rollback_enabled = True

    # set to True to skip the intro sequence (so you can test dialogue faster)
    skip_intro = True

    # ----- CONSTANTS -----
    # the default pause times after certain punctuation marks
    # note to developers: prefix a dialogue line with {no_pause} to disable these pauses for that line
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

    # TBD: determine if we just want a fixed chance of having an event with one of the three (e.g. 75% the event guaranteed has one of them)
    # the multiplier of weight given to events with the top three
    honed_weight_factor = 2

    honing_survey_questions_threshold = 7 # number of honing survey questions that need to be taken

    # the amount helco's text size will decrease when he's thinking
    # must be <= 0
    helco_text_downsize = -15


    # ----- VARIABLES -----
    
    # TODO: determine this value procedurally
    # array of top three personnel from honing survey, in no particular order
    top_three_honed = [
        "aikha",
        "firewal",
        "plutoes"
    ]

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

    # dictionary for number of character points the player has achieved with each personnel
    # {personnel, points}
    character_points = {
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
    }
    


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

define n = Character("", kind=base_char) # narrator, required to render characters as unhighlighted whenever narration is occurring

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

transform disappear(y_offset = 70, duration = 0.5):
    parallel:
        easein duration yoffset y_offset
    parallel:
        linear duration matrixcolor BrightnessMatrix(-1.0)

define default_fade = Fade(1.0, 1.0, 1.0)