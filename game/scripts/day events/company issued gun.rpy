init python:
    gun_img_path = "images/cgs/company_gun/"

    gun_display_display_per_page = 4
    gun_display_page = 0
    gun_display_current_page_title = ""
    gun_selected_item_personnel = ""
    gun_display_current_description = "Hover over an item to see its description."
    gun_display_current_remark = ""
    gun_display_hovering = ""
    gun_base = "gun" # gun or water

    gun_items = {
        "Additional Functions": [
            {
                "name": "Corporeal anomaly proximity radar",
                "personnel": "chan",
                "description": "A turquoise radar. A shrill voice will shriek in your ear if it detects any anomalies and/or ethical violations nearby.",
                "remark": "This was developed by Dr. Chan and detects if there are any anomalies near you! Doesn't work for non-corporeal Cerebrasites, though."
            },
            {
                "name": "Owner locator",
                "personnel": "uriel",
                "description": "A plastic arrow duct-taped to the gun. It doesn't work.",
                "remark": "This was developed by Uriel! It tracks where you are and will alert you on your work phone if your gun gets too far away.",
            },
            {
                "name": "Human proximity radar",
                "personnel": "helco",
                "description": "A golden radar designed for tracking humans. Fortunately, it confirms that you are, in fact, a human.",
                "remark": "This was developed by Dr. Helco! It detects if there are any humans near you. I wonder why he'd need it..."
            },
            {
                "name": "\"Kaching!!!\" silencer",
                "personnel": "meme",
                "description": "A golden \"silencer.\" Lets you defeat enemies with the power of capitalism.",
                "remark": "This was developed by Meme! It silences your gun shots with the sound of money."
            },
            {
                "name": "Fish",
                "personnel": "b6",
                "description": "It goes without saying.",
                "remark": "This was made with b6 in mind. It looks nothing like b6."
            },
            {
                "name": "Sentience",
                "personnel": "aikha",
                "description": "An eyeball that embeds itself near the front of the gun. It squelches whenever it looks around.",
                "remark": "This was developed by Dr. Aikha. To quote, \"We here at VAC Foundation like to ensure that our weapons are in pain.\" Maybe I should look into that."
            },
        ],
        "Lethality Upgrades": [
            {
                "name": "Sniper scope",
                "personnel": "syg",
                "description": "An oversized sniper scope, perfect for long-range encounters. Remember to hold shift while aiming to stabilize.",
                "remark": "This was personally requested and throughoutly tested by Dr. Syg."
            },
            {
                "name": "Flamethrower",
                "personnel": "firewal",
                "description": "A miniature yet highly lethal flamethrower. Flash your enemies an enthusiastic thumbs up as you scorch them alive.",
                "remark": "This was made by the great Dr. Firewal. Every purchase of this upgrade saves one Walbot from poverty."
            },
            {
                "name": "Green laser",
                "personnel": "moon",
                "description": "A bright green laser cannon. You have a feeling it will indiscriminately annihilate everything in its path.",
                "remark": "A laser inspired by our janitor! Unfortunately, the beam is so powerful that it keeps travelling indefinitely."
            },
            {
                "name": "Egg",
                "personnel": "egg",
                "description": "Egg. Unfortunately, this one didn't graduate from Harvard law.",
                "remark": "Sourced locally! Works wonders as ammunition as well as an emergency snack."
            },
            {
                "name": "Hamp certified sharpened spoons",
                "personnel": "hampter",
                "description": "Spoons with their heads gnawed down. They actually look remarkably lethal.",
                "remark": "All hand-crafted by Hamp herself!"
            },
            {
                "name": "Divorce papers",
                "personnel": "paul",
                "description": "An lengthy document detailing the divorce between Paul Demure Johnson and their ex-wife. You have no idea what tactical advantage this would give you in a battle.",
                "remark": "I don't know why this is here, actually."
            },
            
        ],
        "Decorations": [
            {
                "name": "Glow in the dark stickers",
                "personnel": "lee",
                "description": "Small golden stars that you can plaster around your gun. May or may not cause hand cancer, if that's a thing.",
                "remark": "Lets you find your gun in the dark! Unfortunately, it also lets your enemies find your gun in the dark."
            },
            {
                "name": "Star charm",
                "personnel": "caffi",
                "description": "It reminds you of the stars in Caffi's hair. She'll never let you live this down if she sees you with this.",
                "remark": "Designed by Caffi herself!"
            },
            {
                "name": "Bell",
                "personnel": "jessie",
                "description": "It makes a cute little jingle whenever it moves. This would definitely not put you at a disadvantage in a real combat situation.",
                "remark": "Ding ding!"
            },
            {
                "name": "Bandages",
                "personnel": "venture",
                "description": "...Are these used?",
                "remark": "They look cool. One could argue, at least."
            },
            {
                "name": "Cool mustache",
                "personnel": "alex",
                "description": "A piece of black, roughly-cut construction paper in the shape of a mustache. You almost gave yourself a paper cut handling it.",
                "remark": "This barely compares to a fraction of a fraction of the Founder's greatness.",
            },
            {
                "name": "Miku paint",
                "personnel": "deceased",
                "description": "Is that popular Japanese virtual idol Hatsune Miku?!?!",
                "remark": "Miku miku ooeeoo!"
            },
            {
                "name": "Pebbles keychain",
                "personnel": "ryz",
                "description": "An incredibly cool keychain of an incredibly cool goose wearing incredibly cool sunglasses. HONK!!!!!!!!",
                "remark": "Make sure to feed it bread on the daily."
            },
        ],
    }

    gun_img_zorders = {
        "chan": 7,
        "helco": 7,
        "uriel": 7,
        "lee": 7,
        "jessie": 6,
        "caffi": 6,
        "alex": 6,
        "syg": 6,
        "venture": 5,
        "aikha": 5,
        "deceased": 4,
        "gun": 3,
        "water": 3,
        "b6": 3,
        "firewal": 2,
        "moon": 2,
        "ryz": 2,
        "meme": 0,
        "hampter": 0,
        "egg": 0,
        "paul": -1,
    }


    def get_addon_path(addon):
        if addon == "b6":
            return gun_img_path + "b6.png"
        elif addon == "gun" or addon == "water":
            if "b6" in comgun_addons or gun_display_hovering == "b6":
                return ""
            elif addon == "gun":
                return gun_img_path + "gun.png"
            else:
                return gun_img_path + "gunwater.png"
        elif addon == "deceased":
            if "b6" in comgun_addons or gun_display_hovering == "b6":
                return gun_img_path + "deceased_b6.png"
            elif gun_base == "water":
                return gun_img_path + "deceased_gunwater.png"
            else:
                return gun_img_path + "deceased.png"
        elif ("b6" in comgun_addons or gun_display_hovering == "b6") and (addon == "alex" or addon == "venture"):
            return gun_img_path + addon + "_b6.png"
        else:
            return gun_img_path + addon + ".png"

    def sort_by_zorders(arr):
        rv = []
        arr_clone = arr[:]
        while arr_clone:
            min_zorder = gun_img_zorders[arr_clone[0]]
            min_index = 0
            for i, x in enumerate(arr_clone):
                if gun_img_zorders[x] < min_zorder:
                    min_index = i
                    min_zorder = gun_img_zorders[x]
            
            rv.append(arr_clone[min_index])
            arr_clone.pop(min_index)
        
        return rv


