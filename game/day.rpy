init python:
    import random
    random.seed()
    event_labels = ["fire", "paul_demure_johnson", "helco_coffee"]
    # remaining_event_labels = event_labels.copy()
    remaining_event_labels = ["paul_demure_johnson"]

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
    $ random_event_index = random.randint(0, len(remaining_event_labels) - 1)
    $ random_event_label = "day_event_" + remaining_event_labels[random_event_index]
    $ remaining_event_labels.pop(random_event_index)

    # call random event
    $ renpy.call(random_event_label)

    # after event has finished
    scene bg room
    with default_fade
    
    # randomly choose a remark from a pool
    $ random_day_complete_remark = day_complete_remarks[random.randint(0, len(day_complete_remarks) - 1)]
    player "[random_day_complete_remark]"

    # randomly choose another remark from a pool
    $ random_heading_home_remark = heading_home_remarks[random.randint(0, len(heading_home_remarks) - 1)]
    player "[random_heading_home_remark]"

    $ day_number += 1
    # add threshold checker
    if day_number < 7:
        jump day_init