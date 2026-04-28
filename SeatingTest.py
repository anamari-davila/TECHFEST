import flet as ft

SelectedSeats = []
def Wholething(page: ft.Page):

    SelectedSeats = []
    limit = 5
    def SelectSeats(e):
        global SelectedSeats

        seat = e.control

        seat_name = seat.content.value

        if seat_name not in SelectedSeats and len(SelectedSeats) !=limit:
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
    
    ColumnOne = ft.Container(content=ft.Column(controls=[indSeatsA1, indSeatsB1, indSeatsC1, indSeatsD1, indSeatsE1, indSeatsF1], spacing=15))

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
    
    ColumnTwo = ft.Container(content=ft.Column(controls=[indSeatsA2, indSeatsB2, indSeatsC2, indSeatsD2, indSeatsE2, indSeatsF2], spacing=15))

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
    
    ColumnThree = ft.Container(content=ft.Column(controls=[indSeatsA3, indSeatsB3, indSeatsC3, indSeatsD3, indSeatsE3, indSeatsF3], spacing=15))

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
    
    ColumnFour = ft.Container(content=ft.Column(controls=[indSeatsA4, indSeatsB4, indSeatsC4, indSeatsD4, indSeatsE4, indSeatsF4], spacing=15))

    BlockOneRow = ft.Container(content=ft.Row(controls=[ColumnOne, ColumnTwo, ColumnThree, ColumnFour], spacing = 6))

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
    
    ColumnFive = ft.Container(content=ft.Column(controls=[indSeatsA5, indSeatsB5, indSeatsC5, indSeatsD5, indSeatsE5, indSeatsF5], spacing=15))

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
    
    ColumnSix = ft.Container(content=ft.Column(controls=[indSeatsA6, indSeatsB6, indSeatsC6, indSeatsD6, indSeatsE6, indSeatsF6], spacing=15))

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
    
    ColumnSeven = ft.Container(content=ft.Column(controls=[indSeatsA7, indSeatsB7, indSeatsC7, indSeatsD7, indSeatsE7, indSeatsF7], spacing=15))

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
    
    ColumnEight = ft.Container(content=ft.Column(controls=[indSeatsA8, indSeatsB8, indSeatsC8, indSeatsD8, indSeatsE8, indSeatsF8], spacing=15))

    BlockTwoRow = ft.Container(content=ft.Row(controls=[ColumnFive, ColumnSix, ColumnSeven, ColumnEight], spacing = 6))

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
    
    ColumnNine = ft.Container(content=ft.Column(controls=[indSeatsA9, indSeatsB9, indSeatsC9, indSeatsD9, indSeatsE9, indSeatsF9], spacing=15))

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
    
    ColumnTen = ft.Container(content=ft.Column(controls=[indSeatsA10, indSeatsB10, indSeatsC10, indSeatsD10, indSeatsE10, indSeatsF10], spacing=15))

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
    
    ColumnEleven = ft.Container(content=ft.Column(controls=[indSeatsA11,indSeatsB11, indSeatsC11, indSeatsD11, indSeatsE11, indSeatsF11], spacing=15))

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
    
    ColumnTwelve = ft.Container(content=ft.Column(controls=[indSeatsA12, indSeatsB12, indSeatsC12, indSeatsD12, indSeatsE12, indSeatsF12,], spacing=15))

    BlockThreeRow = ft.Container(content=ft.Row(controls=[ColumnNine, ColumnTen, ColumnEleven, ColumnTwelve], spacing = 6))

    MainSeatingRow = ft.Container(content=ft.Row(controls=[BlockOneRow,BlockTwoRow, BlockThreeRow], 
                                                spacing=30, 
                                                alignment=ft.MainAxisAlignment.CENTER))
    
    space = ft.Container(content=None, height = 10)

    ScreenContainer = ft.Container(content=ft.Text(value="SCREEN", 
                                                size=16, 
                                                text_align=ft.TextAlign.CENTER, 
                                                color=ft.Colors.WHITE,), 
                                height=25, 
                                width= 375,
                                
                                bgcolor=ft.Colors.GREY_700, 
                                border_radius=2, )

    WholeThing = ft.Container(content=ft.Column([ScreenContainer, MainSeatingRow],
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            , spacing=40),bgcolor="#c2241f", 
                            width= 560, 
                            height= 360, 
                            border_radius= 7,padding=0)

    return WholeThing