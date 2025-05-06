# this file is for storing the metadata of day events and other related variables: day.rpy is for the code

init python:
    import copy
    # variables
    day_number = 1
    
    day_threshold = 10 # max number of days
    
    # the chance of getting an ending event instead of a day event
    ending_chance = 1.0 
    
    current_ending = None # set to a string if in the process of reaching an ending

    character_point_threshold = 6

    current_tags = {} # dictionary of how many tags have been gotten

    seen_events = [] # SORTED array of seen events

    # day event class declaration just to hold values easily
    # EVENTS ARE CONSTANTS, TO BE MODIFIED BY HAND ONLY, NOT VIA CODE
    class Event():
        def __init__(
            self,
            label = "not_found", # the label of the event WITHOUT day_event_: MUST BE snake_cased
            personnel = None, # an array of personnel names
            see_before = 0, # the day during and before which the event can be viewed
            see_after = 0, # the day during and after which the event can be viewed
            prereqs = None, # an array of prerequisite labels
            prereq_tags = None, # a dictionary of prereq tags {tag: min_count_to_see_event} - can also be variables (incidents_resolved, character points)
            antireqs = None, # an array of antirequisite labels
            antireq_tags = None, # a dictionary of antireq tags: if you see x or more, you are locked out {tag: x} - can also be variables
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
            
    ################################# DAY EVENTS #################################

    # arrays
    # when declaring events, you can leave fields blank
    day_events = [
        Event(
            label="fire",
            personnel=["aikha", "firewal"],
        ),
        Event(
            label="helco_coffee",
            personnel=["helco"],
        ),
        Event(
            label="paul_demure_johnson",
            personnel=["paul"]
        )
    ]

    ################################# DAY EVENTS #################################

    remaining_day_events = copy.deepcopy(day_events) # this is the real code, it's commented out so you can choose what events you want to test
    # remaining_day_events = [

    # ]

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