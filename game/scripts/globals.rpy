# This file will contain global variables and constants

# Constants

init python:
    # ----- STATEMENTS -----
    import copy

    # chanegs the option of moving back in text
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! SET TO FALSE WHEN SHIPPING !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    config.rollback_enabled = True

    # when enabled,
    #   - skips intro
    #   - provides prompt to choose a specific event
    debug_mode = True

    # ----- CONSTANTS -----
    # the default pause times after certain punctuation marks
    # note to developers: prefix a dialogue line with /no_pause to disable these pauses for that line
    # default_text_speed = 30

    punctuation_pauses = {
        "comma": 0.2,
        "period": 0.4,
        "elipsis": 0.133,
        "exclamation": 0.4,
        "question": 0.4,
        "colon": 0.2,
        "semicolon": 0.2,
        "quotation": 0.2,
        "hyphen": 0.2,
    }
    

    # the default time for a standard sprite movement
    default_move_time = 0.7

    honing_survey_questions_threshold = 7 # number of honing survey questions that need to be taken

    # the amount helco's text size will decrease when he's thinking
    # must be <= 0
    helco_text_downsize = -10


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

    # dictionary for number of character points the player has achieved with each personnel, npc or otherwise, and if they have a route
    # {personnel, {"points": number, "has_route": boolean}}
    # to access a personnel's points, do characters["personnel"]["points"]
    characters = {
        "syg": {
            "points": 0,
            "has_route": True
        },
        "alex": {
            "points": 0,
            "has_route": True
        },
        "helco": {
            "points": 0,
            "has_route": True
        },
        "aikha": {
            "points": 0,
            "has_route": True
        },
        "firewal": {
            "points": 0,
            "has_route": True
        },
        "venture": {
            "points": 0,
            "has_route": True
        },
        "uriel": {
            "points": 0,
            "has_route": True
        },
        "ryz": {
            "points": 0,
            "has_route": True
        },
        "deceased": {
            "points": 0,
            "has_route": True
        },
        "chan": {
            "points": 0,
            "has_route": True
        },
        "hampter": {
            "points": 0,
            "has_route": True
        },
        "caffi": {
            "points": 0,
            "has_route": False
        },
        "jessie": {
            "points": 0,
            "has_route": False
        },
        "lee": {
            "points": 0,
            "has_route": False
        },
        "meme": {
            "points": 0,
            "has_route": False
        },
        "plutoes": {
            "points": 0,
            "has_route": False
        },
        "b6": {
            "points": 0,
            "has_route": False
        },
        "egg": {
            "points": 0,
            "has_route": False
        },
        "paul": {
            "points": 0,
            "has_route": False
        }
    }
    


# Player pronouns and names
define default_name = "Jakob"
define player_name = default_name
define player_sub = "they" # subject pronoun (he, she, they)
define player_sub_be = "they're" # subject pronoun + to be (he's, she's, they're)
define player_obj = "them" # object pronoun (him, her, them)
define player_pos_adj = "their" # possessive adjective  (his, her, their)
define player_pos_pro = "theirs" # possessive pronoun (his, hers, theirs)
define player_ref = "themself" # reflexive pronoun (himself, herself, themself)

# bgs

image bg hallway = "images/bgs/hallway.png"
image bg lounge = "images/bgs/hallway.png"
image bg office = "images/bgs/hallway.png"
image bg lobby = "images/bgs/hallway.png"
image bg venue = "images/bgs/venue.png"


# cgs will be defined in the respective event rpy

# other images

image black_screen = Solid("#000000", xsize = 2020, ysize = 1180, xpos = -50, ypos = -50, xanchor = 0.0, yanchor = 0.0) # for fade to black 

# return a Wal No. XX
# init python early:
#     def get_wal_num(no):
#         return Character(name=f"Wal No.{no}", kind=firewal)

# Transitions and transformations

transform appear(y_offset = 70, duration = 0.5, x_align = 0.5, y_align = 1.0):
    xalign x_align
    yalign y_align
    yoffset y_offset
    matrixcolor BrightnessMatrix(-1.0)

    parallel:
        easein duration yoffset 0
    parallel:
        linear duration matrixcolor BrightnessMatrix(0.0)

# usage: 
# show character with disappear
# (any dialogue)
# hide character
transform disappear(y_offset = 70, duration = 0.5):
    parallel:
        easein duration yoffset y_offset
    parallel:
        linear duration alpha 0.0

# shake transform
# usage:
#   use like a normal transform:
#       show helco at shake
#   to shake the screen, shake the master layer
#       show layer master at shake
#   can change strength to presets: show ryz at shake(preset = "strong")
#       presets are "strong", "weak", and none (leave empty)
#       can alternatively determine duration and strength manually (note that if both preset and duration/strength are defined,
#           preset takes priority)
transform shake(duration=0.5, strength=10.0, preset=""):
    function Shake(duration = duration, strength = strength, preset = preset)

init python:
    class Shake(object):
        def __init__(self, duration, strength, preset):
            if preset == "strong":
                self.duration = 1.0
                self.strength = 20.0
            elif present == "weak":
                self.duration = 0.25
                self.strength = 10.0
            else:
                self.duration = duration
                self.strength = strength
                
        
        def __call__(self, trans, shown, anim):
            factor = (self.duration - shown) / self.duration # the factor by which to multiply the shake
            if factor <= 0: # function ended
                trans.xoffset = 0
                trans.yoffset = 0
                return None
            else:
                # randomly choose a corner of the bounding box to move to
                # the bounding box is the box of side length 2 * self.strength * factor
                trans.xoffset = self.strength * factor * (renpy.random.choice([-1, 1])) 
                trans.yoffset = self.strength * factor * (renpy.random.choice([-1, 1]))
                return 0



define default_fade = Fade(1.0, 1.0, 1.0)
