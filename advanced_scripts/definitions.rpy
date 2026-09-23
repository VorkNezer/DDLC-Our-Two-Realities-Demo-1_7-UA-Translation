#This is a copy of definitions.rpy from DDLC.
#Use this as a starting point if you would like to override with your own.

#Explanation for Definitions
#This section defines stuff for the game: sprite poses for the girls, music, and backgrounds
#If you plan on adding new content, pop them over down there and mimic the appropriate lines!
define persistent.demo = False
define persistent.steam = False
define config.developer = False #Change this flag to True to enable dev tools

python early:
    import singleton
    me = singleton.SingleInstance()

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("extra", mixer="sfx", loop=True, tight=True)
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    def delete_character(name):
        if persistent.do_not_delete: return
        import os
        try: os.remove(config.basedir + "/characters/" + name + ".chr")
        except: pass
    def pause(time=None):
        if not time:
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            return
        if time <= 0: return
        renpy.pause(time)

#Music
#The Music section is where you can reference existing DDLC audio

#You'll see this in some existing scripts as command 'play music [t1]' for example
#For easier reference, there are comments next to it so you can go DJ on the mod :)



define audio.t1 = "<loop 22.073>bgm/1.ogg"  #Main theme (title)


define audio.t2 = "<loop 4.499>bgm/2.ogg"   #Sayori theme
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg"   #Main theme (in-game)
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg"  #Poem minigame
define audio.t4g = "<loop 1.000>bgm/4g.ogg"

define audio.t5 = "<loop 4.444>bgm/5.ogg"   #Sharing poems...... 'Okay Everyone~!'
#Hey Mod team, our themes aren't defined here in the original script.
#Did some reading around and there was this + "_character" reference elsewhere.
#Anyhow, I'll try 'defining' them and see if it works!

define audio.tmonika = "<loop 4.444>bgm/5_monika.ogg" #I'm the only one with pianos x3
define audio.tsayori = "<loop 4.444>bgm/5_sayori.ogg" #Hxppy Thoughts with Ukelele & Snapping~!
define audio.tnatsuki = "<loop 4.444>bgm/5_natsuki.ogg" #Was it always cute on purpose?
define audio.tyuri = "<loop 4.444>bgm/5_yuri.ogg" #Fancy harps and instruments!

#Yeah, Monika... that should be good.
#So, take it from her and if you want to define music, make sure it exists in the appropriate folder
#Define its "audio.name" and see how it goes! (this should always be .ogg too, I think)

define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg"  #Yuri/Natsuki theme
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg"   #Causing trouble
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg"   #Trouble resolved
define audio.t9 = "<loop 3.172>bgm/9.ogg"   #Emotional
define audio.t9g = "<loop 1.532>bgm/9g.ogg" #207% speed
define audio.t10 = "<loop 5.861>bgm/10.ogg"   #Confession
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"

define audio.t11 = "<loop 0>mod_assets/music/t11.ogg"#Monika before story ost
define audio.t12 = "<loop 0>mod_assets/music/t12.ogg"

define audio.m1 = "<loop 0>bgm/m1.ogg" #Monika and her spaceroom music
define audio.mend = "<loop 6.424>bgm/monika-end.ogg" #Monika music post-deletion

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"

define audio.debate1 = "<loop 0>mod_assets/music/debate1.mp3"
define audio.debate2 = "<loop 0>mod_assets/music/debate2.mp3"
define audio.war = "<loop 0>mod_assets/music/war.ogg"


# Backgrounds
image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"
image bg residential_day = "bg/residential.png"
image bg class_day = "bg/class.png"
image bg corridor = "bg/corridor.png"
image bg club_day = "bg/club.png"
image bg club_day2 = "bg/club-skill.png"
image bg closet = "bg/closet.png"
image bg bedroom = "bg/bedroom.png"
image bg sayori_bedroom = "bg/sayori_bedroom.png"
image bg house = "bg/house.png"
image bg kitchen = "bg/kitchen.png"

image bg club_morning = "mod_assets/club_morning.png"
image bg music_room = "mod_assets/music_room.png"
image bg music_morning = "mod_assets/music_morning.png"
image bg vendingmachine = "mod_assets/vendingmachine.png"

image bg park = "mod_assets/park.png"
image bg n_park = "mod_assets/nightpark.jpg"
image bg n_sayori_bedroom = "mod_assets/nightsayoribedroom.png"
image bg n_bedroom = "mod_assets/nightbedroom.png"
image bg n_residential = "mod_assets/nightresidential.png"
image bg n_house = "mod_assets/nighthouse.png"
image bg shop_day = "mod_assets/Storeday.png"
image bg park2 = "mod_assets/Parkday.png"
image bg library = "mod_assets/Libraryday.png"
image bg libraryin = "mod_assets/Libraryinterior.png"
image bg shop_night = "mod_assets/Storenight.png"
image bg pool = "mod_assets/Pool.png"
image bg poolhall = "mod_assets/Poolhall.png"
image bg outside = "mod_assets/outside.png"
image bg theater = "mod_assets/theater.png"
image bg residential_aft = "mod_assets/dawnresidential.png"
image bg livingroom = "mod_assets/livingroom.png"
image bg park3 = "mod_assets/park3.png"
image bg balcony = "mod_assets/balcony.png"
image bg gym = "mod_assets/gym.png"
image bg n_outside = "mod_assets/n_outside.png"
image bg a_outside = "mod_assets/a_outside.png"
image bg shower = "mod_assets/shower.png"
image bg water = "mod_assets/water.png"
image bg backyard = "mod_assets/backyard.png"
image bg a_backyard = "mod_assets/a_backyard.png"
image bg empty_club = "mod_assets/empty_club.png"

image bg house_dawn = "ourtime_assets/bg/house_dawn.png"
image bg cafe_inside = "ourtime_assets/bg/cafe-inside.png"
image bg cafe_exterior = "ourtime_assets/bg/cafe_exterior.png"
image bg livingRoom_lightsOn_TvOff = "ourtime_assets/bg/livingRoom_lightsOn_TvOff.png"
image bg livingRoom_lightsOn_TvOn = "ourtime_assets/bg/livingRoom_lightsOn_TvOn.png"
image bg livingRoom_lightsOff = "ourtime_assets/bg/livingRoom_lightsOff.png"
image bg shop_outside_dusk = "ourtime_assets/bg/shop_outside_afternoon.png"
image bg shop_interior = "ourtime_assets/bg/shop_interior.png"
image bg bedroom_night = "ourtime_assets/bg/bedroom_night.png"
image bg trainStation_day = "ourtime_assets/bg/trainStation_day.png"
image bg trainStation_dawn = "ourtime_assets/bg/trainStation_dawn.png"
image bg trainInterior_day = "ourtime_assets/bg/trainInterior_day.png"
image bg trainInterior_dawn = "ourtime_assets/bg/trainInterior_dawn.png"
image bg city_day = "ourtime_assets/bg/city_day.png"
image bg city_day_p = "ourtime_assets/bg/city_day_p.png"
image bg mall_exterior_day = "ourtime_assets/bg/mall_exterior_day.png"
image bg mall_interior_day = "ourtime_assets/bg/mall_interior.png"
image bg mall_interior_dawn = "ourtime_assets/bg/mall_interior_dawn.png"
image bg clothingstore = "ourtime_assets/bg/clothingshop.png"
image bg clothingstore_dressingroom = "ourtime_assets/bg/clothingshop_dressingroom.png"

image bg festival = "mod_assets/festival.png"
image bg sky = "mod_assets/sky.png"

image bg notebook = "bg/notebook.png"
image bg notebook-glitch = "bg/notebook-glitch.png"

image bg glitch = LiveTile("bg/glitch.jpg")

image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0
        #1.0
        #linear 1.0 alpha 0.0

image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0
        #1.0
        #linear 1.0 alpha 0.0


#new day text

image day1:
    ypos 380
    Text("День 1: Новий початок  -  п'ятниця", style="monika_credits_text", size=70)

image day2:
    ypos 380
    Text("День 2: Полум'я письма  -  субота", style="monika_credits_text", size=70)

image day3:
    ypos 380
    Text("День 3: Смак екскурсій  –  неділя", style="monika_credits_text", size=70)

image day4:
    ypos 380
    Text("День 4: Фестиваль  -  понеділок", style="monika_credits_text", size=70)

image day5:
    ypos 380
    Text("День 5: Прибраний номер  –  вівторок", style="monika_credits_text", size=70)

image day6:
    ypos 380
    Text("День 6: Кава та тістечка  –  середа", style="monika_credits_text", size=70)

image day7:
    ypos 380
    Text("День 7: Пакування речей у клубі  –  четвер", style="monika_credits_text", size=70)

image day8:
    ypos 380
    Text("День 8: Іспити та свобода  –  п’ятниця", style="monika_credits_text", size=70)

image day9:
    ypos 380
    Text("День 9: Початок спеки  -  субота", style="monika_credits_text", size=70)

image day10:
    ypos 380
    Text("День 10: Забіг по торговому центру  –  неділя", style="monika_credits_text", size=70)

image day11:
    ypos 380
    Text("День 11: Купання в коханні  -  понеділок", style="monika_credits_text", size=70)

image day12:
    ypos 380
    Text("День 12: Гра, яка руйнує дружбу  -  вівторок", style="monika_credits_text", size=70)

#------------------------------------------------From hereon, the girl's bodies are defined along with their heads.
#-----------------------------------------here's reference for the left half------the right half--------the head

# Sayori
image sayori 1 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 1c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 1d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 1e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 1f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 1g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 1h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 1i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 1j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 1k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 1l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 1m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 1n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 1o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 1p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 1q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 1r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 1s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 1t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 1u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 1v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 1w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 1x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 1y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 2c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 2d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 2e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 2f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 2g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 2h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 2i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 2j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 2k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 2l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 2m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 2n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 2o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 2p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 2q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 2r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 2s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 2t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 2u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 2v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 2w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 2x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 2y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 3 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 3c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 3d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 3e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 3f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 3g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 3h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 3i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 3j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 3k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 3l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 3m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 3n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 3o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 3p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 3q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 3r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 3s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 3t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 3u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 3v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 3w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 3x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 3y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 4 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 4c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 4d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 4e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 4f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 4g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 4h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 4i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 4j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 4k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 4l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 4m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 4n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 4o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 4p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 4q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 4r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 4s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 4t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 4u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 4v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 4w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 4x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 4y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 5 = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5a = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5b = im.Composite((960, 960), (0, 0), "sayori/3b.png")
image sayori 5c = im.Composite((960, 960), (0, 0), "sayori/3c.png")
image sayori 5d = im.Composite((960, 960), (0, 0), "sayori/3d.png")

image sayori 1ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 1bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 1bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 1bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 1be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 1bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 1bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 1bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 1bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 1bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 1bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 1bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 1bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 1bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 1bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 1bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 1bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 1br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 1bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 1bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 1bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 1bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 1bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 1bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 1by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 2ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 2bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 2bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 2bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 2be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 2bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 2bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 2bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 2bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 2bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 2bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 2bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 2bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 2bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 2bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 2bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 2bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 2br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 2bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 2bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 2bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 2bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 2bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 2bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 2by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori 3ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 3bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 3bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 3bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 3be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 3bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 3bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 3bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 3bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 3bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 3bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 3bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 3bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 3bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 3bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 3bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 3bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 3br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 3bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 3bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 3bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 3bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 3bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 3bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 3by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 4ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 4bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 4bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 4bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 4be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 4bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 4bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 4bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 4bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 4bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 4bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 4bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 4bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 4bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 4bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 4bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 4bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 4br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 4bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 4bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 4bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 4bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 4bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 4bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 4by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

