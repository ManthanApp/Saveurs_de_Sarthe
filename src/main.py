import flet as ft
from flet_model import Model, route
from classes.mainClass import *

def main(page: ft.Page):
    page.title = "Saveurs de Sarthe"
    page.go('/home')
ft.app(target=main)
