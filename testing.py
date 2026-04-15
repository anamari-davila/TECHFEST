import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment
import asyncio

def main(page: Page) -> None:
    
    page.fonts = {
        "Main": "Comucan_PERSONAL_USE_ONLY.otf",
        "TtNormsExtra": "TtNormsExtraBlack.otf",
        "TtNormsReg": "TT Norms Pro Regular.otf",
        "BricolageBold": "BricolageBoldened.ttf"
    }

    #Page Setup

    page.window.full_screen = False
    # page.theme = ft.Theme(font_family="Main")
    page.title= "World Of Cinema"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.bgcolor = "#000000"
    page.expand=True
    page.theme= ft.Theme(font_family="TtNormsReg")
    page.update()

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
        Ball.update()
        
        await asyncio.sleep(0.310)
        Ball.left=-250.9
        Ball.top = 200.6
        Ball.scale=1
        Ball.update() 

        await asyncio.sleep(0.310)
        Ball.opacity=1
        Ball.update()

    async def bola3():

        Ball.opacity=0
        Ball.update()
        
        await asyncio.sleep(0.310)
        Ball.left= 1600.9
        Ball.top= -100
        Ball.scale=2.5
        Ball.update()

        await asyncio.sleep(0.310)
        Ball.opacity=1
        Ball.update()

    def testfunc(e):
        print("hello World")

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

    #MainPageTextFields
    MainYellow= ft.Text(
        value="WORLD OF",
        font_family="TtNormsExtra", 
        color="#d5b586", 
        top=100, 
        left=300, 
        size=87.5,
        style=ft.TextStyle(letter_spacing=0)
        )
    
    MainWhite= ft.Text(
        value= "CINEMA", 
        font_family= "BricolageBold", 
        color=ft.Colors.WHITE,
        top= 80, 
        left= 55, 
        size=365,
        style=ft.TextStyle(letter_spacing=-5)
        )
    
    #MiniText
    MiniText= ft.Text(
        value="YOUR FAVORITE MOVE THEATER", 
        color="#ffffff", 
        top=485, 
        left=715    , 
        size=12,
        style=ft.TextStyle(letter_spacing=3),
    )

    #Popcorn image and icons

    PopCorn = ft.Image(
        src="PopCorn.png",
        top=165,
        left=-545,
        expand=False,
        scale=0.75,
        )
    
    MovieIcon1=ft.Image(
        src="CameraV.png",
        scale=0.6,
        top=-420,
        left= 100
        )
    
    Icon1Text = ft.Container(
    content=ft.Text(
        value="ON SCREEN RIGHT NOW",
        size=20,
        style=ft.TextStyle(letter_spacing=2),
    ),
    left=1100,
    top=70,
    on_click=lambda _: page.go('/store'))
    
   

    MovieIcon2=ft.Image(
        src="CameraV.png",
        scale=0.6,
        top=-330,
        left= 100
        )
    
    Icon2Text= ft.Container(
    content= ft.Text(
        value="UPCOMING MOVIES",
        size=20,
        style=ft.TextStyle(letter_spacing=2) 
    
        ),
        top= 160,
        left=1100,
        on_click=lambda e: testfunc(e)
    
    )



    # l1= ft.Button(content="1st", on_click=bola1, top=100)
    # l2= ft.Button(content="2nd", on_click=bola2,top=200)
    # l3= ft.Button(content="3rd", on_click=bola3, top= 300)



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
        if page.route == '/store':
            page.views.append(
            View(
                route='/store',
                controls=[
                    AppBar(title=Text('Store'), bgcolor='blue'),
                    ft.Text(value='Store', size=30),
                    ft.ElevatedButton(text='Go back', on_click=lambda _: page.go('/'))
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
