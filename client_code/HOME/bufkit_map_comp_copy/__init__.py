from ._anvil_designer import bufkit_map_comp_copyTemplate
from anvil import *
import anvil.server


class bufkit_map_comp_copy(bufkit_map_comp_copyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
