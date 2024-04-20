from ._anvil_designer import acars_form_copyTemplate
from anvil import *
import anvil.server

class acars_form_copy(acars_form_copyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def acars_all_profiles_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.acars_all_profiles_list.text = anvil.server.call('get_acars_profile_list',
                                self.acars_date.date.strftime('%Y'),
                                self.acars_date.date.strftime('%m'),
                                self.acars_date.date.strftime('%d'),
                                self.acars_hour.text)


  def acars_airport_profiles_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.acars_airport_profiles_list.text, profile_id_list, profile_all_list = anvil.server.call('get_acars_profile_list',
                                self.acars_date.date.strftime('%Y'),
                                self.acars_date.date.strftime('%m'),
                                self.acars_date.date.strftime('%d'),
                                self.acars_airport_id.text)
 
  def acars_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.acars_standby_label.text = "YOUR REQUEST IS PROCESSING, THIS MAY TAKE A MOMENT..."

    if len(self.acars_direction.text) > 0:
      storm_motion = [int(self.acars_direction.text), int(self.acars_speed.text)]
    else:
      storm_motion = self.acars_sm.selected_value

    if self.acars_simple_check.checked:
      style = 'simple'
    else:
      style = 'full'

    params = anvil.server.call('get_acars_sounding',
                               self.acars_site_id.text[0:8],
                               self.acars_date.date.strftime('%Y'),
                               self.acars_date.date.strftime('%m'),
                               self.acars_date.date.strftime('%d'),
                               self.acars_hour.text,
                               self.acars_color_blind_check.checked,
                               self.acars_dark_mode_check.checked,
                               self.acars_hodo_check.checked,
                               style,
                               storm_motion)
    self.acars_image_display.source = params[0]
    self.acars_plot_label.text = params[1]
