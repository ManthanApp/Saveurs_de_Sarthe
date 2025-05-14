import flet as ft
from flet import *

from flet_navigator import PublicFletNavigator, PageData, route


@route('/')
def main(pg: PageData) -> None:
    pg.add(Text('Hello World!'))

    pg.add(FilledButton('Navigate to the second page!', on_click=lambda _: pg.navigate('second')))

@route
def second(pg: PageData) -> None:
    pg.add(Text('I am the second page!'))

    pg.add(FilledButton('Return to the homepage!', on_click=lambda _: pg.navigate_homepage()))

app(lambda page: PublicFletNavigator(page).render(page))