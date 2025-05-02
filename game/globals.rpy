# This file will contain global variables and constants

# Constants

init python:
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

    closeness = {
        "helco": 0,
        "aikha": 0,
        "firewal": 0,
        "jessie": 0,
        "plutoes": 0,
        "alex": 0,
        "chan": 0
    }
    day_number = 1


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

image jessie neutral = "images/jessie neutral.png"
image jessie sad = "images/jessie sad.png"
image jessie upset = "images/jessie upset.png"

image firewal neutral = "images/firewal neutral.png"

image helco neutral = "images/helco neutral.png"

image aikha neutral = "images/aikha neutral.png"

image plutoes neutral = "images/plutoes neutral.png"



# Characters

define base_char = Character("")

define jessie = Character("Dr. Jessie", kind=base_char, color="#ff6dcf")
define jessie_unknown = Character("???", kind=jessie)

define firewal = Character("Dr. Firewal", kind=base_char, color="#961e44")

define helco = Character("Dr. Helco", kind=base_char, color="#fffda1")

define aikha = Character("Dr. Aikha", kind=base_char, color="#8f76ff")

define plutoes = Character("Plutoes", kind=base_char, color="#62ff58")

define player = Character("[player_name]", kind=base_char)

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