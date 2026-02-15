## 此文件包含有可自定义您游戏的设置。
##
## 以“##”开头的语句是注释，您不应该对其取消注释。以“#”开头的语句是注释掉的代码，
## 在适用的时候您可能需要对其取消注释。



# init python:
    # 共 7 个部分：索引0 = 引子，1~6 = 第一章至第六章
    # if persistent.chapter_unlocked is None:
        # 初始仅引子解锁
        # persistent.chapter_unlocked = [True, False, False, False, False, False, False]




## 基础 ##########################################################################

## 用户可读的游戏名称。此命令用来设置默认窗口标题，并且会在界面和错误报告中出
## 现。
##
## 带有 _() 的字符串表示其可被翻译。

define config.name = _("""光斑
Light Spot""")


## 决定上面给出的标题是否显示在标题界面屏幕。设置为 False 来隐藏标题。

define gui.show_name = True


## 游戏版本号。

define config.version = "1.1"


## 放置在游戏内“关于”屏幕上的文本。将文本放在三个引号之间，并在段落之间留出空
## 行。

define gui.about = _p("""
\n这是一部【FVN批评兽人视觉小说极限创作挑战赛#0——言语肇始】的参赛作品。
\n仅供学习交流使用。
\n文案/美术/音乐/编程：{a=https://wuyeqixun.itch.io/}雾野七浔{/a}（点击跳转itch主页） {size=20}{s}（其实没有美术，只是找了很多图片来当美术资源）{/s}{/size}


{size=60}字体：{/size}
\n霞鹜文楷1.521 ({a=https://www.maoken.com/freefonts/9704.html}此处访问来源{/a})


{size=60}音效：{/size}
\n翻页声（文件名 page.mp3），作者 RGBworks（{a=https://www.aigei.com/sound/cc/}此处访问来源{/a}）


{size=60}背景音乐{/size}（以下均为文件名，按出现的先后顺序排列）{size=60}：{/size}
\n主菜单：Evening
\n引子：Man Down
\n第一章：Morning
\n第二章：Magic Scout - Farm（网站中该曲名为“Farm”），Thinking of You
\n第三章：Procession of the King，Auguish
\n第四章：Decline，Man Down
\n第五章：Fresh Air
\n第六章：Calmant，With Regards
\n"Anguish", "Calmant", "Decline", "Evening", "Farm", "Fresh Air", "Man Down", "Morning", "Procession of the King", "Thinking of You", "With Regards"
\nKevin MacLeod ({a=https://incompetech.com/music/royalty-free/music.html}incompetech.com{/a})
\nLicensed under Creative Commons: By Attribution 4.0
\n{a=http://creativecommons.org/licenses/by/4.0/}http://creativecommons.org/licenses/by/4.0/{/a}


{size=60}图片{/size}（以下均为文件名，游戏内重复出现的为同一张）{size=60}：{/size}
\n主菜单及应用图标：
\n{i}by UNTHINKER via {a=https://pixabay.com/zh/photos/light-lamp-light-spot-bright-4926930/}Pixabay{/a}{/i}
\n第一章： 
\nbg classroom（{i}by DeltaWorks via {a=https://pixabay.com/zh/photos/school-study-education-desk-6900381/}Pixabay{/a}{/i}）
\nbg corridor（{i}by Alger-zhang via {a=https://pixabay.com/photos/school-corridor-6245138/}Pixabay{/a}{/i}）
\nbg diary（{i}by Pexels via {a=https://pixabay.com/photos/notebook-notes-pen-writing-diary-1840276/}Pixabay{/a}{/i}）
\n第二章：
\nbg book（{i}by Pexels via {a=https://pixabay.com/photos/book-pages-open-book-read-reading-1868068/}Pixabay{/a}{/i}）
\nbg homework（{i}by lil_foot_ via {a=https://pixabay.com/photos/open-book-library-education-read-1428428/}Pixabay{/a}{/i}）
\nbg moonlight（{i}by Darkmoon_Art via {a=https://pixabay.com/photos/sea-rock-moon-starry-sky-fantasy-4189164/}Pixabay{/a}{/i}）
\n第三章：
\nbg table（{i}by JillWellington via {a=https://pixabay.com/photos/breakfast-table-kitchen-table-3694120/}Pixabay{/a}{/i}）
\nbg room（{i}{a=https://pixabay.com/photos/real-estate-sofa-living-room-table-9053405/}Pixabay{/a}{/i}）
\nbg phone（{i}by AJEL via {a=https://pixabay.com/photos/iphone6-phone-mobile-cell-phone-1013238/}Pixabay{/a}{/i}）
\n第四章：
\nbg room2（{i}by MedicalPrudens via {a=https://pixabay.com/photos/medical-consultation-diagnosis-room-470496/}Pixabay{/a}{/i}）
\nbg street（{i}by jwvein via {a=https://pixabay.com/photos/way-street-architecture-city-4005288/}Pixabay{/a}{/i}）
\nbg bedroom（{i}{a=https://pixabay.com/photos/bedroom-apartment-house-home-8442903/}Pixabay{/a}{/i}）
\nbg medicine（{i}by stevepb via {a=https://pixabay.com/photos/medicine-pills-prescription-4097308/}Pixabay{/a}{/i}）
\nbg paper（{i}by athree23 via {a=https://pixabay.com/photos/post-it-heap-yellow-orange-work-3660172/}Pixabay{/a}{/i}）
\n第五章：
\nbg hospital（{i}{a=https://pixabay.com/photos/hospital-bed-doctor-surgery-1802679/}Pixabay{/a}{/i}）
\nbg box（{i}by ha11ok via {a=https://pixabay.com/photos/space-wood-deliver-logistics-4967335/}Pixabay{/a}{/i}）


""")


