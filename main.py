import flet as ft
import requests 
import asyncio

def main(page: ft.Page):

    #fonts
    page.fonts = {
        "Main": "Comucan_PERSONAL_USE_ONLY.otf"
    }

    page.window.full_screen = False
    page.theme = ft.Theme(font_family="Main")
    page.title= "World Of Cinema"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.bgcolor = "#000000"
    page.expand=True
    page.update()

    async def bola1():
        Ball.opacity=0
        page.update()
        await asyncio.sleep(.7)
        Ball.left=-630.9
        Ball.top = 390.6
        Ball.scale=1
        Ball.opacity=1
        page.update()

    async def bola2():
        Ball.opacity=0
        page.update()
        await asyncio.sleep(.7)
        Ball.left=240.9
        Ball.top = 200.6
        Ball.scale=1
        Ball.opacity=1
        page.update()

    async def bola3():
        Ball.opacity=0
        page.update()
        await asyncio.sleep(0.7)
        Ball.left= 1600.9
        Ball.top= -100
        Ball.scale=2.5
        Ball.opacity=1
        page.update()


    Background= ft.Image(
                src="lBG.png", fit=ft.Image.fit, scale= 1.2)
    Ball = ft.Image(src="Ball.png", top=390.6, left=-630.9, animate_opacity=300)


    l1= ft.Button(content="1st", on_click=bola1, top=100)
    l2= ft.Button(content="2nd", on_click=bola2,top=200)
    l3= ft.Button(content="3rd", on_click=bola3, top= 300)

    MainStack = ft.Stack(
        expand=True,
        controls=[Background,Ball, l1, l2, l3])
    
    
    
    page.add(MainStack)
    page.update()

ft.run(main, assets_dir="assets")    
