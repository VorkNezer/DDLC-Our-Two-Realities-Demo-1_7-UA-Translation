label d6:
    stop music fadeout 2.0
        pass
    scene day6
    with dissolve_scene_full
    window hide
        pass
    pause 5.0
        pass
    scene black
    with dissolve_scene_full
    pause 4.0
        pass
    "Я повільно відкриваю очі, прокидаючись."
    scene mcg_2
    with Dissolve(2.0)
    play music t9
        pass
    "Я чую легке дихання Моніки, яка спокійно спить поруч зі мною."
    "Ох, вона така мила~"
    "Я міг би знову заснути, просто слухаючи її."
    "Хммм..."
    "Моніка вже якось мене здивувала сніданком, правда ж?"
    "Гадаю, я зроблю для неї те саме."
    "Я повільно підводжуся, намагаючись не розбудити її."
    scene bg bedroom
    with wipeleft_scene
    "Мені вдається, і я йду вниз."
    scene bg kitchen
    with wipeleft_scene
    "Я відкриваю холодильник і дивлюся на інгредієнти."
    "Я дістаю коробку з овочевими котлетами."
    "Цього вистачить."
    "Я беру чотири котлети з коробки й кладу решту назад у холодильник."
    "Я дістаю сковорідку й наливаю на неї трішки олії."
    "Вмикаю плиту й кладу котлети смажитися."
    play sound "mod_assets/sfx/frying.ogg" loop
        pass
    "Вони апетитно шкварчать, поки я беру кілька помідорів і цибулю."
    "Я нарізаю їх і висипаю в миску."
    "Ставлю миску на стіл і повертаюся перевірити котлети."
    "Я перевертаю їх, і вони продовжують шкварчати."
    "Після цього я обпираюся на стільницю й чекаю, поки вони дійдуть."
    stop sound fadeout 2.0
        pass
    "Вони набувають гарного золотавого кольору, і я знімаю їх з вогню."
    "Я розкладаю їх по тарілках і ставлю на стіл."
    "Залишилося тільки дочекатися, коли Моніка спуститься."
    "І якраз співпадінням я чую кроки на сходах."
    show monika p_1k at l11
    m "Доброго ранку~"
    m forward pj ldown rdown vsur cm oe "Ооо~ Що ти приготував?"
    mc "У нас овочеві котлети та салат із помідорів!"
    m p_1b "Виглядає апетитно!"
    show monika p_1a
    mc "Спершу скуштуй, а тоді хвали!"
    m p_1k "З задоволенням!"
    show monika p_1a
    "Ми сідаємо, і Моніка накладає собі салату з миски."
    "Я роблю те саме, і ми разом починаємо трапезу."
    m p_1b "Ммм~!{w=0.5} Це смачно!"
    m "Я й не думала, що ти можеш таке смажити!"
    show monika p_1a
    mc "Просто вирішив спробувати."
    mc "Радий, що тобі подобається!"
    m p_1j "Мгм~"
    m "Дякую тобі, коханий~"
    m "Це дуже мило з твого боку~"
    "Ми закінчуємо, і я ставлю тарілки в посудомийку."
    show monika p_1c
    mc "Отже, сьогодні ми йдемо з клубом у те кафе, яке дивилися вчора, так?"
    m p_1b "Ага!"
    m "Усі погодились, тож ми готові йти!"
    show monika p_1a
    mc "Чудово!"
    "Я закриваю посудомийку й іду нагору, Моніка слідує за мною."
    scene bg bedroom
    with wipeleft_scene
    "Моніка бере свої речі й, як завжди, іде у ванну."
    "Я збираюся до школи й замість клубних матеріалів беру трохи готівки."
    "У мене є передчуття, що цього може бути замало..."
    "Я також беру трохи зі своїх заощаджень, про всяк випадок."
    "Моніка виходить із ванної."
    show monika 1c at l11
    mc "Гей, Моніко..."
    m "Гм?"
    mc "А як ми будемо ділити рахунок за клуб?"
    m 1b "Ми будемо платити!"
    show monika 1a
    mc "Так і думав."
    m 1d "Ти нестимеш гроші?"
    show monika 1c
    mc "Так."
    m 1d "Гаразд, зачекай секунду..."
    show monika 1c
    "Вона дістає свій гаманець і передає його мені."
    m 1b "Ти ж триматимеш, так?"
    show monika 1a
    mc "Добре..."
    "Я кладу гаманець у свій рюкзак, разом із власним."
    m 5a "До того ж, це ж наші гроші."
    m "Ми повинні підтримувати одне одного!"
    show monika 1a
    mc "Так."
    mc "Ти готова?"
    m 1j "Мгм~"
    "Ми спускаємось униз."
    scene bg livingRoom_lightsOn_TvOff
    with wipeleft_scene
    stop music fadeout 2.0
        pass
    "Я взуваюся й виходжу надвір разом із Монікою."
    play sound closet_open
        pass
    scene bg house
    with wipeleft_scene
    play music t2
        pass
    play sound closet_close
        pass
    "Я швидко замикаю двері й підходжу до Сайорі та ГГ, які вже чекають нас."
    show monika 1a at t33
    show protag 1a at t32
    show sayori 1a at t31
    mc "Доброго ранку!"
    show sayori 4r at f31
    s "Раночкууу!"
    show sayori 1a at t31
    show protag 1c at f32
    p "Привіт!"
    scene bg residential_day
    show monika 1a zorder 1 at t33
    show sayori 1a zorder 2 at t31
    show protag 1a zorder 3 at t32
    with wipeleft_scene
    "Ми вирушаємо до школи."
    show sayori 1n
    show monika 1j at f33
    "Моніка притискається до мене, поки ми йдемо."
    show sayori 4q at t42
    show protag 1l
    "Сайорі це помічає й вирішує притулитися до ГГ."
    "Ми йдемо далі, наближаючись до школи."
    "Крок за кроком,{w=0.5} ми дістаємося входу."
    scene bg outside
    with wipeleft_scene
    show monika 3j at t11
    "Ми приходимо до школи й прощаємося з Сайорі та ГГ."
    show monika 1a
    "Моніка та я, як завжди, йдемо до нашого класу."
    scene bg class_day
    with wipeleft_scene
    "Ми займаємо свої місця й чекаємо на початок уроків."
    scene bg class_day
    with wipeleft_scene
    "Урок закінчується знову під дзвінок."
    "Моніка легенько штовхає мене в руку."
    show monika 3k at t11
    m "Ходімо!"
    show monika 1a
    mc "Мгм..."
    stop music fadeout 2.0
        pass
    "Я встаю зі свого місця й прямую за Монікою до клубної кімнати."
    scene bg corridor
    with wipeleft_scene
    play music t12
        pass
    show yuri 2b at t22
    show natsuki 1d at t21
    "Ми приходимо до клубної кімнати."
    "Юрі та Нацукі балакають, чекаючи на нас біля дверей."
    show monika 1b at l31
    show monika at f31
    show natsuki 1a at t32
    show yuri 1a at t33
    m "Привіт, дівчата!"
    show monika 1a at t31
    show natsuki 1d at t32
    n "Йо!"
    show natsuki 1a at t32
    show yuri 2d at f33
    y "Вітаю!"
    show yuri 1e at t11
    show natsuki at thide
    hide natsuki
    show monika at thide
    hide monika
    mc "Сайорі та ГГ уже прийшли?"
    show yuri 1f at f11
    y "Ще ні."
    show yuri 1e at t11
    mc "Добре."
    show yuri at thide
    hide yuri
    "Ми стоїмо й трохи чекаємо, поки Сайорі та ГГ прийдуть."
    "Моніка щось клацає у телефоні."
    "Я краєм ока бачу, що вона перевіряє карту, щоб ще раз упевнитися, де кафе."
    "Юрі й Нацукі продовжують свою розмову."
    "Я обпираюся на стіну й трохи замріюю."
    s "Гейй!"
    show sayori 4r at t21
    show protag 1a at t22
    "Нарешті з’являються Сайорі й ГГ."
    show monika 3k at t11
    show sayori at thide
    hide sayori
    show protag at thide
    hide protag
    m "Добре,{w=0.5} тепер, коли всі зібралися,{w=0.5} вирушаймо!"
    show monika at thide
    hide monika
    "Усі беруть свої речі, і ми вирушаємо до кафе."
    scene bg outside
    with wipeleft_scene
    "Ми дістаємося воріт і йдемо далі вулицею."
    scene bg residential_day
    with wipeleft_scene
    "Ми крокуємо вулицею."
    "Моніка чіпляється за мою руку, а я веду нас уперед."
    "Я підслуховую розмову Юрі та Нацукі."
    show natsuki 1d at f21
    show yuri 1e at t22
    n "...Гадаю, тобі це сподобається."
    show natsuki 1c at t21
    show yuri 2h at f22
    y "Я не впевнена..."
    show yuri 2g at t22
    show natsuki 4f at f21
    n "Ти сказала щось загадкове!"
    n 4e "Загадковішим це вже не зробиш!"
    show natsuki 2g at t21
    show yuri 1k at f22
    y "Гаразд, я гляну на це, коли прийду додому."
    show yuri 1a at t22
    show natsuki 1l at f21
    n "Чудово!"
    show natsuki 1a at t21
    show yuri 1f at f22
    y "Але я також думаю, що й ти маєш прочитати оце..."
    show yuri at thide
    hide yuri
    show natsuki at thide
    hide natsuki
    "Вони продовжують радити одна одній книжки, поки ми йдемо."
    "Я дивлюся на Сайорі та ГГ."
    show sayori 4r at f21
    show protag 1b at t22
    s "Я з’їм стільки солодощів!"
    show sayori 1a at t21
    show protag 1f at f22
    p "Гаразд... тільки не перестарайся."
    p 1w "Минулого разу, коли ти так зробила, у тебе живіт болів цілий день."
    show protag 5e at t22
    show sayori 5c at f21
    s "Ееее?{w=0.5} Ні, не болів..."
    s 2l "Це було просто...{w=0.5} е-е..."
    show sayori 4r at hf21
    s "...жарт, який я з тобою розіграла!"
    s 2l "Так!{w=0.5} Ха-ха..."
    show sayori 1a at t21
    show protag 1d at f22
    p "Добре, Сайорі..."
    show sayori turned ldown rdown nerv cm oe zorder 1
    show protag 1r zorder 2
    p "Але запам’ятай моє попередження..."
    show protag at f11
    p "Інакше ти опинишся в пеклі шлункового болю на дуже довгий час."
    show protag at f42
    p "І ти ж не хочеш знову цього відчути... чи не так?"
    show protag 5v at t42
    show sayori turned ldown rdown nerv om oe at s21
    s "Хе-хе..."
    show sayori at thide
    hide sayori
    show protag at thide
    hide protag
    "ГГ випромінює доволі повчальну ауру, коли повчає Сайорі."
    "Ми йдемо далі й нарешті дістаємося кафе."
    scene bg cafe_exterior
    with wipeleft_scene
    show monika 1b at t11
    m "Гадаю, це тут!"
    m "Ходімо всередину!"
    scene bg cafe_inside
    with wipeleft_scene
    "Ми заходимо всередину."
    "Тут кілька людей: одні працюють, інші спілкуються."
    "Ми займаємо столик і йдемо робити замовлення."
    show sayori 4r at t11
    "Сайорі замовляє купу маленьких тістечок і апельсиновий сік."
    show sayori at thide
    hide sayori
    show natsuki 2l at t11
    "Нацукі бере невелику каву, кілька тістечок і мафін."
    show natsuki at thide
    hide natsuki
    show yuri 2b at t11
    "Юрі бере собі чай Earl Grey."
    show yuri at thide
    hide yuri
    show protag 1c at t11
    "ГГ замовляє лате й пончик."
    show protag at thide
    hide protag
    show monika 3b at t11
    "Моніка бере велику каву й маленьке тістечко."
    show monika at thide
    hide monika
    "Я підходжу до каси, щоб замовити."
    mc "Я візьму..."
    call menuchoice1
