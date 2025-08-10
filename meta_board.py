import displayio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text.label import Label
from adafruit_display_text.scrolling_label import ScrollingLabel
from adafruit_matrixportal.matrix import Matrix
import time
from config import config

class MetaLikeBoard:
    def __init__(self):
        self.display = Matrix().display
        self.parent_group = displayio.Group(scale=1, x=0, y=3)
        
        self.heading_label = ScrollingLabel(
                config['font'],
                text="Initializing...", 
                max_characters=20, 
                scale=1,
                color=config.get("title_color", 0xFFFFFF)
        )

        self.parent_group.append(self.heading_label)

        self.fan_count = 0
        self.fan_display = Label(
            config['font'],
            text=f"{self.fan_count}",
            x=int((config["matrix_width"]/2) - ((len(str(self.fan_count)) * config["character_width"] * config["like_count_scale"] )/2)),
            y=16,
            scale = config["like_count_scale"],
            color = config.get("like_color", 0xFFFFFF)
        )

       
        self.parent_group.append(self.fan_display)

        self.display.root_group = self.parent_group

    
    def update_fan_count(self, fan_count):
        if self.fan_count != fan_count and fan_count != None:
            self.fan_count = fan_count
            self.fan_display.x=int((config["matrix_width"]/2) - ((len(str(self.fan_count)) * config["character_width"] * config["like_count_scale"] )/2))
            self.fan_display.text = str(fan_count)
            
            print("Updating fan count...")

    def update_page_name(self, name):
        if self.heading_label.text.rstrip() != name and name != None:
            print(self.heading_label.text + name, f"name {name[0]} {self.heading_label.text[0]} {name[-1]} {self.heading_label.text[-1]}", self.heading_label.text == name)
            self.heading_label.text = name

    def update_header_scrolling(self):
        self.heading_label.update()
        
    def turn_off_display(self):
        self.display.brightness = 0

    def turn_on_display(self):
        self.display.brightness = 1


