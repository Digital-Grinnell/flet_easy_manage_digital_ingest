import flet as ft
import flet_easy as fs

show_data = fs.AddPagesy(
    route_prefix="/",
)

# We add a new 'show_data' page
@show_data.page(route="/show_data", title="Show Shared Data")
def show_data_page(data: fs.Datasy):
    page = data.page
    view = data.view

    dicts_display = ""

    for key in page.session.get_keys():
        print(f"session['{key}']: {page.session.get(key)}")
        dicts_display += f"session['{key}']: {page.session.get(key)}\n"
    

    return ft.View(
        controls=[
            ft.Text(f"session keys: {page.session.get_keys()}", style=ft.TextStyle(size=16, color=ft.Colors.GREEN_500)),
            ft.Text(dicts_display, style=ft.TextStyle(size=16, color=ft.Colors.BLUE_500)),
            ft.ElevatedButton("Home", on_click=data.go("/home")),
        ],
        vertical_alignment="center",
        horizontal_alignment="center",
        appbar=view.appbar,
    )
