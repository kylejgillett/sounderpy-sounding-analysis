from ._anvil_designer import raob_map_compTemplate
from anvil import *
import anvil.server


class raob_map_comp(raob_map_compTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
