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
    default_text_speed = 30

    punctuation_pauses = {
        "comma": 0.2 * default_text_speed / preferences.text_cps,
        "period": 0.4 * default_text_speed / preferences.text_cps,
        "elipsis": 0.133 * default_text_speed / preferences.text_cps,
        "exclamation": 0.4 * default_text_speed / preferences.text_cps,
        "question": 0.4 * default_text_speed / preferences.text_cps,
        "colon": 0.2 * default_text_speed / preferences.text_cps,
        "semicolon": 0.2 * default_text_speed / preferences.text_cps,
        "quotation": 0.2 * default_text_speed / preferences.text_cps,
        "hyphen": 0.2 * default_text_speed / preferences.text_cps,
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
image jessie = At("images/personnel/jessie/jessie neutral.png", sprite_highlight("jessie"))
image jessie neutral = At("images/personnel/jessie/jessie neutral.png", sprite_highlight("jessie"))
image jessie talk = At("images/personnel/jessie/jessie talk.png", sprite_highlight("jessie"))
image jessie happy = At("images/personnel/jessie/jessie happy.png", sprite_highlight("jessie"))
image jessie sad = At("images/personnel/jessie/jessie sad.png", sprite_highlight("jessie"))
image jessie upset = At("images/personnel/jessie/jessie upset.png", sprite_highlight("jessie"))
image jessie surprise = At("images/personnel/jessie/jessie surprise.png", sprite_highlight("jessie"))
image jessie panic = At("images/personnel/jessie/jessie panic.png", sprite_highlight("jessie"))
image jessie fury = At("images/personnel/jessie/jessie fury.png", sprite_highlight("jessie"))
image jessie pensive = At("images/personnel/jessie/jessie pensive.png", sprite_highlight("jessie"))
image jessie unique = At("images/personnel/jessie/jessie unique.png", sprite_highlight("jessie"))

image aikha = At("images/personnel/aikha/aikha neutral.png", sprite_highlight("aikha"))
image aikha neutral = At("images/personnel/aikha/aikha neutral.png", sprite_highlight("aikha"))
image aikha talk = At("images/personnel/aikha/aikha talk.png", sprite_highlight("aikha"))
image aikha happy = At("images/personnel/aikha/aikha happy.png", sprite_highlight("aikha"))
image aikha sad = At("images/personnel/aikha/aikha sad.png", sprite_highlight("aikha"))
image aikha upset = At("images/personnel/aikha/aikha upset.png", sprite_highlight("aikha"))
image aikha surprise = At("images/personnel/aikha/aikha surprise.png", sprite_highlight("aikha"))
image aikha panic = At("images/personnel/aikha/aikha panic.png", sprite_highlight("aikha"))
image aikha fury = At("images/personnel/aikha/aikha fury.png", sprite_highlight("aikha"))
image aikha pensive = At("images/personnel/aikha/aikha pensive.png", sprite_highlight("aikha"))
image aikha unique = At("images/personnel/aikha/aikha unique.png", sprite_highlight("aikha"))

image alex = At("images/personnel/alex/alex neutral.png", sprite_highlight("alex"))
image alex neutral = At("images/personnel/alex/alex neutral.png", sprite_highlight("alex"))
image alex talk = At("images/personnel/alex/alex talk.png", sprite_highlight("alex"))
image alex happy = At("images/personnel/alex/alex happy.png", sprite_highlight("alex"))
image alex sad = At("images/personnel/alex/alex sad.png", sprite_highlight("alex"))
image alex upset = At("images/personnel/alex/alex upset.png", sprite_highlight("alex"))
image alex surprise = At("images/personnel/alex/alex surprise.png", sprite_highlight("alex"))
image alex panic = At("images/personnel/alex/alex panic.png", sprite_highlight("alex"))
image alex fury = At("images/personnel/alex/alex fury.png", sprite_highlight("alex"))
image alex pensive = At("images/personnel/alex/alex pensive.png", sprite_highlight("alex"))
image alex unique = At("images/personnel/alex/alex unique.png", sprite_highlight("alex"))

image helco = At("images/personnel/helco/helco neutral.png", sprite_highlight("helco"))
image helco neutral = At("images/personnel/helco/helco neutral.png", sprite_highlight("helco"))
image helco talk = At("images/personnel/helco talk.png", sprite_highlight("helco"))
image helco happy = At("images/personnel/helco/helco happy.png", sprite_highlight("helco"))
image helco sad = At("images/personnel/helco sad.png", sprite_highlight("helco"))
image helco upset = At("images/personnel/helco upset.png", sprite_highlight("helco"))
image helco surprise = At("images/personnel/helco surprise.png", sprite_highlight("helco"))
image helco panic = At("images/personnel/helco panic.png", sprite_highlight("helco"))
image helco fury = At("images/personnel/helco fury.png", sprite_highlight("helco"))
image helco pensive = At("images/personnel/helco pensive.png", sprite_highlight("helco"))
image helco unique = At("images/personnel/helco unique.png", sprite_highlight("helco"))

image ryz = At("images/personnel/ryz/ryz neutral.png", sprite_highlight("ryz"))
image ryz neutral = At("images/personnel/ryz/ryz neutral.png", sprite_highlight("ryz"))
image ryz talk = At("images/personnel/ryz/ryz talk.png", sprite_highlight("ryz"))
image ryz happy = At("images/personnel/ryz/ryz happy.png", sprite_highlight("ryz"))
image ryz sad = At("images/personnel/ryz/ryz sad.png", sprite_highlight("ryz"))
image ryz upset = At("images/personnel/ryz/ryz upset.png", sprite_highlight("ryz"))
image ryz surprise = At("images/personnel/ryz/ryz surprise.png", sprite_highlight("ryz"))
image ryz panic = At("images/personnel/ryz/ryz panic.png", sprite_highlight("ryz"))
image ryz fury = At("images/personnel/ryz/ryz fury.png", sprite_highlight("ryz"))
image ryz pensive = At("images/personnel/ryz/ryz pensive.png", sprite_highlight("ryz"))
image ryz unique = At("images/personnel/ryz/ryz unique.png", sprite_highlight("ryz"))

image roose = At("images/personnel/ryz/roose neutral.png", sprite_highlight("roose"), base_char_transform(x = 400, y = 600, yoff = -100))
image roose neutral = At("images/personnel/ryz/roose neutral.png", sprite_highlight("roose"), base_char_transform(x = 400, y = 600, yoff = -100))
image roose talk = At("images/personnel/ryz/roose talk.png", sprite_highlight("roose"), base_char_transform(x = 400, y = 600, yoff = -100))
image roose upset = At("images/personnel/ryz/roose upset.png", sprite_highlight("roose"), base_char_transform(x = 400, y = 600, yoff = -100))

image uriel = At("images/personnel/uriel/uriel neutral.png", sprite_highlight("uriel"))
image uriel neutral = At("images/personnel/uriel/uriel neutral.png", sprite_highlight("uriel"))
image uriel talk = At("images/personnel/uriel/uriel talk.png", sprite_highlight("uriel"))
image uriel happy = At("images/personnel/uriel/uriel happy.png", sprite_highlight("uriel"))
image uriel sad = At("images/personnel/uriel/uriel sad.png", sprite_highlight("uriel"))
image uriel upset = At("images/personnel/uriel/uriel upset.png", sprite_highlight("uriel"))
image uriel surprise = At("images/personnel/uriel/uriel surprise.png", sprite_highlight("uriel"))
image uriel panic = At("images/personnel/uriel/uriel panic.png", sprite_highlight("uriel"))
image uriel fury = At("images/personnel/uriel/uriel fury.png", sprite_highlight("uriel"))
image uriel pensive = At("images/personnel/uriel/uriel pensive.png", sprite_highlight("uriel"))
image uriel unique = At("images/personnel/uriel/uriel unique.png", sprite_highlight("uriel"))

image deceased = At("images/personnel/deceased/deceased neutral.png", sprite_highlight("deceased"))
image deceased neutral = At("images/personnel/deceased/deceased neutral.png", sprite_highlight("deceased"))
image deceased talk = At("images/personnel/deceased/deceased talk.png", sprite_highlight("deceased"))
image deceased happy = At("images/personnel/deceased/deceased happy.png", sprite_highlight("deceased"))
image deceased sad = At("images/personnel/deceased/deceased sad.png", sprite_highlight("deceased"))
image deceased upset = At("images/personnel/deceased/deceased upset.png", sprite_highlight("deceased"))
image deceased surprise = At("images/personnel/deceased/deceased surprise.png", sprite_highlight("deceased"))
image deceased panic = At("images/personnel/deceased/deceased panic.png", sprite_highlight("deceased"))
image deceased fury = At("images/personnel/deceased/deceased fury.png", sprite_highlight("deceased"))
image deceased pensive = At("images/personnel/deceased/deceased pensive.png", sprite_highlight("deceased"))
image deceased unique = At("images/personnel/deceased/deceased unique.png", sprite_highlight("deceased"))

image lee = At("images/personnel/lee/lee neutral.png", sprite_highlight("lee"))
image lee neutral = At("images/personnel/lee/lee neutral.png", sprite_highlight("lee"))
image lee talk = At("images/personnel/lee/lee talk.png", sprite_highlight("lee"))
image lee happy = At("images/personnel/lee/lee happy.png", sprite_highlight("lee"))
image lee sad = At("images/personnel/lee/lee sad.png", sprite_highlight("lee"))
image lee upset = At("images/personnel/lee/lee upset.png", sprite_highlight("lee"))
image lee surprise = At("images/personnel/lee/lee surprise.png", sprite_highlight("lee"))
image lee panic = At("images/personnel/lee/lee panic.png", sprite_highlight("lee"))
image lee fury = At("images/personnel/lee/lee fury.png", sprite_highlight("lee"))
image lee pensive = At("images/personnel/lee/lee pensive.png", sprite_highlight("lee"))
image lee unique = At("images/personnel/lee/lee unique.png", sprite_highlight("lee"))

image firewal = At("images/personnel/firewal/firewal neutral.png", sprite_highlight("firewal"))
image firewal neutral = At("images/personnel/firewal/firewal neutral.png", sprite_highlight("firewal"))
image firewal talk = At("images/personnel/firewal/firewal talk.png", sprite_highlight("firewal"))
image firewal happy = At("images/personnel/firewal/firewal happy.png", sprite_highlight("firewal"))
image firewal sad = At("images/personnel/firewal/firewal sad.png", sprite_highlight("firewal"))
image firewal upset = At("images/personnel/firewal/firewal upset.png", sprite_highlight("firewal"))
image firewal surprise = At("images/personnel/firewal/firewal surprise.png", sprite_highlight("firewal"))
image firewal panic = At("images/personnel/firewal/firewal panic.png", sprite_highlight("firewal"))
image firewal fury = At("images/personnel/firewal/firewal fury.png", sprite_highlight("firewal"))
image firewal pensive = At("images/personnel/firewal/firewal pensive.png", sprite_highlight("firewal"))
image firewal unique = At("images/personnel/firewal/firewal unique.png", sprite_highlight("firewal"))

image chan = At("images/personnel/chan/chan neutral.png", sprite_highlight("chan"))
image chan neutral = At("images/personnel/chan/chan neutral.png", sprite_highlight("chan"))
image chan talk = At("images/personnel/chan/chan talk.png", sprite_highlight("chan"))
image chan happy = At("images/personnel/chan/chan happy.png", sprite_highlight("chan"))
image chan sad = At("images/personnel/chan/chan sad.png", sprite_highlight("chan"))
image chan upset = At("images/personnel/chan/chan upset.png", sprite_highlight("chan"))
image chan surprise = At("images/personnel/chan/chan surprise.png", sprite_highlight("chan"))
image chan panic = At("images/personnel/chan/chan panic.png", sprite_highlight("chan"))
image chan fury = At("images/personnel/chan/chan fury.png", sprite_highlight("chan"))
image chan pensive = At("images/personnel/chan/chan pensive.png", sprite_highlight("chan"))
image chan unique = At("images/personnel/chan/chan unique.png", sprite_highlight("chan"))

image syg = At("images/personnel/syg/syg neutral.png", sprite_highlight("syg"))
image syg neutral = At("images/personnel/syg/syg neutral.png", sprite_highlight("syg"))
image syg talk = At("images/personnel/syg/syg talk.png", sprite_highlight("syg"))
image syg happy = At("images/personnel/syg/syg happy.png", sprite_highlight("syg"))
image syg sad = At("images/personnel/syg/syg sad.png", sprite_highlight("syg"))
image syg upset = At("images/personnel/syg/syg upset.png", sprite_highlight("syg"))
image syg surprise = At("images/personnel/syg/syg surprise.png", sprite_highlight("syg"))
image syg panic = At("images/personnel/syg/syg panic.png", sprite_highlight("syg"))
image syg fury = At("images/personnel/syg/syg fury.png", sprite_highlight("syg"))
image syg pensive = At("images/personnel/syg/syg pensive.png", sprite_highlight("syg"))
image syg unique = At("images/personnel/syg/syg unique.png", sprite_highlight("syg"))

image caffi = At("images/personnel/caffi/caffi neutral.png", sprite_highlight("caffi"))
image caffi neutral = At("images/personnel/caffi/caffi neutral.png", sprite_highlight("caffi"))
image caffi talk = At("images/personnel/caffi/caffi talk.png", sprite_highlight("caffi"))
image caffi happy = At("images/personnel/caffi/caffi happy.png", sprite_highlight("caffi"))
image caffi sad = At("images/personnel/caffi/caffi sad.png", sprite_highlight("caffi"))
image caffi upset = At("images/personnel/caffi/caffi upset.png", sprite_highlight("caffi"))
image caffi surprise = At("images/personnel/caffi/caffi surprise.png", sprite_highlight("caffi"))
image caffi panic = At("images/personnel/caffi/caffi panic.png", sprite_highlight("caffi"))
image caffi fury = At("images/personnel/caffi/caffi fury.png", sprite_highlight("caffi"))
image caffi pensive = At("images/personnel/caffi/caffi pensive.png", sprite_highlight("caffi"))
image caffi unique = At("images/personnel/caffi/caffi unique.png", sprite_highlight("caffi"))

image paul = At("images/personnel/paul/paul neutral.png", sprite_highlight("paul"))
image paul neutral = At("images/personnel/paul/paul neutral.png", sprite_highlight("paul"))
image paul talk = At("images/personnel/paul/paul talk.png", sprite_highlight("paul"))
image paul happy = At("images/personnel/paul/paul happy.png", sprite_highlight("paul"))
image paul sad = At("images/personnel/paul/paul sad.png", sprite_highlight("paul"))
image paul upset = At("images/personnel/paul/paul upset.png", sprite_highlight("paul"))
image paul surprise = At("images/personnel/paul/paul surprise.png", sprite_highlight("paul"))
image paul panic = At("images/personnel/paul/paul panic.png", sprite_highlight("paul"))
image paul fury = At("images/personnel/paul/paul fury.png", sprite_highlight("paul"))
image paul pensive = At("images/personnel/paul/paul pensive.png", sprite_highlight("paul"))
image paul unique = At("images/personnel/paul/paul unique.png", sprite_highlight("paul"))

image plutoes = At("images/personnel/plutoes/plutoes neutral.png", sprite_highlight("plutoes"))
image plutoes neutral = At("images/personnel/plutoes/plutoes neutral.png", sprite_highlight("plutoes"))
image plutoes talk = At("images/personnel/plutoes/plutoes talk.png", sprite_highlight("plutoes"))
image plutoes happy = At("images/personnel/plutoes/plutoes happy.png", sprite_highlight("plutoes"))
image plutoes sad = At("images/personnel/plutoes/plutoes sad.png", sprite_highlight("plutoes"))
image plutoes upset = At("images/personnel/plutoes/plutoes upset.png", sprite_highlight("plutoes"))
image plutoes surprise = At("images/personnel/plutoes/plutoes surprise.png", sprite_highlight("plutoes"))
image plutoes panic = At("images/personnel/plutoes/plutoes panic.png", sprite_highlight("plutoes"))
image plutoes fury = At("images/personnel/plutoes/plutoes fury.png", sprite_highlight("plutoes"))
image plutoes pensive = At("images/personnel/plutoes/plutoes pensive.png", sprite_highlight("plutoes"))
image plutoes unique = At("images/personnel/plutoes/plutoes unique.png", sprite_highlight("plutoes"))

image venture = At("images/personnel/venture/venture neutral.png", sprite_highlight("venture"))
image venture neutral = At("images/personnel/venture/venture neutral.png", sprite_highlight("venture"))
image venture talk = At("images/personnel/venture/venture talk.png", sprite_highlight("venture"))
image venture happy = At("images/personnel/venture/venture happy.png", sprite_highlight("venture"))
image venture sad = At("images/personnel/venture/venture sad.png", sprite_highlight("venture"))
image venture upset = At("images/personnel/venture/venture upset.png", sprite_highlight("venture"))
image venture surprise = At("images/personnel/venture/venture surprise.png", sprite_highlight("venture"))
image venture panic = At("images/personnel/venture/venture panic.png", sprite_highlight("venture"))
image venture fury = At("images/personnel/venture/venture fury.png", sprite_highlight("venture"))
image venture pensive = At("images/personnel/venture/venture pensive.png", sprite_highlight("venture"))
image venture unique = At("images/personnel/venture/venture unique.png", sprite_highlight("venture"))

image b6 = At("images/personnel/b6/b6 neutral.png", sprite_highlight("b6"))
image b6 neutral = At("images/personnel/b6/b6 neutral.png", sprite_highlight("b6"))
image b6 talk = At("images/personnel/b6/b6 talk.png", sprite_highlight("b6"))
image b6 happy = At("images/personnel/b6/b6 happy.png", sprite_highlight("b6"))
image b6 sad = At("images/personnel/b6/b6 sad.png", sprite_highlight("b6"))
image b6 upset = At("images/personnel/b6/b6 upset.png", sprite_highlight("b6"))
image b6 surprise = At("images/personnel/b6/b6 surprise.png", sprite_highlight("b6"))
image b6 panic = At("images/personnel/b6/b6 panic.png", sprite_highlight("b6"))
image b6 fury = At("images/personnel/b6/b6 fury.png", sprite_highlight("b6"))
image b6 pensive = At("images/personnel/b6/b6 pensive.png", sprite_highlight("b6"))
image b6 unique = At("images/personnel/b6/b6 unique.png", sprite_highlight("b6"))

image meem = At("images/personnel/meem/meem neutral.png", sprite_highlight("meem"))
image meem neutral = At("images/personnel/meem/meem neutral.png", sprite_highlight("meem"))
image meem talk = At("images/personnel/meem/meem talk.png", sprite_highlight("meem"))
image meem happy = At("images/personnel/meem/meem happy.png", sprite_highlight("meem"))
image meem sad = At("images/personnel/meem/meem sad.png", sprite_highlight("meem"))
image meem upset = At("images/personnel/meem/meem upset.png", sprite_highlight("meem"))
image meem surprise = At("images/personnel/meem/meem surprise.png", sprite_highlight("meem"))
image meem panic = At("images/personnel/meem/meem panic.png", sprite_highlight("meem"))
image meem fury = At("images/personnel/meem/meem fury.png", sprite_highlight("meem"))
image meem pensive = At("images/personnel/meem/meem pensive.png", sprite_highlight("meem"))
image meem unique = At("images/personnel/meem/meem unique.png", sprite_highlight("meem"))

image moon = At("images/personnel/moon/moon neutral.png", sprite_highlight("moon"))
image moon neutral = At("images/personnel/moon/moon neutral.png", sprite_highlight("moon"))
image moon talk = At("images/personnel/moon/moon talk.png", sprite_highlight("moon"))
image moon happy = At("images/personnel/moon/moon happy.png", sprite_highlight("moon"))
image moon sad = At("images/personnel/moon/moon sad.png", sprite_highlight("moon"))
image moon upset = At("images/personnel/moon/moon upset.png", sprite_highlight("moon"))
image moon surprise = At("images/personnel/moon/moon surprise.png", sprite_highlight("moon"))
image moon panic = At("images/personnel/moon/moon panic.png", sprite_highlight("moon"))
image moon fury = At("images/personnel/moon/moon fury.png", sprite_highlight("moon"))
image moon pensive = At("images/personnel/moon/moon pensive.png", sprite_highlight("moon"))
image moon unique = At("images/personnel/moon/moon unique.png", sprite_highlight("moon"))

image egg = At("images/personnel/egg/egg neutral.png", sprite_highlight("egg"))
image egg neutral = At("images/personnel/egg/egg neutral.png", sprite_highlight("egg"))
image egg talk = At("images/personnel/egg/egg talk.png", sprite_highlight("egg"))
image egg happy = At("images/personnel/egg/egg happy.png", sprite_highlight("egg"))
image egg sad = At("images/personnel/egg/egg sad.png", sprite_highlight("egg"))
image egg upset = At("images/personnel/egg/egg upset.png", sprite_highlight("egg"))
image egg surprise = At("images/personnel/egg/egg surprise.png", sprite_highlight("egg"))
image egg panic = At("images/personnel/egg/egg panic.png", sprite_highlight("egg"))
image egg fury = At("images/personnel/egg/egg fury.png", sprite_highlight("egg"))
image egg pensive = At("images/personnel/egg/egg pensive.png", sprite_highlight("egg"))
image egg unique = At("images/personnel/egg/egg unique.png", sprite_highlight("egg"))

image hampter = At("images/personnel/hampter/hampter neutral.png", sprite_highlight("hampter"))
image hampter neutral = At("images/personnel/hampter/hampter neutral.png", sprite_highlight("hampter"))
image hampter talk = At("images/personnel/hampter/hampter talk.png", sprite_highlight("hampter"))
image hampter happy = At("images/personnel/hampter/hampter happy.png", sprite_highlight("hampter"))
image hampter sad = At("images/personnel/hampter/hampter sad.png", sprite_highlight("hampter"))
image hampter upset = At("images/personnel/hampter/hampter upset.png", sprite_highlight("hampter"))
image hampter surprise = At("images/personnel/hampter/hampter surprise.png", sprite_highlight("hampter"))
image hampter panic = At("images/personnel/hampter/hampter panic.png", sprite_highlight("hampter"))
image hampter fury = At("images/personnel/hampter/hampter fury.png", sprite_highlight("hampter"))
image hampter pensive = At("images/personnel/hampter/hampter pensive.png", sprite_highlight("hampter"))
image hampter unique = At("images/personnel/hampter/hampter unique.png", sprite_highlight("hampter"))

# Characters
define base_char = Character("", callback=name_callback)

define jessie = Character("Dr. Jessie", kind=base_char, color="#ff6dcf", cb_name="jessie", image="jessie")
define jessie_unknown = Character("???", kind=jessie)

define firewal = Character("Dr. Firewal", kind=base_char, color="#961e44", cb_name="firewal", image="firewal")
define firewal_unknown = Character("???", kind=firewal)

define helco = Character("Dr. Helco", kind=base_char, color="#fffda1", cb_name="helco", image="helco")

define aikha = Character("Dr. Aikha", kind=base_char, color="#8f76ff", cb_name="aikha", image="aikha")
define aikha_unknown = Character("???", kind=aikha)

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


define n = Character("", kind=base_char, cb_name="") # narrator, required to unhighlight characters whenever narration is occurring

# bgs

image bg hallway = "images/bgs/hallway.png"
image bg lounge = "images/bgs/hallway.png"
image bg office = "images/bgs/hallway.png"
image bg lobby = "images/bgs/hallway.png"
image bg venue = "images/bgs/venue.png"


# cgs will be defined in the respective event rpy

# other images

image black_screen = Solid("#000000", xsize = 2020, ysize = 1180, xpos = -50, ypos = -50, xanchor = 0.0, yanchor = 0.0) # for fade to black 

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