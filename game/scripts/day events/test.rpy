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
    show egg
    n "a"
    $ shake_screen()
    n "b"
    $ shake_screen(repeat=True)
    n "c"
    $ shake_screen(duration=0)
    n "d"
    n "e"
    n "f"
    n "g"
    n "h"


    
     
    
# player "Hello, Dr. Helco!"
# show helco neutral at appear
# n "He jolts awake at the sound of your voice."
# helco "Oh, hi!"
# show helco neutral at shake(duration = 1.0, strength = 50.0)
# if characters["helco"]["points"] < 1:
#     helco "[misremember_name()], right?"
#     player "It's [player_name], actually."
#     helco "Oh! Sorry!"
#     helco "{size=[helco_text_downsize]}I must write that down...{/size}"
# else:
#     helco "[player_name], right?"
#     player "Yup!"
#     helco "{size=[helco_text_downsize]}Good, good...{/size}"
# n "Helco spaces out briefly, before returning to normal."
# helco "..."
# player "What brings you here?"
# helco "Oh! I'm just...grabbing a coffee, as you do."
# player "here we will insert more awesome dialogue"
# player "later"
# player "bc i just pulled an all nighter so maybe now's not the best time to do so"
# n "Perhaps Dr. Helco could use some guidance."
# menu:
#     n "How will you teach Dr. Helco what it means to be human?"
#     "Teach him personally":
#         jump personally
#     "Gather Dr. Jessie and Dr. Firewal":
#         jump jessie_firewal
#     "Enlist the help of Dr. Plutoes and Dr. Aikha, the most human personnel":
#         jump aikha_plutoes

# label personally:
#     n "You're human! Surely you could teach him a thing or two about human activity."
#     return

# label jessie_firewal:
#     n "You decide to gather the help of other human personnel to give Dr. Helco a group lesson."
#     return

# label aikha_plutoes:
#     n "Perhaps Dr. Helco would best relate to other non-humans struggling to fit in."
#     return
