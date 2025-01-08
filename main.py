from flet import *
from flet import Flashlight

def main(page: Page):
    page.title = "Flash Light"
    page.scroll = "auto"
    page.bgcolor = 'white'
    page.theme_mode = ThemeMode.LIGHT

    flashlight = Flashlight()
    page.overlay.append(flashlight)


    page.add(

        AppBar(
            title= Text('Flash Light'),
            color= 'white',
            bgcolor= colors.BLUE_300,
            actions=[
                IconButton(icons.SETTINGS,)
            ]
        ),
        Row([
            Text('\n\nFlash Light',size=30,color='black')
        ],alignment=MainAxisAlignment.CENTER),

        Row([
            Image(src="./logo.png",width=260,height=260)
        ],alignment=MainAxisAlignment.CENTER),

        Row([
            ElevatedButton(
                "ON",
                width = 100,
                icon = icons.PLAY_ARROW,
                style=ButtonStyle(
                    bgcolor=colors.BLUE_300,
                    color='white',
                    padding=15,
                    shape=ContinuousRectangleBorder(radius=100)
                ),
                on_click=lambda _: flashlight.turn_on()
            ),
            ElevatedButton(
                "OFF",
                width = 100,
                icon = icons.PLAY_DISABLED_SHARP,
                style=ButtonStyle(
                    bgcolor=colors.BLUE_300,
                    color='white',
                    padding=15,
                    shape=ContinuousRectangleBorder(radius=100)
                ),
                on_click=lambda _: flashlight.turn_off()
            ), 
        ],alignment=MainAxisAlignment.CENTER)
    )


    page.update()

app(main)
