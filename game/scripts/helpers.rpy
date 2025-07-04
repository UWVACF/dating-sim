# This folder consists of Python helper functions

init python:
    import re
    import pygame
    # from threading import Timer
    
    class Shake(object):

        def __init__(self, duration, strength, preset, persist, delay, repeat, interval, timeline):
            self.update(duration, strength, preset, persist, delay, repeat, interval, timeline)

        def update(self, duration, strength, preset, persist, delay, repeat, interval, timeline):
            if preset == "strong":
                self.duration = 1.0
                self.strength = 20.0
            elif preset == "medium":
                self.duration = 0.5
                self.strength = 10.0
            elif preset == "weak":
                self.duration = 0.25
                self.strength = 10.0
            elif preset == "rumble":
                self.duration = 0.5
                self.strength = 2.0
            else:
                self.duration = duration
                self.strength = strength
            
            self.persist = persist
            self.delay = delay
            self.repeat = repeat
            self.interval = interval
            self.timeline = timeline
            self.timestamp = 0 # number to offset shown by for timeline

        
        def start(self, trans, shown, anim):
            # function should end 

            # TODO: still repeating when repeat is False bc this never procs
            if type(self.repeat) is int and shown >= self.delay + (self.persist + self.duration + self.interval) * (self.repeat + 1):
                return None

            if shown < self.delay:
                return 0
            shown -= self.delay
            shown %= self.persist + self.duration + self.interval


            factor = 0.0 # factor by which to multiply the shake
            if shown < self.persist:
                factor = 1.0
            elif shown < self.persist + self.duration:
                factor = max(0.0, (self.duration - (shown - self.persist)) / self.duration) # linear decay
            else: # in interval
                factor = 0.0

            if factor <= 0: # function ended
                trans.xoffset = 0
                trans.yoffset = 0
                if self.repeat: # True or int
                    return 0
                return None
            else:
                # randomly choose a corner of the bounding box to move to
                # the bounding box is the box of side length 2 * self.strength * factor
                trans.xoffset = self.strength * factor * (renpy.random.choice([-1, 1])) 
                trans.yoffset = self.strength * factor * (renpy.random.choice([-1, 1]))
                return 0

    shake_obj = Shake(duration=0.5, strength=10.0, preset="", persist=0.0, delay=0.0, repeat=0, interval=0.0, timeline=None)

    # shakes the screen randomly, optionally persisting at max strength for some time before diminishing towards the end
    # usage:
    #   $ shake_screen(layers, duration, strength, preset, persist, delay)
    # parameters:
    #   layers: which layers to shake
    #       this can be an array or a string of a single layer's name
    #       by default, it will shake all layers with sprites on them (not UI)
    #       a value of "all" will shake ALL layers (including UI)
    #   duration: the time it takes for the shake to go from max strength to nothing
    #   strength: the strength of the shake, represented by the maximum displacement of a shake in pixels
    #   preset: will set values of strength and duration to preset values:
    #       strong: duration 1.0, strength 20.0
    #       medium: duration 0.5, strength 10.0 (default)
    #       weak: duration 0.25, strength 10.0
    #       rumble: duration 0.5, strength 2.0, intended to be used for light, persistent rumble effects
    #   persist: the amount of time at the beginning of the shake where it does not decay
    #       example: persist 2.0, strength 10.0, duration 1.0 will cause the screen to shake at strength 10 for 2 seconds, then linearly decay from strength 10 to 0 over the course of 1 second 
    #   delay: the amount of time until the shake starts once called
    #   repeat: the amount of times the shake should repeat, where True repeats it indefinitely
    #       to stop an infinite screen shake, call shake_screen(duration=0) on the same layers as before
    #   interval: the pause between consecutive screen shakes, if repeat is not False
    #   timeline: complicated, unimplemented
    #       array of values indicating interval times between shakes, where 0.0 is a shake
    def shake_screen(layers=None, duration=0.5, strength=10.0, preset="", persist=0.0, delay=0.0, repeat=0, interval=0.0, timeline=None):
        shake_obj.update(duration, strength, preset, persist, delay, repeat, interval, timeline)

        if layers is None:
            layers = ['master0', 'master', 'master1', 'master2', 'top']
        if isinstance(layers, str):
            if layers == "all":
                for layer in config.layers:
                    renpy.show_layer_at(shake, layer=layer)
            else: # single layer
                renpy.show_layer_at(shake, layer=layers)
                    
        else: # multiple layers
            for layer in layers:
                renpy.show_layer_at(shake, layer=layer)
    
    # for clearing all screens' transforms, including stopping the screen shake after using an indefinitely looping screen shake
    def clear_screen_transforms():
        shake_obj.update(duration=0.0, strength=0.0, preset="", persist=0.0, delay=0.0, repeat=0, interval=0.0, timeline=None)
        for layer in config.layers:
            renpy.show_layer_at(null_transform, layer=layer, reset = True)

    # Raise the character points of personnel
    # takes in a dictionary: {"personnel1": points1, "personnel2": points2}
    # example usage: update_character_points({"helco": 1, "plutoes", -2})
    def update_character_points(personnel):
        for person, points in personnel.items():
            characters[person]["points"] += points
        return True

    # Raise the honing survey points of personnel
    # takes in a dictionary: {"personnel1": points1, "personnel2": points2}
    # example usage: update_honing_points({"helco": 1, "plutoes", -2})
    def update_honing_points(personnel):
        for person, points in personnel.items():
            honing_points[person] += points
        return True

    # Automatically adds pauses after punctuations
    # this is some really weird ass reg-ex shit please do not ask me what it means i will not know - ryan
    def auto_pause(text):
        if text[0:9] == "/no_pause":
            return text[9:]
        
        # adds pause after commas
        text = re.sub(
            r',(?!\s*[0-9])', 
            f',{{w={punctuation_pauses["comma"]}}}', 
            text
        )
        # adds pause after periods
        text = re.sub(
            r'(?<!\bMr)(?<!\bMrs)(?<!\bDr)(?<!\bMRS)(?<!\bMR)(?<!\bDR)(?<!\.)\. (?!\s*\s*$|\.|[0-9])', 
            f'. {{w={punctuation_pauses["period"]}}}', 
            text
        )
        # adds pause after elipses
        text = re.sub(
            r'\.{3}(?!\s*)', 
            f'.{{w={punctuation_pauses["elipsis"]}}}.{{w={punctuation_pauses["elipsis"]}}}.{{w={punctuation_pauses["elipsis"]}}}', 
            text
        )
        # adds pause after exclamation mark
        text = re.sub(
            r'! (?!\s*[0-9])', 
            f'! {{w={punctuation_pauses["exclamation"]}}}', 
            text
        )
        # adds pause after question mark
        text = re.sub(
            r'\? (?!\s*[0-9])', 
            f'? {{w={punctuation_pauses["question"]}}}', 
            text
        )
        # adds pause after colon
        text = re.sub(
            r': (?!\s*[0-9])', 
            f': {{w={punctuation_pauses["colon"]}}}', 
            text
        )
        # adds pause after semi colon
        text = re.sub(
            r'; (?!\s*[0-9])', 
            f'; {{w={punctuation_pauses["semicolon"]}}}', 
            text
        )

        # adds pause after quotation mark
        text = re.sub(
            r'" (?!\s*[0-9])', 
            f'" {{w={punctuation_pauses["quotation"]}}}', 
            text
        )

        # adds pause after hyphen
        text = re.sub(
            r'- (?!\s*[0-9])', 
            f'- {{w={punctuation_pauses["hyphen"]}}}', 
            text
        )

        return text

    config.say_menu_text_filter = auto_pause