transform fade_in_out:
    alpha 0.3
    ease 1.5 alpha 0.7
    ease 1.5 alpha 0.3
    repeat

screen gun_display_screen:
    on "show" action [SetVariable("gun_display_page", 0), SetVariable("gun_selected_item_personnel", ""), SetVariable("gun_display_current_description", "Hover over an item to see its description."), SetVariable("speaking_char", ""), SetVariable("gun_display_hovering", "")]

    vbox:
        xalign 0.9
        yalign 0.0
        spacing gui.choice_spacing

        hbox:
            xalign 0.5
            spacing 120
            ypos 150
            xsize 630
            text gun_display_current_page_title:
                size 50
                xsize 450
                xalign 0.0
                yalign 0.5
            textbutton "Back":
                style "choice_button"
                xalign 1.0
                xsize 150
                action Jump("comgun_custom")

        $ gun_display_start = gun_display_page * gun_display_display_per_page
        $ gun_display_end = gun_display_start + gun_display_display_per_page
        $ gun_display_displayed_items = gun_items[gun_display_current_page_title][gun_display_start:gun_display_end] 
        vbox:
            ypos 150
            xalign 0.5
            for item in gun_display_displayed_items:
                textbutton item["name"]:
                    sensitive item["personnel"] not in comgun_addons
                    xsize 700
                    xalign 0.5
                    style "choice_button"
                    hovered [SetVariable("gun_display_current_description", item["description"]), SetVariable("gun_display_hovering", item["personnel"])]
                    unhovered [SetVariable("gun_display_current_description", "Hover over an item to see its description."), SetVariable("gun_display_hovering", "")]
                    action [SetVariable("gun_selected_item_personnel", item["personnel"]), SetVariable("gun_display_current_remark", item["remark"]), Jump("gun_remark")]

    hbox:
        xalign 0.957
        spacing 700
        ypos 440

        textbutton "<":
            xsize 78
            ysize 78
            xalign 0.0

            text_xalign 0.5
            action SetVariable("gun_display_page", gun_display_page - 1)
            sensitive gun_display_page != 0
            idle_background "gui/button/choice_small_idle_background.png"
            hover_background "gui/button/choice_small_hover_background.png"
            insensitive_background "gui/button/choice_small_insensitive_background.png"

        textbutton ">":
            xsize 78
            ysize 78
            xalign 1.0
            text_xalign 0.5
            action SetVariable("gun_display_page", gun_display_page + 1)
            sensitive gun_display_page != int(len(gun_items[gun_display_current_page_title]) / gun_display_display_per_page)
            idle_background "gui/button/choice_small_idle_background.png"
            hover_background "gui/button/choice_small_hover_background.png"
            insensitive_background "gui/button/choice_small_insensitive_background.png"
    
    window:
        id "what"
        text gun_display_current_description style "say_dialogue"
        background Image("gui/textbox.png", xalign=0.5, yalign=1.0)
    
    fixed:
        xalign 0.1
        yalign 0.25
        xsize 875
        ysize 625
        image Image(gun_img_path + "/gun_backdrop.png")

        $ comgun_addons_sorted = comgun_addons[:]
        $ comgun_addons_sorted.append(gun_base)
        if gun_display_hovering:
            $ comgun_addons_sorted.append(gun_display_hovering)
        $ comgun_addons_sorted = sort_by_zorders(comgun_addons_sorted)
        $ print(comgun_addons_sorted)

        for addon in comgun_addons_sorted:
            $ gun_addon_path = get_addon_path(addon)
            if gun_addon_path != "":
                if addon == gun_display_hovering:
                    image Image(gun_addon_path) at fade_in_out
                else:
                    image Image(gun_addon_path)
                    
