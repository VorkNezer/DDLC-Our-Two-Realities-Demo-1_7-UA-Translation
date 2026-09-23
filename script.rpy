label start:
    $ anticheat = persistent.anticheat
    $ chapter = 0
    $ _dismiss_pause = config.developer
    $ s_name = "Сайорі"
    $ m_name = "Моніка"
    $ n_name = "Нацукі"
    $ y_name = "Юрі"
    $ p_name = "ГГ"
    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True
    call intro
    return
label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
        pass
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
        pass
    $ quick_menu = True
    return
