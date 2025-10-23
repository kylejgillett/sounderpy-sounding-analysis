from ._anvil_designer import new_acars_formTemplate
from anvil import *
import anvil.server
from datetime import datetime
from ...SHARED_UTILS import server_call

class new_acars_form(new_acars_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    ### SET DEFAULT DATE PARAMETERS ----------------------
    # set date to current date in UTC
    self.acars_all_date.date = datetime.utcnow().date()
    self.acars_airport_date.date = datetime.utcnow().date()

  def acars_all_profiles_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.acars_profiles_dropdown.items = [anvil.server.call(
      "get_acars_all_profile_list",
      self.acars_all_date.date.strftime("%Y"),
      self.acars_all_date.date.strftime("%m"),
      self.acars_all_date.date.strftime("%d"),
      self.acars_all_hour.text,
    )]

  def acars_airport_profiles_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    (
      self.acars_airport_profiles_list.text,
      self.acars_airport_info_label.text,
      self.profiles_list,
      self.dates_list,
    ) = anvil.server.call(
      "get_acars_airport_profile_list",
      self.acars_airport_date.date.strftime("%Y"),
      self.acars_airport_date.date.strftime("%m"),
      self.acars_airport_date.date.strftime("%d"),
      str.upper(self.acars_airport_id.text),
    )
    return self.profiles_list, self.dates_list

  def acars_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.acars_standby_label.text = (
      "YOUR REQUEST IS PROCESSING, THIS MAY TAKE A MOMENT..."
    )

    if len(self.acars_airport_id.text) > 0:
      try:
        profile_idx = self.profiles_list.index(self.acars_site_id.text)
        year = self.dates_list[profile_idx][0]
        month = self.dates_list[profile_idx][1]
        day = self.dates_list[profile_idx][2]
        hour = self.dates_list[profile_idx][3]
      except:
        year = self.acars_all_date.date.strftime("%Y")
        month = self.acars_all_date.date.strftime("%m")
        day = self.acars_all_date.date.strftime("%d")
        hour = self.acars_all_hour.text
        pass
    else:
      year = self.acars_all_date.date.strftime("%Y")
      month = self.acars_all_date.date.strftime("%m")
      day = self.acars_all_date.date.strftime("%d")
      hour = self.acars_all_hour.text

    # get figure settings
    settings = self.fig_settings_comp_1.get_settings()
    args_list = [self.acars_site_id.text[0:8],
    year,
    month,
    day,
    hour,
    settings['color_blind'],
    settings['dark_mode'],
    settings['show_hodo'],
    settings['storm_motion'],
    settings['modify_sfc'],
    settings['special_parcels'],
    settings['map_zoom'],
    settings['radar'],
    settings['radar_time'],
    settings['hodo_boundary']]
      
    # call server call wrapper
    params = server_call(
      "get_acars_sounding",
      self.acars_standby_label,
      *args_list
    )
    
    if params is not None:
      self.acars_image_display.source = params[0]
      self.acars_plot_label.text = params[1]