#bikini sayori

image sayori 1ca = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/ca.png")
image sayori 1cb = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cb.png")
image sayori 1cc = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cc.png")
image sayori 1cd = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cd.png")
image sayori 1ce = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/ce.png")
image sayori 1cf = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cf.png")
image sayori 1cg = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cg.png")
image sayori 1ch = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/ch.png")
image sayori 1ci = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/ci.png")
image sayori 1cj = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cj.png")
image sayori 1ck = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/ck.png")
image sayori 1cl = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cl.png")
image sayori 1cm = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cm.png")
image sayori 1cn = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cn.png")
image sayori 1co = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/co.png")
image sayori 1cp = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cp.png")
image sayori 1cq = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cq.png")
image sayori 1cr = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cr.png")
image sayori 1cs = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cs.png")
image sayori 1ct = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/ct.png")
image sayori 1cu = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cu.png")
image sayori 1cv = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cv.png")
image sayori 1cw = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cw.png")
image sayori 1cx = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cx.png")
image sayori 1cy = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cy.png")
image sayori 1cz = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cz.png")

image sayori 2ca = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/ca.png")
image sayori 2cb = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cb.png")
image sayori 2cc = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cc.png")
image sayori 2cd = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cd.png")
image sayori 2ce = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/ce.png")
image sayori 2cf = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cf.png")
image sayori 2cg = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cg.png")
image sayori 2ch = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/ch.png")
image sayori 2ci = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/ci.png")
image sayori 2cj = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cj.png")
image sayori 2ck = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/ck.png")
image sayori 2cl = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cl.png")
image sayori 2cm = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cm.png")
image sayori 2cn = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cn.png")
image sayori 2co = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/co.png")
image sayori 2cp = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cp.png")
image sayori 2cq = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cq.png")
image sayori 2cr = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cr.png")
image sayori 2cs = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cs.png")
image sayori 2ct = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/ct.png")
image sayori 2cu = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cu.png")
image sayori 2cv = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cv.png")
image sayori 2cw = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cw.png")
image sayori 2cx = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cx.png")
image sayori 2cy = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c1l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cy.png")

image sayori 3ca = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/ca.png")
image sayori 3cb = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cb.png")
image sayori 3cc = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cc.png")
image sayori 3cd = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cd.png")
image sayori 3ce = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/ce.png")
image sayori 3cf = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cf.png")
image sayori 3cg = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cg.png")
image sayori 3ch = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/ch.png")
image sayori 3ci = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/ci.png")
image sayori 3cj = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cj.png")
image sayori 3ck = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/ck.png")
image sayori 3cl = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cl.png")
image sayori 3cm = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cm.png")
image sayori 3cn = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cn.png")
image sayori 3co = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/co.png")
image sayori 3cp = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cp.png")
image sayori 3cq = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cq.png")
image sayori 3cr = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cr.png")
image sayori 3cs = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cs.png")
image sayori 3ct = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/ct.png")
image sayori 3cu = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cu.png")
image sayori 3cv = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cv.png")
image sayori 3cw = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cw.png")
image sayori 3cx = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cx.png")
image sayori 3cy = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c1r.png", (0, 0), "mod_assets/sayori/cy.png")

image sayori 4ca = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/ca.png")
image sayori 4cb = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cb.png")
image sayori 4cc = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cc.png")
image sayori 4cd = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cd.png")
image sayori 4ce = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/ce.png")
image sayori 4cf = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cf.png")
image sayori 4cg = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cg.png")
image sayori 4ch = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/ch.png")
image sayori 4ci = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/ci.png")
image sayori 4cj = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cj.png")
image sayori 4ck = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/ck2.png")
image sayori 4cl = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cl.png")
image sayori 4cm = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cm.png")
image sayori 4cn = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cn.png")
image sayori 4co = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/co.png")
image sayori 4cp = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cp.png")
image sayori 4cq = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cq.png")
image sayori 4cr = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cr.png")
image sayori 4cs = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cs.png")
image sayori 4ct = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/ct.png")
image sayori 4cu = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cu.png")
image sayori 4cv = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cv.png")
image sayori 4cw = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cw.png")
image sayori 4cx = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cx.png")
image sayori 4cy = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c2l.png", (0, 0), "mod_assets/sayori/c2r.png", (0, 0), "mod_assets/sayori/cy.png")

image sayori 5ca = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c3.png", (0, 0), "mod_assets/sayori/c3a.png")
image sayori 5cb = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c3.png", (0, 0), "mod_assets/sayori/c3a.png", (0, 0), "mod_assets/sayori/3a.png")
image sayori 5cc = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c3.png", (0, 0), "mod_assets/sayori/c3a.png", (0, 0), "mod_assets/sayori/3b.png")
image sayori 5cd = im.Composite((960, 960), (0, 0), "mod_assets/sayori/c3.png", (0, 0), "mod_assets/sayori/c3a.png", (0, 0), "mod_assets/sayori/3d.png")

image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat

# Natsuki
image natsuki 11 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 1a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 1b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 1c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 1d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 1e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 1f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 1g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 1h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 1i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 1j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 1k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 1l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 1m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 1n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 1o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 1p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 1q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 1r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 1s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 1t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 1u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 1v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 1w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 1x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 1y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 1z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 21 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 2a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 2b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 2c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 2d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 2e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 2f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 2g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 2h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 2i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 2j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 2k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 2l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 2m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 2n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 2o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 2p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 2q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 2r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 2s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 2t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 2u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 2v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 2w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 2x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 2y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 2z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 31 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 3a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 3b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 3c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 3d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 3e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 3f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 3g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 3h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 3i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 3j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 3k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 3l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 3m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 3n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 3o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 3p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 3q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 3r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 3s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 3t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 3u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 3v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 3w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 3x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 3y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 3z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 41 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 4a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 4b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 4c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 4d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 4e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 4f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 4g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 4h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 4i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 4j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 4k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 4l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 4m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 4n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 4o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 4p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 4q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 4r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 4s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 4t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 4u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 4v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 4w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 4x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 4y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 4z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 12 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2t.png")
image natsuki 12a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ta.png")
image natsuki 12b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tb.png")
image natsuki 12c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tc.png")
image natsuki 12d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2td.png")
image natsuki 12e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2te.png")
image natsuki 12f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tf.png")
image natsuki 12g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tg.png")
image natsuki 12h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2th.png")
image natsuki 12i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ti.png")

image natsuki 42 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2t.png")
image natsuki 42a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ta.png")
image natsuki 42b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tb.png")
image natsuki 42c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tc.png")
image natsuki 42d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2td.png")
image natsuki 42e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2te.png")
image natsuki 42f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tf.png")
image natsuki 42g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tg.png")
image natsuki 42h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2th.png")
image natsuki 42i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ti.png")

image natsuki 51 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")
image natsuki 5a = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3.png")
image natsuki 5b = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3.png")
image natsuki 5c = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3.png")
image natsuki 5d = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3.png")
image natsuki 5e = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3.png")
image natsuki 5f = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3.png")
image natsuki 5g = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3.png")
image natsuki 5h = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3.png")
image natsuki 5i = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3.png")
image natsuki 5j = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3.png")
image natsuki 5k = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3.png")
image natsuki 5l = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3.png")
image natsuki 5m = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3.png")
image natsuki 5n = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3.png")
image natsuki 5o = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3.png")
image natsuki 5p = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3.png")
image natsuki 5q = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3.png")
image natsuki 5r = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3.png")
image natsuki 5s = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3.png")
image natsuki 5t = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3.png")
image natsuki 5u = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3.png")
image natsuki 5v = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3.png")
image natsuki 5w = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3.png")
image natsuki 5x = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3.png")
image natsuki 5y = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3.png")
image natsuki 5z = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3.png")
#image natsuki 52 = im.Composite((960, 960), (0, 0), "natsuki/3.png", (0, 0), "natsuki/4t.png")


image natsuki 1ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 1bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 1bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 1bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 1be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 1bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 1bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 1bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 1bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 1bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 1bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 1bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 1bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 1bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 1bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 1bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 1bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 1br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 1bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 1bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 1bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 1bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 1bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 1bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 1by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 1bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 2ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 2bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 2bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 2bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 2be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 2bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 2bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 2bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 2bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 2bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 2bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 2bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 2bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 2bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 2bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 2bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 2bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 2br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 2bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 2bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 2bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 2bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 2bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 2bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 2by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 2bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 3ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 3bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 3bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 3bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 3be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 3bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 3bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 3bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 3bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 3bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 3bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 3bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 3bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 3bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 3bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 3bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 3bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 3br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 3bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 3bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 3bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 3bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 3bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 3bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 3by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 3bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 4ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 4bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 4bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 4bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 4be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 4bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 4bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 4bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 4bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 4bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 4bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 4bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 4bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 4bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 4bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 4bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 4bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 4br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 4bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 4bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 4bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 4bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 4bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 4bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 4by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 4bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 12ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bta.png")
image natsuki 12bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btb.png")
image natsuki 12bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btc.png")
image natsuki 12bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btd.png")
image natsuki 12be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bte.png")
image natsuki 12bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btf.png")
image natsuki 12bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btg.png")
image natsuki 12bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bth.png")
image natsuki 12bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bti.png")

image natsuki 42ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bta.png")
image natsuki 42bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btb.png")
image natsuki 42bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btc.png")
image natsuki 42bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btd.png")
image natsuki 42be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bte.png")
image natsuki 42bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btf.png")
image natsuki 42bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btg.png")
image natsuki 42bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bth.png")
image natsuki 42bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bti.png")

image natsuki 5ba = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3b.png")
image natsuki 5bb = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3b.png")
image natsuki 5bc = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3b.png")
image natsuki 5bd = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3b.png")
image natsuki 5be = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3b.png")
image natsuki 5bf = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3b.png")
image natsuki 5bg = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3b.png")
image natsuki 5bh = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3b.png")
image natsuki 5bi = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3b.png")
image natsuki 5bj = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3b.png")
image natsuki 5bk = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3b.png")
image natsuki 5bl = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3b.png")
image natsuki 5bm = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3b.png")
image natsuki 5bn = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3b.png")
image natsuki 5bo = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3b.png")
image natsuki 5bp = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3b.png")
image natsuki 5bq = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3b.png")
image natsuki 5br = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3b.png")
image natsuki 5bs = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3b.png")
image natsuki 5bt = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3b.png")
image natsuki 5bu = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3b.png")
image natsuki 5bv = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3b.png")
image natsuki 5bw = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3b.png")
image natsuki 5bx = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3b.png")
image natsuki 5by = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3b.png")
image natsuki 5bz = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3b.png")

#bikini natsuki

