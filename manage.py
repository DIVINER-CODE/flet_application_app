# -*- coding: utf-8 -*-
import flet as ft
from src.app import App


def main(page: ft.Page):
    win = App(page)
    win.run()


ft.app(target=main)