from ._anvil_designer import test_formTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server


class test_form(test_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.latest_runs_txt.text = anvil.server.call("get_latest_run")

  def bufkit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.bufkit_standby_label.text = (
      "YOUR REQUEST IS PROCESSING, THIS MAY TAKE A MOMENT..."
    )

    if len(self.bufkit_direction.text) > 0:
      storm_motion = [int(self.bufkit_direction.text), int(self.bufkit_speed.text)]
    else:
      storm_motion = self.bufkit_sm.selected_value

    def check_for_vals(T_val, Td_val, ws_val, wd_val):
      modify_sfc = {}
      vals = [T_val, Td_val, ws_val, wd_val]
      keys = ["T", "Td", "ws", "wd"]

      for val, key in zip(vals, keys):
        if len(val) > 0:
          modify_sfc[key] = float(val)

      return modify_sfc

    surface_mod_vals = check_for_vals(
      self.bufkit_temp.text,
      self.bufkit_dewp.text,
      self.bufkit_wspeed.text,
      self.bufkit_wdir.text,
    )

    if len(surface_mod_vals) > 0:
      modify_sfc = surface_mod_vals
    else:
      modify_sfc = False

    if self.bufkit_ecape_check.checked:
      special_parcels = None
    else:
      special_parcels = "simple"

    if self.bufkit_map_check.checked:
      map_zoom = 2
    else:
      map_zoom = 0

    if len(self.bufkit_run_hour.text) > 0:
      params = anvil.server.call(
        "get_bufkit_sounding",
        self.bufkit_model.selected_value,
        self.bufkit_site_id.text,
        self.bufkit_fhour.text,
        self.bufkit_run_date.date.strftime("%Y"),
        self.bufkit_run_date.date.strftime("%m"),
        self.bufkit_run_date.date.strftime("%d"),
        self.bufkit_run_hour.text,
        self.bufkit_color_blind_check.checked,
        self.bufkit_dark_mode_check.checked,
        self.bufkit_hodo_check.checked,
        storm_motion,
        modify_sfc,
        special_parcels,
        map_zoom,
      )

    else:
      params = anvil.server.call(
        "get_latest_bufkit_sounding",
        self.bufkit_model.selected_value,
        self.bufkit_site_id.text,
        self.bufkit_fhour.text,
        self.bufkit_color_blind_check.checked,
        self.bufkit_dark_mode_check.checked,
        self.bufkit_hodo_check.checked,
        storm_motion,
        modify_sfc,
        special_parcels,
        map_zoom,
      )

    self.bufkit_image_display.source = params[0]
    self.bufkit_plot_label.text = params[1]
