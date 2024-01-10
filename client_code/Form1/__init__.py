from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def station_id_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def obs_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    params = anvil.server.call('get_obs_sounding',
                               self.raob_site_id.text,
                               self.raob_date.date.strftime('%Y'),
                               self.raob_date.date.strftime('%m'),
                               self.raob_date.date.strftime('%d'),
                               self.raob_hour.text,
                               self.raob_dark_mode_check.checked,
                               self.raob_color_blind_check.checked)
    self.raob_image_display.source = params[0]
    self.raob_plot_label.text = params[1]
    
