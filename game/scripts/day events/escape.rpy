# init python:
#     escape_passcode_attempts_remaining = 3
#     escape_back_wall_viewed = False

# label day_event_escape:
#     scene bg room containment
#     with default_fade
#     player "Huh? What?"
#     n "You suddenly wake up and find yourself sprawled on the floor of the containment room. You quickly stand up."
#     aikha "Oh, look who the cat dragged in."
#     show aikha at appear(x_align = 0.2)
#     show ryz at appear(x_align = 0.5)
#     show wal at appear(x_align = 0.8)
#     ryz "Morning, [player_name]."
#     player "Where the hell are we?"
#     firewal "We're trapped in a containment room. And unfortunately for us, we don't have the passcode."
#     n "You look at the door to the room and see a notepad next to it. It reads:"
#     n "\"And for those who forgot, the password is simply the anomaly's name, its number in the system and the person who contained it (myself).\""
#     n "\"Signed, ████████\""
#     n "Unfortunately, the name is crossed out."
#     aikha "So we need to figure out the anomaly. New recruit, there should be hints scattered around the room. Try to piece together the puzzle and get us out of here!"
#     jump escape_main_menu

# label escape_main_menu:
#     n "What to do?"
#     "Look around.":
#         jump escape_look_around
#     "Talk.":
#         jump escape_talk
#     "Check inventory.":
#         jump escape_inventory
#     "Submit the pascode.":
#         jump escape_passcode

# # ------------------------------ LOOK ------------------------------
# label escape_look_around:
#     n "Where do you look?"
#     "Left wall.":
#         jump escape_left_wall
#     "Back wall.":
#         jump escape_back_wall
#     "Right wall.":
#         jump escape_right_wall
#     "Go back.":
#         jump escape_main_menu

# label escape_left_wall:
#     n "The left wall features three coloured sticky notes."
#     "Look at the yellow one.":
#         jump escape_left_wall_yellow
#     "Look at the blue one.":
#         jump escape_left_wall_blue
#     "Look at the orange one.":
#         jump escape_left_wall_orange
#     "Go back.":
#         jump escape_look_around

# label escape_left_wall_yellow:
#     n "You read the yellow sticky note."
#     n "\"Reports of the anomaly\""


# label escape_back_wall:
#     if not escape_back_wall_viewed:
#         n "There's a countertop on the back wall, on which a notebook rests. Most of the pages are burnt, bloodstained or otherwise vandalized."
#         $ escape_back_wall_viewed = True
#     menu:
#         n "Which page do you flip to?"
#         "Page 114.":
#             jump escape_back_wall_114
#         "Page 236.":
#             jump escape_back_wall_236
#         "Page 357.":
#             jump escape_back_wall_357
        
    

# # ------------------------------ TALK ------------------------------
# label escape_talk:
#     n "To who?"
#     "Dr. Aikha.":
#         jump escape_talk_aikha
#     "Dr. Ryz.":
#         jump escape_talk_ryz
#     "Dr. Firewal.":
#         jump escape_talk_firewal
#     "Go back.":
#         jump escape_main_menu


# # ------------------------------ PASSCODE ------------------------------
# label escape_passcode:
#     n "You have [escape_passcode_attempts_remaining] attempt["" if escape_passcode_attempts_remaining == 1 else "s"] remaining. Are you sure you would like to submit the code?"
#     "Yes.":
#         jump escape_submit_passcode_1
#     "Go back.":
#         jump escape_main_menu

# label escape_submit_passcode_1:
#     n "What's the anomaly?"
#     "A human-like creature.":
#         jump escape_submit_passcode_2
#     "A basket with legs.":
#         jump escape_submit_passcode_2
#     "An amorphous blob.":
#         jump escape_submit_passcode_2
#     "An invisible entity.":
#         jump escape_submit_passcode_2

# label escape_submit_passcode_2:
#     n "What's its spawn rate value?"
#     "Low (001-333).":
#         jump escape_submit_passcode_3
#     "Medium (334-666).":
#         jump escape_submit_passcode_3
#     "High (667-999).":
#         jump escape_submit_passcode_3

# label escape_submit_passcode_3:
#     n "What's its globalization value?"
#     "Low (001-333).":
#         jump escape_submit_passcode_4
#     "Medium (334-666).":
#         jump escape_submit_passcode_4
#     "High (667-999).":
#         jump escape_submit_passcode_4

# label escape_submit_passcode_4:
#     n "Who contained it?"
#     "Dr. Syg.":
#         jump escape_submit_passcode_end
#     "Dr. Chan.":
#         jump escape_submit_passcode_end
#     "Dr. Deceased.":
#         jump escape_submit_passcode_end
#     "Dr. Jessie.":
#         jump escape_submit_passcode_end

# label escape_submit_passcode_end:
#     n "blegh"

#     player "Say, Dr. Ryz, can't you just like...walk through the wall and free us?"
#     ryz "Hm? Well, I guess, but then this event would be kind of anticlimactic, wouldn't it?"
#     player "What?"
#     ryz "What?"





# # setting: trapped in the containment room
# # need the code for the front door
# # the code is based off the anomaly that was initially contained in here
# # split into three parts:
# # anomaly name + VACF foundation number + personnel who contained it

# # anomaly options: 
# # painting (syg, 243-757)