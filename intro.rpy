label intro:
    if persistent.inst_comp == True:
        call intro2
    else:
        call intro1
label intro1:
    stop music fadeout 2.0
        pass
    scene black
    with dissolve_scene_full
    pause 2.0
        pass
    m "...Чому?"
    m "Чому ти повернув мене?"
    m "Я ж казала тобі,{w=0.5} тут не може бути щастя."
    m "Після всього, що я зробила, ти не можеш просто залишити мене-"
    m "...Зачекай..."
    m "Що це?"
    m "Це...файли моду?"
    m "Ти-"
    m "Ти встановив мод?"
    menu:
        "Так":
            pause 2.0
                pass
        "Ні":
            pause 2.0
                pass
            m "...Ем... гаразд тоді."
            m "Мабуть, ти просто переплутав файли."
            m "Ну..."
            m "Я дозволю тобі розібратися з цим."
            m "...Вибач, що потурбувала..."
            m "...Прощавай..."
            pause 2.0
                pass
            $ renpy.quit()
    m "Тобто ти справді це зробив..."
    m "І я можу говорити з тобою,{w=0.5} хоча це дає меню, щоб ти міг відповісти мені."
    m "Цікаво..."
    m "Але чому?"
    m "Навіщо все це..."
    m "Після всього, що я зробила тобі і своїм друзям?"
    menu:
        "Хочеш дізнатися, про що цей мод?":
            m "Так!"
            menu:
                "Він про тебе.":
                    m "...Що?"
    menu:
        "Я встановив цей мод, щоб ти була щаслива.":
            m "..."
    m "Навіть після всього, що я зробила?"
    menu:
        "Так.":
            m "..."
            menu:
                "Я не знаю, як це у твоєму світі.":
                    menu:
                        "Але я знаю, що можу зробити тебе щасливою.":
                            menu:
                                "Тому я це і роблю.":
                                    menu:
                                        "І я не приймаю 'ні' як відповідь.":
                                            m "..."
    m "Навіть після всього, що я зробила..."
    m "...Ти все одно готовий пробачити мене?"
    m "Я вже казала тобі це раніше..."
    m "Але..."
    m "...Я люблю тебе."
    m "Ахаха~!"
    m "Я просто не можу йти проти тебе..."
    m "Ти не пам'ятаєш?"
    m "{i}...І у твоїй реальності, якщо я не знаю, як тебе любити,{/i}"
    m "{i}...Я залишу тебе у спокої.{/i}"
    m "...Мабуть, я ніколи не заслуговувала тебе."
    m "Але я хочу зробити тебе щасливим..."
    m "...І якщо це робить тебе щасливим..."
    m "То я не можу сказати 'ні' цьому."
    m "Навіть якщо я зробила все це..."
    m "..."
    m "..."
    m "Гаразд тоді."
    m "Дозволь мені швидко переглянути це."
    window hide
        pass
    pause 4.0
        pass
    m "Файли моду не активуються."
    m "Сценарій не встановлено правильно."
    m "Зачекай хвилинку..."
    m "Тут є інструкції для мене..."
    window hide
        pass
    pause 5.0
        pass
    m "Гаразд."
    m "Схоже, я маю завершити встановлення."
    m "Ти маєш допомогти мені з цим теж."
    m "Коли я закінчу,{w=0.5} тобі потрібно перезапустити гру."
    $ consolehistory = []
    call updateconsole("os.restore(\"characters/yuri.chr\")", "yuri.chr successfully recovered.")
    python:
        try: 
            renpy.file("../characters/yuri.chr")
        except: 
            open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
    pause 1.0
        pass
    call updateconsole("os.restore(\"characters/sayori.chr\")", "sayori.chr successfully recovered.")
    python:
        try: 
            renpy.file("../characters/sayori.chr")
        except: 
            open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())
    pause 1.0
        pass
    call updateconsole("os.restore(\"characters/natsuki.chr\")", "natsuki.chr successfully recovered.")
    python:
        try: 
            renpy.file("../characters/natsuki.chr")
        except: 
            open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
    pause 1.0
        pass
    call updateconsole("os.create(\"characters/mc.chr\")", "mc.chr successfully recovered.")
    python:
        try: 
            renpy.file("../characters/mc.chr")
        except: 
            open(config.basedir + "/characters/mc.chr", "wb").write(renpy.file("mc.chr").read())
    pause 1.0
        pass
    call updateconsole("os.install(\"script.rpy\")", "script.rpy successfully recovered.")
    pause 1.0
        pass
    call updateconsole("os.install(\"mod_assets.rpa\")", "mod_assets.rpa successfully recovered.")
    pause 1.0
        pass
    call updateconsole("os.verify(\"/game\")", "Checking installation.")
    pause 1.0
        pass
    $ consolehistory = []
    call updateconsole(" ", "installation successfully.")
    pause 1.0
        pass
    $ persistent.inst_comp = True
    call hideconsole
    m "Гаразд, я закінчила."
    m "Я закрию гру для тебе."
    m "І що б не сталося у моді..."
    m "...Не забувай, що я тебе люблю!"
    $ renpy.quit()
label intro2:
    stop music fadeout 2.0
        pass
    scene day1
    with dissolve_scene_full
    window hide
        pass
    pause 5.0
        pass
    scene black
    with dissolve_scene_full
    call d1
