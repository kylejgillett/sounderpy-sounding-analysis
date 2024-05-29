from ._anvil_designer import composite_formTemplate
from anvil import *
import anvil.server

from fcst_forecast_hr import fcst_forecast_hr

class composite_form(composite_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

      def raob_tab_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.tab_panel.clear()
        self.tab_panel.add_component(raob_form())
        pass
