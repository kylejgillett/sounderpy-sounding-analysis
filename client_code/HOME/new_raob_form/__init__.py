from ._anvil_designer import new_raob_formTemplate
from anvil import *
import anvil.server
from datetime import datetime
from ...SHARED_UTILS import server_call


class new_raob_form(new_raob_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    ### SET DEFAULT DATE PARAMETERS ----------------------
    # set date to current date in UTC
    self.raob_date.date = datetime.utcnow().date()
    # get the current UTC hour
    current_hour = datetime.utcnow().hour
    # set default text to latest "hour" of usual RAOB launches
    if 13 <= current_hour <= 23 or 0 <= current_hour < 1:
        self.raob_hour.text = "12"
    else:
        self.raob_hour.text = "00"

  ### GET SOUNDING FUNCTION -------------------------------
  def raob_button_click(self, **event_args):
    self.raob_standby_label.text = (
      "YOUR REQUEST IS PROCESSING, THIS MAY TAKE A MOMENT..."
    )

    settings = self.fig_settings_comp_1.get_settings()
    
    args_list = [
      self.raob_site_id.text,
      self.raob_date.date.strftime("%Y"),
      self.raob_date.date.strftime("%m"),
      self.raob_date.date.strftime("%d"),
      self.raob_hour.text,
      settings['color_blind'],
      settings['dark_mode'],
      settings['show_hodo'],
      settings['storm_motion'],
      settings['modify_sfc'],
      settings['special_parcels'],
      settings['map_zoom'],
      settings['radar'],
      settings['radar_time'],
      settings['hodo_boundary']
    ]
    
    # call server call wrapper
    params = server_call(
      "get_raob_sounding",
      self.raob_standby_label,
      *args_list
    )

    if params is not None:
      self.raob_image_display.source = params[0]
      self.raob_plot_label.text = params[1]
