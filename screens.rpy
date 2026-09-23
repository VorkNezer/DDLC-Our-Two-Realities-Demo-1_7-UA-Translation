init -1 style default:
    color gui.text_color
    line_overlap_split 1
    line_spacing 1
    font gui.default_font
    outlines [(2, "#000000aa", 0, 0)]
    size gui.text_size
init -1 style default_monika is normal:
    slow_cps 30
init -1 style edited is default:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    ypos gui.text_ypos
    text_align gui.text_xalign
    kerning 8
    xsize gui.text_width
    layout ("subtitle" if gui.text_xalign else "tex")
    font "gui/font/comic-sans-ms.ttf"
    outlines [(10, "#000", 0, 0)]
init -1 style normal is default:
    xpos gui.text_xpos
    layout ("subtitle" if gui.text_xalign else "tex")
    ypos gui.text_ypos
    text_align gui.text_xalign
    xsize gui.text_width
    xanchor gui.text_xalign
init -1 style input:
    color gui.accent_color
init -1 style hyperlink_text:
    color gui.accent_color
    hover_color gui.hover_color
    hover_underline True
init -1 style splash_text:
    color "#000"
    font gui.default_font
    text_align 0.5
    outlines []
    size 24
init -1 style poemgame_text:
    font "gui/font/comic-sans-ms.ttf"
    yalign 0.5
    color "#000"
    hover_xoffset -3
    outlines []
    hover_outlines [(3, "#fef", 0, 0), (2, "#fcf", 0, 0), (1, "#faf", 0, 0)]
    size 30
init -1 style gui_text:
    color gui.interface_text_color
    font gui.interface_font
    size gui.interface_text_size
init -1 style button:
    properties gui.button_properties("button")
init -1 style button_text is gui_text:
    properties gui.button_text_properties("button")
    yalign 0.5
init -1 style label_text is gui_text:
    color gui.accent_color
    size gui.label_text_size
init -1 style prompt_text is gui_text:
    color gui.text_color
    size gui.interface_text_size
init -1 style vbar:
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    xsize gui.bar_size
init -1 style bar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)
init -1 style scrollbar:
    bar_invert True
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    unscrollable "hide"
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)
init -1 style vscrollbar:
    bar_invert True
    unscrollable "hide"
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    xsize 18
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
init -1 style slider:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb "gui/slider/horizontal_hover_thumb.png"
init -1 style vslider:
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    xsize gui.slider_size
    thumb "gui/slider/vertical_[prefix_]thumb.png"
init -1 style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
init -501 screen say(who, what):
    style_prefix "say"
    window:
        id "window"
        text what:
            id "what"
        if who is not None:
            window:
                style "namebox"
                text who:
                    id "who"
    if not renpy.variant("small"):
        add SideImage():
            xalign 0.0
            yalign 1.0
    use quick_menu
init -1 style window is default
init -1 style say_label is default
init -1 style say_dialogue is default
init -1 style say_thought is say_dialogue
init -1 style namebox is default
init -1 style namebox_label is say_label
init -1 style window:
    xalign 0.5
    ysize gui.textbox_height
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)
    yalign gui.textbox_yalign
    xfill True
init -1 style window_monika is window:
    background Image("gui/textbox_monika.png", xalign=0.5, yalign=1.0)
init -1 style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ysize gui.namebox_height
    ypos gui.name_ypos
    padding gui.namebox_borders.padding
    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
init -1 style say_label:
    xalign gui.name_xalign
    yalign 0.5
    color gui.accent_color
    font gui.name_font
    outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]
    size gui.name_text_size
init -1 style say_dialogue:
    xpos gui.text_xpos
    layout ("subtitle" if gui.text_xalign else "tex")
    ypos gui.text_ypos
    text_align gui.text_xalign
    xsize gui.text_width
    xanchor gui.text_xalign
init 499 image ctc:
    xalign 0.81 yalign 0.98 xoffset -5 alpha 0.0 subpixel True
    "gui/ctc.png"
    block:
        easeout 0.75 alpha 1.0 xoffset 0
        easein 0.75 alpha 0.5 xoffset -5
        repeat
