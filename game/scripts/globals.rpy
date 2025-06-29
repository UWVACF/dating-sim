# This file will contain global variables and constants

# Constants

init python:
    # ----- STATEMENTS -----
    import copy

    # toggles the ability of scrolling dialogue backwards
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! SET TO FALSE WHEN SHIPPING !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    config.rollback_enabled = True

    # debug:
    #   - skips intro
    #   - provides prompt to choose a specific event
    # showcase_no_intro:
    #   - follows set pathing for events
    #   - skips intro
    # showcase_intro:
    #   - follows set pathing for events
    game_mode = "debug"


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
        },
        "moon": {
            "points": 0,
            "has_route": False
        },
    }
    

# Player pronouns and names
default default_name = "Jakob"
default player_name = default_name
default player_sub = "they" # subject pronoun (he, she, they)
default player_sub_be = "they're" # subject pronoun + to be (he's, she's, they're)
default player_obj = "them" # object pronoun (him, her, them)
default player_pos_adj = "their" # possessive adjective  (his, her, their)
default player_pos_pro = "theirs" # possessive pronoun (his, hers, theirs)
default player_ref = "themselves" # reflexive pronoun (himself, herself, themselves)
default player_verb_suffix = "" # either s or blank, used after a verb since that part changes (e.g. he puts vs they put)

# bgs

image bg hallway = "images/bgs/misc/hallway.png"
image bg lounge = "images/bgs/misc/lounge.png"
image bg lab = "images/bgs/misc/lab.png"
image bg office = "images/bgs/misc/hallway.png"
image bg lobby = "images/bgs/misc/hallway.png"
image bg venue = "images/bgs/misc/venue.png"
image bg door = "images/bgs/misc/door.png"
image bg meeting hall = "images/bgs/misc/meeting hall.png"
image bg meeting room = "images/bgs/misc/meeting room.png"
image bg room hall = "images/bgs/misc/room hall.png"
image bg containment = "images/bgs/misc/containment.png"
image bg court main = "images/bgs/misc/count_main.png"
image bg court side = "images/bgs/misc/count_side.png"

image bg aikha office = "images/bgs/aikha office/ai office.png"
image bg aikha office close = "images/bgs/aikha office/ai office close.png"
image bg aikha office dark close = "images/bgs/aikha office/ai office dark close.png"
image bg aikha office dark= "images/bgs/aikha office/ai office dark.png"
image bg aikha office leave= "images/bgs/aikha office/ai office leave.png"

# cgs will be defined in the respective event rpy

# other images and transforms related to them

# the basic transform for 2120 x 1280 overlays
transform base_overlay_transform:
    xanchor 0.0
    yanchor 0.0
    xpos -100
    ypos -100


transform white_to_red:
    matrixcolor Matrix([1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0])

transform white_to_green:
    matrixcolor Matrix([0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0])

transform white_to_black:
    matrixcolor Matrix([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0])

transform white_to_orange:
    matrixcolor Matrix([1.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0])

image black_screen = Solid("#000000", xsize = 2020, ysize = 1180, xpos = -50, ypos = -50, xanchor = 0.0, yanchor = 0.0) # for fade to black 
image white_screen = Solid("#ffffff", xsize = 2020, ysize = 1180, xpos = -50, ypos = -50, xanchor = 0.0, yanchor = 0.0)
image yellow_screen = Solid("#fff41d", xsize = 2020, ysize = 1180, xpos = -50, ypos = -50, xanchor = 0.0, yanchor = 0.0)


image haze white = At("images/day events/haze white.png", base_overlay_transform)
image haze white strong = At("images/day events/haze white strong.png", base_overlay_transform)
image haze red = At("haze white", white_to_red)
image haze red strong = At("haze white strong", white_to_red)
image haze green = At("haze white", white_to_green)
image haze green strong = At("haze white strong", white_to_green)
image haze black = At("haze white", white_to_black)
image haze black strong = At("haze white strong", white_to_black)
image haze orange = At("haze white", white_to_orange)
image haze orange strong = At("haze white", white_to_orange)


