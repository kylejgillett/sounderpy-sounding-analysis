from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

from ..bufkit_fcsthrs import bufkit_fcsthrs


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    
  def fcst_hours_tab_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.tab_panel.clear()
    self.tab_panel.add_component(bufkit_fcsthrs())
    pass