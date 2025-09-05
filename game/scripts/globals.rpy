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
        "elipsis": 0.2,
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
    current_bg = ""

    def new_show(attr, layer='master', what=None, zorder=0, tag=None, **kwargs):
        global current_bg
        if attr and attr[0] == "bg":
            current_bg = attr[1].capitalize()
        return renpy.show(attr, layer=layer, what=what, zorder=zorder, tag=tag, **kwargs)

    config.show = new_show
    
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
default player_be = "are" # player's to be
default player_be_past = "were" # player's to be, past tense

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
image bg teaparty meeting = "images/bgs/misc/tea party meeting.png"

image bg office desk close = "images/bgs/office/office desk close.png"
image bg office desk = "images/bgs/office/office desk.png"
image bg office close = "images/bgs/office/office close.png"
image bg office enter = "images/bgs/office/office enter.png"
image bg office monitor = "images/bgs/office/office monitor.png"
image bg office side = "images/bgs/office/office side.png"
image bg office sit = "images/bgs/office/office sit.png"

image bg lobby entrence = "images/bgs/lobby/lobby entrence.png"
image bg lobby wall = "images/bgs/lobby/lobby wall.png"

image bg cubicle inside = "images/bgs/cubicle/cubicle inside.png"
image bg cubicle outside = "images/bgs/cubicle/cubicle outside.png"

image bg caf counter = "images/bgs/caf/caf counter.png"
image bg caf opening = "images/bgs/caf/caf opening.png"
image bg caf seats = "images/bgs/caf/caf seats.png"
image bg caf open = "images/bgs/caf/caf open.png"
image bg caf window = "images/bgs/caf/caf window.png"

image bg aikha office = "images/bgs/aikha office/ai office.png"
image bg aikha office close = "images/bgs/aikha office/ai office close.png"
image bg aikha office dark close = "images/bgs/aikha office/ai office dark close.png"
image bg aikha office dark= "images/bgs/aikha office/ai office dark.png"
image bg aikha office leave= "images/bgs/aikha office/ai office leave.png"

image bg lounge center couch = "images/bgs/lounge/lounge center couch.png"
image bg lounge center kitchen = "images/bgs/lounge/lounge center kitchen.png"
image bg lounge center tv = "images/bgs/lounge/lounge center tv.png"
image bg lounge couch pan = "images/bgs/lounge/lounge couch pan.png"
image bg lounge couch sit = "images/bgs/lounge/lounge couch sit.png"
image bg lounge entrance pan left = "images/bgs/lounge/lounge entrance pan left.png"
image bg lounge entrance pan right = "images/bgs/lounge/lounge entrance pan right.png"
image bg lounge entrance pan middle = "images/bgs/lounge/lounge entrance pan middle.png"
image bg lounge fridge = "images/bgs/lounge/lounge fridge.png"
image bg lounge island = "images/bgs/lounge/lounge island.png"
image bg lounge kitchen cook = "images/bgs/lounge/lounge kitchen cook.png"
image bg lounge kitchen door = "images/bgs/lounge/lounge kitchen door.png"
image bg lounge kitchen sit = "images/bgs/lounge/lounge kitchen sit.png"
image bg lounge oven = "images/bgs/lounge/lounge oven.png"
image bg lounge sink = "images/bgs/lounge/lounge sink.png"
image bg lounge table sit = "images/bgs/lounge/lounge table sit.png"
image bg lounge table = "images/bgs/lounge/lounge table.png"
image bg lounge tv door = "images/bgs/lounge/ lounge tv door.png"
image bg lounge tv sit = "images/bgs/lounge/ lounge tv sit.png"

