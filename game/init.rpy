init python:
   
    def update_gamestate():
        global move_count
        newcount = move_count + 1
        SetVariable("move_count", newcount)()
        return 
    
    def check_intro_reactions(room):
        if room == "MainRoom"
            renpy.call("EnterMainRoom")
        elif room == "Room 1":
            renpy.call("EnterRoom1")
            return