label day_event_fluke_cake:
    scene bg hallway
    n "You're on your way back after a conference when you hear loud cheering from the direction of your office."
    $ shake_screen(duration=1.0, preset="rumble", persist=2)
    crowd "HAPPY BIRTHDAY!!!"
    n "Oh shoot. It's Josh's birthday today."
    n "You know, Josh? The one who treated you to 50 coffees? The one who covered for you the day your cat was sick? Also the day that the newest Mimtemdo Swap 2 arrived and you wanted to go home early?"
    n "You remember them? Right?? Right???"
    n "They told you it's their birthday today and even invited you to their birthday party!"
    n "Listen, they're cheering. Which means it's happening right now."
    n "You have to do something. You can't show up empty handed. That would make you a horrible person."
    n "Perhaps you can go scramble for a gift card during your break, which is now. Showing up late with a gift is better than without one."
    n "You look for the closest Timothy Hort on your phone. Two hours away. This is what you get for working in the middle of nowhere."
    n "Or, maybe you can do some arts and crafts in the lounge. Print out a birthday card and sign it. No one will know."
    n "You hurry into the lounge, praying that no one is there."

    scene bg lounge
    # cg cake
    n "Just as you're trying to get the printer to work, you notice a mysterious cake on the counter."
    n "You check for a nametag for its owner. There isn't one."
    n "You look back at the printer, which is still refusing to turn on. An idea forms in your head."
    n "As the old saying goes: Finders keepers! This is the perfect solution to your gift problem."

    with default_fade
    n "You barely manage to sign your name on the cake box when the crowd migrates into the lounge."
    show aikha at appear(x_align = 0.75)
    show alex happy:
        xzoom -1.0
        appear(x_align = 0.25)
    show syg:
        xzoom -1.0
        appear(x_align = -0.05)
    show uriel at appear(x_align = 1.05)
    person "Ohh!! Is that cake you brought, [player_name]?"
    show aikha pensive
    player "...Yep!!"
    n "You feel Dr. Aikha's forty-six pairs of eyes scan you and squint. You do your best to ignore it."
    alex "Oooo. What flavour is it?"
    player "It's...Birthday cake flavoured?"
    alex "Hahaha you're funny!"
    n "You force a smile. Maybe you should've sneaked a bite earlier instead of spending the time doing a fancy signature."
    josh "Thank you so much, [player_name]!"
    n "You flash Josh a smile as you watch them make their way to the cake. You will now be remembered as a great person."
    # cake slice cg 
    n "Josh cuts the cake and the crowd gasps."
    josh "Wow, you must have put in a ton of effort in making this! There's so many flavours!!"
    josh "No wonder you said it's birthday cake flavour! It was a surprise all along!"
    n "You feel a bead of sweat slide down from your forehead. You are starting to have a bad feeling about this."
    josh "[player_name], since you made it, you should be the one to cut this! Tell us what flavours are there!"
    n "You reluctantly shuffle over in front of the cake. The crowd forms an organized file in front of you."
    $ cake_list = ["Blood Velvet", "Dirt (organic topsoil)", "Eyeball (filling)", "Turnip", "Egg", "Strawberry Tallcake", "Sponge (the washing kind) cake", "Cinco Leche (almond, soy, woolly mammoth, walnut, expired)", "Angel Dust (cocain)", "Sheet cake (papersheets)", "Black Forest (with wood, sawdust and rice crispies)", "Ice Cube cake (now just water)", "Invisible And Incoporal cake (air)", "Pineapple Right-side-up cake", "Pop cake (with jam filling and a popsticle stick)", "Chocolate Coke cake (chocolate flavoured cocain)", "Dehydrated cake (0% water)", "Bun cake (a bun that is cake shaped)", "Butter cake (a block of unsalted butter)", "Pound cake (british currency)", "Catapilliar cake (no catapilliars are harmed in the process of making this)", "Cheesecake (a wheel of brie, not for those latose intorlerant)", "Coffee cake (just coffee grounds with whipped cream on top)", "Marble cake (hollow cake with round marble filling)", "Singlular confetti cake (with a singular sprinkle)"]
    $ cake_this_list = random.sample(cake_list, 5)
    n "You cut a slice. It perfectly seperates a slice of flavour. Weird."
    player "This is a...[cake_this_list[0]]?"
    n "You have no idea what it actually is."
    player "And this is, uh, a [cake_this_list[1]]."
    n "The cakes are looking weirder. You're unsure if what you made up would even be tasty."
    player "This one here, it's a...[cake_this_list[2]]? I think."
    n "The crowd looks delighted, though."
    player "Here, a smaller slice of [cake_this_list[3]] for you."
    n "You would never eat that."
    player "Uh this one? Are you allergic to [cake_this_list[4]]..?"

    scene bg lounge
    with default_fade
    show alex at appear
    n "Your hands shake as you scoop up the last piece and serve it to the Founder himself."
    n "At least this cake looks normal. Just a regular birthday cake with sprinkles."
    alex "Ooo. What is this cake?"
    player "...Birthday cake."
    alex happy "Haha! If you say so."
    n "He gives you a wink. Or, you think he gave you a wink behind those opaque goggles."
    n "You watch as Dr. Alex takes a bite out of the cake. Then he starts coughing and sputtering."
    $ shake_screen(duration=0.3, strength=7, repeat=7, interval=0.3)
    alex panic "{i}SCOFF{/i} I'm {i}COUGH{/i} suffocat- {i}COUGH{/i} -ting!"
    $ shake_screen(duration=0.3, strength=7, repeat=5, interval=0.6)
    alex "You're right {i}COUGH{/i}...It is birthday {i}COUGH{/i} cake...I'm allergic to {i}SCOFF{/i} sprinkles..."
    show alex panic at disappear
    n "He collapses on the ground."
    n "Oh shit. Did you just kill the Founder??"
    n "The immortal Founder. Killed by mere sprinkles."
    n "You look around, but everyone else seems unbothered."
    show hampter at appear
    pause 0.5
    hampter panic "Oh no! Am I too late for cake??"
    n "Hampter teleports in front of you out of nowhere."
    player "Uh, Dr. Alex just got the last slice. But he uh..."
    hampter surprise "Oh!"
    show hampter surprise at disappear
    # dr alex on the floor cg
    n "You see Hampter hop towards Dr. Alex's ragdolled body that is still hyperventillating."
    n "She jumps right over his head and land next to the plate of unfinished birthday cake."
    show hampter happy at appear
    hampter "Don't mind if I do!"
    n "Hampter swallows the leftover cake in one mouthful. She rolls onto her back and lies contently next to Dr. Alex's shaking arm."
    player "...Is the Founder okay..?"
    hampter "Hm? Oh, he's immortal, so he'll be fine!"
    n "He doesn't look fine."
    show hampter happy at disappear
    player "..."
    n "Out of the corner of your eye, you spot a diligent snail making it's way over to Dr. Alex."
    $ shake_screen(duration=0.1, repeat=7, interval=0.4)
    n "You are about to comment on it when Dr. Aikha punts it like a soccer ball. Then they whip their gun out and shoot it repeatedly."
    aikha "Don't mind me! I'll take care of it!"



