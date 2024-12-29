# -*- coding: utf-8 -*-
import flet as ft


class App(object):

    def __init__(self, page: ft.Page):
        self.page = page
        self.app = {}

    def run(self):
        self.page.title = 'Flet Example'
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.update()