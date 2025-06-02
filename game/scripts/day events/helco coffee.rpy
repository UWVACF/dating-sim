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
    show aikha at appear(x_align = -0.1)
    show alex at appear(x_align = 0.15)
    show helco at appear(x_align = 0.35)
    show firewal at appear(x_align = 0.55)
    show ryz at appear(x_align = 0.85)
    show uriel at appear(x_align = 1.1)
    n "the whole gang's here!!!"
    show aikha happy
    show alex happy
    show helco happy
    show firewal happy
    show ryz happy
    show uriel happy
    n "happy"
    show aikha fury
    show alex fury
    show helco fury
    show firewal fury
    show ryz fury
    show uriel fury
    n "fury"
    show aikha talk
    show alex talk
    show helco talk
    show firewal talk
    show ryz talk
    show uriel talk
    n "talk"
    show aikha panic
    show alex panic
    show helco panic
    show firewal panic
    show ryz panic
    show uriel panic
    n "panic"
    show aikha pensive
    show alex pensive
    show helco pensive
    show firewal pensive
    show ryz pensive
    show uriel pensive
    n "pensive"
    show aikha surprise
    show alex surprise
    show helco surprise
    show firewal surprise
    show ryz surprise
    show uriel surprise
    n "surprise"
    show aikha upset
    show alex upset
    show helco upset
    show firewal upset
    show ryz upset
    show uriel upset
    n "upset"
    show aikha unique
    show alex unique
    show helco unique
    show firewal unique
    show ryz unique
    show uriel unique
    n "unique"
    show aikha sad
    show alex sad
    show helco sad
    show firewal sad
    show ryz sad
    show uriel sad
    n "sad"


    
    
    
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
