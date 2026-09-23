label d5:
    stop music fadeout 2.0
        pass
    scene day5
    with dissolve_scene_full
    window hide
        pass
    pause 5.0
        pass
    scene black
    with dissolve_scene_full
    pause 4.0
        pass
    "{i}Дінь-дооон{/i}"
    "Гм?{w=0.5} Що це за шум?"
    scene bg bedroom
    with dissolve_scene_full
    "Я повільно прокидаюсь, і Моніка теж підіймається."
    show monika forward pj lpoint rdown e1e b1b ml at t11
    m "{i}*Позіх*{/i}"
    m forward pj ldown rdown anno om oe "Хто це так рано зранку...?"
    show monika forward pj ldown rdown anno cm oe
    mc "Без поняття..."
    "Я спускаюсь униз, а Моніка йде слідом."
    scene bg house
    with wipeleft_scene
    play sound closet_open
        pass
    "Я відчиняю двері."
    show sayori 4r at f22
    show protag 5a at t21
    play music t2
        pass
    s "Доброго ранкууу!"
    show sayori 1a at t22
    mc "Ранок, а що це ви так рано піднялися?"
    show sayori 1c at f22
    s "Ну, ми тут подумали..."
    s 2x "Пам’ятаєте, як ви допомогли нам з млинцевим інцидентом?"
    s 4r "Так от, ми з ГГ трохи поговорили і вирішили запросити вас на сніданок!"
    show sayori 1a at t22
    mc "Добре, я не проти."
    m "Звісно! Я теж іду!"
    show sayori 4r at f22
    s "Ураа! Добре, тоді побачимось скоро!"
    show sayori 1a at t22
    mc "До зустрічі, ви двоє."
    scene bg livingRoom_lightsOn_TvOff
    with wipeleft_scene
    play sound closet_close
        pass
    "Я зачиняю двері та повертаюся всередину."
    show monika p_1l at t11
    m "Хто б міг подумати, що Сайорі прокинеться раніше за нас?"
    show monika p_1a
    mc "Ха, так, я не очікував!"
    mc "Ходімо перевдягнемось і рушимо до Сайорі."
    m p_2j "Мгм~"
    show monika at thide
    hide monika
    "Ми повертаємось нагору."
    scene bg bedroom
    with wipeleft_scene
    "Моніка знову заходить у ванну, а я перевдягаюсь тут."
    "І все ж, підглянути б-{nw}"
    m "Жодних брудних думок!"
    "Ех, варто було спробувати."
    "Я перевдягаюсь і збираю свої речі."
    "Я знову спускаюсь униз."
    scene bg livingRoom_lightsOn_TvOff
    with wipeleft_scene
    "Я чекаю кілька хвилин, поки Моніка спуститься."
    show monika 4b at t11
    m "Гей! Готовий?"
    show monika 2a
    mc "Ага! Не змушуймо Сайорі та ГГ чекати."
    "Ми беремо свої речі та виходимо за двері."
    scene bg house
    with wipeleft_scene
    show monika 1a at t11
    "Я, як завжди, замикаю двері, і ми рушаємо."
    scene bg house
    with wipeleft_scene
    show monika 1j at t11
    "Ми приходимо до будинку Сайорі."
    "Я дзвоню у двері."
    s "Заходьте!"
    play sound closet_open
        pass
    "Я відчиняю двері та заходжу всередину."
    scene bg livingroom
    with wipeleft_scene
    play sound closet_close
        pass
    "Моніка зачиняє двері за нами."
    "ГГ на кухні, а Сайорі підводиться з дивана, щоб привітати нас."
    show sayori 4r at t11
    s "Приві-і-іт!"
    show sayori 1a
    p "Доброго ранку!"
    p "Я все дороблю за хвилинку."
    mc "Добре!"
    "Ми всі йдемо на кухню."
    scene bg kitchen
    with wipeleft_scene
    show monika 1a at t22
    show sayori 1a at t21
    "Ми сідаємо за стіл і починаємо балакати."
    show monika 2b at f22
    m "Тооож,{w=0.5} що ви вчора робили на фестивалі?"
    show monika 1c at t22
    show sayori turned lup rdown neut e1a mc b1d at f21
    s "Охо-хо,{w=0.5} дай-но я розповім тобі історію,{w=0.5} Моніко!"
    s 1c "Отже, ми трохи походили, так?"
    s "І проходимо повз кімнату аніме-клубу!"
    s 1x "Там лунала музика, і щось бурмотіли."
    s 3j "І ГГ такий: {i}\"Я знаю це!\"{/i}"
    s turned ldown rdown neut mc e4c b1d "І цей бовдур відчиняє двері та вигукує назву пісні й аніме, з якого вона."
    s 2x "У кімнаті настала тиша, а тоді хтось сказав, що він вгадав!"
    s 1l "Я дізналася потім, що вони вгадували аніме-опенінги."
    show sayori 1b at t21
    p "Ви говорите про мене так, ніби мене тут нема!"
    show sayori 4i at f21
    s "Тихо!"
    s 4j "Я розповідаю історію!"
    show sayori 4b at t21
    p "Хе-хе, гаразд..."
    show sayori 1x at f21
    s "Коротше, мені треба було готувати клас до кімнати жахів, тож я попрощалася з ГГ і пішла."
    s 4m "А поки мене не було, за одну лише обідню перерву він встиг стати почесним членом клубу, навчитися володіти катаною та розпочати війну за звання «кращої дівчини»!"
    s 1x "І тоді...{w=0.5}{nw}"
    $ _history_list.pop()
    show sayori 4n at hf21
    s "І тоді...{fast}Ой!"
    show protag 1l at l31
    show monika 1a at t33
    show sayori 1n at t32
    "ГГ підходить від прилавка."
    "Він ставить купу тарілок із різною їжею."
    show protag 1c at f31
    p "У нас є хліб, салямі та ще купа всього!"
    p 5l "Пригощайтесь!"
    show protag 1a at t31
    show sayori 4r
    show monika 3j
    "Ми починаємо наповнювати свої тарілки всім, що викладено."
    "І так, ми їмо досхочу."
    show monika 3c at t33
    show sayori 1c at f32
    s "Отже—"
    show sayori 1b at t32
    show protag 5d at f31
    p "Насправді нічого особливого й не сталося."
    show sayori 1a
    show monika 3a
    p 1c "Та й узагалі, я вже вступив до літературного клубу!"
    p 1l "Назад дороги нема!"
    show protag 1a at t31
    show sayori 1q at f32
    s "Мгм!"
    show sayori 1a at t32
    show monika 1j at f33
    m "Добре, бо інакше мені довелося б попросити Сайорі притягти тебе назад у клуб."
    show sayori turned ldown rdown neut cm oe
    show protag 1b
    m 3n "Але еее,{w=0.5} усі..."
    m 3l "Не хочу псувати настрій, але погляньте на годину..."
    show monika 1m at t33
    show sayori 4m at hf32
    s "О ні! Ми запізнимося!"
    show sayori at thide
    hide sayori
    show monika at thide
    hide monika
    show protag at thide
    hide protag
    "Усі поспіхом прибирають і закидають залишки до холодильника."
    "Я швидко роздаю всім їхні сумки, і ми вибігаємо за двері."
    scene bg house
    with wipeleft_scene
    "ГГ замикає двері, і ми починаємо бігти."
    scene bg residential_day
    with wipeleft_scene
    "Ми мчимо до школи так швидко, як тільки можемо."
    m "Знаєш, [player],{w=0.5} у такі моменти я шкодую, що не маю доступу до своєї консолі!"
    menu:
        "Так, зараз було б дуже зручно, правда ж?":
            m "Ага,{w=0.5} от якби..."
    call updateconsole("os.locsel\"school.loc\")", "Доступ заборонено.")
    m "Ех."
    call hideconsole
    m "Біжимо далі!"
    scene bg outside
    with wipeleft_scene
    "Ми прибуваємо до шкільних воріт."
    "Ледь ми встигаємо зайти, як дзвенить дзвоник."
    s "До зустрічі!"
    m "Бувай!"
    p "Па!"
    mc "Побачимось!"
    "Ми з Монікою біжимо на урок."
    stop music fadeout 2.0
        pass
    scene bg class_day
    with wipeleft_scene
    play music t12
        pass
    "Я сідаю за парту, і Моніка теж."
    scene bg class_day
    with wipeleft_scene
    "Як завжди, урок закінчується дзвоником."
    "Я складаю свої речі й дивлюсь на Моніку."
    show monika 1a at t11
    mc "Готова?"
    m 1b "Ага!"
    show monika 1a
    "Ми встаємо й вирушаємо до клубної кімнати."
    scene bg corridor
    with wipeleft_scene
    show monika 1j at t11
    "Навколо бігає багато учнів."
    "Більшість допомагають прибирати після вчорашнього фестивалю."
    "Тож і в клубній кімнаті нас теж чекає прибирання."
    "Ми заходимо всередину."
    scene bg festival
    with wipeleft_scene
    "Схоже, ми прийшли майже одночасно з усіма іншими."
    "Вони розпаковують свої речі та починають прибирати."
    show natsuki 1g at t11
    "Нацукі — в кінці кімнати."
    "Вона надягає блакитні рукавички."
    "Схоже, вона займається сміттям та миє підлогу."
    show natsuki at thide
    hide natsuki
    show sayori 1a at t11
    "Сайорі бере серветки й шкребки для свічок."
    "Вона наспівує мелодію, поки працює."
    show sayori at thide
    hide sayori
    show yuri 1e at t11
    "Юрі заходить у шафу, щоб узяти драбину."
    "Вона ставить її біля банера."
    show yuri at thide
    hide yuri
    show monika 1a at t11
    "Моніка сідає за свій стіл і починає розбирати документи клубу."
    "Вона дістає невеличку стопку і починає готувати їх до підпису й здачі."
    show monika at thide
    hide monika
    show protag 1a at t11
    "ГГ заходить до кімнати."
    "Він збирає свої речі й підходить допомогти Сайорі."
    show protag at thide
    hide protag
    show yuri 1f at t11
    y "[player], допоможеш мені з банером, будь ласка?"
    show yuri 1e
    mc "Звичайно."
    show yuri at thide
    hide yuri
    "Я підходжу до Юрі й допомагаю їй зняти величезний банер."
    "Ми його знімаємо, і вона кладе його у свою сумку."
    "Я підходжу до Моніки."
    show monika 1c at t11
    mc "Потрібна допомога?"
    m 1d "Не завадила б."
    m "Можеш віднести ці документи до студентської ради, будь ласка?"
    show monika 1c
    mc "Звісно."
    m 1b "Дякую!"
    scene bg corridor
    with wipeleft_scene
    "Я прямую до кімнати студентської ради."
    "Я стукаю у двері."
    "Президент відкриває двері."
    mc "Привіт! Я прийшов передати документи."
    "Міюкі" "\"Добре, я можу прийняти їх тут, якщо хочеш.\""
    mc "Ось, тримай."
    "Міюкі" "\"Дякую!\""
    "Я повертаюсь до клубної кімнати."
    scene bg club_day
    with wipeleft_scene
    "Кімната клубу вже майже прибрана."
    "Лише трохи сміття лишилося на підлозі."
    "Я підходжу до шафи й беру пару блакитних рукавичок з коробки."
    "Поки Нацукі підмітає сміття, я знаходжу швабру."
    "Я мию місця, де підмітала Нацукі, й прибираю плями на підлозі."
    "На щастя, це не займає багато часу, тож я швидко закінчую."
    "І, судячи з вигляду, інші теж впоралися зі своїми обов’язками."
    show monika 3b at f11
    m "Гаразд, усі!"
    m "У мене є ідея!"
    m 1b "А що, як відсвяткувати вчорашній фестиваль?"
    m "Що скажете, якщо завтра замість клубного заняття підемо в кафе?"
    show monika 1a at t11
    s "Ооо! Я за!"
    m 1b "Інші теж не проти?"
    show monika 1a
    mc "Я не проти."
    p "Так само."
    y "Звісно."
    n "Добре!"
    m 1b "Чудово!{w=0.5} Тоді вирішено!"
    m 3k "Завтра підемо в кафе святкувати!"
    m "Сьогодні ввечері я спробую знайти щось неподалік."
    m "А поки що, думаю, на сьогодні цього досить."
    show monika at thide
    hide monika
    "Усі беруть свої речі."
    show monika 1c at t11
    mc "Готова йти додому?"
    m 1j "Мгм~"
    show monika 1c at h11
    s "Ееей!"
    show monika 1c at t31
    show sayori 1x at l32
    show protag 1a at l33
    show sayori 1x at f32
    s "Хочете піти додому разом з нами?"
    show monika 1b at f31
    show sayori 1a at t32
    m "Звісно!"
    m "Ходімо!"
    scene bg corridor
    with wipeleft_scene
    "Моніка зачиняє клубну кімнату."
    "Ми виходимо на вулицю і рушаємо додому."
    scene bg residential_day
    with wipeleft_scene
    show monika 1a zorder 1 at t31
    show sayori 1a zorder 2 at t32
    show protag 1a zorder 3 at t33
    "Ми йдемо вулицею."
    show sayori 4r at t44
    "Сайорі стрибає на спину ГГ."
    show sayori at thide
    hide sayori
    show protag at thide
    hide protag
    show monika 1b at t11
    m "Гей, [player]..."
    m 3j "Не проти, якщо я теж застрибну тобі на спину?"
    menu:
        "Звісно.":
            m 1k "Ура!"
            show monika at thide
            hide monika
            "Моніка стрибає мені на спину."
            "Я тримаю її ноги, а вона міцно обіймає мене, поки я її несу."
            show protag 3l zorder 2 at t11
            show sayori 4r zorder 1 at t43
            s "Гей, давайте змагання!"
            s "Хто перший добіжить до твого дому — той виграв!"
            m "Домовились!"
            m "Не підведи мене, [player]!"
            show protag 3a
            s "Увага..."
            s "Руш!"
            s "Побігли!"
            show protag at thide
            hide protag
            show sayori at thide
            hide sayori
            "ГГ і я починаємо бігти."
            "Хоча, трохи повільніше за максимум, щоб не впустити дівчат."
            "Я помічаю наш будинок неподалік."
            m "Давай, [player]! Ми вже майже на фініші!"
            "Я пришвидшуюсь ще трохи."
            "ГГ і я біжимо нога в ногу, наближаючись до дому."
            scene bg house
            with wipeleft_scene
            "Я вириваюсь на кілька сантиметрів уперед і добігаю до воріт."
            "І ГГ, і я важко дихаємо, зупинившись."
            show protag 3z zorder 2 at t11
            show sayori 4r zorder 1 at t43
            p "Хах..."
            p 3y "Добрий... забіг..."
            mc "Так... гарні... перегони!"
            s "Надобраніч, друзі!"
            m "До зустрічі, Сайорі!"
            show sayori at thide
            hide sayori
            show protag at thide
            hide protag
            "Я однією рукою відчиняю двері, а іншою тримаю Моніку."
            play sound closet_open
                pass
            stop music fadeout 2.0
                pass
            scene bg livingRoom_lightsOn_TvOff
            with wipeleft_scene
            play music t9
                pass
            play sound closet_close
                pass
            "Я ставлю Моніку на підлогу."
            show monika 1j at t11
            mc "Фух, було весело."
            m "Мгм~!"
            m 5a "І я ще й побула так близько до тебе~"
            show monika 1a
            mc "Ага~!"
            mc "Я піду почну робити вечерю."
            m 1b "Добре!"
        "Ні.":
            show monika 1p at s11
            m "Ех, гаразд..."
            show monika 1a at t11
            "Ми йдемо далі додому."
            scene bg house
            with wipeleft_scene
            "Ми махаємо на прощання Сайорі та ГГ і заходимо всередину."
            play sound closet_open
                pass
            stop music fadeout 2.0
                pass
            scene bg livingRoom_lightsOn_TvOff
            with wipeleft_scene
            play music t9
                pass
            play sound closet_close
                pass
            mc "Я піду почну робити вечерю."
            m 1b "Добре!"
    scene bg kitchen
    with wipeleft_scene
    "Я заходжу на кухню."
    "Хммм..."
    "Думаю, сьогодні зроблю спагеті."
    "Я беру каструлю та наповнюю її водою."
    "Трохи олії, макарони — і ставлю варитися."
    "Тим часом беру сковорідку й кидаю туди інгредієнти для соусу."
    "Готую й помішую, поки воно смажиться."
    "Я спираюся на стіл і чекаю, поки звариться."
    "Моніка спускається в піжамі й з ноутбуком у руках."
    show monika p_1b at t11
    m "Оох~!{w=0.5} Смачно пахне!"
    show monika p_1a
    mc "Сподіваюся, на смак буде так само!"
    m p_1b "Поки ти готуєш, я пошукаю місце, куди можна сходити з клубом завтра."
    show monika p_1a
    mc "Добре."
    show monika at thide
    hide monika
    "Вона сідає й починає клацати на ноутбуці, поки я стежу за нашою вечерею."
    m "Гей, що ти думаєш про це місце?"
    mc "Гм?"
    "Вона показує маленьке кафе за квартал від школи."
    mc "Гаразд. Схоже на гарне місце."
    m "Чудово!"
    m "Я надішлю повідомлення всім, щоб вони знали."
    mc "Добре."
    "Вона витягує телефон і швидко щось набирає."
    "За кілька секунд вона піднімає погляд."
    m "Гей,{w=0.5} [player],{w=0.5} якщо хочеш,{w=0.5} я можу наглядати за їжею, поки ти підеш переодягнешся."
    mc "Звісно. Дякую!"
    m "Авжеж!"
    "Я йду нагору."
    scene bg bedroom
    with wipeleft_scene
    "Я швидко переодягаюся у свій одяг для сну й спускаюся вниз."
    scene bg kitchen
    with wipeleft_scene
    "Я знову беру на себе обов’язок наглядати за їжею, поки Моніка знову сідає і гортає щось на ноутбуці."
    "Незабаром макарони розм’якшують, і я вимикаю плиту."
    "Я швидко куштую соус, який приготував, і також знімаю його з вогню."
    "Я беру дві тарілки та накладаю порцію кожному."
    "Моніка закриває ноутбук і бере тарілку."
    show monika p_1k at t11
    m "Дякую!"
    show monika p_1a
    mc "Сподіваюся, тобі сподобається!"
    show monika p_1j
    "Ми бережно смакуємо вечерю разом."
    show monika at thide
    hide monika
    "Ми закінчуємо їсти, а я ставлю залишки в холодильник на завтра."
    "Я швидко прибираю кухню, поки Моніка знову щось клацає на ноутбуці."
    mc "Що робиш?"
    show monika p_1b at t11
    m "Ох, я просто дивилась інші місця, куди ми могли б сходити..."
    m p_2b "Ось знайшла ще одне кафе..."
    m "А тут парк..."
    m p_1k "Просто шукаю місця, де можу проводити час із тобою~"
    show monika p_1a
    mc "Ага, добре."
    mc "Хочеш пошукати їх разом?"
    m p_1j "Мгм~"
    "Я сідаю поруч із нею та починаю нотувати кілька місць і ідей, які ми могли б здійснити."
    m p_1b "Я не хочу, щоб бодай один день минув даремно!"
    m p_1k "Щодня я хочу робити щось веселе з тобою, [player]!"
    show monika p_1a
    mc "Я теж, Моніко."
    "Ми ще кілька хвилин шукаємо, що можна зробити."
    mc "Гаразд..."
    mc "Думаю, на сьогодні досить."
    mc "Вже пізно,{w=0.5} нам варто йти спати."
    m p_1l "Так, я навіть не помітила, як час пролетів."
    show monika at thide
    hide monika
    "Вона вимикає ноутбук, а я вимикаю світло, і ми разом ідемо нагору."
    scene bg bedroom
    with wipeleft_scene
    "Моніка кладе ноутбук на стіл і стрибає в ліжко."
    scene bg n_bedroom
    "Я вимикаю світло й лягаю поруч із нею."
    scene black
    with Dissolve(2.0)
    m "Сьогодні було чудово."
    mc "Так."
    m "Скоро я зможу робити це з тобою по-справжньому, [player]."
    menu:
        "Я теж на це сподіваюся, Моніко.":
            pass
    m "Уфуфу~"
    m "Надобраніч, [player]~"
    "Я повільно засинаю, переходячи в наступний день..."
    call d6