init 499 image input_caret:
    Solid("#b59")
    size (2,25) subpixel True
    block:
        linear 0.35 alpha 0
        linear 0.35 alpha 1
        repeat
init -501 screen input(prompt):
    style_prefix "input"
    window:
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 30
            text prompt:
                style "input_prompt"
            input:
                id "input"
init -1 style input_prompt is default
init -1 style input_prompt:
    xalign gui.text_xalign
    xmaximum gui.text_width
    text_align gui.text_xalign
init -1 style input:
    caret "input_caret"
    xalign 0.5
    xmaximum gui.text_width
    text_align 0.5
init -501 screen choice(items):
    style_prefix "choice"
    vbox:
        for i in items:
            textbutton i.caption:
                action i.action
define -1 config.narrator_menu = True
init -1 style choice_vbox is vbox
init -1 style choice_button is button
init -1 style choice_button_text is button_text
init -1 style choice_vbox:
    xalign 0.5
    spacing gui.choice_spacing
    ypos 270
    yanchor 0.5
init -1 style choice_button is default:
    hover_sound gui.hover_sound
    properties gui.button_properties("choice_button")
    activate_sound gui.activate_sound
init -1 style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines []
init -1 python:
    def RigMouse():
        currentpos = renpy.get_mouse_pos()
        targetpos = [640, 345]
        if currentpos[1] < targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)
init -501 screen rigged_choice(items):
    style_prefix "choice"
    vbox:
        for i in items:
            textbutton i.caption:
                action i.action
    timer 1.0/30.0:
        repeat True
        action Function(RigMouse)
define -1 config.narrator_menu = True
init -1 style choice_vbox is vbox
init -1 style choice_button is button
init -1 style choice_button_text is button_text
init -1 style choice_vbox:
    xalign 0.5
    spacing gui.choice_spacing
    ypos 270
    yanchor 0.5
init -1 style choice_button is default:
    hover_sound gui.hover_sound
    properties gui.button_properties("choice_button")
    activate_sound gui.activate_sound
init -1 style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines []
init -501 screen quick_menu():
    zorder 100
    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 0.995
            textbutton _("Історія"):
                action ShowMenu('history')
            textbutton _("Пропуск"):
                action Skip()
                alternate Skip(fast=True, confirm=True)
            textbutton _("Авто"):
                action Preference("auto-forward", "toggle")
            textbutton _("Зберегти"):
                action ShowMenu('save')
            textbutton _("Завантажити"):
                action ShowMenu('load')
            textbutton _("Налаштування"):
                action ShowMenu('preferences')
default -1 quick_menu = True
init -1 style quick_button:
    properties gui.button_properties("quick_button")
    activate_sound gui.activate_sound
init -1 style quick_button_text:
    properties gui.button_text_properties("quick_button")
    outlines []
init -1 python:
    def FinishEnterName():
        if not player: return
        persistent.playername = player
        renpy.hide_screen("name_input")
        renpy.jump_out_of_context("start")
init -501 screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.8
        spacing gui.navigation_spacing
        if not persistent.autoload or not main_menu:
            if main_menu:
                if persistent.playthrough == 1:
                    textbutton _("ŔŗñĮ¼»ŧþŀÂŻŕěōì«"):
                        action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Будь ласка напишіть ваше ім'я", ok_action=Function(FinishEnterName)))
                else:
                    textbutton _("Нова гра"):
                        action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Будь ласка напишіть ваше ім'я", ok_action=Function(FinishEnterName)))
            else:
                textbutton _("Історія"):
                    action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]
                textbutton _("Зберегти гру"):
                    action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]
            textbutton _("Завантажити гру"):
                action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)]
            if _in_replay:
                textbutton _("End Replay"):
                    action EndReplay(confirm=True)
            elif not main_menu:
                if persistent.playthrough != 3:
                    textbutton _("Головне меню"):
                        action MainMenu()
                else:
                    textbutton _("Головне меню"):
                        action NullAction()
            textbutton _("Налаштування"):
                action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]
            if renpy.variant("pc"):
                textbutton _("Допомога"):
                    action OpenURL("https://t.me/VorkNezer")
                textbutton _("Вихід"):
                    action Quit(confirm=not main_menu)
        else:
            timer 1.75:
                action Start("autoload_yurikill")
