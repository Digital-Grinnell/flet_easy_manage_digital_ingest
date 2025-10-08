import flet as ft
import flet_easy as fs

index = fs.AddPagesy()

# We add a page
@index.page(route="/home", title="Home")
def index_page(data: fs.Datasy):
    view = data.view

    # Read markdown content from a file
    with open("_data/home.md", "r", encoding="utf-8") as file:
        markdown_text = file.read()
    
    # Create a Markdown widget with the content
    md_widget = ft.Markdown(markdown_text, 
                    code_style_sheet=ft.MarkdownStyleSheet(
                        code_text_style=ft.TextStyle(color=ft.Colors.GREEN_400)
        )
    )

    
    return ft.View(
        controls=[
            ft.Text("Flet-Easy: Manage Digital Ingest", size=35),
            ft.Markdown("A Flet-Easy Python app for managing Grinnell College ingest of digital objects to Alma or CollectionBuilder"),
            ft.Divider(height=20, color=ft.Colors.RED_400),
            md_widget,
            # ft.FilledButton("Go to Counter", on_click=data.go("/counter/test/0")),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        drawer=view.appbar,
    )
