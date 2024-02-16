from ._anvil_designer import reanl_formTemplate
from anvil import *
import anvil.server

class reanl_form(reanl_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def reanl_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.reanl_standby_label.text = "YOUR REQUEST IS PROCESSING, THIS MAY TAKE A MOMENT..."
    params = anvil.server.call('get_reanl_sounding',
                                [float(self.reanl_lat.text), float(self.reanl_lon.text)],
                                self.reanl_date.date.strftime('%Y'),
                                self.reanl_date.date.strftime('%m'),
                                self.reanl_date.date.strftime('%d'),
                                self.reanl_hour.text,
                                self.reanl_dark_mode_check.checked,
                                self.reanl_color_blind_check.checked)
    self.reanl_image_display.source = params[0]
    self.reanl_plot_label.text = params[1]