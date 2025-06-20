# init python:
#     # viewed
#     escape_back_wall_viewed = False
#     escape_back_wall_notebook_viewed = False


#     escape_passcode_attempts_remaining = 3
#     escape_inventory = ["Phone (Dead)"]
#     escape_item_labels = {
#         "Phone (Dead)": "escape_item_phone_dead",
#         "Phone (Charged)": "escape_item_phone_charged",
#         "Testimony (Blue Sticky)": "escape_item_testimony",

#     }
#     escape_checked_phone = False
#     escape_testimony_read = False

# screen escape_inventory_screen:
#     style_prefix "choice"
    
#     vbox:
#         for i in escape_inventory:
#             button:
#                 style "choice_button"
#                 child Text(i, style="choice_button_text")
#                 action Call("[escape_item_labels[i]]")
#         button:
#             style "choice_button"
#             child Text("Go back.")
#             action Jump("escape_main_menu")

# label day_event_escape:
#     scene bg hallway
#     player "Yeah!!! It's coffee time!!"
#     n "You excitedly hurry over to the lounge to indulge in your coffee addiction when-"
#     show black_screen
#     with hpunch
#     scene bg room containment
#     with Fade(0.0, 1.0, 1.0)
#     player "Huh? What?"
#     n "You suddenly wake up and find yourself sprawled on the floor of the containment room."
#     aikha "Oh, look who the cat dragged in."
#     show aikha at appear(x_align = 0.2)
#     show ryz at appear(x_align = 0.5)
#     show wal at appear(x_align = 0.8)
#     ryz "Morning, [player_name]."
#     player "Where the hell are we?"
#     firewal "No clue. Think we're in some containment room. We all just kind of woke up here."
#     n "You look at the door to the room and see a torn scrap of paper next to it. It reads:"
#     n "\"...nd for those who forgot, the password is simply the anomaly's name, its number in the system and the person who discovered it (myself).\""
#     n "\"Signed, ████████\""
#     n "Unfortunately, the name is crossed out."
#     aikha "This shouldn't be too bad. New recruit, there should be hints scattered around the room. Try to piece together the puzzle and get us out of here!"
#     jump escape_main_menu

# label escape_main_menu:
#     n "What to do?"
#     "Look around.":
#         jump escape_look_around
#     "Talk.":
#         jump escape_talk
#     "Check inventory.":
#         jump escape_inventory_menu
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
#     if not escape_testimony_read:
#         n "The left wall features three coloured sticky notes."
#         "Look at the yellow one.":
#             jump escape_left_wall_yellow
#         "Look at the blue one.":
#             jump escape_left_wall_blue
#         "Look at the orange one.":
#             jump escape_left_wall_orange
#         "Go back.":
#             jump escape_look_around
#     else:
#         n "The left wall now features two coloured sticky notes."
#         "Look at the yellow one.":
#             jump escape_left_wall_yellow
#         "Look at the orange one.":
#             jump escape_left_wall_orange
#         "Go back.":
#             jump escape_look_around

# label escape_left_wall_yellow:
#     n "You read the yellow sticky note."
#     n "\"...The first sighting of the anomaly was on September 23, 2024. Since then, the number of total sightings has increased to 83, all within the Baltic Region.\""
#     n "\"The anomaly...\""
#     n "...The rest is cut off."
#     jump escape_left_wall

# label escape_left_wall_blue:
#     n "You read the blue sticky note."
#     n "It's labelled, \"Witness Testimony.\""
#     n "..."
#     n "It's in Swedish. You can't read Swedish, unfortunately."
#     if "Phone (Charged)" in escape_inventory:
#         n "You do, however, have a translator on your phone."
#         n "You open Guugle Trunslate and snap a photo of the sticky note."
#         n "It reads:"
#         call escape_item_testimony
#         n "You peel off the sticky note and put it in your inventory."
#         $ escape_inventory.add("Testimony (Blue Sticky)")
#         $ escape_testimony_read = True

# label escape_item_testimony:
#     n  "\"It was, it was this orange human-looking thing, with, with, with reddish-brown streaks in its body - like veins, but not quite. It was huge - maybe six feet, six feet one. And it- holy shit, it just-\""
#     n "The testimony cuts off suddenly."


# label escape_back_wall:
#     if not escape_back_wall_viewed:
#         n "There's a countertop on the back wall, on which a notebook rests. Most of the pages are burnt, bloodstained or otherwise vandalized."
#         $ escape_back_wall_viewed = True
#     menu:
#         n "What to do?"
#         "Open notebook.":
#             jump escape_back_wall_notebook
#         "Go back.":
#             jump escape_look_around

