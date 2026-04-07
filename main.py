import flet as ft
import requests 

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

    #Background Image
    Background= ft.Image(
                src="lBG.png", fit=ft.Image.fit, scale= 1.2)
    
    #Ball For Backgroun
    Ball = ft.Image(src="Ball.png", top=478.6, left=-730.9, expand=False)

    #Main Text
    TitlePT1 = ft.Text(value = "WORLD OF",color= '#d5b586', size=84, left = 194)
    TittlePT2 = ft.Text(value= "CINEMA", color = ft.Colors.WHITE, size = 300)


    MainStack = ft.Stack(
        expand=True,
        controls=[Background,Ball, TitlePT1, TittlePT2])
    
    
    
    page.add(MainStack)
    page.update()

ft.run(main, assets_dir="assets")    
