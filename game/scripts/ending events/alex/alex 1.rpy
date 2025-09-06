image alex_ending = "images/cgs/alex_ending.png"
label ending_event_alex_1:
    scene bg cubicle outside
    with default_fade
    n "Well. That's it."
    n "Your time here at the foundation is done."
    n "The time passed so fast, but your internship ends today."
    n "You're giving yourself a small, imaginary pat on the back for surviving all the horrors when you get a notification on your work phone."
    n "It's from Founder Alex."
    n "\"Hello, [player_name]!\""
    n "\"Please see me in my office to discuss the end of your internship.\""
    n "\"Toodles!\n-#1 Founder Alex\""
    n "..."
    n "You set off on your way towards his office." 
    scene bg hallway
    with default_fade
    n "You arrive in front of his office and knock on the door."
    alex "Come in!"
    show bg office enter
    show alex at appear
    alex happy "Ah! [player_name]! Take a seat."
    alex "How are you?"
    player "I'm good. You?"
    alex neutral "I'm quite well, thank you."
    alex happy "[player_name], I wanted to discuss your internship."
    alex "I must say, I've been {i}extraordinarily{/i} impressed by your performance here."
    alex "You were able to handle everything from interpersonal disputes to anomaly outbreaks!"
    player "Thank you, sir."
    alex neutral "And it's because of your performance that I'm offering you a full-time position at VAC Foundation!"
    player "Are you serious?"
    alex happy "Of course!"
    alex "Your job will be a little different from what you're used to, however."
    alex "You see, the position I'm assigning you to is a little...unique, to say the least."
    player "Well, what are my responsibilities?"
    alex neutral "You will have to..."
    alex happy "Defend me from a snail!"
    player "..."
    alex "..."
    player "...What-"
    alex "You know that little, immortal, ever-so-persistent snail?"
    alex "I'll need you to punt it every so often."
    player "That's all?"
    alex "That's all!"
    alex neutral "I'll send you the specifics later, but expect a six-figure salary."
    player "SIX FIGURES???"
    alex happy "Mhm!"
    alex "I would like to say, once more, [player_name], that I was very happy with your work here."
    alex "Here's to many more years to come!"
    player "Yeah...cheers..."
    show bg hallway
    show alex at disappear
    n "You quietly excuse yourself from the office."
    n "The thought of the six-figure salary has caused your eyes to glaze over."
    n "You stumble your way back to your cubicle, drooling over the virtually infinite supply of coffee a six-figure salary would net you."
    show bg office enter
    with default_fade
    show alex at appear
    n "And thus, you worked under Founder Alex."
    n "You did nothing but sit around, drink coffee and occassionally punt the snail from one end of the facility to the other."
    n "Founder Alex had you follow him everywhere, from his office to his home to a vacation in Egypt."
    show alex_ending:
        xalign 0.5
        yalign 0.3
        zoom 0.5
    n "There were a few close calls, but the snail didn't pose much of a threat otherwise."
    n "You accumulated vast amounts of wealth, and spent it all on coffee thanks to your lack of ambition elsewhere."
    n "It was a slow life..."
    n "...But it was a comfortable life."
    jump day_event_credits