# label escape_back_wall_notebook:
#     n "There's a "
#     python:
#         escape_flip_to_page = renpy.input("What page do you go to?", default=1)
#         if not escape_flip_to_page.isdigit():
#             renpy.notify("Choose a page from 1 to 999.")
#             escape_flip_to_page = renpy.input("My name is...", default=1)
#         escape_flip_to_page = int(escape_flip_to_page)
#     if escape_flip_to_page == 1:
#         n "The notebook reads:"
#         n "Viable Actions for Containment: Attempting to contain, capture or otherwise interact with this anomaly is not recommended. Continued on page #######"
#         n "The rest is cut off. Literally cut off. There are slash marks on the page."
#     elif escape_flip_to_page == 67:


    
# label escape_left_wall:
#     menu:
#         n "On the left wall, there's a newspaper, a lounge chair and some kind of box."
#         "Check the newspaper.":

#         "Check the lounge chair.":
#             jump escape_left_wall_lounge_chair
#         "Check the box.":


# label escape_left_wall_lounge_chair:
#     if "Phone (Charged)" in escape_inventory:
#         n "No time for breaks."
#         jump escape_left_wall
    
#     n "You inspect the lounge chair. It looks very comfy."
#     menu:
#         n "Take a seat?"
#         "Yes.":
#             jump escape_left_wall_lounge_chair_sit
#         "No.":
#             jump escape_left_wall

# label escape_left_wall_lounge_chair_sit:
#     n "You plop yourself happily on the lounge chair."
#     n "..?"
#     n "There's something under the cushion."
#     n "You found a phone charger."
#     if not escape_checked_phone:
#         n "That reminds you. You rummage your pockets and pull out your phone."
#         n "You tap the screen, but it doesn't power on. How convenient of the phone charger to make its presence known."

#     n "You charge your phone at the nearest plug."
#     n "After a little bit, the screen turns on. Nice!"
#     $ escape_inventory.remove("Phone (Dead)")
#     $ escape_inventory.add("Phone (Charged)")
#     jump escape_left_wall
# # ------------------------------ TALK ------------------------------
# label escape_talk:
#     n "To who?"
#     # implement current_task sorted list being the most recent puzzles (e.g. swedish, having a charged phone, briefcase)
#         # each item should be task name (string), aikha_seen (bool), ryz_seen (bool), wal_seen (bool)
#     # go down the list for each personnel and trigger dialogue about them
#     # once list is exhausted, have list of generic dialogue event labels and trigger them sequentially (or random if not too hard)
#     "Dr. Aikha.":
#         jump escape_talk_aikha
#     "Dr. Ryz.":
#         jump escape_talk_ryz
#     "Dr. Firewal.":
#         jump escape_talk_firewal
#     "Go back.":
#         jump escape_main_menu

# # ------------------------------ PASSCODE ------------------------------

# label escape_inventory_menu:
#     call escape_inventory_screen
#     n "You check your inventory."
#     $ ui.interact()
#     jump escape_inventory_menu


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
#     n "Who discovered it?"
#     "Dr. Syg.":
#         jump escape_submit_passcode_end
#     "Dr. Ryz.":
#         jump escape_submit_passcode_end
#     "Dr. Deceased.":
#         jump escape_submit_passcode_end
#     "Dr. Jessie.":
#         jump escape_submit_passcode_end

# label escape_submit_passcode_end:
#     n "blegh"

#     player "Say, Dr. Ryz, can't you just like...walk through the wall and free us?"
#     ryz "Hm? Well, I guess, but I spent too long writing and coding this event."
#     player "What?"
#     ryz "What?"





# # setting: trapped in the containment room
# # need the code for the front door
# # the code is based off the anomaly that was initially contained in here
# # split into three parts:
# # anomaly name + VACF foundation number + personnel who contained it


# # find anomaly physical description: A human-like creature
# # find phone charger in lounge chair (left wall) -> blue sticky note (right wall) -> translate the swedish witness testimony
# # 
# # find spawn rate: 237
# # 
# #
# # find globalization: 050
# # 
# # find who discovered it: ryz
# # 
# # 
# # 
# # 
# # 
# # 
# # 
# # 
# # 
# # 
# # 
# # 
# # 
# # 
# # 
# # 
# # 
# # 
# # 
# # 
