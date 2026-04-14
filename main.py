import flet as ft
import requests 
import asyncio

def main(page: ft.Page):

    
    
    #fonts
    page.fonts = {
        "Main": "Comucan_PERSONAL_USE_ONLY.otf",

        "YellowMain": "TtNormsExtraBlack.otf",
        "Whitemain": "BricolageBoldened.ttf"
    }

    #Page Setup

    page.window.full_screen = False
    # page.theme = ft.Theme(font_family="Main")
    page.title= "World Of Cinema"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.bgcolor = "#000000"
    page.expand=True
    page.update()

    #Balls functions

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
        font_family="YellowMain", 
        color="#d5b586", 
        top=100, 
        left=315, 
        size=87.5,
        style=ft.TextStyle(letter_spacing=0)
        )
    
    MainWhite= ft.Text(
        value= "CINEMA", 
        font_family= "Whitemain", 
        top= 80, 
        left= 40, 
        size=376,
        style=ft.TextStyle(letter_spacing=-5)
        )
    
    #Popcorn image and icons

    PopCorn = ft.Image(
        src="PopCorn.png",
        top=165,
        left=-545,
        expand=False,
        scale=0.72,
        )

    # l1= ft.Button(content="1st", on_click=bola1, top=100)
    # l2= ft.Button(content="2nd", on_click=bola2,top=200)
    # l3= ft.Button(content="3rd", on_click=bola3, top= 300)



    #Main Page

    MainStack = ft.Stack(
        expand=True,
        controls=[Background, Ball, MainYellow, MainWhite, PopCorn]
        )
    
    
    
    page.add(MainStack)
    page.update()

ft.run(main, assets_dir="assets")    