### unnamed co-worker birthday, you find the cake and pretend it's yours (present)
### effects:
# speak/do everything backwards (uriel)
# antis ACE
# b&w (syg)
# body swap (hamp & founder alex, founder alex now on all four, hamp on 2 legs and hands together)
# egg -> gets a call, your law degree has been revoked by harvard -> ... turns into stock image of a regular fried egg
# meme -> speaks in only memes
# caffi -> boomer
#
#
# hamp, syg, alex, uriel, egg, meme, caffi, aikha
## pairs: pick someone to hang out with
    # hamp & founder - body swap problem
    # caffi & meem - translate their communication
    # ai & uriel - deal with ace (good luck soldier), help uriel..?
    # egg & syg - the egg just phases out of existance, syg is depressed (like extra depressed)..?


'''
you hear form the distance at your cubical "happy bday!!!!'
oh no
that co-worker who has been helping you the whole time and mentored you and whom you've developed a wonderful working relationship with! it's their birthday!!! and you don't have anything to show for it you heartless bastard!
how could you forget, when they told you it's coming up soon and even invited you to their birthday party! which is happening, today!
dang it
better go scramble for a gift during lunch break. do you think a tims hortan card is good enough?
nvm, the closest tim hortan is an hour drive away, and your lunch break ends in 30 minutes.
maybe you can do some arts and crafts in the lounge. Just print out a birthday card and sign it. No on will know.
oh wait, there's a cake on the counter. You check it for a name of an owner. There is none. 
Well it's yours now! how convinient.

you're in the lounge. suddenlly you can an email telling eveyone but the person to get in the lounge for the party. roll a deception check. Nat 20!
Dr. Aikha eyes you, raising an eyebrow. But they didn't ask. What's the worse that will happen? Ace.
what flvor is it? you look down at the pristine icing on the cake. it's birthday cake flavoured. It's a birthday cake that is birthday cake flavoured, as all birthday cakes should be.
How convinient that nobody has an allergy to birthday cakes.

slice cake open, all sorts of flavours/colors
wow you must have put a lot of effort in this
start desperatly listing the filling and flavours: blood velvet, dirt, eyeball filling, turnip, egg, strawberry tall cake, sponge (non-edible) cake, cinqo leche (almond, soy, expired, ), angel dust (cocain), sheet cake (paper), black forest (with wood, sawdust and rice crispies), ice cube cake (it's just ice, now water), invisible and incoporal cake (it's just air), pinapple right-side-up cake, pop cake (with jam and a popsticle stick so you can pick it up to eat it), chocolate coke cake (also cocain), dehydrated cake, bun cake (a bun that is cake shaped), butter cake (it's just butter), pound cake (british currency), catapilliar cake (no catapilliars are harmed in the process of making this), cheesecake (a wheel of brie, not for those latose intorlerant), coffee cake (it's just coffee grounds with wipped cream on top), marble cake (hallow cake with round marble filling), and...singlular confetti cake (25)

you serve the cakes. This party has gone well and you are now remembered as a great friend. Surely nothing will go wrong.
(uh oh, the founder seems to be allergic to sprinkles. luckily, it's a sprinkly free confetti cake. so it is edible to those with sprinkle allergies.) > last slice
hamp eats sprinkle leftovers
pop! uh oh.

chaos yippie

birthday person (mentor) disappears :( They'll be fine. Probably. 

'''

