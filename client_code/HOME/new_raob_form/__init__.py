from ._anvil_designer import new_raob_formTemplate
from anvil import *
import anvil.server
from datetime import datetime


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

    self.raob_map_zoom.text = "2"

  ### GET SOUNDING FUNCTION -------------------------------
  def raob_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.raob_standby_label.text = (
      "YOUR REQUEST IS PROCESSING, THIS MAY TAKE A MOMENT..."
    )

    if len(self.raob_direction.text) > 0:
      storm_motion = [int(self.raob_direction.text), int(self.raob_speed.text)]
    else:
      storm_motion = self.raob_sm.selected_value

    def check_for_vals(T_val, Td_val, ws_val, wd_val):
      modify_sfc = {}
      vals = [T_val, Td_val, ws_val, wd_val]
      keys = ["T", "Td", "ws", "wd"]

      for val, key in zip(vals, keys):
        if len(val) > 0:
          modify_sfc[key] = float(val)

      return modify_sfc

    surface_mod_vals = check_for_vals(
      self.raob_temp.text,
      self.raob_dewp.text,
      self.raob_wspeed.text,
      self.raob_wdir.text,
    )

    if len(surface_mod_vals) > 0:
      modify_sfc = surface_mod_vals
    else:
      modify_sfc = False

    if self.raob_ecape_check.checked:
      special_parcels = None
    else:
      special_parcels = "simple"

    params = anvil.server.call(
      "get_raob_sounding",
      self.raob_site_id.text,
      self.raob_date.date.strftime("%Y"),
      self.raob_date.date.strftime("%m"),
      self.raob_date.date.strftime("%d"),
      self.raob_hour.text,
      self.raob_color_blind_check.checked,
      self.raob_dark_mode_check.checked,
      self.raob_hodo_check.checked,
      storm_motion,
      modify_sfc,
      special_parcels,
      int(self.raob_map_zoom.text),
    )
    self.raob_image_display.source = params[0]
    self.raob_plot_label.text = params[1]
