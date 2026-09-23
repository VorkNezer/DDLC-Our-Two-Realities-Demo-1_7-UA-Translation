init:
    $ timer_range = 0
    $ timer_jump = 0
default ing1 = " "
default ing2 = " "
default ing3 = " "
default ing4 = " "
default ing5 = " "
default rheat = "Середній"
default aheat = "Середній"
default milk = False
default pepper = False
default onion = False
default spices = False
default egg = False
default water = False
default carrot = False
default potato = False
default mayo = False
default oil = False
default imilk = False
default ipepper = False
default ionion = False
default ispices = False
default iegg = False
default iwater = False
default icarrot = False
default ipotato = False
default imayo = False
default ioil = False
default apepper = False
default aonion = False
default aspices = False
default aegg = False
default awater = False
default acarrot = False
default apotato = False
default amayo = False
default aoil = False
default reci = "Овочеве соте"
label cookinggame1:
    stop music fadeout 2.0
        pass
    scene expression "mod_assets/wood.png"
    with dissolve_scene_full
    play music t4
        pass
    "Що приготувати?"
    menu:
        "Овочеве соте":
            $ reci = "Овочеве соте"
            $ ing1 = "Цибуля"
            $ aonion = True
            $ ing2 = "Перець"
            $ apepper = True
            $ ing3 = "Морква"
            $ acarrot = True
            $ ing4 = "Олія"
            $ aoil = True
            $ ing5 = "Спеції"
            $ aspices = True
            $ rheat = "Середній"
        "Простий суп":
            $ reci = "Простий суп"
            $ ing1 = "Спеції"
            $ aspices = True
            $ ing2 = "Морква"
            $ acarrot = True
            $ ing3 = "Картопля"
            $ apotato = True
            $ ing4 = "Вода"
            $ awater = True
            $ rheat = "Середній"
        "Картопляний салат":
            $ reci = "Картопляний салат"
            $ ing1 = "Картопля"
            $ apotato = True
            $ ing2 = "Цибуля"
            $ aonion = True
            $ ing3 = "Майонез"
            $ amayo = True
            $ ing4 = "Яйце"
            $ aegg = True
            $ ing5 = "Спеції"
            $ aspices = True
            $ rheat = "Низький"
    $ renpy.call_screen("dialog", "Виберіть інгредієнти для використання.", ok_action=Return())
    call reseter1
label reseter1:
    $ ipepper = True
    $ ionion = True
    $ ispices = True
    $ iegg = True
    $ iwater = True
    $ icarrot = True
    $ ipotato = True
    $ imayo = True
    $ ioil = True
    $ pepper = False
    $ onion = False
    $ spices = False
    $ egg = False
    $ water = False
    $ carrot = False
    $ potato = False
    $ mayo = False
    $ oil = False
    call screen cooking1
        pass
