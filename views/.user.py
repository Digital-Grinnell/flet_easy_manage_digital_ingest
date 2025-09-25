# views/user.py
# This file is for defining user-related pages using flet_easy and flet.  
# From https://daxexs.github.io/flet-easy/latest/add-pages/in-automatic/#app-structure

import flet_easy as fs
import flet as ft

users = fs.AddPagesy(
    route_prefix='/user'
)

# -> Urls to be created:
# * '/user/task'
# * '/user/information'

@users.page('/task', title='Task')
def task_page(data: fs.Datasy):

    return ft.View(
        controls=[
            ft.Text('Task'),
        ],
        vertical_alignment="center",
        horizontal_alignment="center"

    )

@users.page('/information', title='Information')
async def information_page(data: fs.Datasy):

    return ft.View(
        controls=[
            ft.Text('Information'),
        ],
        vertical_alignment="center",
        horizontal_alignment="center"

    )