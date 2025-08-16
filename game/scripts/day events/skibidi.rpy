label day_event_skibidi:
    scene bg hallway
    if day_number > 5:
        n "Take a wild guess as to what you're doing."
        n "Yep. Coffee. It's your only defining trait, at this point."
        n "You should go on a character arc sometime soon. You know, find some new motivations."
    else:
        n "You're on your way to the lounge to fuel your coffee addiction."
        n "This will be a recurring trend. Get comfy with it."
    n "You open the door to the lounge and are greeted by three other personnel, chatting away happily."
    n "You pay them no mind, until Dr. Helco approaches you."
    show helco happy at appear
    helco happy "Hello, [player_name]. What the skibidi is going on?"
    show caffi at appear(x_align = 0.25)
    show meem at appear(x_align = 0.75)
    caffi "Helco! It doesn't work like that!"
    helco neutral "Huh? Did I use it incorrectly?"
    caffi "Yeah! It's like, \"What the hell\" or \"What the fuck,\" you know?"
    helco "Oh."
    helco happy "Hello, [player_name]. What the fuck is going on?"
    show helco scared at move_to(x_align = 1.75)
    show caffi at move_to(x_align = 1.5)
    show meme at move_to(x_align = 1.5, duration = 2 * default_move_time)
    n "Caffi drags Dr. Helco by the sleeve to the back of the room, while Meme, chuckling, follows behind."
    hide helco
    hide caffi
    hide meme
    caffi "You know what? Let's move on. I'll teach you the word \"gyatt\" instead." # im in so much pain
    helco "Oh! Okay!"
    menu:
        n "...Do you intervene?"
        "Save Dr. Helco from brainrot.":
            jump skibidi_helco
        "Save yourself.":
            jump skidibi_yourself
    
    label skibidi_helco:
        n "Well, nobody else is gonna save Dr. Helco from this disaster."
        n "You sigh to yourself and make your way to the back of the room."
        show helco pensive at appear
        show caffi happy at appear(x_align = 0.25)
        show meme at appear(x_align = 0.75)
        caffi happy "You say \"gyatt\" whenever you're really surprised, or when something's really cool."
        caffi "Then we have \"sus\", \"cap\", \"aura\"..."
        n "Your eyes glaze over as you mourn the loss of thousands of years of societal development."
        n "About 14 and a half minutes later, Dr. Helco walks up to you with renewed confidence. You brace yourself for impact."
        helco happy "Wagwan shawty?" # i literally died writing this somebody else can take over
        player "I, uh-"
        helco "Aura farming, as usual? Yeah, me too, fr fr!"
        player "Dr. Helco-"
        caffi happy "Show [player_obj] the thing!"
        helco "Oh, right! Caffi taught me one of your ancient languages! I think she called it \"Chinese.\""
        helco "*ahem*"
        helco "早上好中国，现在我有冰淇淋。"
        helco "真喜欢冰淇淋！"
        
        n "A single teardrop streams down your cheek as you witness the regression of the foundation you loved so dearly. It's the beginning of the end."
        helco "[player_name]? [player_name]! "
        helco "[player_sub_be] not responding (skull emoji). Chat, is this real? [player_sub!c] fell for the ragebait, smh. Negative 10000 social credit."
        helco "ICL, TS PMO. I'm out."
        show helco at disappear
        n "Dr. Helco leaves the room swaggaliciously."
        n "You remain frozen in place, unresponsive and unblinking."
        meme "Hey, buddy! You good?"
        n "Meme shakes your shoulders, but to no avail. You remain in shock."
        meme pensive "Aw, they're gone. Now where did [player_sub] put [player_pos_adj] wallet..."
        caffi "Wake up. Wake. Up."
        n "Caffi smacks your face, and you tumble backwards onto to the floor, spread-eagled."
        meme "Wh- hey, chill! I'm tryna pickpocket [player_obj] here!"
        meme happy "Oh! Found it!"
        show meme at disappear
        n "Meme exits the room, happily humming to themselves. You remain in your vegetative state."
        caffi happy "Moon will take care of you. Toodles!"
        show caffi at disappear
        n "..."
        n "So how long {i}are{/i} you gonna lie there?"
        $ update_character_points() 
        return


    label skibidi_yourself:
        n "Nah. He can fend for himself. Surely."
        n ""


"""
dawg
blud
smthmaxxing
:wilted_rose:
:heartbreak:
alpha, beta, sigma, alpha male
edging
amogus
chungus
one must imagine sisyphus happy
delulu
mewing
we got ... before gta 6
red pilled
-core
-pilled
早上好中国，现在我有冰淇淋
chat is this real
cooked, fried, broiled, sauted, chopped
erm, what the sigma
"""