image natsuki 1ca = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/a.png")
image natsuki 1cb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/b.png")
image natsuki 1cc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/c.png")
image natsuki 1cd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/d.png")
image natsuki 1ce = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/e.png")
image natsuki 1cf = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/f.png")
image natsuki 1cg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/g.png")
image natsuki 1ch = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/h.png")
image natsuki 1ci = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/i.png")
image natsuki 1cj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/j.png")
image natsuki 1ck = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/k.png")
image natsuki 1cl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/l.png")
image natsuki 1cm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/m.png")
image natsuki 1cn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/n.png")
image natsuki 1co = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/o.png")
image natsuki 1cp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/p.png")
image natsuki 1cq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/q.png")
image natsuki 1cr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/r.png")
image natsuki 1cs = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/s.png")
image natsuki 1ct = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/t.png")
image natsuki 1cu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/u.png")
image natsuki 1cv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/v.png")
image natsuki 1cw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/w.png")
image natsuki 1cx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/x.png")
image natsuki 1cy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/y.png")
image natsuki 1cz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/z.png")
image natsuki 1ch2 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/hungry.png")
image natsuki 1ch3 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/hungry2.png")
image natsuki 1ch4 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/hungry3.png")
image natsuki 1clol = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/lol.png")
image natsuki 1cp2 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/scared.png")
image natsuki 1cm2 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/m2.png")
image natsuki 1cg2 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/g2.png")

image natsuki 21 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 2ca = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/a.png")
image natsuki 2cb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/b.png")
image natsuki 2cc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/c.png")
image natsuki 2cd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/d.png")
image natsuki 2ce = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/e.png")
image natsuki 2cf = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/f.png")
image natsuki 2cg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/g.png")
image natsuki 2ch = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/h.png")
image natsuki 2ci = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/i.png")
image natsuki 2cj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/j.png")
image natsuki 2ck = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/k.png")
image natsuki 2cl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/l.png")
image natsuki 2cm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/m.png")
image natsuki 2cn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/n.png")
image natsuki 2co = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/o.png")
image natsuki 2cp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/p.png")
image natsuki 2cq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/q.png")
image natsuki 2cr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/r.png")
image natsuki 2cs = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/s.png")
image natsuki 2ct = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/t.png")
image natsuki 2cu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/u.png")
image natsuki 2cv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/v.png")
image natsuki 2cw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/w.png")
image natsuki 2cx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/x.png")
image natsuki 2cy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/y.png")
image natsuki 2cz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/z.png")
image natsuki 2ch2 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/hungry.png")
image natsuki 2ch3 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/hungry2.png")
image natsuki 2ch4 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/hungry3.png")
image natsuki 2cm2 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/m2.png")

image natsuki 31 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 3ca = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/a.png")
image natsuki 3cb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/b.png")
image natsuki 3cc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/c.png")
image natsuki 3cd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/d.png")
image natsuki 3ce = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/e.png")
image natsuki 3cf = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/f.png")
image natsuki 3cg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/g.png")
image natsuki 3ch = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/h.png")
image natsuki 3ci = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/i.png")
image natsuki 3cj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/j.png")
image natsuki 3ck = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/k.png")
image natsuki 3cl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/l.png")
image natsuki 3cm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/m.png")
image natsuki 3cn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/n.png")
image natsuki 3co = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/o.png")
image natsuki 3cp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/p.png")
image natsuki 3cq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/q.png")
image natsuki 3cr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/r.png")
image natsuki 3cs = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/s.png")
image natsuki 3ct = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/t.png")
image natsuki 3cu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/u.png")
image natsuki 3cv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/v.png")
image natsuki 3cw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/w.png")
image natsuki 3cx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/x.png")
image natsuki 3cy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/y.png")
image natsuki 3cz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/z.png")
image natsuki 3ch2 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/hungry.png")
image natsuki 3ch3 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/hungry2.png")
image natsuki 3ch4 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/hungry3.png")
image natsuki 3cm2 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/1r.png", (0, 0), "mod_assets/natsuki/m2.png")

image natsuki 4c1 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 4ca = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/a.png")
image natsuki 4cb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/b.png")
image natsuki 4cc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/c.png")
image natsuki 4cd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/d.png")
image natsuki 4ce = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/e.png")
image natsuki 4cf = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/f.png")
image natsuki 4cg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/g.png")
image natsuki 4ch = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/h.png")
image natsuki 4ci = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/i.png")
image natsuki 4cj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/j.png")
image natsuki 4ck = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/k.png")
image natsuki 4cl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/l.png")
image natsuki 4cm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/m.png")
image natsuki 4cn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/n.png")
image natsuki 4co = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/o.png")
image natsuki 4cp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/p.png")
image natsuki 4cq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/q.png")
image natsuki 4cr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/r.png")
image natsuki 4cs = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/s.png")
image natsuki 4ct = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/t.png")
image natsuki 4cu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/u.png")
image natsuki 4cv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/v.png")
image natsuki 4cw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/w.png")
image natsuki 4cx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/x.png")
image natsuki 4cy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/y.png")
image natsuki 4cz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/z.png")
image natsuki 4ch2 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/hungry.png")
image natsuki 4ch3 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/hungry2.png")
image natsuki 4ch4 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/hungry3.png")
image natsuki 4cm2 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2l.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/m2.png")

image natsuki 4cdpointy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2p.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/d.png")
image natsuki 4czpointy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2p.png", (0, 0), "mod_assets/natsuki/2r.png", (0, 0), "mod_assets/natsuki/z.png")


# Natsuki legacy
image natsuki 1 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 3 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 4 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 5 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")

image natsuki mouth = LiveComposite((960, 960), (0, 0), "natsuki/0.png", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

image n_moving_mouth:
    "images/natsuki/mouth.png"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

image natsuki_ghost_blood:
    "#00000000"
    "natsuki/ghost_blood.png" with ImageDissolve("images/menu/wipedown.png", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    "natsuki/ghost1.png"
image natsuki ghost1:
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Image("natsuki/ghost2.png")
image natsuki ghost3 = Image("natsuki/ghost3.png")
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"
image natsuki glitch1:
    "natsuki/glitch1.png"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/scream.png")
image natsuki vomit = "natsuki/vomit.png"

image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"

# Yuri
image yuri 1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 4 = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")

image yuri 1a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 1b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/b.png")
image yuri 1c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/c.png")
image yuri 1d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/d.png")
image yuri 1e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/e.png")
image yuri 1f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/f.png")
image yuri 1g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/g.png")
image yuri 1h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/h.png")
image yuri 1i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/i.png")
image yuri 1j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/j.png")
image yuri 1k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/k.png")
image yuri 1l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/l.png")
image yuri 1m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/m.png")
image yuri 1n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/n.png")
image yuri 1o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/o.png")
image yuri 1p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/p.png")
image yuri 1q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/q.png")
image yuri 1r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/r.png")
image yuri 1s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/s.png")
image yuri 1t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/t.png")
image yuri 1u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/u.png")
image yuri 1v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/v.png")
image yuri 1w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/w.png")

image yuri 1y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y1.png")
image yuri 1y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y2.png")
image yuri 1y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y3.png")
image yuri 1y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y4.png")
image yuri 1y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y5.png")
image yuri 1y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y6.png")
image yuri 1y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y7.png")

image yuri 2a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 2b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 2c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 2d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 2e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 2f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 2g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 2h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 2i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 2j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 2k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 2l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 2m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 2n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 2o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 2p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 2q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 2r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 2s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 2t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 2u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 2v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 2w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 2y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 2y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 2y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 2y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 2y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 2y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 2y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 3a = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3b = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 3c = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 3d = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 3e = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 3f = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 3g = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 3h = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 3i = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 3j = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 3k = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 3l = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 3m = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 3n = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 3o = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 3p = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 3q = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 3r = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 3s = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 3t = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 3u = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 3v = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 3w = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 3y1 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 3y2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 3y3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 3y4 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 3y5 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 3y6 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 3y7 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 4a = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")
image yuri 4b = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/b2.png")
image yuri 4c = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/c2.png")
image yuri 4d = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/d2.png")
image yuri 4e = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/e2.png")

image yuri 1ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")

image yuri 2ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")

image yuri 3ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")

image yuri 4ba = im.Composite((960, 960), (0, 0), "yuri/a2.png", (0, 0), "yuri/3b.png")
image yuri 4bb = im.Composite((960, 960), (0, 0), "yuri/b2.png", (0, 0), "yuri/3b.png")
image yuri 4bc = im.Composite((960, 960), (0, 0), "yuri/c2.png", (0, 0), "yuri/3b.png")
image yuri 4bd = im.Composite((960, 960), (0, 0), "yuri/d2.png", (0, 0), "yuri/3b.png")
image yuri 4be = im.Composite((960, 960), (0, 0), "yuri/e2.png", (0, 0), "yuri/3b.png")

#summer yuri

image yuri 1sa = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/1sr.png")
image yuri 1sb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/1sr.png")
image yuri 1sc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/1sr.png")
image yuri 1sd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/1sr.png")
image yuri 1se = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/1sr.png")
image yuri 1sf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/1sr.png")
image yuri 1sg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/1sr.png")
image yuri 1sh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/1sr.png")
image yuri 1si = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/1sr.png")
image yuri 1sj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/1sr.png")
image yuri 1sk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/1sr.png")
image yuri 1sl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/1sr.png")
image yuri 1sm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/1sr.png")
image yuri 1sn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/1sr.png")
image yuri 1so = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/1sr.png")
image yuri 1sp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/1sr.png")
image yuri 1sq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/1sr.png")
image yuri 1sr = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/1sr.png")
image yuri 1ss = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/1sr.png")
image yuri 1st = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/1sr.png")
image yuri 1su = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/1sr.png")
image yuri 1sv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/1sr.png")
image yuri 1sw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/1sr.png")

image yuri 2sa = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 2sb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 2sc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 2sd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 2se = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 2sf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 2sg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 2sh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 2si = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 2sj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 2sk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 2sl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 2sm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 2sn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 2so = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 2sp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 2sq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 2sr = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 2ss = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 2st = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 2su = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 2sv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 2sw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "mod_assets/yuri/1sl.png", (0, 0), "mod_assets/yuri/2sr.png")

image yuri 3sa = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "mod_assets/yuri/2sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 3sb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "mod_assets/yuri/2sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 3sc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "mod_assets/yuri/2sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 3sd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "mod_assets/yuri/2sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 3se = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "mod_assets/yuri/2sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 3sf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "mod_assets/yuri/2sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 3sg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "mod_assets/yuri/2sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 3sh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "mod_assets/yuri/2sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 3si = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "mod_assets/yuri/2sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 3sj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "mod_assets/yuri/2sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 3sk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "mod_assets/yuri/2sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 3sl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "mod_assets/yuri/2sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 3sm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "mod_assets/yuri/2sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 3sn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "mod_assets/yuri/2sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 3so = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "mod_assets/yuri/2sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 3sp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "mod_assets/yuri/2sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 3sq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "mod_assets/yuri/2sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 3sr = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "mod_assets/yuri/2sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 3ss = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "mod_assets/yuri/2sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 3st = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "mod_assets/yuri/2sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 3su = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "mod_assets/yuri/2sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 3sv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "mod_assets/yuri/2sl.png", (0, 0), "mod_assets/yuri/2sr.png")
image yuri 3sw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "mod_assets/yuri/2sl.png", (0, 0), "mod_assets/yuri/2sr.png")

image yuri 4sa = im.Composite((960, 960), (0, 0), "yuri/a2.png", (0, 0), "mod_assets/yuri/3s.png")
image yuri 4sb = im.Composite((960, 960), (0, 0), "yuri/b2.png", (0, 0), "mod_assets/yuri/3s.png")
image yuri 4sc = im.Composite((960, 960), (0, 0), "yuri/c2.png", (0, 0), "mod_assets/yuri/3s.png")
image yuri 4sd = im.Composite((960, 960), (0, 0), "yuri/d2.png", (0, 0), "mod_assets/yuri/3s.png")
image yuri 4se = im.Composite((960, 960), (0, 0), "yuri/e2.png", (0, 0), "mod_assets/yuri/3s.png")

