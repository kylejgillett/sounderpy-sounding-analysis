from ._anvil_designer import utctime_display_compTemplate
from anvil import *
import anvil.server


class utctime_display_comp(utctime_display_compTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
