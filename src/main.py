import flet as ft
import sys
import os

# Ensure 'core' folder is found by adding the root directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.logic_selector import RandomSelector

# --- Flet 0.85.0 API aliases ---
# Icons: ft.icons.Icons.X  (ft.icons.X no longer works)
# Colors: ft.Colors.X      (ft.colors.X no longer works, note capital C)
# Tabs:   ft.Tabs(content=ft.Column([ft.TabBar(...), ft.TabBarView(...)]), length=N)
# Button: ft.Button(...)   (ft.ElevatedButton deprecated since 0.80.0)
Icons = ft.icons.Icons
Colors = ft.Colors


def main(page: ft.Page):
    page.title = "RandomPick Pro"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.scroll = ft.ScrollMode.ADAPTIVE

    selector = RandomSelector()

    # --- SHARED UI: Results Card Helper ---
    def get_result_card(title: str, subtitle: str|None = None, icon=Icons.STAR):
        return ft.Card(
            content=ft.Container(
                content=ft.ListTile(
                    leading=ft.Icon(icon, color=Colors.CYAN),
                    title=ft.Text(title, weight=ft.FontWeight.BOLD),
                    subtitle=ft.Text(subtitle) if subtitle else None,
                ),
                padding=5,
            )
        )

    # --- TAB 1: SIMPLE SELECTION ---
    sel_input = ft.TextField(
        label="Items (e.g. Apple, Orange, Banana)",
        multiline=True,
        min_lines=3,
    )
    sel_count = ft.TextField(label="Pick how many?", value="1", width=150)
    sel_results = ft.Column(spacing=10)

    def do_selection(e):
        sel_results.controls.clear()
        try:
            count = int(sel_count.value)
            results = selector.select_items(sel_input.value, count)
            sel_results.controls.append(
                ft.Text("Selected Items:", size=18, weight=ft.FontWeight.BOLD)
            )
            for item in results:
                sel_results.controls.append(get_result_card(item, icon=Icons.STAR))
        except ValueError as ex:
            sel_results.controls.append(ft.Text(f"⚠️ {ex}", color=Colors.RED_400))
        except Exception as ex:
            sel_results.controls.append(
                ft.Text(f"⚠️ Unexpected error: {ex}", color=Colors.RED_400)
            )
        page.update()

    selection_view = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "Enter a comma-separated list and pick N random items from it.",
                    italic=True,
                    color=Colors.GREY_400,
                ),
                sel_input,
                sel_count,
                ft.Button(
                    "Pick Randomly",
                    icon=Icons.SHUFFLE,
                    on_click=do_selection,
                ),
                sel_results,
            ],
            spacing=20,
        ),
        padding=20,
    )

    # --- TAB 2: RANDOM MAPPING ---
    map_candidates = ft.TextField(
        label="List A — e.g. People, Teams, Slots",
        multiline=True,
        min_lines=3,
    )
    map_targets = ft.TextField(
        label="List B — e.g. Tasks, Prizes, Roles",
        multiline=True,
        min_lines=3,
    )
    map_results = ft.Column(spacing=10)

    def do_mapping(e):
        map_results.controls.clear()
        try:
            mappings, c_len, t_len = selector.assign_mappings(
                map_candidates.value, map_targets.value
            )
            if c_len != t_len:
                map_results.controls.append(
                    ft.Text(
                        f"Note: {c_len} items in List A, {t_len} in List B — "
                        f"only {min(c_len, t_len)} pairs generated.",
                        color=Colors.ORANGE_400,
                        italic=True,
                    )
                )
            map_results.controls.append(
                ft.Text("Assignments:", size=18, weight=ft.FontWeight.BOLD)
            )
            for c, t in mappings:
                map_results.controls.append(
                    get_result_card(c, subtitle=f"→  {t}", icon=Icons.LINK)
                )
        except ValueError as ex:
            map_results.controls.append(ft.Text(f"⚠️ {ex}", color=Colors.RED_400))
        except Exception as ex:
            map_results.controls.append(
                ft.Text(f"⚠️ Unexpected error: {ex}", color=Colors.RED_400)
            )
        page.update()

    mapping_view = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "Randomly pair every item in List A with an item from List B.",
                    italic=True,
                    color=Colors.GREY_400,
                ),
                map_candidates,
                map_targets,
                ft.Button(
                    "Generate Mapping",
                    icon=Icons.COMPARE_ARROWS,
                    on_click=do_mapping,
                ),
                map_results,
            ],
            spacing=20,
        ),
        padding=20,
    )

    # --- TABS (Flet 0.85.0 pattern) ---
    # Tabs is now a controller that wraps a Column of TabBar + TabBarView.
    # Tab() only defines the header (label/icon); content lives in TabBarView.
    tabs_container = ft.Tabs(
        length=2,
        selected_index=0,
        animation_duration=300,
        expand=True,
        content=ft.Column(
            expand=True,
            controls=[
                ft.TabBar(
                    tabs=[
                        ft.Tab(
                            label="Selection",
                            icon=Icons.ADS_CLICK,
                        ),
                        ft.Tab(
                            label="Mapping",
                            icon=Icons.COMPARE_ARROWS,
                        ),
                    ]
                ),
                ft.TabBarView(
                    expand=True,
                    controls=[
                        selection_view,
                        mapping_view,
                    ],
                ),
            ],
        ),
    )

    # --- HEADER ---
    header = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "🎯 RandomPick Pro",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "Unbiased random selection & assignment",
                    size=14,
                    color=Colors.GREY_400,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=4,
        ),
        alignment=ft.alignment.Alignment.CENTER,
        margin=ft.margin.Margin.only(bottom=10),
    )

    page.add(
        header,
        ft.Divider(),
        tabs_container,
    )


if __name__ == "__main__":
    ft.run(main=main)