#bikini yuri

image yuri 1fa = im.Composite((960, 960), (0, 0), "mod_assets/yuri/fa.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1fb = im.Composite((960, 960), (0, 0), "mod_assets/yuri/fb.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1fc = im.Composite((960, 960), (0, 0), "mod_assets/yuri/fc.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1fd = im.Composite((960, 960), (0, 0), "mod_assets/yuri/fd.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1fe = im.Composite((960, 960), (0, 0), "mod_assets/yuri/fe.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1ff = im.Composite((960, 960), (0, 0), "mod_assets/yuri/ff.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1fg = im.Composite((960, 960), (0, 0), "mod_assets/yuri/fg.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1fh = im.Composite((960, 960), (0, 0), "mod_assets/yuri/fh.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1fi = im.Composite((960, 960), (0, 0), "mod_assets/yuri/fi.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1fj = im.Composite((960, 960), (0, 0), "mod_assets/yuri/fj.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1fk = im.Composite((960, 960), (0, 0), "mod_assets/yuri/fk.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1fl = im.Composite((960, 960), (0, 0), "mod_assets/yuri/fl.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1fm = im.Composite((960, 960), (0, 0), "mod_assets/yuri/fm.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1fn = im.Composite((960, 960), (0, 0), "mod_assets/yuri/fn.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1fo = im.Composite((960, 960), (0, 0), "mod_assets/yuri/fo.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1fp = im.Composite((960, 960), (0, 0), "mod_assets/yuri/fp.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1fq = im.Composite((960, 960), (0, 0), "mod_assets/yuri/fq.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1fr = im.Composite((960, 960), (0, 0), "mod_assets/yuri/fr.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1fs = im.Composite((960, 960), (0, 0), "mod_assets/yuri/fs.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1ft = im.Composite((960, 960), (0, 0), "mod_assets/yuri/ft.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1fu = im.Composite((960, 960), (0, 0), "mod_assets/yuri/fu.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1fv = im.Composite((960, 960), (0, 0), "mod_assets/yuri/fv.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1fw = im.Composite((960, 960), (0, 0), "mod_assets/yuri/fw.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1fx = im.Composite((960, 960), (0, 0), "mod_assets/yuri/fx.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1fy = im.Composite((960, 960), (0, 0), "mod_assets/yuri/fy.png", (0, 0), "mod_assets/yuri/1f.png")
image yuri 1fz = im.Composite((960, 960), (0, 0), "mod_assets/yuri/fz.png", (0, 0), "mod_assets/yuri/1f.png")

image yuri 2fa = im.Composite((960, 960), (0, 0), "mod_assets/yuri/f2a.png", (0, 0), "mod_assets/yuri/2f.png")
image yuri 2fb = im.Composite((960, 960), (0, 0), "mod_assets/yuri/f2b.png", (0, 0), "mod_assets/yuri/2f.png")
image yuri 2fc = im.Composite((960, 960), (0, 0), "mod_assets/yuri/f2c.png", (0, 0), "mod_assets/yuri/2f.png")
image yuri 2fd = im.Composite((960, 960), (0, 0), "mod_assets/yuri/f2d.png", (0, 0), "mod_assets/yuri/2f.png")
image yuri 2fe = im.Composite((960, 960), (0, 0), "mod_assets/yuri/f2e.png", (0, 0), "mod_assets/yuri/2f.png")

image y_glitch_head:
    "images/yuri/za.png"
    0.15
    "images/yuri/zb.png"
    0.15
    "images/yuri/zc.png"
    0.15
    "images/yuri/zd.png"
    0.15
    repeat

image yuri stab_1 = "yuri/stab/1.png"
image yuri stab_2 = "yuri/stab/2.png"
image yuri stab_3 = "yuri/stab/3.png"
image yuri stab_4 = "yuri/stab/4.png"
image yuri stab_5 = "yuri/stab/5.png"
image yuri stab_6 = LiveComposite((960,960), (0, 0), "yuri/stab/6-mask.png", (0, 0), "yuri stab_6_eyes", (0, 0), "yuri/stab/6.png")

image yuri stab_6_eyes:
    "yuri/stab/6-eyes.png"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.2
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.2
        repeat
    parallel:
        2.05
        easeout 1.0 yoffset -15
        linear 10 yoffset -15


image yuri oneeye = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/oneeye.png", (0, 0), "yuri oneeye2")
image yuri oneeye2:
    "yuri/oneeye2.png"
    subpixel True
    pause 5.0
    linear 60 xoffset -50 yoffset 20

image yuri glitch:
    "yuri/glitch1.png"
    pause 0.1
    "yuri/glitch2.png"
    pause 0.1
    "yuri/glitch3.png"
    pause 0.1
    "yuri/glitch4.png"
    pause 0.1
    "yuri/glitch5.png"
    pause 0.1
    repeat
image yuri glitch2:
    "yuri/0a.png"
    pause 0.1
    "yuri/0b.png"
    pause 0.5
    "yuri/0a.png"
    pause 0.3
    "yuri/0b.png"
    pause 0.3
    "yuri 1"

image yuri eyes = LiveComposite((1280, 720), (0, 0), "yuri/eyes1.png", (0, 0), "yuripupils")

image yuri eyes_base = "yuri/eyes1.png"

image yuripupils:
    "yuri/eyes2.png"
    yuripupils_move

image yuri cuts = "yuri/cuts.png"

image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"

#------------------------------------------------Our beloved Monika only has her school uniform here, but that can change!
#dev note: mission accomplished

# Just Monika
image monika 1 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 3 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 4 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 5 = im.Composite((960, 960), (0, 0), "monika/3a.png")

image monika 1a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 1b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 1c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 1d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 1e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 1f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 1g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 1h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 1i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 1j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 1k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 1l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 1m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 1n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 1o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 1p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 1q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 1r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 2a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 2b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 2c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 2d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 2e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 2f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 2g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 2h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 2i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 2j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 2k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 2l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 2m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 2n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 2o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 2p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 2q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 2r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 3a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 3b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 3c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 3d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 3e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 3f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 3g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 3h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 3i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 3j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 3k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 3l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 3m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 3n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 3o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 3p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 3q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 3r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 4a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 4b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 4c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 4d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 4e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 4f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 4g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 4h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 4i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 4j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 4k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 4l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 4m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 4n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 4o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 4p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 4q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 4r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 5a = im.Composite((960, 960), (0, 0), "monika/3a.png")
image monika 5b = im.Composite((960, 960), (0, 0), "monika/3b.png")

#casual monika

image monika 1ba = im.Composite((960, 960), (0, 0), "mod_assets/monika/1l.png", (0, 0), "monika/a.png")
image monika 1bb = im.Composite((960, 960), (0, 0), "mod_assets/monika/1l.png", (0, 0), "monika/b.png")
image monika 1bc = im.Composite((960, 960), (0, 0), "mod_assets/monika/1l.png", (0, 0), "monika/c.png")
image monika 1bd = im.Composite((960, 960), (0, 0), "mod_assets/monika/1l.png", (0, 0), "monika/d.png")
image monika 1be = im.Composite((960, 960), (0, 0), "mod_assets/monika/1l.png", (0, 0), "monika/e.png")
image monika 1bf = im.Composite((960, 960), (0, 0), "mod_assets/monika/1l.png", (0, 0), "monika/f.png")
image monika 1bg = im.Composite((960, 960), (0, 0), "mod_assets/monika/1l.png", (0, 0), "monika/g.png")
image monika 1bh = im.Composite((960, 960), (0, 0), "mod_assets/monika/1l.png", (0, 0), "monika/h.png")
image monika 1bi = im.Composite((960, 960), (0, 0), "mod_assets/monika/1l.png", (0, 0), "monika/i.png")
image monika 1bj = im.Composite((960, 960), (0, 0), "mod_assets/monika/1l.png", (0, 0), "monika/j.png")
image monika 1bk = im.Composite((960, 960), (0, 0), "mod_assets/monika/1l.png", (0, 0), "monika/k.png")
image monika 1bl = im.Composite((960, 960), (0, 0), "mod_assets/monika/1l.png", (0, 0), "monika/l.png")
image monika 1bm = im.Composite((960, 960), (0, 0), "mod_assets/monika/1l.png", (0, 0), "monika/m.png")
image monika 1bn = im.Composite((960, 960), (0, 0), "mod_assets/monika/1l.png", (0, 0), "monika/n.png")
image monika 1bo = im.Composite((960, 960), (0, 0), "mod_assets/monika/1l.png", (0, 0), "monika/o.png")
image monika 1bp = im.Composite((960, 960), (0, 0), "mod_assets/monika/1l.png", (0, 0), "monika/p.png")
image monika 1bq = im.Composite((960, 960), (0, 0), "mod_assets/monika/1l.png", (0, 0), "monika/q.png")
image monika 1br = im.Composite((960, 960), (0, 0), "mod_assets/monika/1l.png", (0, 0), "monika/r.png")

image monika 2ba = im.Composite((960, 960), (0, 0), "mod_assets/monika/2l.png", (0, 0), "monika/a.png")
image monika 2bb = im.Composite((960, 960), (0, 0), "mod_assets/monika/2l.png", (0, 0), "monika/b.png")
image monika 2bc = im.Composite((960, 960), (0, 0), "mod_assets/monika/2l.png", (0, 0), "monika/c.png")
image monika 2bd = im.Composite((960, 960), (0, 0), "mod_assets/monika/2l.png", (0, 0), "monika/d.png")
image monika 2be = im.Composite((960, 960), (0, 0), "mod_assets/monika/2l.png", (0, 0), "monika/e.png")
image monika 2bf = im.Composite((960, 960), (0, 0), "mod_assets/monika/2l.png", (0, 0), "monika/f.png")
image monika 2bg = im.Composite((960, 960), (0, 0), "mod_assets/monika/2l.png", (0, 0), "monika/g.png")
image monika 2bh = im.Composite((960, 960), (0, 0), "mod_assets/monika/2l.png", (0, 0), "monika/h.png")
image monika 2bi = im.Composite((960, 960), (0, 0), "mod_assets/monika/2l.png", (0, 0), "monika/i.png")
image monika 2bj = im.Composite((960, 960), (0, 0), "mod_assets/monika/2l.png", (0, 0), "monika/j.png")
image monika 2bk = im.Composite((960, 960), (0, 0), "mod_assets/monika/2l.png", (0, 0), "monika/k.png")
image monika 2bl = im.Composite((960, 960), (0, 0), "mod_assets/monika/2l.png", (0, 0), "monika/l.png")
image monika 2bm = im.Composite((960, 960), (0, 0), "mod_assets/monika/2l.png", (0, 0), "monika/m.png")
image monika 2bn = im.Composite((960, 960), (0, 0), "mod_assets/monika/2l.png", (0, 0), "monika/n.png")
image monika 2bo = im.Composite((960, 960), (0, 0), "mod_assets/monika/2l.png", (0, 0), "monika/o.png")
image monika 2bp = im.Composite((960, 960), (0, 0), "mod_assets/monika/2l.png", (0, 0), "monika/p.png")
image monika 2bq = im.Composite((960, 960), (0, 0), "mod_assets/monika/2l.png", (0, 0), "monika/q.png")
image monika 2br = im.Composite((960, 960), (0, 0), "mod_assets/monika/2l.png", (0, 0), "monika/r.png")

image monika 3ba = im.Composite((960, 960), (0, 0), "mod_assets/monika/3l.png", (0, 0), "monika/a.png")
image monika 3bb = im.Composite((960, 960), (0, 0), "mod_assets/monika/3l.png", (0, 0), "monika/b.png")
image monika 3bc = im.Composite((960, 960), (0, 0), "mod_assets/monika/3l.png", (0, 0), "monika/c.png")
image monika 3bd = im.Composite((960, 960), (0, 0), "mod_assets/monika/3l.png", (0, 0), "monika/d.png")
image monika 3be = im.Composite((960, 960), (0, 0), "mod_assets/monika/3l.png", (0, 0), "monika/e.png")
image monika 3bf = im.Composite((960, 960), (0, 0), "mod_assets/monika/3l.png", (0, 0), "monika/f.png")
image monika 3bg = im.Composite((960, 960), (0, 0), "mod_assets/monika/3l.png", (0, 0), "monika/g.png")
image monika 3bh = im.Composite((960, 960), (0, 0), "mod_assets/monika/3l.png", (0, 0), "monika/h.png")
image monika 3bi = im.Composite((960, 960), (0, 0), "mod_assets/monika/3l.png", (0, 0), "monika/i.png")
image monika 3bj = im.Composite((960, 960), (0, 0), "mod_assets/monika/3l.png", (0, 0), "monika/j.png")
image monika 3bk = im.Composite((960, 960), (0, 0), "mod_assets/monika/3l.png", (0, 0), "monika/k.png")
image monika 3bl = im.Composite((960, 960), (0, 0), "mod_assets/monika/3l.png", (0, 0), "monika/l.png")
image monika 3bm = im.Composite((960, 960), (0, 0), "mod_assets/monika/3l.png", (0, 0), "monika/m.png")
image monika 3bn = im.Composite((960, 960), (0, 0), "mod_assets/monika/3l.png", (0, 0), "monika/n.png")
image monika 3bo = im.Composite((960, 960), (0, 0), "mod_assets/monika/3l.png", (0, 0), "monika/o.png")
image monika 3bp = im.Composite((960, 960), (0, 0), "mod_assets/monika/3l.png", (0, 0), "monika/p.png")
image monika 3bq = im.Composite((960, 960), (0, 0), "mod_assets/monika/3l.png", (0, 0), "monika/q.png")
image monika 3br = im.Composite((960, 960), (0, 0), "mod_assets/monika/3l.png", (0, 0), "monika/r.png")

image monika 4ba = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "monika/a.png")
image monika 4bb = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "monika/b.png")
image monika 4bc = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "monika/c.png")
image monika 4bd = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "monika/d.png")
image monika 4be = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "monika/e.png")
image monika 4bf = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "monika/f.png")
image monika 4bg = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "monika/g.png")
image monika 4bh = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "monika/h.png")
image monika 4bi = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "monika/i.png")
image monika 4bj = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "monika/j.png")
image monika 4bk = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "monika/k.png")
image monika 4bl = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "monika/l.png")
image monika 4mb = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "monika/m.png")
image monika 4bn = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "monika/n.png")
image monika 4bo = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "monika/o.png")
image monika 4bp = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "monika/p.png")
image monika 4bq = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "monika/q.png")
image monika 4br = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "monika/r.png")

