# FilePicker does NOT work in macOS w/ Flet version 0.28.3 due to permissions/security, so we need to run 
# it as a browser app, OR degrade to Flet 0.28.2 which does work in macOS.  See https://github.com/flet-dev/flet/issues/5334#issuecomment-3065024264
#
# Unfortunately, Flet-Easy does not work properly in Flet 0.28.2 as navigation is broken,
# so we need to run this as a browser app for now in macOS using Flet 0.28.3 or later.

import flet as ft
import flet_easy as fs

picker = fs.AddPagesy(
    route_prefix="/",
)


# We add a third page
@picker.page(route="/picker", title="Picker")
def picker_page(data: fs.Datasy):

    # Standard Flet-Easy page stuff
    page = data.page
    view = data.view

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
        # logger = page.session.get("logger")
        # status_container = page.session.get("status_container")
        # result_text = status_container.result_text

        # if e.files:
        #     num_files = len(e.files)
        #     directory = os.path.dirname(e.files[0].path)
        #     result_text.value = f"{num_files} files selected from {directory}."
            
        #     # Clear the previous selection
        #     page.session.set("selected_object_paths", [ ])
        #     objects = page.session.get("selected_object_paths")
            
        #     # Loop through the selected files and log their paths. Append each path to page.session[selected_object_paths]
        #     for file in e.files:
        #         logger.info(f"Selected file: {file.name} (Path: {file.path})")  
        #         status_container.result_text.value += f"\n- {file.name}"  
        #         objects.append(file.path)
        #         page.update( )

        #     utils.show_message(page, f"{num_files} files selected from {directory}.")
        #     page.session.set("selected_object_paths", objects)
        #     page.update( )
        #     # process_files(page, directory, e.files)  # Pass the list of files to the processing function

        # else:
        #     status_container.result_text.value = "Selection cancelled."
        #     utils.show_message(page, "File selection was cancelled.", is_error=True)
        #     page.session.set

        page.update( )

    # Create an instance of the FilePicker control
    file_picker = ft.FilePicker(on_result=pick_files_result)

    # Add the FilePicker control to the page
    page.overlay.append(file_picker)    

    def plus_click(e):
        open_file_picker(e)
        page.update()

    return ft.View(
        controls=[
            ft.Text("Picker page", size=30),
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
