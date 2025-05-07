# This folder consists of Python helper functions

init python:
    import re
    
    # Capitalize the first letter of the passed string
    def cap_first(s):
        return s[0].upper() + s[1:] if s else s

    # Raise the character points of personnel
    # takes in a dictionary: {"personnel1": points1, "personnel2": points2}
    # example usage: update_character_points({"helco": 1, "plutoes", -2})
    def update_character_points(personnel):
        for person, tuple in personnel.items():
            character_points[person][0] += points
        return True

    # Raise the honing survey points of personnel
    # takes in a dictionary: {"personnel1": points1, "personnel2": points2}
    # example usage: update_honing_points({"helco": 1, "plutoes", -2})
    def update_honing_points(personnel):
        for person, points in personnel.items():
            honing_points[person] += points
        return True

    # Automatically adds pauses after commas and periods
    # this is some really weird ass reg-ex shit please do not ask me what it means i will not know - ryan
    def auto_pause(text):
        if text[0:9] == "{no_pause}":
            return text[10:]
        
        # adds pause after commas
        text = re.sub(
            r',(?!\s*{[^}]*}|[0-9])', 
            f',{{w={comma_pause}}}', 
            text
        )
        # adds pause after periods
        text = re.sub(
            r'(?<!\bMr)(?<!\bMrs)(?<!\bDr)(?<!\.)\. (?!\s*{[^}]*}|\s*$|\.|[0-9])', 
            f'. {{w={period_pause}}}', 
            text
        )
        # adds pause after elipses
        text = re.sub(
            r'\.{3}(?!\s*{[^}]*})', 
            f'.{{w={elipsis_pause}}}.{{w={elipsis_pause}}}.{{w={elipsis_pause}}}', 
            text
        )
        # adds pause after exclamation mark
        text = re.sub(
            r'! (?!\s*{[^}]*}|[0-9])', 
            f'! {{w={exclamation_pause}}}', 
            text
        )
        # adds pause after question mark
        text = re.sub(
            r'\? (?!\s*{[^}]*}|[0-9])', 
            f'? {{w={comma_pause}}}', 
            text
        )
        # adds pause after colon
        text = re.sub(
            r': (?!\s*{[^}]*}|[0-9])', 
            f': {{w={colon_pause}}}', 
            text
        )
        # adds pause after semi colon
        text = re.sub(
            r'; (?!\s*{[^}]*}|[0-9])', 
            f'; {{w={semicolon_pause}}}', 
            text
        )

        # adds pause after quotation mark
        text = re.sub(
            r'" (?!\s*{[^}]*}|[0-9])', 
            f'" {{w={semicolon_pause}}}', 
            text
        )

        return text

    config.say_menu_text_filter = auto_pause

