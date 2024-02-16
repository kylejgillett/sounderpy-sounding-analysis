from ._anvil_designer import acars_formTemplate
from anvil import *
import anvil.server

class acars_form(acars_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def acars_profiles_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.acars_profiles_list.text = anvil.server.call('get_acars_profile_list',
                                self.acars_date.date.strftime('%Y'),
                                self.acars_date.date.strftime('%m'),
                                self.acars_date.date.strftime('%d'),
                                self.acars_hour.text)

  def acars_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.acars_standby_label.text = "YOUR REQUEST IS PROCESSING, THIS MAY TAKE A MOMENT..."
    params = anvil.server.call('get_acars_sounding',
                               self.acars_site_id.text,
                               self.acars_date.date.strftime('%Y'),
                               self.acars_date.date.strftime('%m'),
                               self.acars_date.date.strftime('%d'),
                               self.acars_hour.text,
                               self.acars_dark_mode_check.checked,
                               self.acars_color_blind_check.checked)
    self.acars_image_display.source = params[0]
    self.acars_plot_label.text = params[1]