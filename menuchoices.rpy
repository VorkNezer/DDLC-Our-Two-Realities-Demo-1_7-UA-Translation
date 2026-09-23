label menuchoice1:
    menu:
        "Звичайна кава":
            $ persistent.coffee = "cof"
            $ persistent.cofname = "звичайна кава"
            call d6p2
        "Лате":
            $ persistent.coffee = "lat"
            $ persistent.cofname = "лате"
            call d6p2
        "Капучіно":
            $ persistent.coffee = "cap"
            $ persistent.cofname = "капучіно"
            call d6p2
        "Еспресо":
            $ persistent.coffee = "esp"
            $ persistent.cofname = "еспресо"
            call d6p2
        "Американо":
            $ persistent.coffee = "amr"
            $ persistent.cofname = "американо"
            call d6p2
        "Далі":
            call menuchoice2
label menuchoice2:
    menu:
        "Темний обсмажений":
            $ persistent.coffee = "dr"
            $ persistent.cofname = "темна кава"
            call d6p2
        "Без кофеїну":
            $ persistent.coffee = "dc"
            $ persistent.cofname = "безкофеїновий напій"
            call d6p2
        "Гарячий шоколад":
            $ persistent.coffee = "hc"
            $ persistent.cofname = "гарячий шоколад"
            call d6p2
        "Мокко":
            $ persistent.coffee = "moc"
            $ persistent.cofname = "мокко"
            call d6p2
        "Назад":
            call menuchoice1
        "Далі":
            call menuchoice3
label menuchoice3:
    menu:
        "Апельсиновий сік":
            $ persistent.coffee = "oj"
            $ persistent.cofname = "апельсиновий сік"
            call d6p2
        "Яблучний сік":
            $ persistent.coffee = "aj"
            $ persistent.cofname = "яблучний сік"
            call d6p2
        "Френч Ваніль":
            $ persistent.coffee = "fv"
            $ persistent.cofname = "френч ваніль"
            call d6p2
        "Холодна кава":
            $ persistent.coffee = "ic"
            $ persistent.cofname = "холодна кава"
            call d6p2
        "Назад":
            call menuchoice2
        "Далі":
            call menuchoice4
label menuchoice4:
    menu:
        "Макіато":
            $ persistent.coffee = "mac"
            $ persistent.cofname = "макіато"
            call d6p2
        "Лимонад":
            $ persistent.coffee = "lem"
            $ persistent.cofname = "лимонад"
            call d6p2
        "Кола":
            $ persistent.coffee = "col"
            $ persistent.cofname = "кола"
            call d6p2
        "Вода":
            $ persistent.coffee = "wat"
            $ persistent.cofname = "склянка води"
            call d6p2
        "Назад":
            call menuchoice3
label menuchoice5:
    menu:
        "Звичайна кава":
            $ persistent.coffee = "cof"
            $ persistent.cofname = "звичайна кава"
            call d10p2
        "Лате":
            $ persistent.coffee = "lat"
            $ persistent.cofname = "лате"
            call d10p2
        "Капучіно":
            $ persistent.coffee = "cap"
            $ persistent.cofname = "капучіно"
            call d10p2
        "Еспресо":
            $ persistent.coffee = "esp"
            $ persistent.cofname = "еспресо"
            call d10p2
        "Американо":
            $ persistent.coffee = "amr"
            $ persistent.cofname = "американо"
            call d10p2
        "Далі":
            call menuchoice6
label menuchoice6:
    menu:
        "Темний обсмажений":
            $ persistent.coffee = "dr"
            $ persistent.cofname = "темна кава"
            call d10p2
        "Без кофеїну":
            $ persistent.coffee = "dc"
            $ persistent.cofname = "безкофеїновий напій"
            call d10p2
        "Гарячий шоколад":
            $ persistent.coffee = "hc"
            $ persistent.cofname = "гарячий шоколад"
            call d10p2
        "Мокко":
            $ persistent.coffee = "moc"
            $ persistent.cofname = "мокко"
            call d10p2
        "Назад":
            call menuchoice5
        "Далі":
            call menuchoice7
label menuchoice7:
    menu:
        "Апельсиновий сік":
            $ persistent.coffee = "oj"
            $ persistent.cofname = "апельсиновий сік"
            call d10p2
        "Яблучний сік":
            $ persistent.coffee = "aj"
            $ persistent.cofname = "яблучний сік"
            call d10p2
        "Френч Ваніль":
            $ persistent.coffee = "fv"
            $ persistent.cofname = "френч ваніль"
            call d10p2
        "Холодна кава":
            $ persistent.coffee = "ic"
            $ persistent.cofname = "холодна кава"
            call d10p2
        "Назад":
            call menuchoice6
        "Далі":
            call menuchoice8
label menuchoice8:
    menu:
        "Макіато":
            $ persistent.coffee = "mac"
            $ persistent.cofname = "макіато"
            call d10p2
        "Лимонад":
            $ persistent.coffee = "lem"
            $ persistent.cofname = "лимонад"
            call d10p2
        "Кола":
            $ persistent.coffee = "col"
            $ persistent.cofname = "кола"
            call d10p2
        "Вода":
            $ persistent.coffee = "wat"
            $ persistent.cofname = "склянка води"
            call d10p2
        "Назад":
            call menuchoice7
label icecreamchoice:
    menu:
        "М’ята":
            $ persistent.ic = "м'ятне"
        "Шоколад":
            $ persistent.ic = "шоколадне"
        "Ваніль":
            $ persistent.ic = "ванільне"
        "Полуниця":
            $ persistent.ic = "полуничне"
        "Печиво та крем":
            $ persistent.ic = "з печивом та кремом"
        "Рокі Роуд":
            $ persistent.ic = "рокі роуд"
    return