image monika 5ba = im.Composite((960, 960), (0, 0), "mod_assets/monika/5l.png")
image monika 5bb = im.Composite((960, 960), (0, 0), "mod_assets/monika/6l.png")

#------------Our Time outfits

image monika o1_1a = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_1l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/a.png")
image monika o1_1b = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_1l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/b.png")
image monika o1_1c = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_1l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/c.png")
image monika o1_1d = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_1l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/d.png")
image monika o1_1e = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_1l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/e.png")
image monika o1_1f = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_1l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/f.png")
image monika o1_1g = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_1l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/g.png")
image monika o1_1h = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_1l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/h.png")
image monika o1_1i = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_1l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/i.png")
image monika o1_1j = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_1l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/j.png")
image monika o1_1k = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_1l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/k.png")
image monika o1_1l = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_1l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/l.png")
image monika o1_1m = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_1l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/m.png")
image monika o1_1n = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_1l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/n.png")
image monika o1_1o = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_1l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/o.png")
image monika o1_1p = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_1l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/p.png")
image monika o1_1q = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_1l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/q.png")
image monika o1_1r = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_1l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/r.png")



image monika o1_2a = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_2l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/a.png")
image monika o1_2b = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_2l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/b.png")
image monika o1_2c = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_2l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/c.png")
image monika o1_2d = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_2l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/d.png")
image monika o1_2e = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_2l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/e.png")
image monika o1_2f = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_2l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/f.png")
image monika o1_2g = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_2l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/g.png")
image monika o1_2h = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_2l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/h.png")
image monika o1_2i = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_2l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/i.png")
image monika o1_2j = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_2l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/j.png")
image monika o1_2k = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_2l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/k.png")
image monika o1_2l = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_2l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/l.png")
image monika o1_2m = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_2l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/m.png")
image monika o1_2n = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_2l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/n.png")
image monika o1_2o = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_2l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/o.png")
image monika o1_2p = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_2l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/p.png")
image monika o1_2q = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_2l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/q.png")
image monika o1_2r = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_2l.png", (0, 0), "ourtime_assets/monika/o1_1r.png", (0, 0), "ourtime_assets/monika/r.png")



image monika o1_5b = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_3b.png")
image monika o1_5a = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o1_3a.png")



image monika o2_1a = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/a.png")
image monika o2_1b = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/b.png")
image monika o2_1c = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/c.png")
image monika o2_1d = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/d.png")
image monika o2_1e = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/e.png")
image monika o2_1f = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/f.png")
image monika o2_1g = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/g.png")
image monika o2_1h = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/h.png")
image monika o2_1i = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/i.png")
image monika o2_1j = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/j.png")
image monika o2_1k = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/k.png")
image monika o2_1l = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/l.png")
image monika o2_1m = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/m.png")
image monika o2_1n = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/n.png")
image monika o2_1o = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/o.png")
image monika o2_1p = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/p.png")
image monika o2_1q = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/q.png")
image monika o2_1r = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/r.png")

image monika o2_2a = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/a.png")
image monika o2_2b = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/b.png")
image monika o2_2c = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/c.png")
image monika o2_2d = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/d.png")
image monika o2_2e = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/e.png")
image monika o2_2f = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/f.png")
image monika o2_2g = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/g.png")
image monika o2_2h = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/h.png")
image monika o2_2i = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/i.png")
image monika o2_2j = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/j.png")
image monika o2_2k = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/k.png")
image monika o2_2l = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/l.png")
image monika o2_2m = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/m.png")
image monika o2_2n = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/n.png")
image monika o2_2o = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/o.png")
image monika o2_2p = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/p.png")
image monika o2_2q = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/q.png")
image monika o2_2r = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_1r.png", (0, 0), "ourtime_assets/monika/r.png")

image monika o2_3a = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/a.png")
image monika o2_3b = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/b.png")
image monika o2_3c = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/c.png")
image monika o2_3d = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/d.png")
image monika o2_3e = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/e.png")
image monika o2_3f = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/f.png")
image monika o2_3g = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/g.png")
image monika o2_3h = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/h.png")
image monika o2_3i = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/i.png")
image monika o2_3j = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/j.png")
image monika o2_3k = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/k.png")
image monika o2_3l = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/l.png")
image monika o2_3m = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/m.png")
image monika o2_3n = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/n.png")
image monika o2_3o = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/o.png")
image monika o2_3p = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/p.png")
image monika o2_3q = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/q.png")
image monika o2_3r = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_1l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/r.png")

image monika o2_4a = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/a.png")
image monika o2_4b = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/b.png")
image monika o2_4c = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/c.png")
image monika o2_4d = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/d.png")
image monika o2_4e = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/e.png")
image monika o2_4f = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/f.png")
image monika o2_4g = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/g.png")
image monika o2_4h = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/h.png")
image monika o2_4i = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/i.png")
image monika o2_4j = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/j.png")
image monika o2_4k = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/k.png")
image monika o2_4l = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/l.png")
image monika o2_4m = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/m.png")
image monika o2_4n = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/n.png")
image monika o2_4o = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/o.png")
image monika o2_4p = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/p.png")
image monika o2_4q = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/q.png")
image monika o2_4r = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_2l.png", (0, 0), "ourtime_assets/monika/o2_2r.png", (0, 0), "ourtime_assets/monika/r.png")

image monika o2_5b = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_3b.png")
image monika o2_5a = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o2_3a.png")



image monika o3_1a = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/a.png")
image monika o3_1b = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/b.png")
image monika o3_1c = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/c.png")
image monika o3_1d = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/d.png")
image monika o3_1e = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/e.png")
image monika o3_1f = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/f.png")
image monika o3_1g = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/g.png")
image monika o3_1h = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/h.png")
image monika o3_1i = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/i.png")
image monika o3_1j = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/j.png")
image monika o3_1k = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/k.png")
image monika o3_1l = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/l.png")
image monika o3_1m = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/m.png")
image monika o3_1n = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/n.png")
image monika o3_1o = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/o.png")
image monika o3_1p = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/p.png")
image monika o3_1q = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/q.png")
image monika o3_1r = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/r.png")

image monika o3_2a = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/a.png")
image monika o3_2b = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/b.png")
image monika o3_2c = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/c.png")
image monika o3_2d = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/d.png")
image monika o3_2e = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/e.png")
image monika o3_2f = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/f.png")
image monika o3_2g = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/g.png")
image monika o3_2h = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/h.png")
image monika o3_2i = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/i.png")
image monika o3_2j = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/j.png")
image monika o3_2k = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/k.png")
image monika o3_2l = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/l.png")
image monika o3_2m = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/m.png")
image monika o3_2n = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/n.png")
image monika o3_2o = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/o.png")
image monika o3_2p = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/p.png")
image monika o3_2q = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/q.png")
image monika o3_2r = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_1r.png", (0, 0), "ourtime_assets/monika/r.png")

image monika o3_3a = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/a.png")
image monika o3_3b = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/b.png")
image monika o3_3c = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/c.png")
image monika o3_3d = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/d.png")
image monika o3_3e = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/e.png")
image monika o3_3f = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/f.png")
image monika o3_3g = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/g.png")
image monika o3_3h = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/h.png")
image monika o3_3i = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/i.png")
image monika o3_3j = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/j.png")
image monika o3_3k = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/k.png")
image monika o3_3l = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/l.png")
image monika o3_3m = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/m.png")
image monika o3_3n = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/n.png")
image monika o3_3o = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/o.png")
image monika o3_3p = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/p.png")
image monika o3_3q = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/q.png")
image monika o3_3r = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_1l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/r.png")

image monika o3_4a = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/a.png")
image monika o3_4b = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/b.png")
image monika o3_4c = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/c.png")
image monika o3_4d = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/d.png")
image monika o3_4e = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/e.png")
image monika o3_4f = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/f.png")
image monika o3_4g = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/g.png")
image monika o3_4h = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/h.png")
image monika o3_4i = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/i.png")
image monika o3_4j = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/j.png")
image monika o3_4k = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/k.png")
image monika o3_4l = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/l.png")
image monika o3_4m = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/m.png")
image monika o3_4n = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/n.png")
image monika o3_4o = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/o.png")
image monika o3_4p = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/p.png")
image monika o3_4q = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/q.png")
image monika o3_4r = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o3_2l.png", (0, 0), "ourtime_assets/monika/o3_2r.png", (0, 0), "ourtime_assets/monika/r.png")



