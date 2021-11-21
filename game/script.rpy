define ch_ptg = Character("미녕", color = "#00092b")
define ch_narrator = Character(None, color = "#6b6b6b")
define narrator = Character(None, kind = nvl)
image bang = "bg/bang.jpg"
label start:

    $melancholia = 85
    $nameofyou = "minyoung"
    $is_male = True

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

label normal_ending:
    "끝"
    return

label good_ending:
    "ㅋㅋ루쿠크다스"
    return