## 在构建的发布版中，可执行文件和目录所使用的短名称。此处仅限使用 ASCII 字符，并
## 且不能包含空格、冒号或分号。

define build.name = "LightSpot"


## 音效和音乐 #######################################################################

## 这三个变量控制哪些内置的混音器会默认显示给用户。将其中一个设置为 False 将隐藏
## 对应的混音器。

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## 为了让用户在音效或语音轨道上播放测试音频，请取消对下面一行的注释并设置播放的
## 样本声音。

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## 将以下语句取消注释就可以设置标题界面播放的背景音乐文件。此文件将在整个游戏中
## 持续播放，直至音乐停止或其他文件开始播放。

define config.main_menu_music = "evening.mp3"


## 转场 ##########################################################################
##
## 这些变量用来控制某些事件发生时的转场。每一个变量都应设置成一个转场，或者是
## None 来表示无转场。

## 进入或退出游戏菜单。

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## 各个游戏菜单之间的转场。

define config.intra_transition = dissolve


## 载入游戏后使用的转场。

define config.after_load_transition = None


## 在游戏结束之后进入主菜单时使用的转场。

define config.end_game_transition = dissolve


## 用于控制在游戏开始标签不存在时转场的变量。作为替代，在显示初始化场景后使用
## with 语句。


## 窗口管理 ########################################################################
##
## 此命令控制对话框窗口何时显示。若为 show，对话框将总是显示。若为 hide，对话框
## 仅在对话出现时显示。若为 auto，对话框会在 scene 语句前隐藏，并在有新对话时重
## 新显示。
##
## 在游戏开始后，可以用 window show、window hide 和 window auto 语句来改变其状
## 态。

define config.window = "auto"


## 用于显示和隐藏对话框窗口的转场

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## 默认设置 ########################################################################

## 控制默认的文字显示速度。默认的 0 为瞬间，而其他数字则是每秒显示出的字符数。

default preferences.text_cps = 40


## 默认的自动前进延迟。数字越大，等待时间越长，有效范围为 0 - 30。

default preferences.afm_time = 15


## 存档目录 ########################################################################
##
## 控制 Ren'Py 放置游戏存档的特定操作系统目录。存档文件将放置在：
##
## Windows：%APPDATA\RenPy\<config.save_directory>
##
## Macintosh：$HOME/Library/RenPy/<config.save_directory>
##
## Linux：$HOME/.renpy/<config.save_directory>
##
## 该语句通常不应变更，若要变更，应为有效字符串而不是表达式。

define config.save_directory = "LightSpot-1770716389"


## 图标 ##########################################################################
##
## 在任务栏或 Dock 上显示的图标。

define config.window_icon = "gui/window_icon.png"


## 构建配置 ########################################################################
##
## 此部分控制 Ren'Py 如何将您的项目转变为发行版文件。

init python:

    ## 以下函数接受文件模式。文件模式不区分大小写，并与基础目录的相对路径相匹配，
    ## 包括或不包括 /。如果多个模式匹配，则使用第一个模式。
    ##
    ## 在一个模式中：
    ##
    ## / 是目录分隔符。
    ##
    ## * 匹配所有字符，目录分隔符除外。
    ##
    ## ** 匹配所有字符，包括目录分隔符。
    ##
    ## 例如，“*.txt”匹配基础目录中的 txt 文件，“game/**.ogg”匹配游戏目录或任何子
    ## 目录中的 ogg 文件，“**.psd”匹配项目中任何位置的 psd 文件。

    ## 将文件列为 None 来使其从构建的发行版中排除。

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## 若要封装文件，需将其列为“archive”。

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## 匹配为文档模式的文件会在 Mac 应用程序构建中被复制，因此它们同时出现在 APP
    ## 和 ZIP 文件中。

    build.documentation('*.html')
    build.documentation('*.txt')


## 执行应用内购需要一个 Google Play 许可密钥。许可密钥可以在 Google Play 开发者
## 控制台的“Monetize” > “Monetization Setup” > “Licensing”页面找到。

# define build.google_play_key = "..."


## 与 itch.io 项目相关的用户名和项目名，以 / 分隔。

# define build.itch_project = "renpytom/test-project"