image monika o4_1a = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/a.png")
image monika o4_1b = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/b.png")
image monika o4_1c = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/c.png")
image monika o4_1d = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/d.png")
image monika o4_1e = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/e.png")
image monika o4_1f = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/f.png")
image monika o4_1g = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/g.png")
image monika o4_1h = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/h.png")
image monika o4_1i = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/i.png")
image monika o4_1j = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/j.png")
image monika o4_1k = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/k.png")
image monika o4_1l = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/l.png")
image monika o4_1m = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/m.png")
image monika o4_1n = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/n.png")
image monika o4_1o = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/o.png")
image monika o4_1p = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/p.png")
image monika o4_1q = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/q.png")
image monika o4_1r = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/r.png")

image monika o4_2a = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/a.png")
image monika o4_2b = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/b.png")
image monika o4_2c = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/c.png")
image monika o4_2d = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/d.png")
image monika o4_2e = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/e.png")
image monika o4_2f = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/f.png")
image monika o4_2g = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/g.png")
image monika o4_2h = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/h.png")
image monika o4_2i = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/i.png")
image monika o4_2j = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/j.png")
image monika o4_2k = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/k.png")
image monika o4_2l = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/l.png")
image monika o4_2m = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/m.png")
image monika o4_2n = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/n.png")
image monika o4_2o = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/o.png")
image monika o4_2p = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/p.png")
image monika o4_2q = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/q.png")
image monika o4_2r = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_1r.png", (0, 0), "ourtime_assets/monika/r.png")

image monika o4_3a = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/a.png")
image monika o4_3b = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/b.png")
image monika o4_3c = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/c.png")
image monika o4_3d = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/d.png")
image monika o4_3e = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/e.png")
image monika o4_3f = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/f.png")
image monika o4_3g = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/g.png")
image monika o4_3h = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/h.png")
image monika o4_3i = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/i.png")
image monika o4_3j = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/j.png")
image monika o4_3k = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/k.png")
image monika o4_3l = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/l.png")
image monika o4_3m = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/m.png")
image monika o4_3n = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/n.png")
image monika o4_3o = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/o.png")
image monika o4_3p = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/p.png")
image monika o4_3q = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/q.png")
image monika o4_3r = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_1l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/r.png")

image monika o4_4a = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/a.png")
image monika o4_4b = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/b.png")
image monika o4_4c = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/c.png")
image monika o4_4d = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/d.png")
image monika o4_4e = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/e.png")
image monika o4_4f = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/f.png")
image monika o4_4g = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/g.png")
image monika o4_4h = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/h.png")
image monika o4_4i = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/i.png")
image monika o4_4j = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/j.png")
image monika o4_4k = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/k.png")
image monika o4_4l = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/l.png")
image monika o4_4m = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/m.png")
image monika o4_4n = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/n.png")
image monika o4_4o = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/o.png")
image monika o4_4p = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/p.png")
image monika o4_4q = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/q.png")
image monika o4_4r = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o4_2l.png", (0, 0), "ourtime_assets/monika/o4_2r.png", (0, 0), "ourtime_assets/monika/r.png")



image monika o5_1a = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o5_1l.png", (0, 0), "ourtime_assets/monika/o5_1r.png", (0, 0), "ourtime_assets/monika/a.png")
image monika o5_1b = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o5_1l.png", (0, 0), "ourtime_assets/monika/o5_1r.png", (0, 0), "ourtime_assets/monika/b.png")
image monika o5_1c = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o5_1l.png", (0, 0), "ourtime_assets/monika/o5_1r.png", (0, 0), "ourtime_assets/monika/c.png")
image monika o5_1d = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o5_1l.png", (0, 0), "ourtime_assets/monika/o5_1r.png", (0, 0), "ourtime_assets/monika/d.png")
image monika o5_1e = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o5_1l.png", (0, 0), "ourtime_assets/monika/o5_1r.png", (0, 0), "ourtime_assets/monika/e.png")
image monika o5_1f = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o5_1l.png", (0, 0), "ourtime_assets/monika/o5_1r.png", (0, 0), "ourtime_assets/monika/f.png")
image monika o5_1g = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o5_1l.png", (0, 0), "ourtime_assets/monika/o5_1r.png", (0, 0), "ourtime_assets/monika/g.png")
image monika o5_1h = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o5_1l.png", (0, 0), "ourtime_assets/monika/o5_1r.png", (0, 0), "ourtime_assets/monika/h.png")
image monika o5_1i = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o5_1l.png", (0, 0), "ourtime_assets/monika/o5_1r.png", (0, 0), "ourtime_assets/monika/i.png")
image monika o5_1j = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o5_1l.png", (0, 0), "ourtime_assets/monika/o5_1r.png", (0, 0), "ourtime_assets/monika/j.png")
image monika o5_1k = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o5_1l.png", (0, 0), "ourtime_assets/monika/o5_1r.png", (0, 0), "ourtime_assets/monika/k.png")
image monika o5_1l = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o5_1l.png", (0, 0), "ourtime_assets/monika/o5_1r.png", (0, 0), "ourtime_assets/monika/l.png")
image monika o5_1m = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o5_1l.png", (0, 0), "ourtime_assets/monika/o5_1r.png", (0, 0), "ourtime_assets/monika/m.png")
image monika o5_1n = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o5_1l.png", (0, 0), "ourtime_assets/monika/o5_1r.png", (0, 0), "ourtime_assets/monika/n.png")
image monika o5_1o = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o5_1l.png", (0, 0), "ourtime_assets/monika/o5_1r.png", (0, 0), "ourtime_assets/monika/o.png")
image monika o5_1p = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o5_1l.png", (0, 0), "ourtime_assets/monika/o5_1r.png", (0, 0), "ourtime_assets/monika/p.png")
image monika o5_1q = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o5_1l.png", (0, 0), "ourtime_assets/monika/o5_1r.png", (0, 0), "ourtime_assets/monika/q.png")
image monika o5_1r = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/o5_1l.png", (0, 0), "ourtime_assets/monika/o5_1r.png", (0, 0), "ourtime_assets/monika/r.png")




image monika p_1a = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_1l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/a.png")
image monika p_1b = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_1l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/b.png")
image monika p_1c = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_1l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/c.png")
image monika p_1d = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_1l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/d.png")
image monika p_1e = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_1l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/e.png")
image monika p_1f = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_1l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/f.png")
image monika p_1g = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_1l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/g.png")
image monika p_1h = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_1l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/h.png")
image monika p_1i = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_1l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/i.png")
image monika p_1j = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_1l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/j.png")
image monika p_1k = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_1l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/k.png")
image monika p_1l = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_1l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/l.png")
image monika p_1m = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_1l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/m.png")
image monika p_1n = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_1l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/n.png")
image monika p_1o = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_1l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/o.png")
image monika p_1p = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_1l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/p.png")
image monika p_1q = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_1l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/q.png")
image monika p_1r = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_1l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/r.png")



image monika p_2a = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_2l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/a.png")
image monika p_2b = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_2l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/b.png")
image monika p_2c = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_2l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/c.png")
image monika p_2d = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_2l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/d.png")
image monika p_2e = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_2l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/e.png")
image monika p_2f = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_2l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/f.png")
image monika p_2g = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_2l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/g.png")
image monika p_2h = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_2l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/h.png")
image monika p_2i = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_2l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/i.png")
image monika p_2j = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_2l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/j.png")
image monika p_2k = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_2l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/k.png")
image monika p_2l = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_2l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/l.png")
image monika p_2m = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_2l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/m.png")
image monika p_2n = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_2l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/n.png")
image monika p_2o = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_2l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/o.png")
image monika p_2p = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_2l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/p.png")
image monika p_2q = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_2l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/q.png")
image monika p_2r = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_2l.png", (0, 0), "ourtime_assets/monika/p_1r.png", (0, 0), "ourtime_assets/monika/r.png")



image monika p_5a = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_3a.png")
image monika p_5b = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/p_3b.png")



image monika h1_1a = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/a.png")
image monika h1_1b = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/b.png")
image monika h1_1c = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/c.png")
image monika h1_1d = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/d.png")
image monika h1_1e = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/e.png")
image monika h1_1f = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/f.png")
image monika h1_1g = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/g.png")
image monika h1_1h = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/h.png")
image monika h1_1i = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/i.png")
image monika h1_1j = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/j.png")
image monika h1_1k = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/k.png")
image monika h1_1l = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/l.png")
image monika h1_1m = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/m.png")
image monika h1_1n = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/n.png")
image monika h1_1o = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/o.png")
image monika h1_1p = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/p.png")
image monika h1_1q = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/q.png")
image monika h1_1r = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/r.png")

image monika h1_2a = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/a.png")
image monika h1_2b = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/b.png")
image monika h1_2c = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/c.png")
image monika h1_2d = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/d.png")
image monika h1_2e = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/e.png")
image monika h1_2f = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/f.png")
image monika h1_2g = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/g.png")
image monika h1_2h = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/h.png")
image monika h1_2i = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/i.png")
image monika h1_2j = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/j.png")
image monika h1_2k = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/k.png")
image monika h1_2l = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/l.png")
image monika h1_2m = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/m.png")
image monika h1_2n = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/n.png")
image monika h1_2o = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/o.png")
image monika h1_2p = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/p.png")
image monika h1_2q = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/q.png")
image monika h1_2r = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_1r.png", (0, 0), "ourtime_assets/monika/r.png")

image monika h1_3a = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/a.png")
image monika h1_3b = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/b.png")
image monika h1_3c = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/c.png")
image monika h1_3d = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/d.png")
image monika h1_3e = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/e.png")
image monika h1_3f = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/f.png")
image monika h1_3g = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/g.png")
image monika h1_3h = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/h.png")
image monika h1_3i = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/i.png")
image monika h1_3j = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/j.png")
image monika h1_3k = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/k.png")
image monika h1_3l = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/l.png")
image monika h1_3m = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/m.png")
image monika h1_3n = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/n.png")
image monika h1_3o = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/o.png")
image monika h1_3p = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/p.png")
image monika h1_3q = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/q.png")
image monika h1_3r = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_1l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/r.png")

image monika h1_4a = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/a.png")
image monika h1_4b = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/b.png")
image monika h1_4c = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/c.png")
image monika h1_4d = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/d.png")
image monika h1_4e = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/e.png")
image monika h1_4f = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/f.png")
image monika h1_4g = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/g.png")
image monika h1_4h = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/h.png")
image monika h1_4i = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/i.png")
image monika h1_4j = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/j.png")
image monika h1_4k = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/k.png")
image monika h1_4l = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/l.png")
image monika h1_4m = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/m.png")
image monika h1_4n = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/n.png")
image monika h1_4o = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/o.png")
image monika h1_4p = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/p.png")
image monika h1_4q = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/q.png")
image monika h1_4r = im.Composite((960, 960), (0, 0), "ourtime_assets/monika/h1_2l.png", (0, 0), "ourtime_assets/monika/h1_2r.png", (0, 0), "ourtime_assets/monika/r.png")

#bikini monika