init -1 style navigation_button is gui_button
init -1 style navigation_button_text is gui_button_text
init -1 style navigation_button:
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound
    size_group "navigation"
    properties gui.button_properties("navigation_button")
init -1 style navigation_button_text:
    color "#fff"
    insensitive_outlines [(4, "#fce", 0, 0), (2, "#fce", 2, 2)]
    outlines [(4, "#b59", 0, 0), (2, "#b59", 2, 2)]
    font "gui/font/comic-sans-ms-bold.ttf"
    properties gui.button_text_properties("navigation_button")
    hover_outlines [(4, "#fac", 0, 0), (2, "#fac", 2, 2)]
init -501 screen main_menu():
    tag menu
    style_prefix "main_menu"
    if persistent.ghost_menu:
        add "white"
        add "menu_art_y_ghost"
        add "menu_art_n_ghost"
    else:
        add "menu_bg"
        add "menu_art_y"
        add "menu_art_n"
    frame
    use navigation
    if gui.show_name:
        vbox:
            text "[config.name!t]":
                style "main_menu_title"
            text "[config.version]":
                style "main_menu_version"
    if not persistent.ghost_menu:
        add "menu_particles"
        add "menu_particles"
        add "menu_particles"
        add "menu_logo"
    if persistent.ghost_menu:
        add "menu_art_s_ghost"
        add "menu_art_m_ghost"
    else:
        if persistent.playthrough == 1 or persistent.playthrough == 2:
            add "menu_art_s_glitch"
        else:
            add "menu_art_s"
    add "menu_particles"
    if persistent.playthrough != 4:
        add "menu_art_m"
        add "menu_fade"
    key "K_ESCAPE":
        action Quit(confirm=False)
init -1 style main_menu_frame is empty
init -1 style main_menu_vbox is vbox
init -1 style main_menu_text is gui_text
init -1 style main_menu_title is main_menu_text
init -1 style main_menu_version is main_menu_text:
    color "#000000"
    outlines []
    size 16
init -1 style main_menu_frame:
    yfill True
    background "menu_nav"
    xsize 310
init -1 style main_menu_vbox:
    xalign 1.0
    xmaximum 800
    yalign 1.0
    xoffset -20
    yoffset -20
init -1 style main_menu_text:
    color gui.accent_color
    xalign 1.0
    layout "subtitle"
    text_align 1.0
init -1 style main_menu_title:
    size gui.title_text_size
init -501 screen game_menu_m():
    $ persistent.menu_bg_m = True
    add "gui/menu_bg_m.png"
    timer 0.3:
        action Hide("game_menu_m")
init -501 screen game_menu(title, scroll=None):
    style_prefix "game_menu"
    if main_menu:
        add gui.main_menu_background
    else:
        key "mouseup_3":
            action Return()
        add gui.game_menu_background
    frame:
        style "game_menu_outer_frame"
        hbox:
            frame:
                style "game_menu_navigation_frame"
            frame:
                style "game_menu_content_frame"
                if scroll == "viewport":
                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        yinitial 1.0
                        side_yfill True
                        vbox:
                            transclude
                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial 1.0
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        side_yfill True
                        transclude
                else:
                    transclude
    use navigation
    if not main_menu and persistent.playthrough == 2 and not persistent.menu_bg_m and renpy.random.randint(0, 49) == 0:
        on "show":
            action Show("game_menu_m")
    textbutton _("Назад"):
        style "return_button"
        action Return()
    label title
    if main_menu:
        key "game_menu":
            action ShowMenu("main_menu")
init -1 style game_menu_outer_frame is empty
init -1 style game_menu_navigation_frame is empty
init -1 style game_menu_content_frame is empty
init -1 style game_menu_viewport is gui_viewport
init -1 style game_menu_side is gui_side
init -1 style game_menu_scrollbar is gui_vscrollbar
init -1 style game_menu_label is gui_label
init -1 style game_menu_label_text is gui_label_text
init -1 style return_button is navigation_button
init -1 style return_button_text is navigation_button_text
init -1 style game_menu_outer_frame:
    top_padding 120
    bottom_padding 30
    background "gui/overlay/game_menu.png"
