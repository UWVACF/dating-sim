init python:
    # helper functions

    # returns an array of events with the following properties
    # all parameters are optional - you probably only want to use one or two filters at a time, MAYBE three
    def filter_events(
        events = None, # can also specify it to be day_events (instead of remaining day events) or character_events
        label = "", # should probably only be used for character_events
        personnel = None, # array, finds event with ALL listed personnel
        viewable_on_day = 0, # finds events viewable on this day, according to see_before and see_after
        prereqs = None, # array, finds events with ALL listed prerequisite labels
        prereq_tags = None, # dictionary, finds events with ALL listed prereq tags of value at LEAST x
        antireqs = None, # array, finds events with ANY listed antireq labels
        antireq_tags = None, # dictionary, finds events with ANY listed antireq tags of value GREATER THAN x
        chain = "", # finds the UNIQUE event with that chain
        tags = None # array, finds events with ALL listed tags
    ):
        if events is None:
            events = remaining_day_events
        
        filtered = []

        label = label.replace(" ", "_")
        
        for event in events:
            if label and event.label != label:
                continue

            if personnel and not all(p in event.personnel for p in personnel):
                continue
                
            if viewable_on_day > 0:
                if event.see_before != 0 and viewable_on_day > event.see_before:
                    continue
                if event.see_after != 0 and viewable_on_day < event.see_after:
                    continue
            
            if prereqs and not all(req in event.prereqs for req in prereqs):
                continue
                
            if prereq_tags:
                if not event.prereq_tags:
                    continue
                if not all(tag in event.prereq_tags for tag in prereq_tags):
                    continue
            
            if antireqs and any(antireq in event.antireqs for antireq in antireqs):
                continue
                
            if antireq_tags:
                if any(tag in event.antireq_tags for tag in antireq_tags):
                    continue
            
            if chain and event.chain != chain:
                continue
                
            if tags and not all(tag in event.tags for tag in tags):
                continue
                
            filtered.append(event)
        
        return filtered
            
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


        if debug_mode:
            type_of_event = renpy.input("Choose either day or ending (for day and ending event respectively)").lower()
            while type_of_event != "day" and type_of_event != "ending":
                renpy.notify("Type either \"day\" or \"event\"!")
                type_of_event = renpy.input("Choose either day or ending (for day and ending event respectively)").lower()

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
            else:
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
    $ renpy.call(today_event_label)
    $ renpy.call(today_outro_label)

    "{nw}" # again, .call jumps to next renpy statement so we place a pseudo renpy statement here
    
    python:

        day_number += 1
        seen_events.append(today_event_label)

        for tag in today_event.tags:
            if tag not in current_tags:
                current_tags[tag] = 0
            current_tags[tag] += 1
        for person in today_event.personnel:
            characters[person]["points"] += 1

        # check if an ending has been reached
        if current_ending is None:
            for person, dic in characters.items():
                first_label = person + "_1"
                if first_label not in seen_events and characters[person]["has_route"] and characters[person]["points"] >= character_point_threshold:
                    # first ending label should be ending_event_(person)_1
                    current_ending = first_label
                    break
    
    if day_number < day_threshold:
        jump day_init



label default_intro:
    scene bg intro
    with default_fade
    player "Intro sequence!!!!!!"
    player "aughaghaghagh"
    return

label default_outro:
    scene bg room
    with default_fade
    
    # randomly choose a remark from a pool
    $ random_day_complete_remark = renpy.random.choice(day_complete_remarks)
    player "[random_day_complete_remark]"

    # randomly choose another remark from a pool
    $ random_heading_home_remark = renpy.random.choice(heading_home_remarks)
    player "[random_heading_home_remark]"
    return
