import flet as ft
import requests 

def main(page: ft.Page):

    page.window.full_screen = True
    #page.theme = ft.Theme(font_family="Main")
    page.title= "World Of Cinema"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.bgcolor = "#ffffff"
    page.expand=True
    page.update()

    MainStack = ft.Stack(
        width=1800, 
        height=750,
        controls=[ft.Image(
            src="BG.png",
            width=1800,
            height=750)])
    
    page.add(MainStack)
    page.update()

ft.run(main, assets_dir="assets")    