screen cooking1:
    vbox:
        yalign 0.1
        xalign 0.05
        text "[reci]"
        text "~~~~~~~~~~"
        text "[ing1]"
        text "[ing2]"
        text "[ing3]"
        text "[ing4]"
        text "[ing5]"
        text " "
        text "Час приготування: [rheat]"
    if (imilk==True):
        imagebutton:
            yalign 0.5
            xalign 0.5
            idle "mod_assets/ingr/milk_idle.png"
            hover "mod_assets/ingr/milk_hover.png"
            selected If("milk" == True)
            action ToggleVariable("milk", true_value = True, false_value = False)
    if (milk==True):
        add "mod_assets/milk_hover.png":
            xalign 0.5
            yalign 0.5
    if (ipepper==True):
        imagebutton:
            yalign 0.0
            xalign 0.2
            auto "mod_assets/ingr/pepper_%s.png"
            selected If("pepper" == True)
            action ToggleVariable("pepper", true_value = True, false_value = False)
    if (pepper==True):
        add "mod_assets/ingr/pepper_hover.png":
            xalign 0.2
            yalign 0.0
    if (ionion==True):
        imagebutton:
            yalign 0.0
            xalign 0.5
            auto "mod_assets/ingr/onion_%s.png"
            selected If("onion" == True)
            action ToggleVariable("onion", true_value = True, false_value = False)
    if (onion==True):
        add "mod_assets/ingr/onion_hover.png":
            xalign 0.5
            yalign 0.0
    if (ispices==True):
        imagebutton:
            yalign 0.0
            xalign 0.8
            auto "mod_assets/ingr/spices_%s.png"
            selected If("spices" == True)
            action ToggleVariable("spices", true_value = True, false_value = False)
    if (spices==True):
        add "mod_assets/ingr/spices_hover.png":
            xalign 0.8
            yalign 0.0
    if (iegg==True):
        imagebutton:
            yalign 0.4
            xalign 0.34
            auto "mod_assets/ingr/egg_%s.png"
            selected If("egg" == True)
            action ToggleVariable("egg", true_value = True, false_value = False)
    if (egg==True):
        add "mod_assets/ingr/egg_hover.png":
            xalign 0.34
            yalign 0.4
    if (iwater==True):
        imagebutton:
            yalign 0.65
            xalign 0.6
            auto "mod_assets/ingr/water_%s.png"
            selected If("water" == True)
            action ToggleVariable("water", true_value = True, false_value = False)
    if (water==True):
        add "mod_assets/ingr/water_hover.png":
            xalign 0.6
            yalign 0.65
    if (icarrot==True):
        imagebutton:
            yalign 0.4
            xalign 0.9
            auto "mod_assets/ingr/carrot_%s.png"
            selected If("carrot" == True)
            action ToggleVariable("carrot", true_value = True, false_value = False)
    if (carrot==True):
        add "mod_assets/ingr/carrot_hover.png":
            xalign 0.9
            yalign 0.4
    if (ipotato==True):
        imagebutton:
            yalign 0.95
            xalign 0.3
            auto "mod_assets/ingr/potato_%s.png"
            selected If("potato" == True)
            action ToggleVariable("potato", true_value = True, false_value = False)
    if (potato==True):
        add "mod_assets/ingr/potato_hover.png":
            xalign 0.3
            yalign 0.95
    if (imayo==True):
        imagebutton:
            yalign 0.9
            xalign 0.8
            auto "mod_assets/ingr/mayo_%s.png"
            selected If("mayo" == True)
            action ToggleVariable("mayo", true_value = True, false_value = False)
    if (mayo==True):
        add "mod_assets/ingr/mayo_hover.png":
            xalign 0.8
            yalign 0.9
    if (ioil==True):
        imagebutton:
            yalign 0.9
            xalign 0.1
            auto "mod_assets/ingr/oil_%s.png"
            selected If("oil" == True)
            action ToggleVariable("oil", true_value = True, false_value = False)
    if (oil==True):
        add "mod_assets/ingr/oil_hover.png":
            xalign 0.1
            yalign 0.9
    textbutton "Далі":
        xalign 0.95
        yalign 0.95
        action Call("cook1ttr")
label cook1ttr:
    hide screen cooking1
        pass
    $ renpy.call_screen("dialog", "Дочекайтеся, поки шкала потрапить у потрібну зону, щоб отримати правильний час приготування.", ok_action=Return())
    scene expression "mod_assets/wood.png"
    with wipeleft_scene
    call screen cook1tstart
        pass
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
screen countdown2:
    timer 0.01:
        repeat True
        action If(time < 30, true=SetVariable('time', time + 0.01), false=[Hide('countdown2'), Jump(timer_jump)])
    bar:
        value time
        range timer_range
        xalign 0.5
        yalign 0.9
        xmaximum 300
        at alpha_dissolve
screen cook1tstart:
    textbutton "Почати готувати":
        xalign 0.5
        yalign 0.5
        action Call("whilestuff1")
screen halt1:
    textbutton "Зупинити":
        xalign 0.5
        yalign 0.5
        action [Hide("countdown2"), Call("later1")]
label whilestuff1:
    $ timer_range = 30
    $ timer_jump = "later1"
    $ time = 0
    hide screen cooking1tstart
        pass
    show screen countdown2
        pass
    show screen halt1
        pass
    pause
        pass
label later1:
    hide screen countdown2
        pass
    hide screen halt1
        pass
    if time <= 10:
        $ aheat = "Низький"
    elif time <= 20:
        $ aheat = "Середній"
    elif time < 30:
        $ aheat = "Високий"
    else:
        $ aheat = "Підгоріло"
    jump foolproofing1
label foolproofing1:
    if aheat == rheat and apepper == pepper and aonion == onion and aspices == spices and aegg == egg and awater == water and acarrot == carrot and apotato == potato and amayo == mayo and aoil == oil:
        "Хмм... виглядає добре."
        jump d2contcook
    else:
        "Щось не так..."
        jump reseter1
