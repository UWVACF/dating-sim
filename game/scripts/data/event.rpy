init -1000 python:
    import copy
    # variables
    day_number = 1
    
    day_threshold = 11 # max number of days
    
    # the chance of getting an ending event instead of a day event
    ending_chance = 1.0 
    
    current_ending = None # set to a personnel name if in the process of reaching an ending

    character_point_threshold = 6 # required amount of points to see an ending gate

    # TODO: determine if we just want a fixed chance of having an event with one of the three (e.g. 75% the event guaranteed has one of them)
    base_weight = 10 # the base weight value of an event
    bonus_weight_for_honed = 2 # the bonus weight given to events with honed personnel
    bonus_weight_per_point = 1 # the bonus weight per point given to events with certain personnel

    current_tags = {} # dictionary of how many tags have been gotten

    seen_events = [] # SORTED array of seen events, where the last entry is the most recently seen

    day_events = []
    remaining_day_events = []
    fixed_events = []
    remaining_fixed_events = []
    ending_events = []

    # day event class declaration just to hold values easily
    # EVENTS ARE CONSTANTS, TO BE MODIFIED BY HAND ONLY, NOT VIA CODE
    class Event():
        def __init__(
            self,
            label = "not_found", # the label of the event WITHOUT day_event_: MUST BE snake_cased
            personnel = None, # an array of personnel names involved in the event, route-able or not
            see_before = 0, # the day during and before which the event can be viewed (the last day this can be viewed, inclusive)
            see_after = 0, # the day during and after which the event can be viewed (the first day this can be viewed, inclusive)
            prereqs = None, # an array of prerequisite labels
            prereq_tags = None, # a dictionary of prereq tags {tag: min_count_to_see_event} - can also be variables (incidents_resolved, character points)
            antireqs = None, # an array of antirequisite labels
            antireq_tags = None, # a dictionary of antireq tags: if you see x or more, you are locked out {tag: x} - can also be variables
            chain = "", # a SINGLE label indicating the event that must directly follow this one
            intro_label = "", # the label of the custom intro, if any
            outro_label = "", # the label of the custom outro, if any 
            tags = None, # an array of tags this event has; used for categorization for prereq tags and antireq tags

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
        "At least I'm free now.",
        "Get me out get me oug getm ouget mgetou mteot"
    ]

    

    ## inter-event variables here
    didnt_miku_bingo2 = 0