from typing import Optional

import flet as ft
import win32gui

from states import SimulatedUniverse


class Page(ft.Page):
    su: Optional[SimulatedUniverse]
    debug_mode: int
    show_map_mode: bool
    speed_mode: int
    force_update: bool


def init_page(page: Page):
    page.su = None
    page.debug_mode = 0
    page.show_map_mode = False
    page.speed_mode = 0
    page.force_update = False


def show_snack_bar(page, text, color, selectable=False):
    return page.show_snack_bar(
        ft.SnackBar(
            open=True,
            content=ft.Text(text, selectable=selectable),
            bgcolor=color,
        )
    )


def cleanup():
    try:
        win32gui.ShowWindow(mynd, 1)
    except:
        pass


def enum_windows_callback(hwnd, hwnds, f):
    class_name = win32gui.GetClassName(hwnd)
    name = win32gui.GetWindowText(hwnd)
    try:
        if (
            class_name == "ConsoleWindowClass"
            and win32gui.IsWindowVisible(hwnd)
            and f(name)
        ):
            hwnds.append(hwnd)
    except:
        pass
    return True


def list_handles(f=lambda n:"gui" in n[-7:]):
    hwnds = []
    win32gui.EnumWindows(enum_windows_callback, hwnds, f)
    hwnds.append(0)
    return hwnds


mynd = list_handles()[0]