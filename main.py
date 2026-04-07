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


    

    MainStack = ft.Stack(
        width=1920, 
        height=1080,
        controls=[ft.Image(
                src="lBG.jpg")])
    
    
    
    page.add(MainStack)
    page.update()

ft.run(main, assets_dir="assets")    
