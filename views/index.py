import flet as ft
import flet_easy as fs
import my_logger

index = fs.AddPagesy()

# We add a page
@index.page(route="/home", title="Home")
def index_page(data: fs.Datasy):
    view = data.view
    page = data.page

    # Read markdown content from a file
    with open("_data/home.md", "r", encoding="utf-8") as file:
        markdown_text = file.read( )
    
    # Create a Markdown widget with the content
    md_widget = ft.Markdown(markdown_text, 
        md_style_sheet=ft.MarkdownStyleSheet(blockquote_text_style=ft.TextStyle(bgcolor=ft.Colors.PURPLE_50, color=ft.Colors.BLACK, size=16, weight=ft.FontWeight.BOLD),
                                             p_text_style=ft.TextStyle(color=ft.Colors.BLACK, size=16, weight=ft.FontWeight.NORMAL),
                                             code_text_style=ft.TextStyle(color=ft.Colors.ORANGE_400, size=16, weight=ft.FontWeight.BOLD),
        )
    )

    page.session.set("last_status", "At Home page") 

    # If we don't yet have a logger in the session, we create one and store it there
    if not page.session.get("logger"):
        page.session.set("last_status", "Initialized the logger") 
        logger = my_logger.init_logger( )
        logger.info(f"Initialized logging for {__name__}")
        page.session.set("logger", logger)

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
