import flet as ft
import flet_easy as fs
import utils

exit = fs.AddPagesy(
    route_prefix="/",
)

# We add a new 'exit' page
@exit.page(route="/exit", title="Exit and Close Application")
def exit_page(data: fs.Datasy):
    page = data.page
    view = data.view

    return ft.View(
        controls=[
            ft.Text("Are you sure you want to close the application now?", style=ft.TextStyle(size=16, color=ft.Colors.RED_500)),
            ft.FilledButton(
                text="Yes! Close Application Now",
                on_click=shutdown_handler,
                bgcolor=ft.Colors.RED_500,
                color=ft.Colors.WHITE,
            ),
            ft.FilledButton(
                text="No! Return to Home Page",
                on_click=data.go("/home"),
                bgcolor=ft.Colors.GREEN_500,
                color=ft.Colors.WHITE,
            ),
        ],
        vertical_alignment="center",
        horizontal_alignment="center",
        appbar=view.appbar,
    )

# Alternative hard shutdown method
import os   
def shutdown_handler(e):
    # Optional: show a message or log before shutdown
    e.page.controls.clear()
    e.page.add(ft.Text("App is shutting down. Please close this browser tab."))
    e.page.update()
    # Give the UI a brief moment to update/display the message
    import time
    time.sleep(1)
    os._exit(0)  # Hard termination