label d6p2:
    mc "Я візьму, будь ласка, [persistent.cofname]!"
    "Бариста" "\"Добре. Ще щось бажаєте?\""
    mc "Ні, дякую."
    "Бариста" "\"Гаразд, ви оплачуєте за всю компанію?\""
    mc "Так, нас шестеро разом."
    "Бариста" "\"Ох, добре тоді.\""
    "Бариста" "\"Ваш рахунок становить $45.79.\""
    mc "Добре, зачекайте хвилинку."
    "Я витягую гаманець і рахує гроші."
    "40...45...75...80..."
    mc "Ось, будь ласка!"
    "Бариста" "\"Дякую! Ваші замовлення будуть готові за мить.\""
    "Я сідаю разом з усіма, закінчивши оплату."
    "Звісно, я сідаю поруч з Монікою."
    show yuri 1a at t31
    show sayori 1a at t32
    show protag 1a at t33
    m "Отже, коли почнеться літо, що ви всі хочете робити?"
    show sayori 4r at f32
    s "Ооо! Давайте всі підемо разом плавати!"
    show sayori 1a at t32
    m "Гарна ідея!"
    show protag 1c at f33
    p "Ми також могли б піти в похід!"
    p 3k "Провести кілька днів на природі здається цікавим!"
    show protag 1a at t33
    n "Я хочу якось покататися на велосипеді!"
    m "Було б класно!"
    m "Ми також могли б сходити на трекінг!"
    "Бариста підходить до нашого столу з напоями в руках."
    "Бариста" "\"Ось ваші напої. Смачного!\""
    show sayori 4r at f32
    show yuri 1b at f31
    show protag 1b at f33
    "Всі" "\"Дякуємо!\""
    show sayori 1a at t32
    show yuri 1a at t31
    show protag 1a at t33
    "Бариста повертається до стійки, щоб продовжити обслуговування клієнтів."
    n "Хех, ми щойно звучали як група школярів."
    n "Усі кричали 'дякую' так голосно!"
    show sayori 4r
    show yuri 2d
    show protag 1k
    "Всі трохи сміються над коментарем Нацукі."
    show sayori 1a
    show yuri 1a
    show protag 1a
    n "До речі, я маю вас усіх колись запросити."
    n "Мої батьки ведуть пекарню біля мого дому, так що можу показати вам справжній рівень своїх навичок!"
    show sayori 1x at f32
    s "Там є солодощі?"
    show sayori 1a at t32
    n "Тонни."
    show sayori 4r at f32
    s "Я згодна!"
    s 3r "Гей, ГГ, ходімо зараз!"
    show sayori 3n at t32
    n "Ого, повільніше, Сайо!"
    n "Спочатку закінчи замовлення тут!"
    n "До того ж, ми відкриті лише до 3."
    show sayori 2l at f32
    s "Ааа..."
    show sayori 1n at t11
    n "Також, я дозволю тобі брати тільки за однієї умови."
    n "Тобі доведеться щось приготувати на кухні БЕЗ того, щоб спалити її!"
    show sayori 1m at f32
    s 1m "Еее??? Ти про це знаєш???"
    show sayori at t32
    n "Пффф, так. Новини розлітаються швидко, коли таке трапляється!"
    s 5d "{i}*нечітке бурмотіння*{/i}"
    show sayori 1a at t32
    "Ми потягуючи напої, слухаємо обмін реплік між Сайорі та Нацукі."
    mc "Ну, я хочу запросити всіх на барбекю!"
    show yuri 1m at f31
    y "Мені це цікаво."
    show yuri at t31
    show protag 5g at f33
    p "Справді? Ти не виглядаєш як та, хто любить таке."
    show protag at t33
    show yuri 1b at f31
    y "Мені не лише до спокійного. Я також інколи насолоджуюсь гарною гриль-вечіркою."
    show yuri 1a at t31
    mc "Добре, тоді візьму це як позитивну відповідь."
    show protag 1a
    n "Йо, мені треба йти."
    n "Вже пізно, і мої батьки почнуть хвилюватися."
    m "Так, подумавши, справді трохи пізно."
    m "До того ж, завтра школа."
    m "Думаю, сьогоднішнє зібрання клубу завершено."
    m "До завтра!"
    show yuri at thide
    hide yuri
    show sayori at thide
    hide sayori
    show protag at thide
    hide protag
    "Всі встають, щоб піти."
    "Ми прибираємо місця та збираємо речі."
    "Бариста" "\"Гарного вечора!\""
    scene bg cafe_exterior
    with wipeleft_scene
    n "Мій дім ось тут, побачимось пізніше!"
    y "Так, а я йду в інший бік, тому добраніч всім!"
    s "До завтра!"
    m "Па!"
    "Нацукі та Юрі йдуть у свої боки."
    m "Підемо?"
    mc "Ммм~"
    scene bg residential_aft
    with wipeleft_scene
    "Ми йдемо додому разом з Сайорі та ГГ."
    show monika 1e at f11
    m "Гей..."
    m 3k "Ми повинні знову сюди піти."
    m 1e "...тільки ми двоє."
    mc "Хмм? Так, це було б добре."
    show monika at thide
    hide monika
    "Ми тихо йдемо додому."
    "Сайорі знову стрибнула на спину ГГ і трохи подрімала під час ходьби."
    "Через кілька хвилин ми доходимо до наших будинків."
    scene bg house_dawn
    with wipeleft_scene
    stop music fadeout 2.0
        pass
    s "До зустрічі!"
    "Сайорі та ГГ йдуть додому, а я з Монікою заходжу всередину."
    play sound closet_open
        pass
    scene bg livingRoom_lightsOn_TvOff
    with wipeleft_scene
    play music t9
        pass
    play sound closet_close
        pass
    "Ми знімаємо взуття та йдемо наверх."
    scene bg bedroom
    with wipeleft_scene
    show monika 1d at t11
    m "Я піду трохи в душ, гаразд?"
    show monika 1c
    mc "Добре. Я поки підготую вечерю."
    show monika at lhide
    hide monika
    "Я переодягаюся, поки Моніка миється."
    mc "Повідом, коли закінчиш, щоб я міг помитися."
    m "Добре!"
    "Я йду вниз."
    scene bg kitchen
    with wipeleft_scene
    "Хммм..."
    "Відкриваю холодильник."
    "Схоже, ще залишилися залишки їжі."
    "Я витягую залишки вчорашньої вечері і кладу їх у мікрохвильовку."
    "Вона біпає, і я витягую їжу."
    "Беремо дві тарілки і кладемо на них підігріті спагеті."
    "Ставлю їх на стіл."
    m "Гей, коханий?{w=0.5} Я закінчила в душі, якщо хочеш піти зараз."
    mc "Добре, дякую."
    mc "І вечеря готова на столі."
    mc "Ми їмо залишки вчорашньої вечері."
    m "М'кей."
    "Я повертаюся наверх у ванну."
    scene black
    with wipeleft_scene
    "Я заходжу і приймаю душ."
    "Закінчив, одягнув піжаму і йду вниз."
    scene bg kitchen
    show monika p_1b at t11
    with wipeleft_scene
    m "Гей, я чекаю..."
    show monika p_1a
    mc "Дякую."
    "Ми сідаємо і тихо їмо разом."
    mc "Гей, Моніка..."
    m p_1c "Хмм?"
    mc "Ми повинні записати всі ідеї на літо, які придумали сьогодні."
    m p_1d "Гарна ідея,{w=0.5} я зроблю це після їжі."
    show monika p_1a
    "Ми продовжуємо їсти, а я знову відношу тарілки в посудомийку."
    show monika at thide
    hide monika
    "Моніка йде наверх."
    "Я закінчую тут,{w=0.5} і вимикаю світло, щоб піти наверх."
    scene bg bedroom
    with wipeleft_scene
    show monika p_1c at t11
    "Моніка сідає за стіл і записує список ідей."
    m p_1d "Добре, думаю, готово."
    m "Пішли спати, вже пізно."
    show monika p_1c
    mc "Так, ти права."
    show monika at thide
    hide monika
    "Вона вимикає лампу на столі і лягає спати."
    scene bg n_bedroom
    "Я вмикаю світло і лягаю поруч."
    scene black
    with wipeleft_scene
    m "Ми обов'язково повинні повторити це."
    mc "Так, варто."
    m "На добраніч, [player]!"
    mc "На добраніч, Моніка."
    "І з цим я знову занурююсь у світ снів."
    call d7
