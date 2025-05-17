image overlay_ai_1 = Image("images/day events/overlay ai 1.png", xpos = -100, ypos = -100, xanchor = 0.0, yanchor = 0.0)
image aikha flairup1 = Image("images/personnel/aikha/aikha flairup1.png", sprite_highlight("aikha"))
image aikha flairup2 = Image("images/personnel/aikha/aikha flairup2.png", sprite_highlight("aikha"))

label day_event_aikha_flair:

    transform bobbing(duration = 0.1):
        block:
            easein duration xalign 0.495
            pause 0.02
            easein duration xalign 0.5
            pause 0.02
            repeat

    scene bg hallway
    n "You have just finished your last errand of the day and are very excited to go home."
    n "You skip down to the path-para office to report completing the errand."
    n "You knock on the office door, which could only be opened with a path-para employee ID."
    n "..."
    n "You knock again, this time more impatiently. You really want to finish this and go home."
    show plutoes at appear(x_align = 1.0)
    n "Plutoes comes out of the office. Clearly not to answer your knocking."
    player "Is Dr. Aikha in?"
    show plutoes at move_to(x_align = -0.5)
    n "Plutoes ignores you and shrooms away."
    n "You catch the door just as it closes and piggyback in."

    scene bg office
    show aikha flairup1
    show aikha flairup1 at bobbing()
    pause 0.5
    # dark filter
    player "I've delivered the old path-para files to the archive, Dr. Aikha."
    player "Here are the trial records you wanted."
    player "Can I go home now?"
    aikha "..."
    player "Dr. Aikha?"
    aikha "..."
    show aikha flairup1 at bobbing(duration = 0.3)
    player "Helloooo?"
    aikha "..."
    # slightly darker
    n "You suddenly remember an old entry you read at the archive earlier about an anomaly that impesonates foundation personnel and eats unsuspecting coworkers."
    n "The defining traits of it are that it cannot speak, and show odd behavior patterns."
    # EVEN darker
    show aikha:
        xalign 0.5
    show aikha flairup2
    n "Uh oh, it must have spotted you."
    show aikha flairup2:
        linear 5 zoom 1.5
    n "It gets up from the seat and makes its ways towards you."
    n "You see your life flash before your eyes. Tomorrow, you'll just be a statistic on the {i}Monthly Foundation Casualty Report{/i}."

    menu:
        n "You pull out your company issued gun."
        "Shoot":
            jump ahoot
        "Shoot":
            jump ahoot
        "Shoot":
            jump ahoot
        "Shoot":
            jump ahoot 

    label ahoot:
        show layer master at shake (duration = 0.2)
        n "You shoot withuot hesitation."
        # STOP SHOOTING WHY IS IT CONTINUING
        show overlay_ai_2 onlayer top:
                alpha 0.0
                linear 0.4 alpha 1.0
        n "The figure begins melting away. You've survived another day at the foundation!"
        aikha "euuuuughhh..."
        n "Wait...Did it just make a sound..."
        aikha "euuuuugHHH..."
        n "... this might be the real Dr. Aikha."
        aikha "ARGGGGGGG...HURT....HUNGRY..."
        show aikha flairup2:
            linear 4 zoom 2
        n "Uh oh. You are about to actually get eaten, just not by a Mimimic, but Dr. Aikha."
        n "You backup against the door and try to open it. The door does not budge without an ID card."
        n "Out of the corner of your eye, you see Dr Aikha's ID wallet on the desk behind them."
        show aikha flairup2:
            linear 4 zoom 2.5
        menu:
            n "How do you get out of this?"
            "Attempt to take Dr. Aikha's wallet on the desk. Hopefully their employee badge is in there and you can use it to escape the room.":
                jump swipe_id
            "Try to reason with Dr. Aikha. Surely they're in there somewhere, right?":
                jump reason

        label swipe_id:
            show aikha at move_to(x_align = 0.2)
            n "You lunge to the side and barely dodge out of Dr. Aikha's reach."
            hide aikha
            n "Scrambling to your feet, you run towards the desk with all your might."
            n "You can hear the flesh sloping after you."
            n "You reach the wallet and grab it, knocking over 7 bottles in the process."
            n "The flesh blob quickly approaches. In a panic, you throw a chair over it and run back towards the door."
            # the chair slows down dr aikha and the player manage to gain distance, triggering pocket wal's security alert and activating him.
            return

        label reason:

            return



# end of day -> player excited to go home
# report errand at path-para
# run into weird dr ai
# plutoes leave and you entered the door that only path-para personnel badges can open - forced proximity
# finds dr aikha, who seems out of it (relaxed, auto-pilot), who doesn't respond to player
# player remember report of a "missing" anomaly that was reported to shapeshift into personnels, trick their unsuspecting coworkers and kill them. just as you think of that, dr aikha spots you and starts walking towards you, some of their eyes and seams opening
# choice:
# shoot
# shoot
# shoot (wait)
# shoot

#(wait)
#dr aikha snaps out of it and you have a nice convo and then they dismiss you. You feel closer to dr. Aikha. [+1]


#shoot
#you shoot and dr aikha doesn't go down. In fact, they are more aggravated. the seams open fully and the flesh slides across the office floor towards you.

#choice to escape:
#grab dr ai’s badge that is on the ground
#try to reason with dr ai

#grab_badge -> activates pocket wal as id leaves pocket wal’s proximity, sees what's happening, directs you to the safe, open the safe (puzzle) to find aikha’s stash of emergency eyeballs [net -1]

#try_reason -> eats your arm??? recovers??? blocks out? Eats emergency eyeballs while you bleed with a missing arm. makes you a new arm? "If you want your memory wiped, you can ask the ethic department?" [net 0]