init -1 style game_menu_navigation_frame:
    yfill True
    xsize 280
init -1 style game_menu_content_frame:
    right_margin 20
    top_margin 10
    left_margin 40
init -1 style game_menu_viewport:
    xsize 920
init -1 style game_menu_vscrollbar:
    unscrollable gui.unscrollable
init -1 style game_menu_side:
    spacing 10
init -1 style game_menu_label:
    xpos 50
    ysize 120
init -1 style game_menu_label_text:
    color "#fff"
    font "gui/font/comic-sans-ms-bold.ttf"
    outlines [(6, "#b59", 0, 0), (3, "#b59", 2, 2)]
    yalign 0.5
    size gui.title_text_size
init -1 style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30
init -501 screen about():
    tag menu
    use game_menu(_("About"), scroll="viewport"):
        style_prefix "about"
        vbox:
            label "[config.name!t]"
            text _("Version [config.version!t]\n")
            if gui.about:
                text "[gui.about!t]\n"
            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")
define -1 gui.about = ""
init -1 style about_label is gui_label
init -1 style about_label_text is gui_label_text
init -1 style about_text is gui_text
init -1 style about_label_text:
    size gui.label_text_size
init -501 screen save():
    tag menu
    use file_slots(_("Зберегти"))
init -501 screen load():
    tag menu
    use file_slots(_("Завантажити"))
init -1 python:
    def FileActionMod(name, page=None, **kwargs):
        if persistent.playthrough == 1 and not persistent.deleted_saves and renpy.current_screen().screen_name[0] == "load" and FileLoadable(name):
            return Show(screen="dialog", message="File error: \"characters/sayori.chr\"\n\nThe file is missing or corrupt.",
                    ok_action=Show(screen="dialog", message="The save file is corrupt. Starting a new game.", ok_action=Function(renpy.full_restart, label="start")))
        elif persistent.playthrough == 3 and renpy.current_screen().screen_name[0] == "save":
            return Show(screen="dialog", message="There's no point in saving anymore.\nDon't worry, I'm not going anywhere.", ok_action=Hide("dialog"))
        else:
            return FileAction(name)
init -501 screen file_slots(title):
    default page_name_value = FilePageNameInputValue()
    use game_menu(title):
        fixed:
            order_reverse True
            button:
                style "page_label"
                xalign 0.5
                input:
                    style "page_label_text"
                    value page_name_value
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing
                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    button:
                        action FileActionMod(slot)
                        vbox:
                            add FileScreenshot(slot):
                                xalign 0.5
                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                style "slot_time_text"
                            text FileSaveName(slot):
                                style "slot_name_text"
                            key "save_delete":
                                action FileDelete(slot)
            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0
                spacing gui.page_spacing
                for page in range(1, 10):
                    textbutton "[page]":
                        action FilePage(page)
init -1 style page_label is gui_label
init -1 style page_label_text is gui_label_text
init -1 style page_button is gui_button
init -1 style page_button_text is gui_button_text
init -1 style slot_button is gui_button
init -1 style slot_button_text is gui_button_text
init -1 style slot_time_text is slot_button_text
init -1 style slot_name_text is slot_button_text
init -1 style page_label:
    ypadding 3
    xpadding 50
init -1 style page_label_text:
    color "#000"
    hover_color gui.hover_color
    layout "subtitle"
    outlines []
    text_align 0.5
init -1 style page_button:
    properties gui.button_properties("page_button")
init -1 style page_button_text:
    properties gui.button_text_properties("page_button")
    outlines []
init -1 style slot_button:
    properties gui.button_properties("slot_button")
init -1 style slot_button_text:
    color "#666"
    properties gui.button_text_properties("slot_button")
    outlines []