image bg clinic bed = "images/bgs/clinic/clinic bed.png"
image bg clinic bedside = "images/bgs/clinic/clinic bedside.png"
image bg clinic checkup bed = "images/bgs/clinic/clinic checkup bed.png"
image bg clinic checkup bedside door = "images/bgs/clinic/clinic checkup bedside door.png"
image bg clinic checkup bedside = "images/bgs/clinic/clinic checkup bedside.png"
image bg clinic checkup computer = "images/bgs/clinic/clinic checkup computer.png"
image bg clinic checkup door = "images/bgs/clinic/clinic checkup door.png"
image bg clinic checkup enter = "images/bgs/clinic/clinic checkup enter.png"
image bg clinic checkup full = "images/bgs/clinic/clinic checkup full.png"
image bg clinic checkup pan = "images/bgs/clinic/clinic checkup pan.png"
image bg clinic containment capture = "images/bgs/clinic/clinic containment capture.png"
image bg clinic containment door = "images/bgs/clinic/clinic containment door.png"
image bg clinic containment window = "images/bgs/clinic/clinic containment window.png"
image bg clinic pan back = "images/bgs/clinic/clinic pan back.png"
image bg clinic pan front = "images/bgs/clinic/clinic pan front.png"
image bg clinic pan left = "images/bgs/clinic/clinic pan left.png"
image bg clinic pan right = "images/bgs/clinic/clinic pan right.png"
image bg clinic reception computer = "images/bgs/clinic/clinic reception computer.png"
image bg clinic reception left = "images/bgs/clinic/clinic reception left.png"
image bg clinic reception = "images/bgs/clinic/clinic reception.png"

image bg observation = "images/bgs/observation/observation.png"
image bg observation far = "images/bgs/observation/observation far.png"
image bg observation close = "images/bgs/observation/observation close.png"

image bg containment cam = "images/bgs/containment/containment cam.png"
image bg containment corner = "images/bgs/containment/containment corner.png"
image bg containment door = "images/bgs/containment/containment door.png"
image bg containment mirror = "images/bgs/containment/containment mirror.png"
image bg containment overall = "images/bgs/containment/containment overall.png"
image bg containment side = "images/bgs/containment/containment side.png"

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

# i think it's pretty self explanatory
image explosion:
    "images/cgs/explosion/frame_00_delay-0.1s.png"
    pause 0.1
    "images/cgs/explosion/frame_01_delay-0.1s.png"
    pause 0.1
    "images/cgs/explosion/frame_02_delay-0.1s.png"
    pause 0.1
    "images/cgs/explosion/frame_03_delay-0.1s.png"
    pause 0.1
    "images/cgs/explosion/frame_04_delay-0.1s.png"
    pause 0.1
    "images/cgs/explosion/frame_05_delay-0.1s.png"
    pause 0.1
    "images/cgs/explosion/frame_06_delay-0.1s.png"
    pause 0.1
    "images/cgs/explosion/frame_07_delay-0.1s.png"
    pause 0.1
    "images/cgs/explosion/frame_08_delay-0.1s.png"
    pause 0.1
    "images/cgs/explosion/frame_09_delay-0.1s.png"
    pause 0.1
    "images/cgs/explosion/frame_10_delay-0.1s.png"
    pause 0.1
    "images/cgs/explosion/frame_11_delay-0.1s.png"
    pause 0.1
    "images/cgs/explosion/frame_12_delay-0.1s.png"
    pause 0.1
    "images/cgs/explosion/frame_13_delay-0.1s.png"
    pause 0.1
    "images/cgs/explosion/frame_14_delay-0.1s.png"
    pause 0.1
    "images/cgs/explosion/frame_15_delay-0.1s.png"
    pause 0.1
    "images/cgs/explosion/frame_16_delay-0.1s.png"
    pause 0.1
    Solid("#00000000")

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
transform appear(x_align = 0.5, y_offset = 70, duration = 0.5, y_align = 1.0, final_brightness = 0.0):
    xalign x_align
    yalign y_align
    yoffset y_offset
    matrixcolor BrightnessMatrix(-1.0)
    alpha 1.0

    parallel:
        easein duration yoffset 0
    parallel:
        linear duration matrixcolor BrightnessMatrix(final_brightness)

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

transform shake:
    function shake_obj.start

transform null_transform: # do nothing
    alpha 1.0

define default_fade = Fade(1.0, 1.0, 1.0)