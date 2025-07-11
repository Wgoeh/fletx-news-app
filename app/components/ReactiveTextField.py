"""
Formtextrield Component.

This component was auto-generated by fletx.

🛠️ Customization Guide:
- You can change the parent class (`ft.Container`) to inherit from any other Flet control.
  → Example: `ft.Text`, `ft.Row`, `ft.Column`, or any custom Flet widget.
- You can add or modify internal reactive attributes.
  → Example: `self.title: RxStr = rx_title`
- You can define simple or advanced bindings using the fletx decorators
"""

import flet as ft
from fletx.core import (
    RxStr, RxBool, RxDict
)
from fletx.decorators import (
    two_way_reactive
)

####
##      TWO WAY REACTIVE TEXT FIELD
####
@two_way_reactive({
    'value': 'rx_value',
    'visible': 'rx_visible',
    'disabled': 'rx_disabled'
})
class FromTextField(ft.TextField):
    """Example of two way Reactive TextField"""
    
    def __init__(
        self, 
        rx_value: RxStr = RxStr(""), 
        rx_visible: RxBool = RxBool(True),
        rx_disabled: RxBool = RxBool(False),
        **kwargs
    ):
        # Define reative attributes
        self.rx_value = rx_value
        self.rx_visible = rx_visible
        self.rx_disabled = rx_disabled
        
        super().__init__(**kwargs)