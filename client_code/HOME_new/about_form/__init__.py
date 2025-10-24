from ._anvil_designer import about_formTemplate
from anvil import *
import anvil.server
import anvil.js


class about_form(about_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Replace 'https://www.google.com' with your desired URL
    url_to_open = 'https://joss.theoj.org/papers/10.21105/joss.08087' 
    # The second argument '_blank' tells the browser to open the link in a new tab/window
    anvil.js.window.open(url_to_open, '_blank')
