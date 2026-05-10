import flet as ft
from core.logic_selector import RandomSelector # HINT: Ensure path is correct!

def main(page: ft.Page):
    page.title = "RandomPick Pro"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Initialize logic
    selector = RandomSelector()
    
    # UI Elements
    options_input = ft.TextField(label="Enter options (comma separated)", width=400)
    count_input = ft.TextField(label="How many to pick?", width=200, value="1")
    result_text = ft.Text(size=30, color="cyan", weight="bold")
    
    def pick_clicked(e):
        # BUG 1: They need to add the options from the input to the selector first!
        # BUG 2: This function runs but doesn't show anything on screen... 
        # (Hint: page.update() is missing!)
        
        try:
            count = int(count_input.value)
            # Connecting to backend logic
            picked = selector.select_items(count)
            result_text.value = f"Selected: {', '.join(picked)}"
            print(f"DEBUG: Picked {picked}") # This shows in console but not app
        except Exception as ex:
            result_text.value = f"Error: {ex}"

    # BUG 3: The button is created but it's not connected to the function correctly
    pick_button = ft.ElevatedButton("Pick Randomly", on_click=None) 

    # Building the layout
    page.add(
        ft.Column(
            [
                ft.Text("🎯 RandomPick", size=40, weight="bold"),
                options_input,
                count_input,
                pick_button,
                result_text,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


if __name__ == "__main__":
    ft.app(target=main)