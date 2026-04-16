# The script of the game goes in this file.

label start:
    call screen start

#chapters
screen start:
    imagebutton:
        auto "chapter/chap1_%s.png"
        action jump("ch1_start")

    imagebutton:
        auto "chapter/chap2_%s.png"
        action jump("ch2_start")

    imagebutton:
        auto "chapter/chap3_%s.png"
        action jump("ch3_start")

    imagebutton:
        auto "chapter/chap4_%s.png"
        action jump("ch4_start")