init -501 screen preferences():
    tag menu
    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4
    use game_menu(_("Налаштування"), scroll="viewport"):
        vbox:
            xoffset 50
            hbox:
                box_wrap True
                if renpy.variant("pc"):
                    vbox:
                        style_prefix "radio"
                        label _("Режим")
                        textbutton _("Вікно"):
                            action Preference("display", "window")
                        textbutton _("Повноекранний"):
                            action Preference("display", "fullscreen")
                if config.developer:
                    vbox:
                        style_prefix "radio"
                        label _("Сторона відкату")
                        textbutton _("Відключити"):
                            action Preference("rollback side", "disable")
                        textbutton _("Зліва"):
                            action Preference("rollback side", "left")
                        textbutton _("Справа"):
                            action Preference("rollback side", "right")
                vbox:
                    style_prefix "check"
                    label _("Пропустити")
                    textbutton _("Непрочитане"):
                        action Preference("skip", "toggle")
                    textbutton _("Після вибору"):
                        action Preference("after choices", "toggle")
            null:
                height (4 * gui.pref_spacing)
            hbox:
                style_prefix "slider"
                box_wrap True
                vbox:
                    label _("Швидкість тексту")
                    bar:
                        value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, style="slider", offset=20)
                    label _("Швидкість авто-читання")
                    bar:
                        value Preference("auto-forward time")
                vbox:
                    if config.has_music:
                        label _("Музика")
                        hbox:
                            bar:
                                value Preference("music volume")
                    if config.has_sound:
                        label _("Звук")
                        hbox:
                            bar:
                                value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Тест"):
                                    action Play("sound", config.sample_sound)
                    if config.has_voice:
                        label _("Голос")
                        hbox:
                            bar:
                                value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("Тест"):
                                    action Play("voice", config.sample_voice)
                    if config.has_music or config.has_sound or config.has_voice:
                        null:
                            height gui.pref_spacing
                        textbutton _("Заглушити все"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
    text "v[config.version]":
        xalign 1.0
        yalign 1.0
        xoffset -10
        yoffset -10
        style "main_menu_version"
init -1 style pref_label is gui_label
init -1 style pref_label_text is gui_label_text
init -1 style pref_vbox is vbox
init -1 style radio_label is pref_label
init -1 style radio_label_text is pref_label_text
init -1 style radio_button is gui_button
init -1 style radio_button_text is gui_button_text
init -1 style radio_vbox is pref_vbox
init -1 style check_label is pref_label
init -1 style check_label_text is pref_label_text
init -1 style check_button is gui_button
init -1 style check_button_text is gui_button_text
init -1 style check_vbox is pref_vbox
init -1 style slider_label is pref_label
init -1 style slider_label_text is pref_label_text
init -1 style slider_slider is gui_slider
init -1 style slider_button is gui_button
init -1 style slider_button_text is gui_button_text
init -1 style slider_pref_vbox is pref_vbox
init -1 style mute_all_button is check_button
init -1 style mute_all_button_text is check_button_text
init -1 style pref_label:
    bottom_margin 2
    top_margin gui.pref_spacing
init -1 style pref_label_text:
    color "#fff"
    font "gui/font/comic-sans-ms-bold.ttf"
    outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]
    yalign 1.0
    size 24
init -1 style pref_vbox:
    xsize 225
init -1 style radio_vbox:
    spacing gui.pref_button_spacing
init -1 style radio_button:
    foreground "gui/button/check_[prefix_]foreground.png"
    properties gui.button_properties("radio_button")
init -1 style radio_button_text:
    font "gui/font/comic-sans-ms-bold.ttf"
    properties gui.button_text_properties("radio_button")
    outlines []
init -1 style check_vbox:
    spacing gui.pref_button_spacing
init -1 style check_button:
    foreground "gui/button/check_[prefix_]foreground.png"
    properties gui.button_properties("check_button")
init -1 style check_button_text:
    font "gui/font/comic-sans-ms.ttf"
    properties gui.button_text_properties("check_button")
    outlines []
init -1 style slider_slider:
    xsize 350
init -1 style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10
init -1 style slider_button_text:
    properties gui.button_text_properties("slider_button")
init -1 style slider_vbox:
    xsize 450
