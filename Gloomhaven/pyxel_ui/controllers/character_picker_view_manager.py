import pyxel

from pyxel_ui.constants import (
    BITS,
    FONT_PATH,
)
from pyxel_ui.models.font import PixelFont
from pyxel_ui.views.sprite import SpriteManager
from pyxel_ui.models import view_section as view


class CharacterPickerViewManager:

    def __init__(self, pyxel_width, pyxel_height):
        self.sprite_manager = SpriteManager()
        self.font = PixelFont(pyxel, f"../{FONT_PATH}")
        self.canvas_width = pyxel_width
        self.canvas_height = pyxel_height

        self.character_picker = view.CharacterPickerView(
            self.font, [0, 0], [self.canvas_width, self.canvas_height]
        )

    def draw(self):
        self.character_picker.draw()

    def handle_btn_press(self, btn):
        if btn == pyxel.KEY_RIGHT:
            self.character_picker.go_to_next_page()
        elif btn == pyxel.KEY_LEFT:
            self.character_picker.go_to_prev_page()

    def clear_screen(self):
        self.character_picker.clear_bounds()
