# This folder consists of Python helper functions

init python:
    import re
    
    # Raise the character points of personnel
    # takes in a dictionary: {"personnel1": points1, "personnel2": points2}
    # example usage: update_character_points({"helco": 1, "plutoes", -2})
    def update_character_points(personnel):
        for person, points in personnel.items():
            characters[person]["points"] += points
        return True

    # Raise the honing survey points of personnel
    # takes in a dictionary: {"personnel1": points1, "personnel2": points2}
    # example usage: update_honing_points({"helco": 1, "plutoes", -2})
    def update_honing_points(personnel):
        for person, points in personnel.items():
            honing_points[person] += points
        return True

    # Automatically adds pauses after punctuations
    # this is some really weird ass reg-ex shit please do not ask me what it means i will not know - ryan
    def auto_pause(text):
        if text[0:9] == "/no_pause":
            return text[9:]
        
        # adds pause after commas
        text = re.sub(
            r',(?!\s*[0-9])', 
            f',{{w={punctuation_pauses["comma"]}}}', 
            text
        )
        # adds pause after periods
        text = re.sub(
            r'(?<!\bMr)(?<!\bMrs)(?<!\bDr)(?<!\bMRS)(?<!\bMR)(?<!\bDR)(?<!\.)\. (?!\s*\s*$|\.|[0-9])', 
            f'. {{w={punctuation_pauses["period"]}}}', 
            text
        )
        # adds pause after elipses
        text = re.sub(
            r'\.{3}(?!\s*)', 
            f'.{{w={punctuation_pauses["elipsis"]}}}.{{w={punctuation_pauses["elipsis"]}}}.{{w={punctuation_pauses["elipsis"]}}}', 
            text
        )
        # adds pause after exclamation mark
        text = re.sub(
            r'! (?!\s*[0-9])', 
            f'! {{w={punctuation_pauses["exclamation"]}}}', 
            text
        )
        # adds pause after question mark
        text = re.sub(
            r'\? (?!\s*[0-9])', 
            f'? {{w={punctuation_pauses["question"]}}}', 
            text
        )
        # adds pause after colon
        text = re.sub(
            r': (?!\s*[0-9])', 
            f': {{w={punctuation_pauses["colon"]}}}', 
            text
        )
        # adds pause after semi colon
        text = re.sub(
            r'; (?!\s*[0-9])', 
            f'; {{w={punctuation_pauses["semicolon"]}}}', 
            text
        )

        # adds pause after quotation mark
        text = re.sub(
            r'" (?!\s*[0-9])', 
            f'" {{w={punctuation_pauses["quotation"]}}}', 
            text
        )

        # adds pause after hyphen
        text = re.sub(
            r'- (?!\s*[0-9])', 
            f'- {{w={punctuation_pauses["hyphen"]}}}', 
            text
        )

        return text

    config.say_menu_text_filter = auto_pause

