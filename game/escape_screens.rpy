screen MainRoomScreen():
    vbox:
        text "Main Room"
        text "Move Count: " + str(move_count)
        textbutton "Go to Room 1":
            action [SensitiveIf(in_room), SetVariable("current_room", "Room 1"), Jump("MyRoom")]
        textbutton "End Game":
            action [SensitiveIf(in_room), Jump("EndGame")]

screen Room1_Screen():
    vbox:
        text "Room 1"
        text "Move Count: " + str(move_count)
        textbutton "Go to Main Room":
            action [SensitiveIf(in_room), SetVariable("current_room", "MainRoom"), Jump("MyRoom")]
        textbutton "Look at pencil":
            action [SensitiveIf(in_room), Jump("LookAtPencil")]