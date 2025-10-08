# FilePicker does NOT work in macOS w/ Flet version 0.28.3 due to permissions/security, so we need to run 
# it as a browser app, OR degrade to Flet 0.28.2 which does work in macOS.  See https://github.com/flet-dev/flet/issues/5334#issuecomment-3065024264
#
# Unfortunately, Flet-Easy does not work properly in Flet 0.28.2 as navigation is broken,
# so we need to run this as a browser app for now in macOS using Flet 0.28.3 or later.

import flet as ft
import flet_easy as fs
import os
from enhanced_logger import EnhancedLogger
import logging

picker = fs.AddPagesy(
    route_prefix="/",
)


# We add a new 'picker' page
@picker.page(route="/picker", title="Picker")
def picker_page(data: fs.Datasy):

    # Standard Flet-Easy page stuff
    page = data.page
    view = data.view


    def find_file(filename, search_path='.'):
        """
        Search for a file by name starting from the specified directory.
        Returns absolute path if found, otherwise None.
        """
        for root, dirs, files in os.walk(search_path):
            if filename in files:
                return root 
        return None


    # Function to open the file picker dialog
    # This is called when a valid directory option is selected in the file selection RadioGroup
    # -----------------------------------------------------------
    def open_file_picker(e):
        """
        Function to open the file picker dialog.
        """
        page = e.page
        # logger = page.session.get("logger")
        # logger.info("Opening file picker dialog...")

        file_picker.pick_files(
            allow_multiple=True,
            allowed_extensions=["jpg", "jpeg", "png", "pdf", ".tiff", "tif"],
            dialog_title="Select multiple images and/or PDF files",
            initial_directory="/Users/mark/Downloads",  # Change this to a valid directory on your system
        )

    # Callback function to handle the result of the file picker dialog
    # This function saves the selected files/paths in ft.page.session for later processing
    # -----------------------------------------------------------
    def pick_files_result(e: ft.FilePickerResultEvent):
        """
        Callback function executed when the file picker dialog is closed.
        It updates the UI and passes the selected file/paths to ft.page.session ...the processing function.
        """
        page = e.page
        logger = page.session.get("logger")
        logger.info(f"File picker result event: {e}")
        logger.info(f"Number of files selected: {len(e.files)}")
        logger.info(f"Selected files: {[file.name for file in e.files]}")
        
        num_files = len(e.files)

        if num_files > 0:
            dir1 = False

            directory = find_file(e.files[0].name, search_path='/Users')
            if directory:
                logger.info(f"First file directory found: {directory}")
            else:
                logger.warning(f"Directory for the first file not found!")

            if num_files > 1:
                dir1 = find_file(e.files[num_files-1].name, search_path='/Users')
                if dir1:
                    logger.info(f"Last file directory found: {dir1}")
                else:
                    logger.warning(f"Directory for the last file not found!")
            
            if directory != dir1:
                logger.warning(f"Warning: Selected files are from different directories: {directory} and {dir1}")   
                directory = False
            else:
                logger.info(f"All selected files are from the same directory: {directory}")
                logger.info(f"{num_files} files selected from {directory}.")
                directory = directory  # Use this directory for processing

            # Clear the previous selection
            page.session.set("selected_object_paths", [ ])
            objects = page.session.get("selected_object_paths")

            # Loop through the selected files and log their paths. Append each path to page.session[selected_object_paths]
            for file in e.files:
                logger.info(f"Selected file: {file.name} (Path: {directory})")  
                objects.append(directory + "/" + file.name)

            page.session.set("selected_object_paths", objects)
            page.update( )

            # process_files(page, directory, e.files)  # Pass the list of files to the processing function

        page.update( )

    # Create an instance of the FilePicker control
    file_picker = ft.FilePicker(on_result=pick_files_result)

    # Add the FilePicker control to the page
    page.overlay.append(file_picker)    

    # Read markdown content from a file
    with open("_data/picker.md", "r", encoding="utf-8") as file:
        markdown_text = file.read( )
    
    # Create a Markdown widget with the content
    md_widget = ft.Markdown(markdown_text, 
        md_style_sheet=ft.MarkdownStyleSheet(blockquote_text_style=ft.TextStyle(bgcolor=ft.Colors.PURPLE_50, color=ft.Colors.BLACK, size=16, weight=ft.FontWeight.BOLD),
                                             p_text_style=ft.TextStyle(color=ft.Colors.BLACK, size=16, weight=ft.FontWeight.NORMAL),
                                             code_text_style=ft.TextStyle(color=ft.Colors.ORANGE_400, size=16, weight=ft.FontWeight.BOLD),
        )
    )

    def plus_click(e):
        open_file_picker(e)
        page.update()

    return ft.View(
        controls=[
            ft.Text("File Picker page", size=30),
            ft.Divider(height=20, color=ft.Colors.RED_400),
            md_widget,
            ft.Row(
                [
                    ft.IconButton(ft.Icons.ADD, on_click=plus_click),
                ],
                alignment="center",
            ),
        ],
        vertical_alignment="center",
        horizontal_alignment="center",
        appbar=view.appbar,
    )
