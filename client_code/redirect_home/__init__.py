from ._anvil_designer import redirect_homeTemplate
from anvil import *
import anvil.server
from anvil.js import window

class redirect_home(redirect_homeTemplate):
  def __init__(self, **properties):
    # Set Form Properties and Data Bindings.
    self.init_components(**properties)

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    window.open("https://sounderpy.app/", "sounderpy.app")