init -501 screen history():
    tag menu
    predict False
    use game_menu(_("Історія"), scroll=("vpgrid" if gui.history_height else "viewport")):
        style_prefix "history"
        for h in _history_list:
            window:
                fixed:
                    yfit True
                    if h.who:
                        label h.who:
                            style "history_name"
                            if "color" in h.who_args:
                                text_color h.who_args["color"]
                    text h.what
        if not _history_list:
            label _("Історія діалогів пуста.")
init -1 style history_window is empty
init -1 style history_name is gui_label
init -1 style history_name_text is gui_label_text
init -1 style history_text is gui_text
init -1 style history_text is gui_text
init -1 style history_label is gui_label
init -1 style history_label_text is gui_label_text
init -1 style history_window:
    ysize gui.history_height
    xfill True
init -1 style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width
init -1 style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
init -1 style history_text:
    xpos gui.history_text_xpos
    xanchor gui.history_text_xalign
    ypos gui.history_text_ypos
    text_align gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    layout ("subtitle" if gui.history_text_xalign else "tex")
init -1 style history_label:
    xfill True
init -1 style history_label_text:
    xalign 0.5
init -501 screen name_input(message, ok_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    key "K_RETURN":
        action [Play("sound", gui.activate_sound), ok_action]
    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 30
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            input:
                default ""
                value VariableInputValue("player")
                length 12
                allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгдеєжзийклмнопрстуфхцчшщьюя-"
            hbox:
                xalign 0.5
                spacing 100
                textbutton _("OK"):
                    action ok_action
init -501 screen dialog(message, ok_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 30
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            hbox:
                xalign 0.5
                spacing 100
                textbutton _("OK"):
                    action ok_action
init 499 image confirm_glitch:
    "gui/overlay/confirm_glitch.png"
    pause 0.02
    "gui/overlay/confirm_glitch2.png"
    pause 0.02
    repeat
init -501 screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 30
            if in_sayori_kill and message == layout.QUIT:
                add "confirm_glitch":
                    xalign 0.5
            else:
                label _(message):
                    style "confirm_prompt"
                    xalign 0.5
            hbox:
                xalign 0.5
                spacing 100
                textbutton _("Так"):
                    action yes_action
                textbutton _("Ні"):
                    action no_action
init -1 style confirm_frame is gui_frame
init -1 style confirm_prompt is gui_prompt
init -1 style confirm_prompt_text is gui_prompt_text
init -1 style confirm_button is gui_medium_button
init -1 style confirm_button_text is gui_medium_button_text
init -1 style confirm_frame:
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
init -1 style confirm_prompt_text:
    color "#000"
    layout "subtitle"
    outlines []
    text_align 0.5
init -1 style confirm_button:
    hover_sound gui.hover_sound
    properties gui.button_properties("confirm_button")
    activate_sound gui.activate_sound
init -1 style confirm_button_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")
init -501 screen fake_skip_indicator():
    use skip_indicator
init -501 screen skip_indicator():
    zorder 100
    style_prefix "skip"
    frame:
        hbox:
            spacing 6
            text _("Пропуск")
            text "▸":
                at delayed_blink(0.0, 1.0)
                style "skip_triangle"
            text "▸":
                at delayed_blink(0.2, 1.0)
                style "skip_triangle"
            text "▸":
                at delayed_blink(0.4, 1.0)
                style "skip_triangle"
transform -1 delayed_blink(delay, cycle):
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat
init -1 style skip_frame is empty
init -1 style skip_text is gui_text
init -1 style skip_triangle is skip_text
init -1 style skip_frame:
    padding gui.skip_frame_borders.padding
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
init -1 style skip_text:
    size gui.notify_text_size
init -1 style skip_triangle:
    font "DejaVuSans.ttf"
init -501 screen notify(message):
    zorder 100
    style_prefix "notify"
    frame:
        at notify_appear
        text message
    timer 3.25:
        action Hide('notify')
transform -1 notify_appear:
    on hide:
        linear .5 alpha 0.0
    on show:
        alpha 0
        linear .25 alpha 1.0
init -1 style notify_frame is empty
init -1 style notify_text is gui_text
init -1 style notify_frame:
    padding gui.notify_frame_borders.padding
    ypos gui.notify_ypos
    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
init -1 style notify_text:
    size gui.notify_text_size
