from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def station_id_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