# return a Wal No. XX
# init python early:
#     def get_wal_num(no):
#         return Character(name=f"Wal No.{no}", kind=firewal)

# Transitions and transformations

# causes the character to rise up slightly and fade in from black
# usage:
#   show character at appear
# parameters (all optional):
#   x_align: the horizontal alignment of the character, with 0.0 being left, 0.5 being center and 1.0 being right
#               probably the only parameter you will edit
#   y_offset: how low the sprite starts when appearing, in px
#   duration: how long the transition takes, in seconds
#   y_align: the vertical alignment of the character, with 0.0 being the top, 0.5 being the center and 1.0 being the bottom
transform appear(x_align = 0.5, y_offset = 70, duration = 0.5, y_align = 1.0):
    xalign x_align
    yalign y_align
    yoffset y_offset
    matrixcolor BrightnessMatrix(-1.0)

    parallel:
        easein duration yoffset 0
    parallel:
        linear duration matrixcolor BrightnessMatrix(0.0)

# causes the character to lower slightly and fade out
# usage: 
#   show character at disappear
#   (any dialogue)
#   hide character
# parameters (all optional):
#   y_offset: how low the sprite will sink to, in px
#   duration: how long the sprite takes to complete the animation
transform disappear(y_offset = 70, duration = 0.5):
    parallel:
        easein duration yoffset y_offset
    parallel:
        linear duration alpha 0.0

# moves the character to the specified xalign after the specified duration
# usage:
#   show character at move_to(x_align = <VALUE>)
# parameters (all optional):
#   x_align: the horizontal alignment of the character
#   duration: how long the character will take to move
transform move_to(x_align = 0.5, duration = default_move_time):
    linear duration xalign x_align

# shakes the given sprite or layer randomly, optionally persisting at max strength for some time before diminishing towards the end
# usage:
#   use like a normal transform:
#       show helco at shake
#   to shake the screen, shake the master layer
#       show layer master at shake
# parameters:
#   duration: how long the shake will last, not including persist time
#   strength: the max strength of the shake, measured in pixels of offset
#   preset: sets predefined values of duration and strength. will override duration and strength if set. can be set to:
#       "strong"
#       "weak"
#       "rumble" (recommended if persist)
#   persist: how long the shake will last WITHOUT DIMINISHING. happens at the start of the shake, and does not run down duration time
# example:
#   show layer master at shake(duration = 3.0, strength = 10.0, persist = 1.0)
#       this will shake the screen at max strength (10px displacement) for 1.0 seconds before fading out over the course of of 3.0 seconds
transform shake(duration=0.5, strength=10.0, preset="", persist=0.0):
    function Shake(duration = duration, strength = strength, preset = preset, persist = persist)

init python:
    class Shake(object):
        def __init__(self, duration, strength, preset, persist):
            if preset == "strong":
                self.duration = 1.0
                self.strength = 20.0
            elif preset == "weak":
                self.duration = 0.25
                self.strength = 10.0
            elif preset == "rumble":
                self.duration = 0.5
                self.strength = 2.0
            else:
                self.duration = duration
                self.strength = strength
            self.persist = persist
        
        def __call__(self, trans, shown, anim):
            factor = min(1.0, (self.duration - shown + self.persist) / self.duration) # the factor by which to multiply the shake
            if factor <= 0: # function ended
                trans.xoffset = 0
                trans.yoffset = 0
                del self
                return None
            else:
                # randomly choose a corner of the bounding box to move to
                # the bounding box is the box of side length 2 * self.strength * factor
                trans.xoffset = self.strength * factor * (renpy.random.choice([-1, 1])) 
                trans.yoffset = self.strength * factor * (renpy.random.choice([-1, 1]))
                return 0

define default_fade = Fade(1.0, 1.0, 1.0)
