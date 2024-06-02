from ._anvil_designer import acars_formTemplate
from anvil import *
import anvil.server

class acars_form(acars_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
  
  def acars_all_profiles_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.acars_all_profiles_list.text = anvil.server.call('get_acars_all_profile_list',
                                self.acars_all_date.date.strftime('%Y'),
                                self.acars_all_date.date.strftime('%m'),
                                self.acars_all_date.date.strftime('%d'),
                                self.acars_all_hour.text)


  def acars_airport_profiles_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.acars_airport_profiles_list.text, self.acars_airport_info_label.text, self.profiles_list, self.dates_list = anvil.server.call('get_acars_airport_profile_list',
                                self.acars_airport_date.date.strftime('%Y'),
                                self.acars_airport_date.date.strftime('%m'),
                                self.acars_airport_date.date.strftime('%d'),
                                str.upper(self.acars_airport_id.text))
    return self.profiles_list, self.dates_list
  
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

    if len(self.acars_temp.text) > 0:
      modify_sfc = [self.acars_temp.text, self.acars_dewp.text]
    else:
      modify_sfc = False

    if self.acars_ecape_check.checked:
      special_parcels = None
    else:
      special_parcels = 'simple'

    if self.acars_map_check.checked:
      map_zoom = 2
    else:
      map_zoom = 0

    
    if len(self.acars_airport_id.text) > 0:
      try:
        profile_idx = self.profiles_list.index(self.acars_site_id.text) 
        year = self.dates_list[profile_idx][0]
        month = self.dates_list[profile_idx][1]
        day = self.dates_list[profile_idx][2]
        hour = self.dates_list[profile_idx][3]
      except:
         year = self.acars_all_date.date.strftime('%Y')
         month = self.acars_all_date.date.strftime('%m')
         day = self.acars_all_date.date.strftime('%d')
         hour = self.acars_all_hour.text
         pass
    else:
      year = self.acars_all_date.date.strftime('%Y')
      month = self.acars_all_date.date.strftime('%m')
      day = self.acars_all_date.date.strftime('%d')
      hour = self.acars_all_hour.text
    
    params = anvil.server.call('get_acars_sounding',
                               self.acars_site_id.text[0:8],
                               year,
                               month,
                               day,
                               hour,
                               self.acars_color_blind_check.checked,
                               self.acars_dark_mode_check.checked,
                               self.acars_hodo_check.checked,
                               style,
                               storm_motion,
                               modify_sfc, 
                               special_parcels,
                               map_zoom)
    self.acars_image_display.source = params[0]
    self.acars_plot_label.text = params[1]
    self.acars_plot_label.text = params[1]
