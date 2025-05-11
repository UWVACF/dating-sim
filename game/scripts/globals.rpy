# This file will contain global variables and constants

# Constants

init python:
    # ----- STATEMENTS -----
    import copy
    random.seed() # makes a new seed to ensure randomness

    # disables the option of moving back in text
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! SET TO FALSE WHEN SHIPPING !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    config.rollback_enabled = True

    # when enabled,
    #   - skips intro
    #   - provides prompt to choose a specific event
    debug_mode = True

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
    hyphen_pause = comma_pause

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
    # to access a personnel's points, do characters["personnel"][0]
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
        "meem": {
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

# Image transform
transform base_char_transform(x = 666, y = 1000, xoff = 0, yoff = 0):
    xsize x
    ysize y
    xoffset xoff
    yoffset yoff

# Personnel images
image jessie = At("images/jessie/jessie neutral.png", sprite_highlight("jessie"))
image jessie neutral = At("images/jessie/jessie neutral.png", sprite_highlight("jessie"))
image jessie talk = At("images/jessie/jessie talk.png", sprite_highlight("jessie"))
image jessie happy = At("images/jessie/jessie happy.png", sprite_highlight("jessie"))
image jessie sad = At("images/jessie/jessie sad.png", sprite_highlight("jessie"))
image jessie upset = At("images/jessie/jessie upset.png", sprite_highlight("jessie"))
image jessie surprise = At("images/jessie/jessie surprise.png", sprite_highlight("jessie"))
image jessie panic = At("images/jessie/jessie panic.png", sprite_highlight("jessie"))
image jessie fury = At("images/jessie/jessie fury.png", sprite_highlight("jessie"))
image jessie pensive = At("images/jessie/jessie pensive.png", sprite_highlight("jessie"))
image jessie unique = At("images/jessie/jessie unique.png", sprite_highlight("jessie"))

image aikha = At("images/aikha/aikha neutral.png", sprite_highlight("aikha"))
image aikha neutral = At("images/aikha/aikha neutral.png", sprite_highlight("aikha"))
image aikha talk = At("images/aikha/aikha talk.png", sprite_highlight("aikha"))
image aikha happy = At("images/aikha/aikha happy.png", sprite_highlight("aikha"))
image aikha sad = At("images/aikha/aikha sad.png", sprite_highlight("aikha"))
image aikha upset = At("images/aikha/aikha upset.png", sprite_highlight("aikha"))
image aikha surprise = At("images/aikha/aikha surprise.png", sprite_highlight("aikha"))
image aikha panic = At("images/aikha/aikha panic.png", sprite_highlight("aikha"))
image aikha fury = At("images/aikha/aikha fury.png", sprite_highlight("aikha"))
image aikha pensive = At("images/aikha/aikha pensive.png", sprite_highlight("aikha"))
image aikha unique = At("images/aikha/aikha unique.png", sprite_highlight("aikha"))

image alex = At("images/alex/alex neutral.png", sprite_highlight("alex"))
image alex neutral = At("images/alex/alex neutral.png", sprite_highlight("alex"))
image alex talk = At("images/alex/alex talk.png", sprite_highlight("alex"))
image alex happy = At("images/alex/alex happy.png", sprite_highlight("alex"))
image alex sad = At("images/alex/alex sad.png", sprite_highlight("alex"))
image alex upset = At("images/alex/alex upset.png", sprite_highlight("alex"))
image alex surprise = At("images/alex/alex surprise.png", sprite_highlight("alex"))
image alex panic = At("images/alex/alex panic.png", sprite_highlight("alex"))
image alex fury = At("images/alex/alex fury.png", sprite_highlight("alex"))
image alex pensive = At("images/alex/alex pensive.png", sprite_highlight("alex"))
image alex unique = At("images/alex/alex unique.png", sprite_highlight("alex"))

image helco = At("images/helco/helco neutral.png", sprite_highlight("helco"))
image helco neutral = At("images/helco/helco neutral.png", sprite_highlight("helco"))
image helco talk = At("images/helco talk.png", sprite_highlight("helco"))
image helco happy = At("images/helco/helco happy.png", sprite_highlight("helco"))
image helco sad = At("images/helco sad.png", sprite_highlight("helco"))
image helco upset = At("images/helco upset.png", sprite_highlight("helco"))
image helco surprise = At("images/helco surprise.png", sprite_highlight("helco"))
image helco panic = At("images/helco panic.png", sprite_highlight("helco"))
image helco fury = At("images/helco fury.png", sprite_highlight("helco"))
image helco pensive = At("images/helco pensive.png", sprite_highlight("helco"))
image helco unique = At("images/helco unique.png", sprite_highlight("helco"))

image ryz = At("images/ryz/ryz neutral.png", sprite_highlight("ryz"))
image ryz neutral = At("images/ryz/ryz neutral.png", sprite_highlight("ryz"))
image ryz talk = At("images/ryz/ryz talk.png", sprite_highlight("ryz"))
image ryz happy = At("images/ryz/ryz happy.png", sprite_highlight("ryz"))
image ryz sad = At("images/ryz/ryz sad.png", sprite_highlight("ryz"))
image ryz upset = At("images/ryz/ryz upset.png", sprite_highlight("ryz"))
image ryz surprise = At("images/ryz/ryz surprise.png", sprite_highlight("ryz"))
image ryz panic = At("images/ryz/ryz panic.png", sprite_highlight("ryz"))
image ryz fury = At("images/ryz/ryz fury.png", sprite_highlight("ryz"))
image ryz pensive = At("images/ryz/ryz pensive.png", sprite_highlight("ryz"))
image ryz unique = At("images/ryz/ryz unique.png", sprite_highlight("ryz"))

image roose = At("images/ryz/roose neutral.png", sprite_highlight("roose"), base_char_transform(x = 400, y = 600, yoff = -100))
image roose neutral = At("images/ryz/roose neutral.png", sprite_highlight("roose"), base_char_transform(x = 400, y = 600, yoff = -100))
image roose talk = At("images/ryz/roose talk.png", sprite_highlight("roose"), base_char_transform(x = 400, y = 600, yoff = -100))
image roose upset = At("images/ryz/roose upset.png", sprite_highlight("roose"), base_char_transform(x = 400, y = 600, yoff = -100))

image uriel = At("images/uriel/uriel neutral.png", sprite_highlight("uriel"))
image uriel neutral = At("images/uriel/uriel neutral.png", sprite_highlight("uriel"))
image uriel talk = At("images/uriel/uriel talk.png", sprite_highlight("uriel"))
image uriel happy = At("images/uriel/uriel happy.png", sprite_highlight("uriel"))
image uriel sad = At("images/uriel/uriel sad.png", sprite_highlight("uriel"))
image uriel upset = At("images/uriel/uriel upset.png", sprite_highlight("uriel"))
image uriel surprise = At("images/uriel/uriel surprise.png", sprite_highlight("uriel"))
image uriel panic = At("images/uriel/uriel panic.png", sprite_highlight("uriel"))
image uriel fury = At("images/uriel/uriel fury.png", sprite_highlight("uriel"))
image uriel pensive = At("images/uriel/uriel pensive.png", sprite_highlight("uriel"))
image uriel unique = At("images/uriel/uriel unique.png", sprite_highlight("uriel"))

image deceased = At("images/deceased/deceased neutral.png", sprite_highlight("deceased"))
image deceased neutral = At("images/deceased/deceased neutral.png", sprite_highlight("deceased"))
image deceased talk = At("images/deceased/deceased talk.png", sprite_highlight("deceased"))
image deceased happy = At("images/deceased/deceased happy.png", sprite_highlight("deceased"))
image deceased sad = At("images/deceased/deceased sad.png", sprite_highlight("deceased"))
image deceased upset = At("images/deceased/deceased upset.png", sprite_highlight("deceased"))
image deceased surprise = At("images/deceased/deceased surprise.png", sprite_highlight("deceased"))
image deceased panic = At("images/deceased/deceased panic.png", sprite_highlight("deceased"))
image deceased fury = At("images/deceased/deceased fury.png", sprite_highlight("deceased"))
image deceased pensive = At("images/deceased/deceased pensive.png", sprite_highlight("deceased"))
image deceased unique = At("images/deceased/deceased unique.png", sprite_highlight("deceased"))

image lee = At("images/lee/lee neutral.png", sprite_highlight("lee"))
image lee neutral = At("images/lee/lee neutral.png", sprite_highlight("lee"))
image lee talk = At("images/lee/lee talk.png", sprite_highlight("lee"))
image lee happy = At("images/lee/lee happy.png", sprite_highlight("lee"))
image lee sad = At("images/lee/lee sad.png", sprite_highlight("lee"))
image lee upset = At("images/lee/lee upset.png", sprite_highlight("lee"))
image lee surprise = At("images/lee/lee surprise.png", sprite_highlight("lee"))
image lee panic = At("images/lee/lee panic.png", sprite_highlight("lee"))
image lee fury = At("images/lee/lee fury.png", sprite_highlight("lee"))
image lee pensive = At("images/lee/lee pensive.png", sprite_highlight("lee"))
image lee unique = At("images/lee/lee unique.png", sprite_highlight("lee"))

image firewal = At("images/firewal/firewal neutral.png", sprite_highlight("firewal"))
image firewal neutral = At("images/firewal/firewal neutral.png", sprite_highlight("firewal"))
image firewal talk = At("images/firewal/firewal talk.png", sprite_highlight("firewal"))
image firewal happy = At("images/firewal/firewal happy.png", sprite_highlight("firewal"))
image firewal sad = At("images/firewal/firewal sad.png", sprite_highlight("firewal"))
image firewal upset = At("images/firewal/firewal upset.png", sprite_highlight("firewal"))
image firewal surprise = At("images/firewal/firewal surprise.png", sprite_highlight("firewal"))
image firewal panic = At("images/firewal/firewal panic.png", sprite_highlight("firewal"))
image firewal fury = At("images/firewal/firewal fury.png", sprite_highlight("firewal"))
image firewal pensive = At("images/firewal/firewal pensive.png", sprite_highlight("firewal"))
image firewal unique = At("images/firewal/firewal unique.png", sprite_highlight("firewal"))

image chan = At("images/chan/chan neutral.png", sprite_highlight("chan"))
image chan neutral = At("images/chan/chan neutral.png", sprite_highlight("chan"))
image chan talk = At("images/chan/chan talk.png", sprite_highlight("chan"))
image chan happy = At("images/chan/chan happy.png", sprite_highlight("chan"))
image chan sad = At("images/chan/chan sad.png", sprite_highlight("chan"))
image chan upset = At("images/chan/chan upset.png", sprite_highlight("chan"))
image chan surprise = At("images/chan/chan surprise.png", sprite_highlight("chan"))
image chan panic = At("images/chan/chan panic.png", sprite_highlight("chan"))
image chan fury = At("images/chan/chan fury.png", sprite_highlight("chan"))
image chan pensive = At("images/chan/chan pensive.png", sprite_highlight("chan"))
image chan unique = At("images/chan/chan unique.png", sprite_highlight("chan"))

image syg = At("images/syg/syg neutral.png", sprite_highlight("syg"))
image syg neutral = At("images/syg/syg neutral.png", sprite_highlight("syg"))
image syg talk = At("images/syg/syg talk.png", sprite_highlight("syg"))
image syg happy = At("images/syg/syg happy.png", sprite_highlight("syg"))
image syg sad = At("images/syg/syg sad.png", sprite_highlight("syg"))
image syg upset = At("images/syg/syg upset.png", sprite_highlight("syg"))
image syg surprise = At("images/syg/syg surprise.png", sprite_highlight("syg"))
image syg panic = At("images/syg/syg panic.png", sprite_highlight("syg"))
image syg fury = At("images/syg/syg fury.png", sprite_highlight("syg"))
image syg pensive = At("images/syg/syg pensive.png", sprite_highlight("syg"))
image syg unique = At("images/syg/syg unique.png", sprite_highlight("syg"))

image caffi = At("images/caffi/caffi neutral.png", sprite_highlight("caffi"))
image caffi neutral = At("images/caffi/caffi neutral.png", sprite_highlight("caffi"))
image caffi talk = At("images/caffi/caffi talk.png", sprite_highlight("caffi"))
image caffi happy = At("images/caffi/caffi happy.png", sprite_highlight("caffi"))
image caffi sad = At("images/caffi/caffi sad.png", sprite_highlight("caffi"))
image caffi upset = At("images/caffi/caffi upset.png", sprite_highlight("caffi"))
image caffi surprise = At("images/caffi/caffi surprise.png", sprite_highlight("caffi"))
image caffi panic = At("images/caffi/caffi panic.png", sprite_highlight("caffi"))
image caffi fury = At("images/caffi/caffi fury.png", sprite_highlight("caffi"))
image caffi pensive = At("images/caffi/caffi pensive.png", sprite_highlight("caffi"))
image caffi unique = At("images/caffi/caffi unique.png", sprite_highlight("caffi"))

image paul = At("images/paul/paul neutral.png", sprite_highlight("paul"))
image paul neutral = At("images/paul/paul neutral.png", sprite_highlight("paul"))
image paul talk = At("images/paul/paul talk.png", sprite_highlight("paul"))
image paul happy = At("images/paul/paul happy.png", sprite_highlight("paul"))
image paul sad = At("images/paul/paul sad.png", sprite_highlight("paul"))
image paul upset = At("images/paul/paul upset.png", sprite_highlight("paul"))
image paul surprise = At("images/paul/paul surprise.png", sprite_highlight("paul"))
image paul panic = At("images/paul/paul panic.png", sprite_highlight("paul"))
image paul fury = At("images/paul/paul fury.png", sprite_highlight("paul"))
image paul pensive = At("images/paul/paul pensive.png", sprite_highlight("paul"))
image paul unique = At("images/paul/paul unique.png", sprite_highlight("paul"))

image plutoes = At("images/plutoes/plutoes neutral.png", sprite_highlight("plutoes"))
image plutoes neutral = At("images/plutoes/plutoes neutral.png", sprite_highlight("plutoes"))
image plutoes talk = At("images/plutoes/plutoes talk.png", sprite_highlight("plutoes"))
image plutoes happy = At("images/plutoes/plutoes happy.png", sprite_highlight("plutoes"))
image plutoes sad = At("images/plutoes/plutoes sad.png", sprite_highlight("plutoes"))
image plutoes upset = At("images/plutoes/plutoes upset.png", sprite_highlight("plutoes"))
image plutoes surprise = At("images/plutoes/plutoes surprise.png", sprite_highlight("plutoes"))
image plutoes panic = At("images/plutoes/plutoes panic.png", sprite_highlight("plutoes"))
image plutoes fury = At("images/plutoes/plutoes fury.png", sprite_highlight("plutoes"))
image plutoes pensive = At("images/plutoes/plutoes pensive.png", sprite_highlight("plutoes"))
image plutoes unique = At("images/plutoes/plutoes unique.png", sprite_highlight("plutoes"))

image venture = At("images/venture/venture neutral.png", sprite_highlight("venture"))
image venture neutral = At("images/venture/venture neutral.png", sprite_highlight("venture"))
image venture talk = At("images/venture/venture talk.png", sprite_highlight("venture"))
image venture happy = At("images/venture/venture happy.png", sprite_highlight("venture"))
image venture sad = At("images/venture/venture sad.png", sprite_highlight("venture"))
image venture upset = At("images/venture/venture upset.png", sprite_highlight("venture"))
image venture surprise = At("images/venture/venture surprise.png", sprite_highlight("venture"))
image venture panic = At("images/venture/venture panic.png", sprite_highlight("venture"))
image venture fury = At("images/venture/venture fury.png", sprite_highlight("venture"))
image venture pensive = At("images/venture/venture pensive.png", sprite_highlight("venture"))
image venture unique = At("images/venture/venture unique.png", sprite_highlight("venture"))

image b6 = At("images/b6/b6 neutral.png", sprite_highlight("b6"))
image b6 neutral = At("images/b6/b6 neutral.png", sprite_highlight("b6"))
image b6 talk = At("images/b6/b6 talk.png", sprite_highlight("b6"))
image b6 happy = At("images/b6/b6 happy.png", sprite_highlight("b6"))
image b6 sad = At("images/b6/b6 sad.png", sprite_highlight("b6"))
image b6 upset = At("images/b6/b6 upset.png", sprite_highlight("b6"))
image b6 surprise = At("images/b6/b6 surprise.png", sprite_highlight("b6"))
image b6 panic = At("images/b6/b6 panic.png", sprite_highlight("b6"))
image b6 fury = At("images/b6/b6 fury.png", sprite_highlight("b6"))
image b6 pensive = At("images/b6/b6 pensive.png", sprite_highlight("b6"))
image b6 unique = At("images/b6/b6 unique.png", sprite_highlight("b6"))

image meem = At("images/meem/meem neutral.png", sprite_highlight("meem"))
image meem neutral = At("images/meem/meem neutral.png", sprite_highlight("meem"))
image meem talk = At("images/meem/meem talk.png", sprite_highlight("meem"))
image meem happy = At("images/meem/meem happy.png", sprite_highlight("meem"))
image meem sad = At("images/meem/meem sad.png", sprite_highlight("meem"))
image meem upset = At("images/meem/meem upset.png", sprite_highlight("meem"))
image meem surprise = At("images/meem/meem surprise.png", sprite_highlight("meem"))
image meem panic = At("images/meem/meem panic.png", sprite_highlight("meem"))
image meem fury = At("images/meem/meem fury.png", sprite_highlight("meem"))
image meem pensive = At("images/meem/meem pensive.png", sprite_highlight("meem"))
image meem unique = At("images/meem/meem unique.png", sprite_highlight("meem"))

image moon = At("images/moon/moon neutral.png", sprite_highlight("moon"))
image moon neutral = At("images/moon/moon neutral.png", sprite_highlight("moon"))
image moon talk = At("images/moon/moon talk.png", sprite_highlight("moon"))
image moon happy = At("images/moon/moon happy.png", sprite_highlight("moon"))
image moon sad = At("images/moon/moon sad.png", sprite_highlight("moon"))
image moon upset = At("images/moon/moon upset.png", sprite_highlight("moon"))
image moon surprise = At("images/moon/moon surprise.png", sprite_highlight("moon"))
image moon panic = At("images/moon/moon panic.png", sprite_highlight("moon"))
image moon fury = At("images/moon/moon fury.png", sprite_highlight("moon"))
image moon pensive = At("images/moon/moon pensive.png", sprite_highlight("moon"))
image moon unique = At("images/moon/moon unique.png", sprite_highlight("moon"))

image egg = At("images/egg/egg neutral.png", sprite_highlight("egg"))
image egg neutral = At("images/egg/egg neutral.png", sprite_highlight("egg"))
image egg talk = At("images/egg/egg talk.png", sprite_highlight("egg"))
image egg happy = At("images/egg/egg happy.png", sprite_highlight("egg"))
image egg sad = At("images/egg/egg sad.png", sprite_highlight("egg"))
image egg upset = At("images/egg/egg upset.png", sprite_highlight("egg"))
image egg surprise = At("images/egg/egg surprise.png", sprite_highlight("egg"))
image egg panic = At("images/egg/egg panic.png", sprite_highlight("egg"))
image egg fury = At("images/egg/egg fury.png", sprite_highlight("egg"))
image egg pensive = At("images/egg/egg pensive.png", sprite_highlight("egg"))
image egg unique = At("images/egg/egg unique.png", sprite_highlight("egg"))

image hampter = At("images/hampter/hampter neutral.png", sprite_highlight("hampter"))
image hampter neutral = At("images/hampter/hampter neutral.png", sprite_highlight("hampter"))
image hampter talk = At("images/hampter/hampter talk.png", sprite_highlight("hampter"))
image hampter happy = At("images/hampter/hampter happy.png", sprite_highlight("hampter"))
image hampter sad = At("images/hampter/hampter sad.png", sprite_highlight("hampter"))
image hampter upset = At("images/hampter/hampter upset.png", sprite_highlight("hampter"))
image hampter surprise = At("images/hampter/hampter surprise.png", sprite_highlight("hampter"))
image hampter panic = At("images/hampter/hampter panic.png", sprite_highlight("hampter"))
image hampter fury = At("images/hampter/hampter fury.png", sprite_highlight("hampter"))
image hampter pensive = At("images/hampter/hampter pensive.png", sprite_highlight("hampter"))
image hampter unique = At("images/hampter/hampter unique.png", sprite_highlight("hampter"))

# Characters
define base_char = Character("", callback=name_callback)

define jessie = Character("Dr. Jessie", kind=base_char, color="#ff6dcf", cb_name="jessie", image="jessie")
define jessie_unknown = Character("???", kind=jessie)

define firewal = Character("Dr. Firewal", kind=base_char, color="#961e44", cb_name="firewal", image="firewal")

define helco = Character("Dr. Helco", kind=base_char, color="#fffda1", cb_name="helco", image="helco")

define aikha = Character("Dr. Aikha", kind=base_char, color="#8f76ff", cb_name="aikha", image="aikha")

define plutoes = Character("Plutoes", kind=base_char, color="#62ff58", cb_name="plutoes", image="plutoes")

define alex = Character("Dr. Alex", kind=base_char, color="#000000", cb_name="alex", image="alex")

define deceased = Character("Dr. Deceased", kind=base_char, color="#894bb2", cb_name="deceased", image="deceased")

define syg = Character("Dr. Syg", kind=base_char, color="#6e7384", cb_name="syg", image="syg")

define chan = Character("Dr. Chan", kind=base_char, color="#46bdc6", cb_name="chan", image="chan")
define ethy = Character("Ethy", kind=chan, color="#000000")

define lee = Character("Dr. Lee", kind=base_char, color="#ff0000", cb_name="lee", image="lee")
define lee_unknown = Character("???", kind=lee)

define b6 = Character("b6c5b6", kind=base_char, color="#364036", cb_name="b6", image="b6")

define paul = Character("Paul Demure Johnson", kind=base_char, color="#6e7f55", cb_name="paul", image="paul")

define uriel = Character("Uriel", kind=base_char, color="#acced2", cb_name="uriel", image="uriel")

define egg = Character("Harvard Egg", kind=base_char, color="#ff8561", cb_name="egg", image="egg")

define caffi = Character("\"Dr\" Caffi", kind=base_char, color="#000000", cb_name="caffi", image="caffi") # change colour

define moon = Character("Hustlemoon", kind=base_char, color="#caff85", cb_name="moon", image="moon")

define hampter = Character("Hampter", kind=base_char, color="#6b78ac", cb_name="hampter", image="hampter")

define meem = Character("Meme", kind=base_char, color="#e4f8fe", cb_name="meem", image="meem") # change colour

define ryz = Character("Dr. Ryz", kind=base_char, color="#f9be82", cb_name="ryz", image="ryz")
define roose = Character("Roose", kind=ryz, image="roose", cb_name="roose")

define venture = Character("Dr. Wayne Venture", kind=base_char, color="#8f7557", cb_name="venture", image="venture") # change colour

define player = Character("[player_name]", kind=base_char, color="#444444", cb_name="player")


define n = Character("", kind=base_char) # narrator, required to unhighlight characters whenever narration is occurring

# other images we need
image black_screen = Solid("#000000", xsize = 2120, ysize = 1280, xpos = -100, ypos = -100, xanchor = 0.0, yanchor = 0.0) # for fade to black 

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

define default_fade = Fade(1.0, 1.0, 1.0)

transform move_to(x_align = 0.5, duration = default_move_time):
    linear duration xalign x_align