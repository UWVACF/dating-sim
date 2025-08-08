label day_event_company_issued_gun:
    scene bg hr office

    n "You're getting your company issued gun today! Finally!"
    n "You will now have a way to defend yourself against the anomalies and people! No longer shall you live in fear for your life!"
    show egg at appear(y_align = 0.3)
    egg "Hello, your name?" #egg assistant
    player "It's [player_name]."
    show egg at disappear
    n "You watch as The Egg floats off its assistant's head, levitates through the air, and lands on the side of the cabinets. It slides into one of the drawers through the slim crack and it pops open."
    n "The Egg reappears out of the drawer, now larger and rectangle shaped." 
    #rectangle egg cg????
    show egg at appear(y_align = 0.3)
    n "It floats down on the table and reveals the content in its stomach. It's a metal case, just like the ones from the movies."
    n "You open the case. A plain pistol lies in the foam."
    n "You reach out to grab it when The Egg hops onto the upper half of the case, slamming it shut. It smiles at you and your fingers that were two inches from being sandwiched by the case."
    egg "Apologies. Before we can give you the gun, we must conduct a simple questionnaire to determine whether you are capable of responsibly owning and handling a company gun."
    player "I thought all employees are delegated one."
    egg "That is correct. The outcome of this questionnaire will simply dictate which security level arms you can be assigned."
    $ gun_sanity_points = 0
    egg "First question:"
    menu:
        egg "Under what situations can you fire your company issued gun?" 
        "Situations above level 3 emergensies":
            $ gun_sanity_points -= 1
            egg "mhm."
        "When I feel my life is threatened":
            $ gun_sanity_points -= 1
            egg "mhm."
        "Situations above level 4 emergensies":
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
        # egg watergun cg
        show egg:
            xalign 0.5
        n "It returns, this time gun shaped."
        n "It drops the gun in front of you. It's a watergun."
        egg "We have decided that you're qualified for a company issued water gun."
        player "A water gun?? How am I supposed to defend myself with just a water gun???"
        egg happy "Do not worry, we also have a variety of add-ons to customize every employee's gun to their own needs."
        egg neutral "Or if you cannot accept this gun, you can also choose to not take a gun."
        n "You decide to settle for the water gun. Perhaps the upgrades can still save you in the events of a life threatening incident."
    else:
        n "The Egg floats back on top of its assistant's head. It smiles at you satisfied."
        egg "This is now yours! We also offer add-ons to customize each employee's gun to their own needs."

        n "The assistant directs you towards a shelf that you can swear wasn't there before."
        #show gun cg, customization screen starts
        egg "We have Additional functions, Lethality upgrades, and Decorations."
        egg "You can pick up to 3 total for your gun. Any additional add-ons will cost extra and will be deducted from your salary."
    $ n_o_gun_addons = 0
    $ comgun_addons = []

    # add chibi heads to choices! 
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
        $ gun_menu = 1
        menu: 
            n "Additional functions:"
            "Corporal anomaly proximity radar - chan":
                # show cg
                egg "This is developed by Dr. Chan and detects if there are any anomalies near you! Doesn't work for non corporal Cerebersites though."
                $ gun_temp = "chan"
            "Owner locator - ufo":
                # show cg
                egg "This is developed by Uriel, it tracks where you are and will alert you on your work phone if your gun gets too far away."
                $ gun_temp = "ufo"
            "Hunan proximity radar - Helco":
                # show cg
                egg "This is developed by Dr. Helco and it detects if there are any humans near you!"
                $ gun_temp = "helco"
            "\"Kaching!!!\" silencer - meme":
                # show cg
                egg "This is developed by Meme and silences your gun shots with the sound of money."
                $ gun_temp = "meme"
            "Fish. - b6":
                # show cg
                egg "This is made with b6 as inspiration. It doesn't look anything like b6."
                $ gun_temp = "b6"
            "Sentient. - aikha":
                # show cg
                egg "This is developed by Dr. Aikha. We're working on allowing it to speak on the next upgrade."
                $ gun_temp = "aikha"
        jump gun_yes_no

    label comgun_lu:
        $ gun_menu = 2
        menu: 
            n "Lethaloty upgrades:"
            "Sniper scope - syg":
                # show cg
                egg "This is requested and tested by Dr. Syg."
                $ gun_temp = "syg"
            "Flamethrower - firewal":
                # show cg
                egg "This is made by the great Dr. Firewal. Every purchase of this upgrade saves one Wal from poverty."
                $ gun_temp = "firewal"
            "Green laser - moon":
                # show cg
                n "You wonder if its range can reach the moon."
                $ gun_temp = "moon"
            "The Egg certified organic free-ranged eggs - Egg":
                # show cg
                egg "Sourced locally! Works wonder as ammunition as well as an emergency snack (raw)."
                $ gun_temp = "egg"
            "Hamp certified sharpened spoons (reusable and reloadable!) - hamp":
                # show cg
                egg "All hand-crafted by Hamp themselves."
                $ gun_temp = "hamp"
            "Divorce papers - paul":
                # show cg
                egg "I don't know why this is here, actually."
                $ gun_temp = "paul"
        jump gun_yes_no

    label comgun_dec:
        $ gun_menu = 3
        menu: 
            n "Decorations:"
            "glow in the dark stickers - lee":
                # show cg
                egg "Lets you find your gun in the dark."
                $ gun_temp = "lee"
            "star charm - caffi":
                # show cg
                n "It reminds you of the stars in Caffi's hair."
                $ gun_temp = "caffi"
            "Bell - Jessie":
                # show cg
                n "It reminds you of Dr. Jessie."
                $ gun_temp = "jessie"
            "bandages - venture":
                # show cg
                n "It just looks cool. Not very functional."
                $ gun_temp = "venture"
            "cool mustache - alex":
                # show cg
                n "This can barely compare to 1%% of the founder's greatness."
                $ gun_temp = "alex"
            "miku!!! - deceased":
                # show cg
                n "It's miku colored."
                $ gun_temp = "deceased"
            "Pebbles keychain - ryz":
                # show cg
                egg "Comes with sound!"
                roose "HONK HONK HONKKKK!!!"
                $ gun_temp = "ryz"
        jump gun_yes_no


    label gun_yes_no:
        menu:
            n "Do you want this function?"
            "Yes":
                $ comgun_addons.append(gun_temp)
                $ update_character_points({gun_temp: 2})
                $ n_o_gun_addons += 1
                if n_o_gun_addons >= 3:
                    jump comgun_end
            "No":
                #remove cg
                if gun_menu == 1:
                    jump comgun_af
                elif gun_menu == 2:
                    jump comgun_lu
                else:
                    jump comgun_dec

    label comgun_end:
        # hide cg
        egg "That's three add-ons! If you want to add anymore, each is about...three months of your pay."
        egg happy "Please take utmost care and responsibility of this company property. We will not reissue another gun for free if your gun is damaged or lost."
        egg "At least not after Dr. Deceased kept on eating theirs."
        
        scene bg hallway
        n "You hold your new gun like it's your newborn child."
        n "It will surely keep you safe."
        n "For the first time, you felt comfort since working here."
        show deceased at appear()
        deceased "Oh hey [player_name]! What are you doing at HR?"
        n "You see their head turns towards what you're cradling in your arms. Your grip tightens."
        deceased happy "OH! You got your company issued gun!"
        deceased "The company benefits here sure are great, eh?"
        show deceased happy:
            linear 1.0 zoom 1.2
            linear 1.0 yalign 1.5
        n "They inch closer to you. Your motherly instincts demand you to run."
        deceased "What upgrades did you get? May I have a look?"
        show deceased happy:
            linear 1.0 zoom 1.4
            linear 1.0 yalign 2.5
        menu:
            n "They reach their arm forward, about to snatch your gun."
            "Run":
                hide deceased
                n "You decided to turn around and flee. You hear the sounds of rapid footsteps and crows cacking behind you."
                deceased "Hey where are you going,, [player_name]? I just want a bite- I mean look!"
                n "It seems you have overestimated the capability of the gun."
            "Shoot":
                $ shake_screen()
                n "In a panic, you test out your new gun."
                # different outcomes depending on bullets/silencers...
                n "Only after the gun shot did you realize what you're done."
                n "To your surprise, Dr. Deceased seems fine, minus the hole on their forehead. They aren't even bleeding."
                deceased neutral "...Did you just shoot me?"
                n "You feel as if the temperature has droped by 50 degrees. The plague doctor mask suddenly looks a lot more intimidating staring down at you."
                n "Uh oh. It seems you're about to lose your prized weapon."
                deceased "..."
                deceased happy "Well, if it's a gun fight you want, I have a gun too!"
                show deceased happy:
                    linear 1.5 zoom 1.0
                n "Dr. Deceased begins coughing uncontrollably. After a few cough, they throw up a gun from their beak.. A much larger gun, with almost every upgrades you saw back in The Egg's office. Then they backs up a bit."
                deceased "They won't give me a new gun, so you're stuck with this one I had for a snack last week. Don'y worry, it still has full ammo!"
                deceased "On the count of three! We'll take a shot at each other and see who hits more! Bonus points for the head!"
                deceased neutral "Three..."
                deceased "Two..."
                show deceased happy at disappear
                n "You turn and run without waiting to hear \"one\"."
                n "It seems like your gun will not be able to keep you safe here."