image monika 5ca = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/binmonika.png")
image monika 1ca = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/1.png", (0, 0), "mod_assets/binmonika/ca.png")
image monika 1cb = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/1.png", (0, 0), "mod_assets/binmonika/cb.png")
image monika 1cc = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/1.png", (0, 0), "mod_assets/binmonika/cc.png")
image monika 1cd = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/1.png", (0, 0), "mod_assets/binmonika/cd.png")
image monika 1ce = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/1.png", (0, 0), "mod_assets/binmonika/ce.png")
image monika 1cf = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/1.png", (0, 0), "mod_assets/binmonika/cf.png")
image monika 1cg = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/1.png", (0, 0), "mod_assets/binmonika/cg.png")
image monika 1ch = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/1.png", (0, 0), "mod_assets/binmonika/ch.png")
image monika 1ci = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/1.png", (0, 0), "mod_assets/binmonika/ci.png")
image monika 1cj = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/1.png", (0, 0), "mod_assets/binmonika/cj.png")
image monika 1ck = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/1.png", (0, 0), "mod_assets/binmonika/ck.png")
image monika 1cl = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/1.png", (0, 0), "mod_assets/binmonika/cl.png")
image monika 1cm = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/1.png", (0, 0), "mod_assets/binmonika/cm.png")
image monika 1cn = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/1.png", (0, 0), "mod_assets/binmonika/cn.png")
image monika 1co = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/1.png", (0, 0), "mod_assets/binmonika/co.png")
image monika 1cp = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/1.png", (0, 0), "mod_assets/binmonika/cp.png")
image monika 1cq = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/1.png", (0, 0), "mod_assets/binmonika/cq.png")
image monika 1cr = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/1.png", (0, 0), "mod_assets/binmonika/cr.png")

image monika 2ca = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/2.png", (0, 0), "mod_assets/binmonika/ca.png")
image monika 2cb = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/2.png", (0, 0), "mod_assets/binmonika/cb.png")
image monika 2cc = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/2.png", (0, 0), "mod_assets/binmonika/cc.png")
image monika 2cd = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/2.png", (0, 0), "mod_assets/binmonika/cd.png")
image monika 2ce = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/2.png", (0, 0), "mod_assets/binmonika/ce.png")
image monika 2cf = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/2.png", (0, 0), "mod_assets/binmonika/cf.png")
image monika 2cg = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/2.png", (0, 0), "mod_assets/binmonika/cg.png")
image monika 2ch = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/2.png", (0, 0), "mod_assets/binmonika/ch.png")
image monika 2ci = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/2.png", (0, 0), "mod_assets/binmonika/ci.png")
image monika 2cj = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/2.png", (0, 0), "mod_assets/binmonika/cj.png")
image monika 2ck = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/2.png", (0, 0), "mod_assets/binmonika/ck.png")
image monika 2cl = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/2.png", (0, 0), "mod_assets/binmonika/cl.png")
image monika 2cm = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/2.png", (0, 0), "mod_assets/binmonika/cm.png")
image monika 2cn = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/2.png", (0, 0), "mod_assets/binmonika/cn.png")
image monika 2co = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/2.png", (0, 0), "mod_assets/binmonika/co.png")
image monika 2cp = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/2.png", (0, 0), "mod_assets/binmonika/cp.png")
image monika 2cq = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/2.png", (0, 0), "mod_assets/binmonika/cq.png")
image monika 2cr = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/2.png", (0, 0), "mod_assets/binmonika/cr.png")

image monika 3ca = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/3.png", (0, 0), "mod_assets/binmonika/ca.png")
image monika 3cb = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/3.png", (0, 0), "mod_assets/binmonika/cb.png")
image monika 3cc = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/3.png", (0, 0), "mod_assets/binmonika/cc.png")
image monika 3cd = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/3.png", (0, 0), "mod_assets/binmonika/cd.png")
image monika 3ce = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/3.png", (0, 0), "mod_assets/binmonika/ce.png")
image monika 3cf = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/3.png", (0, 0), "mod_assets/binmonika/cf.png")
image monika 3cg = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/3.png", (0, 0), "mod_assets/binmonika/cg.png")
image monika 3ch = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/3.png", (0, 0), "mod_assets/binmonika/ch.png")
image monika 3ci = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/3.png", (0, 0), "mod_assets/binmonika/ci.png")
image monika 3cj = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/3.png", (0, 0), "mod_assets/binmonika/cj.png")
image monika 3ck = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/3.png", (0, 0), "mod_assets/binmonika/ck.png")
image monika 3cl = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/3.png", (0, 0), "mod_assets/binmonika/cl.png")
image monika 3cm = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/3.png", (0, 0), "mod_assets/binmonika/cm.png")
image monika 3cn = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/3.png", (0, 0), "mod_assets/binmonika/cn.png")
image monika 3co = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/3.png", (0, 0), "mod_assets/binmonika/co.png")
image monika 3cp = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/3.png", (0, 0), "mod_assets/binmonika/cp.png")
image monika 3cq = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/3.png", (0, 0), "mod_assets/binmonika/cq.png")
image monika 3cr = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/3.png", (0, 0), "mod_assets/binmonika/cr.png")

image monika 4ca = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/4.png", (0, 0), "mod_assets/binmonika/ca.png")
image monika 4cb = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/4.png", (0, 0), "mod_assets/binmonika/cb.png")
image monika 4cc = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/4.png", (0, 0), "mod_assets/binmonika/cc.png")
image monika 4cd = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/4.png", (0, 0), "mod_assets/binmonika/cd.png")
image monika 4ce = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/4.png", (0, 0), "mod_assets/binmonika/ce.png")
image monika 4cf = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/4.png", (0, 0), "mod_assets/binmonika/cf.png")
image monika 4cg = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/4.png", (0, 0), "mod_assets/binmonika/cg.png")
image monika 4ch = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/4.png", (0, 0), "mod_assets/binmonika/ch.png")
image monika 4ci = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/4.png", (0, 0), "mod_assets/binmonika/ci.png")
image monika 4cj = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/4.png", (0, 0), "mod_assets/binmonika/cj.png")
image monika 4ck = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/4.png", (0, 0), "mod_assets/binmonika/ck.png")
image monika 4cl = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/4.png", (0, 0), "mod_assets/binmonika/cl.png")
image monika 4cm = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/4.png", (0, 0), "mod_assets/binmonika/cm.png")
image monika 4cn = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/4.png", (0, 0), "mod_assets/binmonika/cn.png")
image monika 4co = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/4.png", (0, 0), "mod_assets/binmonika/co.png")
image monika 4cp = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/4.png", (0, 0), "mod_assets/binmonika/cp.png")
image monika 4cq = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/4.png", (0, 0), "mod_assets/binmonika/cq.png")
image monika 4cr = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/4.png", (0, 0), "mod_assets/binmonika/cr.png")

image monika 5ca = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/5.png")
image monika 5cb = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/5.png", (0, 0), "mod_assets/binmonika/cb.png")
image monika 5cc = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/5.png", (0, 0), "mod_assets/binmonika/cc.png")
image monika 5cd = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/5.png", (0, 0), "mod_assets/binmonika/cd.png")
image monika 5ce = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/5.png", (0, 0), "mod_assets/binmonika/ce.png")
image monika 5cf = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/5.png", (0, 0), "mod_assets/binmonika/cf.png")
image monika 5cg = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/5.png", (0, 0), "mod_assets/binmonika/cg.png")
image monika 5ch = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/5.png", (0, 0), "mod_assets/binmonika/ch.png")
image monika 5ci = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/5.png", (0, 0), "mod_assets/binmonika/ci.png")
image monika 5cj = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/5.png", (0, 0), "mod_assets/binmonika/cj.png")
image monika 5ck = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/5.png", (0, 0), "mod_assets/binmonika/ck.png")
image monika 5cl = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/5.png", (0, 0), "mod_assets/binmonika/cl.png")
image monika 5cm = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/5.png", (0, 0), "mod_assets/binmonika/cm.png")
image monika 5cn = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/5.png", (0, 0), "mod_assets/binmonika/cn.png")
image monika 5co = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/5.png", (0, 0), "mod_assets/binmonika/co.png")
image monika 5cp = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/5.png", (0, 0), "mod_assets/binmonika/cp.png")
image monika 5cq = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/5.png", (0, 0), "mod_assets/binmonika/cq.png")
image monika 5cr = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/5.png", (0, 0), "mod_assets/binmonika/cr.png")

image monika 6ca = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/6.png")
image monika 6cb = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/6.png", (0, 0), "mod_assets/binmonika/cb.png")
image monika 6cc = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/6.png", (0, 0), "mod_assets/binmonika/cc.png")
image monika 6cd = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/6.png", (0, 0), "mod_assets/binmonika/cd.png")
image monika 6ce = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/6.png", (0, 0), "mod_assets/binmonika/ce.png")
image monika 6cf = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/6.png", (0, 0), "mod_assets/binmonika/cf.png")
image monika 6cg = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/6.png", (0, 0), "mod_assets/binmonika/cg.png")
image monika 6ch = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/6.png", (0, 0), "mod_assets/binmonika/ch.png")
image monika 6ci = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/6.png", (0, 0), "mod_assets/binmonika/ci.png")
image monika 6cj = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/6.png", (0, 0), "mod_assets/binmonika/cj.png")
image monika 6ck = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/6.png", (0, 0), "mod_assets/binmonika/ck.png")
image monika 6cl = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/6.png", (0, 0), "mod_assets/binmonika/cl.png")
image monika 6cm = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/6.png", (0, 0), "mod_assets/binmonika/cm.png")
image monika 6cn = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/6.png", (0, 0), "mod_assets/binmonika/cn.png")
image monika 6co = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/6.png", (0, 0), "mod_assets/binmonika/co.png")
image monika 6cp = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/6.png", (0, 0), "mod_assets/binmonika/cp.png")
image monika 6cq = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/6.png", (0, 0), "mod_assets/binmonika/cq.png")
image monika 6cr = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/6.png", (0, 0), "mod_assets/binmonika/cr.png")

image monika 7ca = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/7.png")
image monika 7cb = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/7b.png")
image monika 7cc = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/7c.png")

image monika 8ca = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/8.png")
image monika 8cb = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/8b.png")
image monika 8cc = im.Composite((960, 960), (0, 0), "mod_assets/binmonika/8c.png")

image monika hug = im.Composite((960, 960), (0, 0), "mod_assets/monika/hug.png")

image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat

#tovarisch ГГ

image protag 1 = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/a.png")
image protag 2 = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/a.png")
image protag 3 = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/a.png")
image protag 4 = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/a.png")
image protag 5 = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/a.png")

image protag 1a = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/a.png")
image protag 1b = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/b.png")
image protag 1c = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/c.png")
image protag 1d = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/d.png")
image protag 1e = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/e.png")
image protag 1f = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/f.png")
image protag 1g = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/g.png")
image protag 1h = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/h.png")
image protag 1i = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/i.png")
image protag 1j = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/j.png")
image protag 1k = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/k.png")
image protag 1l = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/l.png")
image protag 1m = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/m.png")
image protag 1n = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/n.png")
image protag 1o = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/o.png")
image protag 1p = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/p.png")
image protag 1q = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/q.png")
image protag 1r = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/r.png")
image protag 1s = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/s.png")
image protag 1t = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/t.png")
image protag 1u = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/u.png")
image protag 1v = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/v.png")
image protag 1w = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/w.png")
image protag 1x = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/x.png")
image protag 1y = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/y.png")
image protag 1z = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/z.png")
image protag 1sh = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/shock.png")

