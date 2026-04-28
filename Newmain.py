import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment
import asyncio
import os
import requests
from SeatingTest import pepito


x = 0
y = -1
z = 1
CurrentMovie= 0
SelectedSeats = []
def main(page: Page) -> None:

   

    times = ["03:00 PM", "03:45 PM", "04:15 PM", "05:00 PM", "05:30 PM", "06:15 PM", 
            "06:45 PM", "07:30 PM", "08:00 PM", "08:45 PM", "09:15 PM", "10:00 PM", "10:30 PM"]

    language = {
    "en": "English", "es": "Spanish", "fr": "French", "de": "German", 
    "it": "Italian", "pt": "Portuguese", "ru": "Russian", "zh": "Chinese",
    "ja": "Japanese", "ko": "Korean", "hi": "Hindi", "ar": "Arabic",
    
    "pl": "Polish", "tr": "Turkish", "nl": "Dutch", "sv": "Swedish",
    "el": "Greek", "cs": "Czech", "hu": "Hungarian", "ro": "Romanian",
    "da": "Danish", "fi": "Finnish", "no": "Norwegian", "bg": "Bulgarian",
    "hr": "Croatian", "sk": "Slovak", "uk": "Ukrainian", "sr": "Serbian",
    
    "th": "Thai", "vi": "Vietnamese", "id": "Indonesian", "ms": "Malay",
    "he": "Hebrew", "fa": "Persian", "bn": "Bengali", "ur": "Urdu",
    "ta": "Tamil", "te": "Telugu", "mr": "Marathi", "gu": "Gujarati",
    
    "ca": "Catalan", "eu": "Basque", "gl": "Galician", "af": "Afrikaans",
    "sw": "Swahili", "is": "Icelandic", "et": "Estonian", "lv": "Latvian",
    "lt": "Lithuanian"
}

    assigns = {    #THIS WAS MADE WITH AI, but the Idea not, randomnized and with AI, and the one from above
        'movie0': [0, 4, 8, 11],
        'movie1': [2, 6, 9, 12],
        'movie2': [1, 5, 7, 10],
        'movie3': [0, 3, 7, 10],
        'movie4': [1, 4, 8, 11],
        'movie5': [2, 6, 9],
        'movie6': [0, 4, 8],
        'movie7': [1, 5, 9, 12],
        'movie8': [2, 6, 10],
        'movie9': [0, 3, 7, 11],
        'movie10': [1, 5, 8],
        'movie11': [2, 6, 9, 12],
        'movie12': [0, 4, 7, 10],
        'movie13': [1, 5, 8, 11],
        'movie14': [2, 6, 9],
        'movie15': [0, 3, 8, 11],
        'movie16': [1, 4, 7, 10],
        'movie17': [2, 6, 9, 12],
        'movie18': [0, 4, 8],
        'movie19': [1, 5, 9, 11]
    }

    page.fonts = {
        "Main": "Comucan_PERSONAL_USE_ONLY.otf",
        "TtNormsExtra": "TtNormsExtraBlack.otf",
        "TtNormsReg": "TT Norms Pro Regular.otf",
        "BricolageBold": "BricolageBoldened.ttf"
    }

    
    
    #Page Setup

    page.window.full_screen = False
    page.theme = ft.Theme(font_family="Main")
    page.title= "World Of Cinema"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.bgcolor = "#000000"
    page.expand=True
    page.theme= ft.Theme(font_family="TtNormsReg")
    page.update()


    def Seating(e):
        Cabra= pepito(page)

        page.open(Cabra)
    #1st view
    async def bola1():

        Ball.opacity=0
        Ball.update()
        
        await asyncio.sleep(0.350)
        Ball.left=-630.9
        Ball.top = 390.6
        Ball.scale=1
        Ball.update()

        await asyncio.sleep(0.310)
        Ball.opacity=1
        Ball.update()

        
    async def bola2():

        Ball.opacity=0
        MainWhite.opacity=0
        MainYellow.opacity=0
        MiniText.opacity=0
        PopCorn.opacity=0
        MovieIcon1.opacity=0
        MovieIcon2.opacity=0
        Icon1Text.opacity=0
        Icon2Text.opacity=0
        page.update()
        
     

    async def bola3():

        Ball.opacity=0
        MainWhite.opacity=0
        MainYellow.opacity=0
        MiniText.opacity=0
        PopCorn.opacity=0
        MovieIcon1.opacity=0
        MovieIcon2.opacity=0
        Icon1Text.opacity=0
        Icon2Text.opacity=0
        page.update()

    async def changeview(e):
        
        await bola2()

        page.update()
        await asyncio.sleep(1)
        page.go('/')

        
        Ball.left=-630.9
        Ball.top = 390.6
        Ball.scale=1
        Ball.update()
        Ball.scale=1
        buttonchoose.opacity=0
        page.update() 

        await asyncio.sleep(0.310)
        MainWhite.opacity=1
        MainYellow.opacity=1
        MiniText.opacity=1
        PopCorn.opacity=1
        MovieIcon1.opacity=1
        MovieIcon2.opacity=1
        Icon1Text.opacity=1
        Icon2Text.opacity=1
        Ball.opacity=1
        buttonchoose.opacity=1
        page.update()
        
    async def changeview_2(e):
        
        await bola2()

        page.update()
        await asyncio.sleep(1)
        page.go('/catalog')

        
        Ball.left=-250.9
        Ball.top = 200.6
        Ball.scale=1
        buttonchoose.opacity=0
        page.update() 

        await asyncio.sleep(0.310)
        Ball.opacity=1
        buttonchoose.opacity=1
        page.update()

    async def changeview_3(e):
        
        await bola2()

        page.update()
        await asyncio.sleep(1)
        page.go('/incoming')
        
        
        Ball.left=-250.9
        Ball.top = 200.6
        Ball.scale=1
        buttonchoose.opacity=0
        page.update() 

        await asyncio.sleep(0.310)
        Ball.opacity=1
        buttonchoose.opacity=1
        page.update()

    # Background and ball
    Background= ft.Image(
                src="lBG.png", 
                fit=ft.Image.fit, 
                scale= 1.2
                )
    
    Ball = ft.Image(
        src="Ball.png", 
        top=390.6, 
        left=-630.9, animate_opacity=300
        )

    #MainPageTextArea
    MainYellow= ft.Text(
        value="WORLD OF",
        font_family="TtNormsExtra", 
        color="#d5b586", 
        top=100, 
        left=300, 
        size=87.5,
        style=ft.TextStyle(letter_spacing=0),
        animate_opacity=300 
        )
    
    MainWhite= ft.Text(
        value= "CINEMA", 
        font_family= "BricolageBold", 
        color=ft.Colors.WHITE,
        top= 80, 
        left= 55, 
        size=365,
        style=ft.TextStyle(letter_spacing=-5),
        animate_opacity=300
        )
    
    #MiniText
    MiniText= ft.Text(
        value="YOUR FAVORITE MOVE THEATER", 
        color="#ffffff", 
        top=485, 
        left=715    , 
        size=12,
        style=ft.TextStyle(letter_spacing=3),
        animate_opacity=300
    )

    #Popcorn image and icons

    PopCorn = ft.Image(
        src="PopCorn.png",
        top=165,
        left=-545,
        expand=False,
        scale=0.75,
        animate_opacity=300
        )
    
    MovieIcon1=ft.Image(
        src="CameraV.png",
        scale=0.6,
        top=-420,
        left= 100,
        animate_opacity=300
        )
    
    Icon1Text = ft.Container(
    content=ft.Text(
        value="ON SCREEN RIGHT NOW",
        size=20,
        style=ft.TextStyle(letter_spacing=2),
    ),
    left=1100,
    top=70,
    on_click= changeview_2,
    animate_opacity=300
    )
    
   

    MovieIcon2=ft.Image(
        src="CameraV.png",
        scale=0.6,
        top=-330,
        left= 100,
        animate_opacity=300
        )
    
    Icon2Text= ft.Container(
    content= ft.Text(
        value="UPCOMING MOVIES",
        size=20,
        style=ft.TextStyle(letter_spacing=2) 
    
        ),
        top= 160,
        left=1100,
        on_click= changeview_3,
        animate_opacity=300
    
    )

    #Main Page

    MainStack = ft.Stack(
        expand=True,
        controls=[

            #Generals
            ft.Container(
            expand=True,
            image=ft.DecorationImage(
                src="lBG.png",
                fit=ft.ImageFit.COVER,
                scale=1.2
            )
        ),
            Ball,
            #MainPage
            MainYellow, 
            MainWhite, 
            PopCorn, 
            MiniText,

            MovieIcon1,
            
            MovieIcon2,
            Icon1Text,
            Icon2Text

            

            ]
        )   
    


    # 2nd Page

    from dotenv import load_dotenv

    load_dotenv()
    API_KEY= os.getenv("TMDB_API_KEY")

    if not API_KEY:
        raise ValueError("TMDB_API_KEY not found, if you do not have a key read the README file from github: ")
    


    url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
        
    }

    response = requests.get(url, headers=headers)

    data = response.json()


    #SUBPAGE
    async def ChooseMovie(e):
        global CurrentMovie

        buttonchoose.opacity=0
        await bola3()
        
        page.update()
        await asyncio.sleep(1)

        CurrentMovie = x % len(data["results"])
        ChosenMovieTitle.content.value = movieTitles[CurrentMovie]
        ChosenMovie.src = imgsurls[CurrentMovie]
        MovieDescription.content.value = MovieDescriptions[CurrentMovie]
        MovLanguage.content.value = MovieLang[CurrentMovie]
        page.go('/catalog/ChooseMoviePage')
        
        Ball.left= 1600.9
        Ball.top= -100
        Ball.scale=2.5
        MovLanguage.content.value=f"{language[MovieLang[CurrentMovie]]}"
        
        Screening3.content.controls[1].content.value=f"{times[assigns[f"movie{CurrentMovie}"][0]]}"
        Screening4.content.controls[1].content.value=f"{times[assigns[f"movie{CurrentMovie}"][1]]}"
        Screening5.content.controls[1].content.value=f"{times[assigns[f"movie{CurrentMovie}"][2]]}"
        if len(assigns[f"movie{CurrentMovie}"]) < 4:
            Screening6.opacity= 0
        else:
            Screening6.content.controls[1].content.value=f"{times[assigns[f"movie{CurrentMovie}"][3]]}"
        page.update() 

        await asyncio.sleep(0.310)
        Ball.opacity=1
        Ball.opacity = 1
        ChosenMovie.opacity = 1
        ChosenMovieTitle.opacity = 1
        DescriptionText.opacity = 1
        MovieDescription.opacity = 1
        MovLanguageText.opacity = 1
        MovLanguage.opacity = 1
        AvailableScreenings.opacity = 1
        Screenings1.opacity = 1
        Screenings2.opacity = 1
        BackButton0.opacity = 1
        page.update()

    #API Callings
    imgsurls= [(f"https://image.tmdb.org/t/p/original{data["results"][x]["poster_path"]}") for x in range(len(data["results"]))]
    
    movieTitles = [data["results"][x]["title"] for x in range(len(data["results"]))]

    MovieDescriptions = [data["results"][x]["overview"] for x in range(len(data["results"]))]
    
    MovieLang = [data["results"][x]["original_language"] for x in range(len(data["results"]))]



    #2nd - MAIN
    
    buttonchoose = ft.Container(
                        content=ft.Image(src='ChooseButton.jpg'),
                        on_click= ChooseMovie,
                        scale=0.25,
                        border_radius=215,
                        top=640,
                        left=0,
                        right=0,
                        alignment=ft.alignment.center,
                        animate_opacity=310 
        )
    
    async def MCLeft(e):
        global x
        global y
        global z
        x-=1
        y-=1
        z-=1
        ImageSlide.controls[1].src=imgsurls[x%len(data["results"])]
        MovTitle.content.value=movieTitles[x%len(data["results"])]
        DILeft.src=imgsurls[y%len(data["results"])]
        DILeftText.value = movieTitles[y % len(movieTitles)]
        DIRight.src=imgsurls[z%len(data["results"])]
        DIRightText.value = movieTitles[z % len(movieTitles)]
        print(x)
        page.update()
        

    async def MCRight(e):
        global x
        global y
        global z
        x+=1
        y+=1
        z+=1
        ImageSlide.controls[1].src=imgsurls[x%len(data["results"])]
        MovTitle.content.value=movieTitles[x%len(data["results"])]
        DILeft.src=imgsurls[y%len(data["results"])]
        DILeftText.value = movieTitles[y % len(movieTitles)]
        DIRight.src=imgsurls[z%len(data["results"])]
        DIRightText.value = movieTitles[z % len(movieTitles)]
        print(x)
        page.update()

    MovTitle = ft.Container(content=ft.Text(value=movieTitles[x],
        text_align=ft.TextAlign.CENTER,
        size=25),
            top=250,
            left=0,
            right=0,
            alignment=ft.alignment.center
            )
            

    DILeft = ft.Image(
        src=imgsurls[y],
        width=200,
        height=300,
    )
    DILeftText = ft.Text(
        value=movieTitles[y],
        size=20,
        color=ft.Colors.WHITE,
        text_align=ft.TextAlign.CENTER,
        width=260,
    )
    
    DILeftColumn = ft.Container(content=ft.Column(controls=[DILeftText,DILeft], horizontal_alignment=ft.CrossAxisAlignment.CENTER), 
                                width=260, 
                                top=350, 
                                left=170,
                                )


    DIRight = ft.Image(
        src=imgsurls[z], 
        width=200,
        height=300,
    )

    DIRightText = ft.Text(
        value=movieTitles[z],
        size=20,
        color=ft.Colors.WHITE,
        text_align=ft.TextAlign.CENTER,
        width=260,
            )
    
    DIRightColumn = ft.Container(content=ft.Column(controls=[DIRightText,DIRight], horizontal_alignment=ft.CrossAxisAlignment.CENTER), 
                                width=260, 
                                top=350, 
                                right=170, )
    MainYellow1 = ft.Text(
        value="WORLD OF",
        font_family="TtNormsExtra",
        color="#d5b586",
        top=20,
        left=0,
        right=0,
        text_align=ft.TextAlign.CENTER,
        size=35,
        style=ft.TextStyle(letter_spacing=0),
        animate_opacity=300
    )

    MainWhite1 = ft.Text(
        value="CINEMA",
        font_family="BricolageBold",
        color=ft.Colors.WHITE,
        top=5,
        left=0,
        right=0,
        text_align=ft.TextAlign.CENTER,
        size=170,
        style=ft.TextStyle(letter_spacing=4),
        animate_opacity=300
    )
    ImageSlide = ft.Row(controls=[
                            ft.Container(content=ft.Icon(ft.Icons.KEYBOARD_ARROW_LEFT_ROUNDED, color= ft.Colors.WHITE), on_click=MCLeft, ink=True,scale= 4, border_radius=50),
                            ft.Image(src=imgsurls[x], scale=0.87, width=300, height=500),
                            ft.Container(content=ft.Icon(ft.Icons.KEYBOARD_ARROW_RIGHT_ROUNDED, color= ft.Colors.WHITE), on_click=MCRight, ink=True, scale=4, border_radius=50),
                        ], 
                        top=250,
                        left=0,
                        right=0,
                        alignment=ft.MainAxisAlignment.CENTER,
                        scale=1, 
                        spacing= 5,
                        wrap=False,)
    
    MovieIcon1PT2=ft.Image(
        src="CameraV.png",
        scale=0.6,
        top=-450,
        right=410,
        animate_opacity=300
        )
    
    Icon1TextPT2 = ft.Container(
    content=ft.Text(
        value="ON SCREEN RIGHT NOW",
        size=16,
        style=ft.TextStyle(letter_spacing=2),
    ),
    left=40,
    top=90,
    
    animate_opacity=300
    )

    HomeIcon = ft.Image(src="Homeicon.png", 
                        scale=0.170,
                        top=-180,
                        right=-220,
                        animate_opacity=300
                        )
    
    HomeText = ft.Container(
    content=ft.Text(
        value="HOME PAGE",
        size=15,
        style=ft.TextStyle(letter_spacing=2),
    ),
    right=25,
    top=90,
    on_click= changeview,
    animate_opacity=300
    )


    HomePage = ft.Stack(
        controls=[
            HomeIcon,
            HomeText]
        )
    
    OnScreenRN = ft.Stack(
        controls=[
            MovieIcon1PT2,
            Icon1TextPT2
        ]
        )

    ndStack= ft.Stack(
        expand=True,
        controls=[

            #Generals
            ft.Container(
            expand=True,
            image=ft.DecorationImage(
                src="lBG.png",
                fit=ft.ImageFit.COVER,
                scale=1.2
            )
        ),
            MainYellow1,
            MainWhite1,
            OnScreenRN,
            HomePage,
            Ball,
            buttonchoose,
            ImageSlide,
            MovTitle,
            DILeftColumn,
            DIRightColumn
        ]

    )
    

    #Sub Second Page 

    
    ChosenMovieTitle = ft.Container(content=ft.Text(value=movieTitles[CurrentMovie],
        text_align=ft.TextAlign.CENTER,
        size=80, font_family= "BricolageBold"),
            top=40,
            left=525,
            )
    ChosenMovie = ft.Image(
                        src=imgsurls[CurrentMovie],
                        height=600,
                        top=150,
                        left=50
                )
    DescriptionText = ft.Container(content= ft.Text(value="Description", 
                                                    text_align=ft.TextAlign.CENTER, 
                                                    size = 35, 
                                                    font_family="BricolageBold"), top =200,
                                                    left=525)
    MovieDescription = ft.Container(content=ft.Text(value=MovieDescriptions[CurrentMovie], size =15), 
                                    top=260,
                                    left=525, 
                                    width=800)
    
    MovLanguageText = ft.Container(content= ft.Text(value="Original Language", 
                                                    text_align=ft.TextAlign.CENTER, 
                                                    size = 35, 
                                                    font_family="BricolageBold"), top =380,
                                                    left=525)
    
    MovLanguage = ft.Container(content=ft.Text(value=f"{language[MovieLang[CurrentMovie]]}", size =20), 
                                    top=430,
                                    left=528, 
                                    width=800)
    
    AvailableScreenings = ft.Container(content= ft.Text(value="Available Screenings", 
                                                    text_align=ft.TextAlign.CENTER, 
                                                    size = 35, 
                                                    font_family="BricolageBold"), top =500,
                                                    left=525)
    


    Question1 = ft.Container(content=ft.Text(value="How many seats would you like?", size=30, 
                                            font_family="BricolageBold"), 
                                            top=300, 
                                            left=525)
    test = ft.Text(value="Min 1. Max 72", color=ft.Colors.BLACK)

    
    

    ChooseSeats = ft.Container(content=ft.Stack(controls=[
                            ft.Container(
                                content=ft.Image(src="Redbuttonbg.png"),
                                    
                                    ink=True,
                                    width=372,
                                    height=90,
                                    scale=0.65,
                                    border_radius=100
                        ),
                        ft.Container(
                                content=ft.Text(f"CHOOSE SEATS",
                                                text_align=ft.TextAlign.CENTER,
                                                size=16,
                                                style=ft.TextStyle(letter_spacing=2),
                                                font_family="TtNormsExtra"),
                                                
                                width=372,
                                height=90,
                                alignment=ft.alignment.center,
                                
                            
                        )
                ]
            ),
            top=450,
            left=460,
            on_click= Seating
            
        )

    async def BackToCatalog(e):

        Ball.opacity = 0
        ChosenMovie.opacity = 0
        ChosenMovieTitle.opacity = 0
        DescriptionText.opacity = 0
        MovieDescription.opacity = 0
        MovLanguageText.opacity = 0
        MovLanguage.opacity = 0
        AvailableScreenings.opacity = 0
        Screenings1.opacity = 0
        Screenings2.opacity = 0
        BackButton0.opacity = 0
        
        page.update()

        await bola2()

        page.update()
        await asyncio.sleep(1)
        page.go('/catalog')

        
        Ball.left=-250.9
        Ball.top = 200.6
        Ball.scale=1
        buttonchoose.opacity=0
        page.update() 

        await asyncio.sleep(0.310)
        Ball.opacity=1
        buttonchoose.opacity=1
        page.update()

    async def BackToScreenTimes(e):
        print("back clicked")

        

        global CurrentMovie

        buttonchoose.opacity=0
        await bola3()
        
        page.update()
        await asyncio.sleep(1)

        CurrentMovie = x % len(data["results"])
        ChosenMovieTitle.content.value = movieTitles[CurrentMovie]
        ChosenMovie.src = imgsurls[CurrentMovie]
        MovieDescription.content.value = MovieDescriptions[CurrentMovie]
        MovLanguage.content.value = MovieLang[CurrentMovie]
        
        
        Ball.left= 1600.9
        Ball.top= -100
        Ball.scale=2.5
        MovLanguage.content.value=f"{language[MovieLang[CurrentMovie]]}"
        
        Screening3.content.controls[1].content.value=f"{times[assigns[f"movie{CurrentMovie}"][0]]}"
        Screening4.content.controls[1].content.value=f"{times[assigns[f"movie{CurrentMovie}"][1]]}"
        Screening5.content.controls[1].content.value=f"{times[assigns[f"movie{CurrentMovie}"][2]]}"
        if len(assigns[f"movie{CurrentMovie}"]) < 4:
            Screening6.opacity= 0
        else:
            Screening6.content.controls[1].content.value=f"{times[assigns[f"movie{CurrentMovie}"][3]]}"
        page.update() 

        await asyncio.sleep(0.310)
        Ball.opacity=1
        Ball.opacity = 1
        ChosenMovie.opacity = 1
        ChosenMovieTitle.opacity = 1
        DescriptionText.opacity = 1
        MovieDescription.opacity = 1
        MovLanguageText.opacity = 1
        MovLanguage.opacity = 1
        AvailableScreenings.opacity = 1
        Screenings1.opacity = 1
        Screenings2.opacity = 1
        BackButton0.opacity = 1
        page.update()

    BackButton0 = ft.Container(content=ft.Icon(ft.Icons.KEYBOARD_ARROW_LEFT_ROUNDED, color= ft.Colors.WHITE), 
                            on_click=BackToCatalog, 
                            ink=True,
                            scale= 3, 
                            border_radius=50, 
                            left=50, top=50)
    
    BackButton = ft.Container(content=ft.Icon(ft.Icons.KEYBOARD_ARROW_LEFT_ROUNDED, color= ft.Colors.WHITE), 
                            on_click=BackToScreenTimes, 
                            ink=True,
                            scale= 3, 
                            border_radius=50, 
                            left=50, top=50)

    async def TotalMoney(e):
        try:
            UserInput = int(TextBox.value)
            print(UserInput)
            if 0 < UserInput < 73:
                TotalPrice = TicketPrice*UserInput
                print(TotalPrice)
                TotalBox.content.value = f"Total Price: {TotalPrice}$RD"
                sub2nd.controls.append(ChooseSeats)
                page.update()
            else:
                TotalBox.content.value = "Number of seats range from 1 to 72"
                page.update()
        except:
            TotalBox.content.value = "Number of seats range from 1 to 72 and must a number."
            page.update()

    TextBox = ft.TextField(
                        label=test,
                        width=400,
                        height=60,
                        border_radius=15,
                        bgcolor=ft.colors.WHITE,
                        border_color=ft.colors.BLACK,
                        
                        border_width=2,
                        on_change=TotalMoney,
                        value = None
                    )
    TextBoxContainer = ft.Container(content=TextBox, top=350,
                        left = 525)
    TotalBox = ft.Container(content=ft.Text(value="",size = 20), top= 420, left=525)
    
    TicketPrice = 450

    async def chooseScreening(e):
        print(e.control.content.controls[1].content.value)

        for item in [
            DescriptionText,
            MovieDescription,
            MovLanguageText,
            MovLanguage,
            AvailableScreenings,
            Screenings1,
            Screenings2
        ]:
            if item in sub2nd.controls:
                sub2nd.controls.remove(item)
                page.update()
            else:
                None

        sub2nd.controls.append(Question1)
        sub2nd.controls.append(TextBoxContainer)
        sub2nd.controls.append(TotalBox)
        sub2nd.controls.append(BackButton)
        page.update()

    Screening3 = ft.Container(content=ft.Stack(controls=[
                            ft.Container(
                                content=ft.Image(src="Redbuttonbg.png"),
                                    
                                    ink=True,
                                    width=372,
                                    height=90,
                                    scale=0.65,
                                    border_radius=100
                        ),
                            ft.Container(
                                content=ft.Text(f"{times[assigns[f"movie{CurrentMovie}"][0]]}",
                                                text_align=ft.TextAlign.CENTER,
                                                size=16,
                                                font_family="TtNormsExtra"),
                                                

                                width=372,
                                height=90,
                                alignment=ft.alignment.center
                                
                            
                            )
                            
        
        ]
    ) ,  on_click=chooseScreening)

    Screening4 = ft.Container(content=ft.Stack(controls=[
                            ft.Container(
                                content=ft.Image(src="Redbuttonbg.png"),
                                    
                                    ink=True,
                                    width=372,
                                    height=90,
                                    scale=0.65,
                                    border_radius=100
                        ),
                            ft.Container(
                                content=ft.Text(f"{times[assigns[f"movie{CurrentMovie}"][1]]}",
                                                text_align=ft.TextAlign.CENTER,
                                                size=16,
                                                font_family="TtNormsExtra"),
                                                
                                width=372,
                                height=90,
                                alignment=ft.alignment.center
                                
                            
                            )
                            
        
        ]
    ) ,  on_click=chooseScreening)


    Screening5 = ft.Container(content=ft.Stack(controls=[
                            ft.Container(
                                content=ft.Image(src="Redbuttonbg.png"),
                                    
                                    ink=True,
                                    width=372,
                                    height=90,
                                    scale=0.65,
                                    border_radius=100
                        ),
                            ft.Container(
                                content=ft.Text(f"{times[assigns[f"movie{CurrentMovie}"][2]]}",
                                                text_align=ft.TextAlign.CENTER,
                                                size=16,
                                                font_family="TtNormsExtra"),
                                                
                                width=372,
                                height=90,
                                alignment=ft.alignment.center
                                
                            
                            )
                            
        
        ]
    ) ,  on_click=chooseScreening)
    
    Screening6 = ft.Container(content=ft.Stack(controls=[
                            ft.Container(
                                content=ft.Image(src="Redbuttonbg.png"),
                                    
                                    ink=True,
                                    width=372,
                                    height=90,
                                    scale=0.65,
                                    border_radius=100
                        ),
                            ft.Container(
                                content=ft.Text("",
                                                text_align=ft.TextAlign.CENTER,
                                                size=16,
                                                font_family="TtNormsExtra"),
                                                
                                width=372,
                                height=90,
                                alignment=ft.alignment.center
                                
                            
                            )
                            
        
        ]
    ) ,  on_click=chooseScreening)

    
    Screenings1 = ft.Container(content=ft.Row(controls=[Screening3,Screening4,Screening5],spacing=-100),
                                top =550,
                                left=455)
    Screenings2 = ft.Container(content=ft.Row(controls=[Screening6],spacing=-100),
                                top =640,
                                left=455)

    SelectedSeats = []

    def SelectSeats(e):
        global SelectedSeats
        seat = e.control

        seat_name = seat.content.value

        if seat_name not in SelectedSeats:
            SelectedSeats.append(seat_name)
            seat.bgcolor = ft.Colors.GREEN
        else:
            SelectedSeats.remove(seat_name)
            seat.bgcolor = ft.Colors.GREY_400

        print(SelectedSeats)
        page.update()

