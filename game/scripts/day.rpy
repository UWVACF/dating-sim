init python:
    # where the day events are stored
    # format:
    # array of dictionaries
    #   - dictionary
    #       - "label": string
    #       - "personnel": array of strings
    #           - person (string)
    #       - "prereq": string (empty or another label)
    # for labels:
    #   - in renpy, write "label day_event_(label)", but in the array, do NOT include the "day_event_" prefix
    #   - labels should be snake_case
    day_events = [
        {
            "label": "fire",
            "personnel": ["aikha", "firewal"],
            "prereq": ""
        },
        {
            "label": "helco_coffee",
            "personnel": ["helco"],
            "prereq": ""
        },
        {
            "label": "paul_demure_johnson",
            "personnel": ["paul", "firewal", "aikha"],
            "prereq": ""
        }
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

label day_init:
    # TODO:
    #   to give additional weight to events with more honed-in personnel, go through the entire remaining events and assign a weight value 
    #   sum of the total weights and generate a random number between 1 and that
    #   then go through the remaining events once more, subtracting each weight from the random number
    #   if weight <= 0, choose that event

    python:
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
    # add threshold checker
    if day_number < day_threshold and not ending_reached:
        jump day_init