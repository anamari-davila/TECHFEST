import flet as ft
import requests 

def main(page: ft.Page):

    page.window.full_screen = False
    #page.theme = ft.Theme(font_family="Main")
    page.title= "World Of Cinema"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.bgcolor = "#000000"
    page.expand=True
    page.update()

    
    Background= ft.Image(
                src="lBG.png", fit=ft.Image.fit, scale= 1.2)
    Ball = ft.Image(src="Ball.png", top=478.6, left=-730.9, expand=False)


    MainStack = ft.Stack(
        expand=True,
        controls=[Background,Ball])
    
    
    
    page.add(MainStack)
    page.update()

ft.run(main, assets_dir="assets")    