#Individual Seats 1st Column
    indSeatsA1 = ft.Container(content=(ft.Text(value="A1", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.Colors.GREY_400,
                            border_radius= 3, 
                            on_click=SelectSeats)
    indSeatsB1 = ft.Container(content=(ft.Text(value="B1", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.Colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsC1 = ft.Container(content=(ft.Text(value="C1", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsD1 = ft.Container(content=(ft.Text(value="D1", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsE1 = ft.Container(content=(ft.Text(value="E1", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsF1 = ft.Container(content=(ft.Text(value="F1", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    
    ColumnOne = ft.Container(content=ft.Column(controls=[indSeatsA1, indSeatsB1, indSeatsC1, indSeatsD1, indSeatsE1, indSeatsF1]))

#Column of Seats 2
    indSeatsA2 = ft.Container(content=(ft.Text(value="A2", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsB2 = ft.Container(content=(ft.Text(value="B2", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsC2 = ft.Container(content=(ft.Text(value="C2", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsD2 = ft.Container(content=(ft.Text(value="D2", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsE2 = ft.Container(content=(ft.Text(value="E2", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsF2 = ft.Container(content=(ft.Text(value="F2", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    
    ColumnTwo = ft.Container(content=ft.Column(controls=[indSeatsA2, indSeatsB2, indSeatsC2, indSeatsD2, indSeatsE2, indSeatsF2]))

#Column of seats 3
    indSeatsA3 = ft.Container(content=(ft.Text(value="A3", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsB3 = ft.Container(content=(ft.Text(value="B3", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsC3 = ft.Container(content=(ft.Text(value="C3", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsD3 = ft.Container(content=(ft.Text(value="D3", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsE3 = ft.Container(content=(ft.Text(value="E3", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsF3 = ft.Container(content=(ft.Text(value="F3", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    
    ColumnThree = ft.Container(content=ft.Column(controls=[indSeatsA3, indSeatsB3, indSeatsC3, indSeatsD3, indSeatsE3, indSeatsF3]))

#Column of seats 4
    indSeatsA4 = ft.Container(content=(ft.Text(value="A4", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsB4 = ft.Container(content=(ft.Text(value="B4", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsC4 = ft.Container(content=(ft.Text(value="C4", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsD4 = ft.Container(content=(ft.Text(value="D4", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsE4 = ft.Container(content=(ft.Text(value="E4", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsF4 = ft.Container(content=(ft.Text(value="F4", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    
    ColumnFour = ft.Container(content=ft.Column(controls=[indSeatsA4, indSeatsB4, indSeatsC4, indSeatsD4, indSeatsE4, indSeatsF4]))

    BlockOneRow = ft.Container(content=ft.Row(controls=[ColumnOne, ColumnTwo, ColumnThree, ColumnFour], spacing = 4))

#Seats Column 5
    indSeatsA5 = ft.Container(content=(ft.Text(value="A5", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsB5 = ft.Container(content=(ft.Text(value="B5", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsC5 = ft.Container(content=(ft.Text(value="C5", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsD5 = ft.Container(content=(ft.Text(value="D5", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsE5 = ft.Container(content=(ft.Text(value="E5", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsF5 = ft.Container(content=(ft.Text(value="F5", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    
    ColumnFive = ft.Container(content=ft.Column(controls=[indSeatsA5, indSeatsB5, indSeatsC5, indSeatsD5, indSeatsE5, indSeatsF5]))

#Column of Seats 2
    indSeatsA6 = ft.Container(content=(ft.Text(value="A6", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsB6 = ft.Container(content=(ft.Text(value="B6", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsC6 = ft.Container(content=(ft.Text(value="C6", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsD6 = ft.Container(content=(ft.Text(value="D6", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsE6 = ft.Container(content=(ft.Text(value="E6", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsF6 = ft.Container(content=(ft.Text(value="F6", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    
    ColumnSix = ft.Container(content=ft.Column(controls=[indSeatsA6, indSeatsB6, indSeatsC6, indSeatsD6, indSeatsE6, indSeatsF6]))

#Column of seats 7
    indSeatsA7 = ft.Container(content=(ft.Text(value="A7", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsB7 = ft.Container(content=(ft.Text(value="B7", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsC7 = ft.Container(content=(ft.Text(value="C7", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsD7 = ft.Container(content=(ft.Text(value="D7", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsE7 = ft.Container(content=(ft.Text(value="E7", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsF7 = ft.Container(content=(ft.Text(value="F7", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    
    ColumnSeven = ft.Container(content=ft.Column(controls=[indSeatsA7, indSeatsB7, indSeatsC7, indSeatsD7, indSeatsE7, indSeatsF7]))

#Column of seats 8
    indSeatsA8 = ft.Container(content=(ft.Text(value="A8", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsB8 = ft.Container(content=(ft.Text(value="B8", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsC8 = ft.Container(content=(ft.Text(value="C8", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsD8 = ft.Container(content=(ft.Text(value="D8", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsE8 = ft.Container(content=(ft.Text(value="E8", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsF8 = ft.Container(content=(ft.Text(value="F8", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    
    ColumnEight = ft.Container(content=ft.Column(controls=[indSeatsA8, indSeatsB8, indSeatsC8, indSeatsD8, indSeatsE8, indSeatsF8]))

    BlockTwoRow = ft.Container(content=ft.Row(controls=[ColumnFive, ColumnSix, ColumnSeven, ColumnEight], spacing = 4))

#Block Three

#Column of seats 9 
    indSeatsA9 = ft.Container(content=(ft.Text(value="A9", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsB9 = ft.Container(content=(ft.Text(value="B9", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsC9 = ft.Container(content=(ft.Text(value="C9", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsD9 = ft.Container(content=(ft.Text(value="D9", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsE9 = ft.Container(content=(ft.Text(value="E9", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsF9 = ft.Container(content=(ft.Text(value="F9", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    
    ColumnNine = ft.Container(content=ft.Column(controls=[indSeatsA9, indSeatsB9, indSeatsC9, indSeatsD9, indSeatsE9, indSeatsF9]))

#Column of Seats 1010
    indSeatsA10 = ft.Container(content=(ft.Text(value="A10", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsB10 = ft.Container(content=(ft.Text(value="B10", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsC10 = ft.Container(content=(ft.Text(value="C10", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsD10 = ft.Container(content=(ft.Text(value="D10", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsE10 = ft.Container(content=(ft.Text(value="E10", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsF10 = ft.Container(content=(ft.Text(value="F10", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    
    ColumnTen = ft.Container(content=ft.Column(controls=[indSeatsA10, indSeatsB10, indSeatsC10, indSeatsD10, indSeatsE10, indSeatsF10]))

#Column of seats 1111
    indSeatsA11 = ft.Container(content=(ft.Text(value="A11", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsB11 = ft.Container(content=(ft.Text(value="B11", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsC11 = ft.Container(content=(ft.Text(value="C11", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsD11 = ft.Container(content=(ft.Text(value="D11", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsE11 = ft.Container(content=(ft.Text(value="E11", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsF11 = ft.Container(content=(ft.Text(value="F11", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    
    ColumnEleven = ft.Container(content=ft.Column(controls=[indSeatsA11,indSeatsB11, indSeatsC11, indSeatsD11, indSeatsE11, indSeatsF11]))

#Column of seats 1212,
    indSeatsA12 = ft.Container(content=(ft.Text(value="A12", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsB12 = ft.Container(content=(ft.Text(value="B12", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsC12 = ft.Container(content=(ft.Text(value="C12", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsD12 = ft.Container(content=(ft.Text(value="D12", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsE12 = ft.Container(content=(ft.Text(value="E12", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    indSeatsF12 = ft.Container(content=(ft.Text(value="F12", text_align=ft.TextAlign.CENTER, weight=5)), 
                            height = 30, 
                            width = 30, 
                            bgcolor=ft.colors.GREY_400,
                            border_radius= 3,
                            on_click=SelectSeats)
    
    ColumnTwelve = ft.Container(content=ft.Column(controls=[indSeatsA12, indSeatsB12, indSeatsC12, indSeatsD12, indSeatsE12, indSeatsF12,]))
    BlockThreeRow = ft.Container(content=ft.Row(controls=[ColumnNine, ColumnTen, ColumnEleven, ColumnTwelve], spacing = 4))
    MainSeatingRow = ft.Container(content=ft.Row(controls=[BlockOneRow,BlockTwoRow, BlockThreeRow], 
                                                spacing=30, 
                                                alignment=ft.MainAxisAlignment.CENTER))
    space = ft.Container(content=None, height = 10)
    ScreenContainer = ft.Container(content=ft.Text(value="SCREEN", 
                                                size=20, 
                                                text_align=ft.TextAlign.CENTER, 
                                                color=ft.Colors.WHITE), 
                                height=30, 
                                width= 200, 
                                bgcolor=ft.Colors.GREY_800, 
                                border_radius=5, )
    WholeThing = ft.Container(content=ft.Column([space,ScreenContainer, MainSeatingRow],
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ),bgcolor="#c2241f", 
                            width= 490, 
                            height= 300, 
                            border_radius= 7)
    
    
    sub2nd= ft.Stack(
        expand=True,
        controls=[

            #Generals
            ft.Container(
            expand=True,
            image=ft.DecorationImage(
                src="lBG.png",
                fit=ft.ImageFit.COVER,
                scale=1.2
            )
        ),
            Ball,
            ChosenMovie,
            ChosenMovieTitle,
            DescriptionText,
            MovieDescription,
            MovLanguageText,
            MovLanguage,
            AvailableScreenings,
            Screenings1,
            Screenings2,
            BackButton0
            ]

    )



    #3rd page


    rdStack= ft.Stack(
        expand=True,
        controls=[

            #Generals
            ft.Container(
            expand=True,
            image=ft.DecorationImage(
                src="lBG.png",
                fit=ft.ImageFit.COVER,
                scale=1.2
            )
        ),
            MainYellow1,
            MainWhite1,
            HomePage,
            Ball,
        
            
        ]

    )




    #Page View Controls

    def route_change (e: RouteChangeEvent) -> None:
        page.views.clear()
        
        page.views.append(
            View(
                route='/',
                controls=[MainStack
                ],
                vertical_alignment= MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER
            )
            
        )
        page.update()

        #Store
        if page.route == '/catalog':
            page.views.append(
            View(
                route='/catalog',
                controls=[
                    
                    ndStack,

                ],
                vertical_alignment= MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26
            )
        )
            page.update()

        if page.route == '/incoming':
            page.views.append(
            View(
                route='/incoming',
                controls=[
                    
                rdStack

                ],
                vertical_alignment= MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26
            )
        )
            
        if page.route == '/catalog/ChooseMoviePage':
            page.views.append(
            View(
                route='/catalog/ChooseMoviePage',
                controls=[sub2nd
                    
                 

                ],
                vertical_alignment= MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26
            )
        )
            page.update()

    def view_pop(e: ViewPopEvent) -> None:      
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)
        page.update()
    
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == '__main__':
    ft.app(target=main)