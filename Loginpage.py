import flet as ft

registrations = []


def login(page: ft.Page):
    page.bgcolor = "#000000"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    name = ft.TextField(label="Name", width=300)
    user_id = ft.TextField(label="ID", width=300)

    def save(e):
        registrations.append(user_id.value)
        registrations.append(name.value)
        name.value = ""
        user_id.value = ""
        print(registrations)
        page.update()

    page.add(name, user_id, ft.ElevatedButton("Save", on_click=save))


