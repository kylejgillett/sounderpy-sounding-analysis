from ._anvil_designer import airport_map_compTemplate
from anvil import *
import anvil.server


class airport_map_comp(airport_map_compTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
