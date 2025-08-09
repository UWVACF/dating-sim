label day_init:

    # priority of calling events:
    # chain event
    # ending event
    # standard event
    python:
        today_intro_label = "default_intro"
        today_event_label = "day_event_not_found"
        today_event = None
        today_outro_label = "default_outro"


        if game_mode == "debug":
            type_of_event = renpy.input("Choose either \"day\", \"fixed\" or \"ending\".").lower()
            while type_of_event != "day" and type_of_event != "ending" and type_of_event != "fixed":
                renpy.notify("Type either \"day\", \"fixed\" or \"event\"!")
                type_of_event = renpy.input("Choose either \"day\", \"fixed\" or \"ending\".").lower()

            if type_of_event == "day":
                today_event_label = renpy.input("Choose a day event label to see:")
                while not today_event_label or not filter_events(label = today_event_label):
                    renpy.notify("Event not found (don't include \"day_event_\")")
                    today_event_label = renpy.input("Choose a day event label to see:")
                
                today_event = filter_events(label = today_event_label)[0]
                today_event_label = "day_event_" + today_event_label
                if today_event.intro_label:
                    today_intro_label = today_event.intro_label
                if today_event.outro_label:
                    today_outro_label = today_event.outro_label
            elif type_of_event == "ending":
                today_event_label = renpy.input("Choose an ending event label to see:")
                while not today_event_label or not filter_events(events = ending_events, label = today_event_label):
                    renpy.notify("Event not found (don't include \"day_event_\")")
                    today_event_label = renpy.input("Choose an ending event label to see:")
                
                today_event = filter_events(label = today_event_label)[0]
                today_event_label = "ending_event_" + today_event_label
                if today_event.intro_label:
                    today_intro_label = today_event.intro_label
                if today_event.outro_label:
                    today_outro_label = today_event.outro_label
            else:
                today_event_label = renpy.input("Choose a fixed event label to see:")
                while not today_event_label or not filter_events(label = today_event_label):
                    renpy.notify("Event not found (don't include \"fixed_event_\")")
                    today_event_label = renpy.input("Choose a fixed event label to see:")
                
                today_event = filter_events(label = today_event_label, events = fixed_events)[0]
                today_event_label = "fixed_event_" + today_event_label
                if today_event.intro_label:
                    today_intro_label = today_event.intro_label
                if today_event.outro_label:
                    today_outro_label = today_event.outro_label
        elif game_mode == "showcase_no_intro" or game_mode == "showcase_intro":
            if showcase_events:
                today_event = showcase_events[0]
                today_event_label = "day_event_" + today_event.label
                if today_event.intro_label:
                    today_intro_label = today_event.intro_label
                if today_event.outro_label:
                    today_outro_label = today_event.outro_label
                
                showcase_events.pop(0)
            else:
                Jump("ending_event_neutral_ending")
        else:
            # call a chain event
            # assumptions: all prerequisites of the chain event are satisfied/are placed under the head of the chain
            filtered = filter_events(chain = seen_events[-1]) if seen_events else None
            if filtered:
                today_event = filtered[0]
                today_event_label = "day_event_" + today_event.label
                if today_event.intro_label:
                    today_intro_label = today_event.intro_label
                if today_event.outro_label:
                    today_outro_label = today_event.outro_label
            
            # call the ending event instead of a day event
            elif current_ending is not None and renpy.random.random() < ending_chance:
                today_event_label = "ending_event_" + current_ending
                today_event = filter_events(events = ending_events, label = current_ending)[0]
                if today_event.intro_label:
                    today_intro_label = today_event.intro_label
                if today_event.outro_label:
                    today_outro_label = today_event.outro_label
            
            # find standard events
            else:
                # chat im not doing set theory im going to commit a programming sin and repeat code
                total_weight = 0
                event_weights = [] # tuple with event, weight
                for event in filter_events(viewable_on_day = day_number):
                    fail = False # failure flag
                    # check it's compatible via prereqs and antireqs
                    if any(prereq not in seen_events for prereq in event.prereqs):
                        fail = True # missing prereq
                    elif any(antireq in seen_events for antireq in event.antireqs):
                        fail = True # any antireq present
                    else:
                        for key, val in enumerate(event.prereq_tags):
                            if key in current_tags and val < current_tags[key]:
                                fail = True # prereq tag count too low
                                break
                        
                        for key, val in enumerate(event.antireq_tags):
                            if key in current_tags and val >= current_tags[key]:
                                fail = True # antireq tag count too high
                                break
                    
                    if fail:
                        continue
                    
                    weight = base_weight
                    # award bonus weight for events with at least one honed personnel
                    if any(person in event.personnel for person in top_three_honed):
                        weight += bonus_weight_for_honed
                    
                    # award bonus weight for events depending on points of characters
                    for person in event.personnel:
                        weight += bonus_weight_per_point * characters[person][0]
                    event_weights.append((event, weight))
                    total_weight += weight
                
                # randomly choose an event based on weight
                remaining_weight = renpy.random.randint(0, total_weight)
                for event, weight in event_weights:
                    remaining_weight -= weight
                    if remaining_weight <= 0:
                        if event.intro_label:
                            today_intro_label = event.intro_label
                        if event.outro_label:
                            today_outro_label = event.outro_label
                        today_event_label = "day_event_" + event.label
                        today_event = event
                        break
            
        today_event_label = today_event_label.replace(" ", "_").lower() # just in case someone uses spaces or capitals

    # call the events (in renpy cuz call jumps to the next renpy statement, not python statement)
    $ renpy.call(today_intro_label)
    $ clear_screen_transforms()
    $ renpy.call(today_event_label)
    $ clear_screen_transforms()
    $ renpy.call(today_outro_label)
    $ clear_screen_transforms()

    "{nw}" # again, .call jumps to next renpy statement so we place a pseudo renpy statement here
    
    python:

        day_number += 1
        seen_events.append(today_event_label)

        for tag in today_event.tags:
            if tag not in current_tags:
                current_tags[tag] = 0
            current_tags[tag] += 1
        # for person in today_event.personnel: # automatically add points to characters
        #     characters[person]["points"] += 1

        # check if an ending has been reached
        if current_ending is None:
            for person, dic in characters.items():
                first_label = person + "_1"
                if first_label not in seen_events and characters[person]["has_route"] and characters[person]["points"] >= character_point_threshold:
                    # first ending label should be ending_event_(person)_1
                    current_ending = first_label
                    break
    
    # jump day_init
    if day_number < day_threshold:
        jump day_init
    else:
        jump ending_event_neutral_ending

label default_intro:
    scene bg cubicle
    show screen day_intro
    with default_fade
    $ ui.interact() 
    hide screen day_intro # i don't know how this works but it does so hopefully it stays that way (should technically be hiding it before the fade transition but it doesn't)
    return

label default_outro:
    scene bg lounge
    with default_fade
    
    # randomly choose a remark from a pool
    $ random_day_complete_remark = renpy.random.choice(day_complete_remarks)
    player "[random_day_complete_remark]"

    # randomly choose another remark from a pool
    $ random_heading_home_remark = renpy.random.choice(heading_home_remarks)
    player "[random_heading_home_remark]"
    return
