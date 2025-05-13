import flet as ft
from flet_model import Model, route

@route("/home")
class HomeModel(Model):

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.page.bgcolor = "#C7DBE6"  # Couleur de fond principale
        self.page.appbar = self.appbar
        self.page.controls.append(self.navigation_rail)
        self.page.update()

    def handle_change(self, e):
        if self.navigation_rail.selected_index == 0:
            self.page.go("/home")
        elif self.navigation_rail.selected_index == 1:
            self.page.go("/book")
        elif self.navigation_rail.selected_index == 2:
            self.page.go("/contact")
        elif self.navigation_rail.selected_index == 3:
            self.page.go("/help")

    appbar = ft.CupertinoAppBar(
        leading=ft.Icon(ft.Icons.FOOD_BANK),
        bgcolor="#A9DEF9",
        trailing=ft.Icon(ft.Icons.EMOJI_FOOD_BEVERAGE),
        middle=ft.Text("Saveurs de Sarthe"),
    )

    navigation_rail = ft.NavigationRail(
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
        on_change=lambda e: None,  # Remplacez par `self.handle_change` si nécessaire
        expand=True,
        bgcolor="#F2C57C",
        width=150,
    )