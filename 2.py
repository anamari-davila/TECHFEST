import flet as ft

def main(page: ft.Page):
    
    def open_dialog(e):
        page.open(my_dialog)
    
    def close_dialog(e):
        page.close(my_dialog)
    
    # Define your popup
    my_dialog = ft.AlertDialog(
        modal=True,  # True = user must interact with it; False = can dismiss by tapping outside
        title=ft.Text("My Custom Popup"),
        content=ft.Column(
            [
                ft.Text("Put whatever you want in here:"),
                ft.TextField(label="Name"),
                ft.Dropdown(
                    label="Pick one",
                    options=[
                        ft.dropdown.Option("Option A"),
                        ft.dropdown.Option("Option B"),
                    ],
                ),
                ft.Checkbox(label="I agree"),
            ],
            tight=True,
            height=250,
        ),
        actions=[
            ft.TextButton("Cancel", on_click=close_dialog),
            ft.TextButton("OK", on_click=close_dialog),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    
    page.views.append(
        ft.View(
            "/",
            controls=[
                ft.ElevatedButton("Open popup", on_click=open_dialog),
            ],
        )
    )
    page.update()

ft.app(main)