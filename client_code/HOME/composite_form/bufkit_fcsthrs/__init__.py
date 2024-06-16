from ._anvil_designer import bufkit_fcsthrsTemplate
from anvil import *
import anvil.server


class bufkit_fcsthrs(bufkit_fcsthrsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    
