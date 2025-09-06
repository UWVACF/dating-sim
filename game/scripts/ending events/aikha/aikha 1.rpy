image aikha_ending = "images/cgs/aikha_ending.png"

label ending_event_aikha_1:
    scene bg cubicle
    with default_fade
    n "57...58...59..."
    n "The clock hits 5:00! You're finally free."
    n "Free from this bizarre place. Free from its...questionably legal practices."
    n "Most importantly, free from its-"
    show aikha at appear
    aikha "Oh hey, new recruit!"
    n "...personnel."
    aikha "Looks like you're off the clock now, huh?"
    player "Yeah, my internship is finally over."
    aikha "Congrats! It's been a really weird time, hmm?"
    player "Yeah, saw a bunch of crazy shit here."
    aikha happy "Crazy shit you {i}won't{/i} be telling anybody else, right?"
    player "Yeah! Yeah. My lips are sealed."
    aikha neutral "Perfect!"
    aikha "Got any plans?"
    player "Mmmm..."
    player "Nah. Not really."
    aikha "Great! Come with me."
    player "...?"
    n "Dr. Aikha practically drags you to their office."
    show bg office enter
    aikha "So I have a proposition for you!"
    player "I'm listening."
    aikha "It's quite easy, really."
    aikha happy "Won't even require much effort on your part!"
    player "Uh huh."
    aikha neutral "So basically..."
    aikha happy "Be my lab rat!"
    player "..."
    player "...What?"
    aikha neutral "You heard me!"
    aikha "No effort on your part, really."
    aikha "Just need to come in every day, same time as usual, and let me just inject a bunch of medicines and chemicals into you!"
    menu:
        aikha happy "What do you say?"
        "Yes!":
            jump ending_aikha_yes
        "NO!":
            jump ending_aikha_no
    
    label ending_aikha_yes:
        player "Sure."
        n "...What?"
        aikha "Oh, actually?"
        aikha panic "That was surprisingly easy, actually."
        aikha neutral "Okay, just sign here, here and here... you can read the documents if you want, they're not that important-"
        n "Dr. Aikha hands you a handful of documents, and you compliantly sign all of them, back to back."
        n "Skimming the documents, you see clauses about signing the rights of your life away, not being allowed to sue, etc, etc."
        n "A bunch of unimportant legal jargon you don't really care about, really."
        n "Once you finish signing everything, you hand it back to Dr. Aikha."
        aikha happy "Perfect!"
        aikha neutral "You start Monday, 9:00. Don't be late!"
        player "Yeah, see you."
        scene bg office
        with default_fade
        n "And thus ended your internship at VACF, and began your full-time position as a guinea pig."
        show aikha_ending:
            xalign 0.5
            yalign 0.3
        n "You were injected with many strange substances, many of which caused you indescribable pain."
        n "You were compensated fairly for your agony, of course, with a generous six-figure salary."
        n "Unfortunately, you didn't get to live long enough to spend it all."
        n "You passed away after only two years at your job, due to a failed experiment where Dr. Aikha tried to give you more hearts."
        n "R.I.P. [player_name]."
        return

    label ending_aikha_no:
        player "Uhh, no, thanks."
        player "Thanks for the offer, I guess."
        aikha sad "too bad, too bad."
        aikha "Are you certain?"
        player "Yes. Very certain."
        aikha neutral "Well, in that case..."
        aikha "See you never!"
        show bg hallway
        n "And thus ended your internship at VACF."
        n "You found a job elsewhere, at some corporate 9-5, where you lead an uneventful life and filled your veins with coffee."
        n "Occasionally, you think back to Dr. Aikha's offer and wonder what your life would've been had you accepted."
        n "But there's no point thinking about that now, is there?"
        return