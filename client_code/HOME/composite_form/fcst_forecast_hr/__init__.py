from ._anvil_designer import fcst_forecast_hrTemplate
from anvil import *
import anvil.server


class fcst_forecast_hr(fcst_forecast_hrTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
