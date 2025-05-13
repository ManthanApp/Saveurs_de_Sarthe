import flet as ft
from flet_model import Model, route

class SideBar(ft.NavigationRail):
    def __init__(self, page):
        self.page = page
        super().__init__(
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.HOME_OUTLINED,
                    selected_icon=ft.icons.HOME,
                    label="Accueil",
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.BOOKMARK_OUTLINED,
                    selected_icon=ft.icons.BOOKMARK,
                    label="Réserver",
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.CONTACT_PAGE_OUTLINED,
                    selected_icon=ft.icons.CONTACT_PAGE,
                    label="Nous contacter",
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.HELP_OUTLINED,
                    selected_icon=ft.icons.HELP,
                    label="Aide",
                ),
            ],
            selected_index=0,
            on_change=self.handle_change,
            expand=True,
            bgcolor="#F2C57C",
            width=150,
        )

    def handle_change(self, e):
        if self.selected_index == 0:
            self.page.go("/home")
        elif self.selected_index == 1:
            self.page.go("/book")
        elif self.selected_index == 2:
            self.page.go("/contact")
        elif self.selected_index == 3:
            self.page.go("/help")