label fixed_event_company_issued_gun:
    scene bg hr office
    image eggcase = "images/cgs/gun_egg_case.png"
    image egggun = "images/cgs/gun_egg_gun.png"

    n "You're getting your company issued gun today! Finally!"
    n "You will now have a way to defend yourself against the anomalies and people! No longer shall you live in fear for your life!"
    show egg at appear(y_align = 0.3)
    egg "Hello, your name?" #egg assistant
    player "It's [player_name]."
    show egg at disappear
    n "You watch as The Egg floats off its assistant's head, levitates through the air, and lands on the side of the cabinets. It slides into one of the drawers through the slim crack and it pops open."
    n "The Egg reappears out of the drawer, now larger and rectangle shaped." 
    show eggcase:
        zoom 0.5
        xalign 0.5
    show egg at appear(y_align = 0.3)
    n "It floats down on the table and reveals the content in its stomach. It's a metal case, just like the ones from the movies."
    hide eggcase
    n "You open the case. A plain pistol lies in the foam."
    n "You reach out to grab it when The Egg hops onto the upper half of the case, slamming it shut. It smiles at you and your fingers that were two inches from being sandwiched by the case."
    egg "Apologies. Before we can give you the gun, we must conduct a simple questionnaire to determine whether you are capable of responsibly owning and handling a company gun."
    player "I thought all employees are delegated one."
    egg "That is correct. The outcome of this questionnaire will simply dictate which security level arms you can be assigned."
    $ gun_sanity_points = 0
    egg "First question:"
    menu:
        egg "Under what situations can you fire your company issued gun?" 
        "Situations above level 3 emergencies":
            $ gun_sanity_points -= 1
            egg "mhm."
        "When I feel my life is threatened":
            $ gun_sanity_points -= 1
            egg "mhm."
        "Situations above level 4 emergencies":
            $ gun_sanity_points += 1
            egg happy "mhm."
        "When I feel like it":
            $ gun_sanity_points -= 1
            egg sad "mhm."
    egg neutral "Question two:"
    menu:
        egg "What are appropriate targets for shooting?"
        "Anomalies":
            $ gun_sanity_points -= 1
            n "The Egg wobbles."
        "Co-workers":
            $ gun_sanity_points -= 1
            n "The assistant shivers."
        "Both":
            $ gun_sanity_points += 1
            n "The Egg and the assistant both shift slightly away from you."
        "Myself":
            $ gun_sanity_points -= 1
            n "The Egg seems to look concerned despite wearing the same smile."
    egg neutral "Last question:"
    menu:
        egg "Where do you aim your first shot?"
        "The ceiling - I fire a warning shot first.": 
            egg "hm."
            $ gun_sanity_points -= 1
        "At limbs (or anomalous equivalent) - it is best to incapacitated threats.":
            egg happy "hm."
            $ gun_sanity_points += 1
        "The head - danger should be eliminated as soon as possible.":
            egg "hm."
            $ gun_sanity_points += 1
        "Aim?":
            egg sad "mhm."
            $ gun_sanity_points -= 1
    if gun_sanity_points < 0:
        show egg at move_to(x_align = 1.5, duration = 1.5)
        n "The Egg re-swallows the case and returns it into the cabinet." 
        show egggun:
            zoom 0.5
            xalign 0.5
        show egg:
            xalign 0.5
        n "It returns, this time gun shaped."
        n "It drops the gun in front of you. It's a watergun."
        hide egggun    
        egg "We have decided that you're qualified for a company issued water gun."
        player "A water gun?? How am I supposed to defend myself with just a water gun???"
        egg happy "Do not worry, we also have a variety of add-ons to customize every employee's gun to their own needs."
        egg neutral "Or if you cannot accept this gun, you can also choose to not take a gun."
        n "You decide to settle for the water gun. Perhaps the upgrades can still save you in the events of a life threatening incident."
        $ gun_base = "water"
    else:
        n "The Egg floats back on top of its assistant's head. It smiles at you satisfied."
        egg "This is now yours! We also offer add-ons to customize each employee's gun to their own needs."

        n "The assistant directs you towards a shelf that you can swear wasn't there before."
        #show gun cg, customization screen starts
        egg "We have Additional functions, Lethality upgrades, and Decorations."
        egg "You can pick 3 total for your gun. Any additional add-ons will cost extra and will be deducted from your salary."
        $ gun_base = "gun"
    $ n_o_gun_addons = 0
    $ comgun_addons = []

    # add chibi heads to choices! AHHHHHHHHHHHHH
    label comgun_custom:
        menu:
            n "Choose a category:"
            "Additional functions":
                jump comgun_af
            "Lethality upgrades":
                jump comgun_lu
            "Decorations": 
                jump comgun_dec
    label comgun_af:
        $ gun_display_current_page_title = "Additional Functions"
        call screen gun_display_screen

    label comgun_lu:
        $ gun_display_current_page_title = "Lethality Upgrades"
        call screen gun_display_screen

    label comgun_dec:
        $ gun_display_current_page_title = "Decorations"
        call screen gun_display_screen

    label gun_remark:
        # show cg
        egg "[gun_display_current_remark]"
        # hide cg
        jump gun_confirm

    label gun_confirm:
        menu:
            n "Do you want this upgrade?"
            "Yes":
                $ comgun_addons.append(gun_selected_item_personnel)
                $ update_character_points({gun_selected_item_personnel: 2})
                $ n_o_gun_addons += 1
                if n_o_gun_addons >= 3:
                    jump comgun_end
            "No":
                #remove cg
                egg "Take your time picking!"
        
        if gun_display_current_page_title == "Additional Functions":
            jump comgun_af
        elif gun_display_current_page_title == "Lethality Upgrades":
            jump comgun_lu
        else:
            jump comgun_dec

    label comgun_end:
        # hide cg
        egg "That's three add-ons! If you want to add anymore, each is about...three months of your pay."
        egg happy "Please take utmost care and responsibility of this company property. We will not reissue another gun for free if your gun is damaged or lost."
        egg "At least, not after Dr. Deceased kept on eating theirs."
        
        scene bg hallway
        n "You hold your new gun like it's your newborn child."
        n "It will surely keep you safe."
        n "For the first time, you felt comfort since working here."
        if "chan" in comgun_addons and "helco" in comgun_addons:
            n "Suddenly, both the anomaly radar and the human radar start flashing. You see a dot matching on both radar a few meters behind you."
            n "The anomaly radar emits a piercing scream resembling Ethy's, while the human radar blip-blobs."
        elif "chan" in comgun_addons and "helco" not in comgun_addons:
            n "Suddenly, the anomaly radar lets out a piercing scream resembling Ethy's. You see a dot on the radar a few meters behind you."
        elif "helco" in comgun_addons:
            n "Suddenly, the human radar begins blip-blobing. You see a dot on the radar a few meters behind you."
        show deceased at appear
        deceased "Oh hey [player_name]! What are you doing at HR?"
        n "You see their head turns towards what you're cradling in your arms. Your grip tightens."
        deceased happy "OH! You got your company issued gun!"
        deceased "The company benefits here sure are great, eh?"
        show deceased happy:
            linear 1.0 zoom 1.2
        n "They inch closer to you. Your parental instincts demand you to run."
        deceased "What upgrades did you get? Can I have a look?"
        show deceased happy:
            parallel:
                linear 1.0 zoom 1.4
            parallel:
                linear 1.0 yalign 0.0
        menu:
            n "They reach their arm forward, about to snatch your gun."
            "Run":
                hide deceased
                n "You decided to turn around and flee. You hear the sounds of rapid footsteps and crows cackling behind you."
                if "ryz" in comgun_addons:
                    n "Pebble's keychain makes a HONK! at your every step, as if shaming you for your cowardice."
                deceased "Hey where are you going, [player_name]? I just want a bite- I mean to look!"
                n "It seems you have overestimated the capability of the gun."
            "Shoot":
                $ shake_screen()
                n "In a panic, you test out your new gun."
                if "meme" in comgun_addons:
                    n "The sound of hitting jackpot at the casino rings out from the silencer."
                if "egg" in comgun_addons:
                    if "firewal" in comgun_addons and "hampter" in comgun_addons:
                        n "You shoot an assortment of ammunition from your gun."
                        n "The sharpened spoon cracks the egg. The flamethrower sets the egg remnants ablze and a burning smell fills the air."
                        n "The now burnt egg residue lands on Dr. Deceased's goggles."
                    elif "hampter" in comgun_addons:
                        n "You shoot an assortment of ammunition from your gun."
                        n "The sharpened spoon cracks the egg. The egg white flys out and slops onto Dr. Deceased's face."
                    elif "firewal" in comgun_addons:
                        n "The flamethrower roars as you shoot the egg at Dr. Deceased."
                        n "It smacks them hard in the forhead and cracks, revealing a perfectly \"boiled\" egg."
                    else:
                        n "You shoot the egg at Dr. Deceased. It cracks on their forhead. The egg white slops down their mask."
                elif "firewal" in comgun_addons:
                    if "hampter" in comgun_addons:
                        n "You shoot the sharpened spoon at Dr. Deceased. It glows red from being heated by the flames."
                        n "It stabs right through their left goggle."
                    if "b6" in comgun_addons:
                        n "The fish shoots fire form its mouth. The smell of fried fish hits your nose."
                        n "Unfortunately, Dr. Deceased is just a step too far for the tip of the flame to reach."
                    else:
                        n "The fire from the flamethrower shoots at Dr. Deceased. Unfortunately, they're just a step too far for the tip of the flame to reach."
                elif "hampter" in comgun_addons:
                    n "You shoot the sharpened spoon at Dr. Deceased. It stabs right through their right goggle."
                if "moon" in comgun_addons:
                    if "egg" not in comgun_addons and "firewal" not in comgun_addons and "hamp" not in comgun_addons:
                        n "A green beam of light pierce through Dr. Deceased's forhead and through the wall at the end of the corridor."
                        n "You hear sounds of beaker breaking from that direction. The fire alarm starts going off."
                    else:
                        n "The laser finally finishes charging and activates. A green beam of light pierce through Dr. Deceased's forhead and through the wall at the end of the corridor."
                        n "You hear a faint scream from that direction. It appears that the laser shot more than Dr. Deceased."
                else:
                    if gun_sanity_points < 0:
                        if "b6" in comgun_addons:
                            n "Your fish spits water at Dr. Deceased's face. It does nothing to stop the approaching plague doctor."
                        else:
                            n "Water squirts from the gun onto Dr. Deceased's face. It does nothing to stop the approaching plague doctor."
                        if "paul" in comgun_addons:
                            n "In your last-ditch effort, you throw the divorce papers at Dr. Deceased. It becomes soaked by the water and sticks on their mask."
                        n "Only after you ran out of water in your watergun did you realize what you're done."
                        n "Dr. Deceased remains unscartched, minus being drenched."
                        jump gun_continue
                
                n "Only after the gun shot did you realize what you're done."
                n "To your surprise, Dr. Deceased seems fine. They aren't even bleeding."
                
                label gun_continue:
                    deceased neutral "...Did you just shoot at me?"
                    n "You feel as if the temperature has droped by 50 degrees. The plague doctor mask suddenly looks a lot more intimidating staring down at you."
                    n "Uh oh. It seems you're about to lose your prized weapon."
                    deceased "..."
                    deceased happy "Well, if it's a gun fight you want, I have a gun too!"
                    show deceased happy:
                        parallel:
                            linear 1.0 zoom 1.0
                        parallel:
                            linear 1.0 yalign 1.0
                    n "Dr. Deceased begins coughing uncontrollably. After a few cough, they throw up a gun out of their beak. A much larger gun, with almost every upgrade you saw back in The Egg's office. Then they back up a bit."
                    deceased "They won't give me a new gun, so you're stuck with this one I had for a snack last week. Don'y worry, it still has full ammo!"
                    deceased "On the count of three! We'll take a shot at each other and see who hits more! Bonus points for the head!"
                    deceased neutral "Three..."
                    deceased "Two..."
                    show deceased happy at disappear
                    n "You turn and run without waiting to hear \"one\"."
                    n "It seems like your gun will not be able to keep you safe here."




