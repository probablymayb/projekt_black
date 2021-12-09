define ch_ptg = Character("미녕", color = "#00092b")
define ch_narrator = Character(None, color = "#6b6b6b")
define narrator = Character(None, kind = nvl)
image bang = "bg/bang.jpg"

default in_room = False #whether or not we should make the scene interactive
default move_count = 0
default current_room = "MainRoom"
default previous_room = ""

label start:
    $ melancholia = 85
    $ nameofyou = "minyoung"
    $ is_male = True
    
    call story_day1

    ch_ptg "게임스타뜨"
    $ current_room = "MainRoom"
    call MyRoom
    ch_ptg "게임끝"

    return

label story_day1:

    narrator "끝이다."
    narrator "더이상 살아갈 수 없어."
    narrator "숨이 쉬어지질 않는다."
    
    scene bang with fade
   
    nvl clear

    scene 
    menu:
        "흠좀무":
            ch_ptg "TT"
            $melancholia = melancholia +16

        "가나다라마비사":
            ch_ptg "No"


    ch_ptg "You've created a new Ren'Py game."

    ch_ptg "Once you add a story, pictures, and music, you can release it to the world!"
    
    narrator "흠좀무좀무"

    if(melancholia > 100):
        jump normal_ending
    return

label MyRoom:
    $ update_gamestate()

    $ in_room = False:
    $ renpy.show_screen(current_room + "Screen")

    if current_room != previous_room:
        $ check_intro_reactions(current_room)
    $ previous_room = current_room

    $ in_room = True:
    $ renpy.call_screen(current_room + "Screen")
    
    return

label normal_ending:
    "끝"
    return

label good_ending:
    "ㅋㅋ루쿠크다스"
    return

label EndGame:
    
    ch_ptg "게임끝"
    
    return

label LookAtPencil:
    $ in_room = False
    $ renpy.show_screen(current_room + "Screen")
    ch_ptg "연필이다."
    jump MyRoom

label EnterMainRoom:
    
    ch_ptg "로비에 들어왔다."
    
    return

label EnterRoom1:
    
    ch_ pth "1번방에 들어왔다."
    
    return