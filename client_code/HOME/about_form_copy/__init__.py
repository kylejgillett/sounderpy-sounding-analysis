from ._anvil_designer import about_form_copyTemplate
from anvil import *
import anvil.server

class about_form_copy(about_form_copyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
