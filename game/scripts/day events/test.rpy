init python:
    # random ass function for helco to misremember the player's name if they don't know each other enough lmao
    # example: Jakob -> Jekob, Aikha -> Eikha
    def misremember_name():
        replacements = [
            ("a", "e"),
            ("e", "a"),
            ("A", "E"),
            ("E", "A"),
            ("i", "o"),
            ("o", "i"),
            ("I", "O"),
            ("O", "I")
        ]
        for old, new in replacements:
            new_player_name = player_name.replace(old, new, 1)
            if new_player_name != player_name:
                return new_player_name
        
        return "o" + player_name[1:] if player_name[0] != "o" else "u" + player_name[1:]





label day_event_test:
    scene bg lounge
    with default_fade
    show chan at appear(x_align = 0.5)
    show b6 at appear(x_align = 0.0)
    show aikha at appear(x_align = 1.0)
    n ""
    uriel "asdasd"
    n ""
    n ""
    n ""
    n ""
    n ""
