init python:
    # day event class declaration just to hold values easily
    class DayEvent():
        def __init__(
            self,
            label = "not_found", # the label of the event WITHOUT day_event_
            personnel = None, # an array of personnel names
            see_before = 0, # the day during and after which the event can be viewed
            see_after = 0, # the day before (not during) the event can be viewed
            prereqs = None, # an array of prerequisite labels
            prereq_tags = None, # a dictionary of prereq tags {tag: min_count_to_see_event}
            antireqs = None, # an array of antirequisite labels
            antireq_tags = None, # a dictionary of antireq tags: if you see x or more, you are locked out {tag: x}
            chain = "", # a SINGLE label indicating the event that MUST PRECEDE this one
            intro_label = "", # the label of the custom intro, if any
            outro_label = "", # the label of the custom outro, if any 
            tags = None # an array of tags used for categorization for prereq tags and antireq tags
        ):
            self.label = str(label)
            self.see_before = see_before
            self.see_after = see_after
            self.chain = str(chain)
            self.intro_label = str(intro_label)
            self.outro_label = str(outro_label)

            self.personnel = list(personnel) if personnel is not None else []
            self.prereqs = list(prereqs) if prereqs is not None else []
            self.antireqs = list(antireqs) if antireqs is not None else []
            self.tags = list(tags) if tags is not None else []

            self.prereq_tags = dict(prereq_tags) if prereq_tags is not None else {}
            self.antireq_tags = dict(antireq_tags) if antireq_tags is not None else {}
            
    
    # arrays
    day_events = [
        
    ]

    # remaining_day_events = copy.deep_copy(event_labels)
    remaining_day_events = [
        {
            "label": "fire",
            "personnel": ["aikha", "firewal"],
            "prereq": ""
        },
    ]

    day_complete_remarks = [
        "Another day survived at this crazy place.",
        "Check that day off.",
        "Phew. Tough day.",
        "aughhhhHHHHHHHHHhhhh",
        "Not a bad day, I suppose.",
        "Could've been worse.",
        "At least it's over.",
        "..."
    ]

    heading_home_remarks = [
        "Well, I should get going.",
        "Home time!",
        "I'm off the clock.",
        "Signing off.",
        "Welp, let's go.",
        "At least I'm free now."
    ]

    # helper functions

    # returns an array of day events with the following properties
    # def get_day_events_with
                



label day_init:
    scene bg intro
    with default_fade
    player "Intro sequence!!!!!!"
    player "aughaghaghagh"

    python:
        if current_ending is not None and random.random() < ending_chance:
            # call the ending event instead of a day event
            renpy.call("ending_event_" + current_ending)

        else:
            # assign weights to events to allow honed personnel to appear more often
            total_weight = 0
            event_weights = {}
            for event in remaining_day_events:
                if event["prereq"] in remaining_day_events: # prereq is still in the possible events, so it was not seen yet
                    continue
                if len(set(event["personnel"]) & set(top_three_honed)) > 0:
                    event_weights[event["label"]] = top_three_weight_factor
                else:
                    event_weights[event["label"]] = 1
                total_weight += event_weights[event["label"]]
            
            # randomly select an event
            random_event_label = "not_found" # default value
            remaining_weight = random.randint(0, total_weight)
            for event_label, weight in event_weights.items():
                remaining_weight -= weight
                if remaining_weight <= 0:
                    random_event_label = event_label
                    break

            for i, event in enumerate(remaining_day_events):
                if event["label"] == random_event_label:
                    remaining_day_events.pop(i)
                    break

            # call random event
            renpy.call("day_event_" + random_event_label)

    # after event has finished
    scene bg room
    with default_fade
    
    # randomly choose a remark from a pool
    $ random_day_complete_remark = random.choice(day_complete_remarks)
    player "[random_day_complete_remark]"

    # randomly choose another remark from a pool
    $ random_heading_home_remark = random.choice(heading_home_remarks)
    player "[random_heading_home_remark]"

    $ day_number += 1

    # check if an ending has been reached
    python:
        if current_ending is None:
            for person, points in character_points.items():
                if points >= character_point_threshold:
                    # first ending label should be ending_event_(person)_1
                    current_ending = person + "_1"
                    character_points[person] = -100
                    break

    
    if day_number < day_threshold:
        jump day_init