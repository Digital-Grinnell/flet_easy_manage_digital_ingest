import flet as ft
import flet_easy as fs

mode = fs.AddPagesy(
    route_prefix="/",
)

# Define the change event handler for the RadioGroup
def mode_radio_group_changed(e):
    # print(e)
    logger = e.page.session.get("logger")
    mode = e.control.value
    e.page.session.set("mode", mode)
    msg = f"Selected processing mode: '{mode}'"
    # print(msg)
    e.page.session.set("last_status", msg)
    logger.info(msg)

    # utils.show_message(page, msg, False)
        
    # Add logic here to handle the selection, for example:
    # if e.control.value == "Alma":
    #     ...
    # elif e.control.value == "CollectionBuilder":
    #     ...


# We add a new 'mode' page
@mode.page(route="/mode", title="Mode Selection")
def mode_page(data: fs.Datasy):
    page = data.page
    view = data.view
    logger = page.session.get("logger")

    # Create the RadioGroup with the two radio buttons
    mode_options = ft.RadioGroup(
        content=ft.Column(
            controls=[
                ft.Radio(value="Alma", label="Alma"),
                ft.Radio(value="CollectionBuilder", label="CollectionBuilder"),
            ],
            expand=True,
            spacing=0
        ),
        on_change = mode_radio_group_changed,
    )

    return ft.View(
        controls=[
            ft.Text("Mode Selection", size=30),
            ft.Markdown("Select the processing mode for digital ingest:"),
            ft.Divider(height=20, color=ft.Colors.RED_400),
            ft.Row([mode_options,], alignment=ft.MainAxisAlignment.CENTER)
        ],
        vertical_alignment="center",
        horizontal_alignment="center",
        appbar=view.appbar,
    )