image protag 2a = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/a.png")
image protag 2b = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/b.png")
image protag 2c = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/c.png")
image protag 2d = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/d.png")
image protag 2e = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/e.png")
image protag 2f = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/f.png")
image protag 2g = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/g.png")
image protag 2h = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/h.png")
image protag 2i = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/i.png")
image protag 2j = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/j.png")
image protag 2k = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/k.png")
image protag 2l = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/l.png")
image protag 2m = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/m.png")
image protag 2n = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/n.png")
image protag 2o = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/o.png")
image protag 2p = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/p.png")
image protag 2q = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/q.png")
image protag 2r = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/r.png")
image protag 2s = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/s.png")
image protag 2t = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/t.png")
image protag 2u = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/u.png")
image protag 2v = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/v.png")
image protag 2w = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/w.png")
image protag 2x = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/x.png")
image protag 2y = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/y.png")
image protag 2z = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/z.png")
image protag 2sh = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/shock.png")

image protag 3a = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/a.png")
image protag 3b = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/b.png")
image protag 3c = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/c.png")
image protag 3d = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/d.png")
image protag 3e = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/e.png")
image protag 3f = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/f.png")
image protag 3g = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/g.png")
image protag 3h = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/h.png")
image protag 3i = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/i.png")
image protag 3j = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/j.png")
image protag 3k = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/k.png")
image protag 3l = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/l.png")
image protag 3m = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/m.png")
image protag 3n = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/n.png")
image protag 3o = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/o.png")
image protag 3p = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/p.png")
image protag 3q = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/q.png")
image protag 3r = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/r.png")
image protag 3s = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/s.png")
image protag 3t = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/t.png")
image protag 3u = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/u.png")
image protag 3v = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/v.png")
image protag 3w = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/w.png")
image protag 3x = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/x.png")
image protag 3y = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/y.png")
image protag 3z = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/z.png")
image protag 3sh = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/shock.png")

image protag 4a = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/a.png")
image protag 4b = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/b.png")
image protag 4c = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/c.png")
image protag 4d = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/d.png")
image protag 4e = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/e.png")
image protag 4f = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/f.png")
image protag 4g = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/g.png")
image protag 4h = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/h.png")
image protag 4i = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/i.png")
image protag 4j = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/j.png")
image protag 4k = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/k.png")
image protag 4l = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/l.png")
image protag 4m = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/m.png")
image protag 4n = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/n.png")
image protag 4o = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/o.png")
image protag 4p = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/p.png")
image protag 4q = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/q.png")
image protag 4r = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/r.png")
image protag 4s = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/s.png")
image protag 4t = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/t.png")
image protag 4u = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/u.png")
image protag 4v = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/v.png")
image protag 4w = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/w.png")
image protag 4x = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/x.png")
image protag 4y = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/y.png")
image protag 4z = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/z.png")
image protag 4sh = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/shock.png")

image protag 5a = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/a.png")
image protag 5b = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/b.png")
image protag 5c = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/c.png")
image protag 5d = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/d.png")
image protag 5e = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/e.png")
image protag 5f = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/f.png")
image protag 5g = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/g.png")
image protag 5h = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/h.png")
image protag 5i = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/i.png")
image protag 5j = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/j.png")
image protag 5k = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/k.png")
image protag 5l = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/l.png")
image protag 5m = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/m.png")
image protag 5n = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/n.png")
image protag 5o = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/o.png")
image protag 5p = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/p.png")
image protag 5q = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/q.png")
image protag 5r = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/r.png")
image protag 5s = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/s.png")
image protag 5t = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/t.png")
image protag 5u = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/u.png")
image protag 5v = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/v.png")
image protag 5w = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/w.png")
image protag 5x = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/x.png")
image protag 5y = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/y.png")
image protag 5z = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/z.png")
image protag 5sh = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/shock.png")

#ГГ casual

image protag 1ba = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/a.png")
image protag 1bb = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/b.png")
image protag 1bc = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/c.png")
image protag 1bd = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/d.png")
image protag 1be = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/e.png")
image protag 1bf = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/f.png")
image protag 1bg = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/g.png")
image protag 1bh = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/h.png")
image protag 1bi = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/i.png")
image protag 1bj = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/j.png")
image protag 1bk = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/k.png")
image protag 1bl = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/l.png")
image protag 1bm = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/m.png")
image protag 1bn = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/n.png")
image protag 1bo = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/o.png")
image protag 1bp = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/p.png")
image protag 1bq = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/q.png")
image protag 1br = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/r.png")
image protag 1bs = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/s.png")
image protag 1bt = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/t.png")
image protag 1bu = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/u.png")
image protag 1bv = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/v.png")
image protag 1bw = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/w.png")
image protag 1bx = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/x.png")
image protag 1by = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/y.png")
image protag 1bz = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/z.png")
image protag 1bsh = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/shock.png")

image protag 2ba = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/a.png")
image protag 2bb = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/b.png")
image protag 2bc = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/c.png")
image protag 2bd = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/d.png")
image protag 2be = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/e.png")
image protag 2bf = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/f.png")
image protag 2bg = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/g.png")
image protag 2bh = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/h.png")
image protag 2bi = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/i.png")
image protag 2bj = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/j.png")
image protag 2bk = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/k.png")
image protag 2bl = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/l.png")
image protag 2bm = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/m.png")
image protag 2bn = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/n.png")
image protag 2bo = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/o.png")
image protag 2bp = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/p.png")
image protag 2bq = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/q.png")
image protag 2br = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/r.png")
image protag 2bs = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/s.png")
image protag 2bt = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/t.png")
image protag 2bu = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/u.png")
image protag 2bv = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/v.png")
image protag 2bw = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/w.png")
image protag 2bx = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/x.png")
image protag 2by = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/y.png")
image protag 2bz = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/z.png")
image protag 2bsh = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/shock.png")

image protag 3ba = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/a.png")
image protag 3bb = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/b.png")
image protag 3bc = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/c.png")
image protag 3bd = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/d.png")
image protag 3be = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/e.png")
image protag 3bf = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/f.png")
image protag 3bg = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/g.png")
image protag 3bh = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/h.png")
image protag 3bi = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/i.png")
image protag 3bj = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/j.png")
image protag 3bk = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/k.png")
image protag 3bl = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/l.png")
image protag 3bm = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/m.png")
image protag 3bn = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/n.png")
image protag 3bo = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/o.png")
image protag 3bp = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/p.png")
image protag 3bq = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/q.png")
image protag 3br = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/r.png")
image protag 3bs = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/s.png")
image protag 3bt = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/t.png")
image protag 3bu = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/u.png")
image protag 3bv = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/v.png")
image protag 3bw = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/w.png")
image protag 3bx = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/x.png")
image protag 3by = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/y.png")
image protag 3bz = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/z.png")
image protag 3bsh = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/shock.png")

image protag 4ba = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/a.png")
image protag 4bb = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/b.png")
image protag 4bc = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/c.png")
image protag 4bd = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/d.png")
image protag 4be = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/e.png")
image protag 4bf = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/f.png")
image protag 4bg = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/g.png")
image protag 4bh = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/h.png")
image protag 4bi = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/i.png")
image protag 4bj = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/j.png")
image protag 4bk = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/k.png")
image protag 4bl = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/l.png")
image protag 4bm = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/m.png")
image protag 4bn = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/n.png")
image protag 4bo = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/o.png")
image protag 4bp = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/p.png")
image protag 4bq = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/q.png")
image protag 4br = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/r.png")
image protag 4bs = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/s.png")
image protag 4bt = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/t.png")
image protag 4bu = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/u.png")
image protag 4bv = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/v.png")
image protag 4bw = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/w.png")
image protag 4bx = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/x.png")
image protag 4by = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/y.png")
image protag 4bz = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/z.png")
image protag 4bsh = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bl.png", (0, 0), "mod_assets/mc/2br.png", (0, 0), "mod_assets/mc/shock.png")

image protag 5ba = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/a.png")
image protag 5bb = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/b.png")
image protag 5bc = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/c.png")
image protag 5bd = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/d.png")
image protag 5be = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/e.png")
image protag 5bf = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/f.png")
image protag 5bg = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/g.png")
image protag 5bh = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/h.png")
image protag 5bi = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/i.png")
image protag 5bj = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/j.png")
image protag 5bk = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/k.png")
image protag 5bl = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/l.png")
image protag 5bm = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/m.png")
image protag 5bn = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/n.png")
image protag 5bo = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/o.png")
image protag 5bp = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/p.png")
image protag 5bq = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/q.png")
image protag 5br = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/r.png")
image protag 5bs = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/s.png")
image protag 5bt = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/t.png")
image protag 5bu = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/u.png")
image protag 5bv = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/v.png")
image protag 5bw = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/w.png")
image protag 5bx = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/x.png")
image protag 5by = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/y.png")
image protag 5bz = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/z.png")
image protag 5bsh = im.Composite((960, 960), (0, 0), "mod_assets/mc/3b.png", (0, 0), "mod_assets/mc/shock.png")

###### Character Variables ######
# These configure the shortcuts for writing dialog for each character.
define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define p = DynamicCharacter('p_name', image='protag', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

define ph = DynamicCharacter('ph_name',  what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define e = DynamicCharacter('e_name',  what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define v = DynamicCharacter('v_name',  what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define vn = Character('VorkNezer', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

define _dismiss_pause = config.developer

###### Persistent Variables ######
# These values are automatically loaded/saved on game start and exit.
# These exist across all saves

default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None

###### Other global variables ######
# It's good practice to define global variables here, just so you know what you can call later

default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None

default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"
default p_name = "ГГ"

default ph_name = "Phoenix"
default e_name = "Miles"
default v_name = "Franziska"

# Instantiating variables for poem appeal. This is how much each character likes the poem for each day.
# -1 = Dislike, 0 = Neutral, 1 = Like
default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]

# The last winner of the poem minigame.
default poemwinner = ['sayori', 'sayori', 'sayori']

# Keeping track of who read your poem when you're showing it to each of the girls.
default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False

# Used in poemresponse_start because it's easier than checking true/false on everyone's read state.
default poemsread = 0

# The main appeal points. Whoever likes your poem the most gets an appeal point for that chapter.
# Appeal points are used to keep track of which exclusive scene to show each chapter.
default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0

# We keep track of whether we watched Natsuki's and sayori's second exclusive scenes
# to decide whether to play them in chapter 3.
default n_exclusivewatched = False
default y_exclusivewatched = False

# Yuri runs away after the first exclusive scene of playthrough 2.
default y_gave = False
default y_ranaway = False

# We choose who to side with in chapter 1.
default ch1_choice = "sayori"

# If we choose to help Sayori in ch3, some of the dialogue changes.
default help_sayori = None
default help_monika = None

# We choose who to spend time with in chapter 4.
default ch4_scene = "yuri"
default ch4_name = "Yuri"
default sayori_confess = True

# We read Natsuki's confession poem in chapter 23.
default natsuki_23 = None

#is the install finished?
default inst_comp = False

#daily variables
default persistent.cookd2 = True
default persistent.inst_comp = False
default persistent.coffee = "cof"
default persistent.cofname = "a coffee"
default persistent.goodatschool = False
default persistent.dodgewin = False
default persistent.fris = True
default persistent.parkchoice = None
default persistent.gifted = False
default persistent.goondate = True
default persistent.revealloc = False