from ._anvil_designer import new_bufkit_formTemplate
from anvil import *
import anvil.server
from ...SHARED_UTILS import server_call


class new_bufkit_form(new_bufkit_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.file_download_panel.visible = False

    text_list = anvil.server.call("get_latest_run")

    self.bufkit_model.items = text_list

  def csv_button_click(self, files, **event_args):
      anvil.media.download(files['CSV'])

  def cm1_button_click(self, files, **event_args):
      anvil.media.download(files['CM1'])
  
  def sharppy_button_click(self, files, **event_args):
        anvil.media.download(files['SHARPPY'])

      
  def bufkit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.bufkit_standby_label.text = (
      "YOUR REQUEST IS PROCESSING, THIS MAY TAKE A MOMENT..."
    )

    # get figure settings
    settings = self.fig_settings_comp_1.get_settings()

    if len(self.bufkit_run_hour.text) > 0:
      args_list = [
        self.bufkit_model.selected_value.split(" ", 1)[0],
        self.bufkit_site_id.text,
        self.bufkit_fhour.text,
        self.bufkit_run_date.date.strftime("%Y"),
        self.bufkit_run_date.date.strftime("%m"),
        self.bufkit_run_date.date.strftime("%d"),
        self.bufkit_run_hour.text,
        settings["color_blind"],
        settings["dark_mode"],
        settings["show_hodo"],
        settings["storm_motion"],
        settings["modify_sfc"],
        settings["special_parcels"],
        settings["map_zoom"],
        settings["radar"],
        settings["radar_time"],
        settings["hodo_boundary"],
      ]

      # call server call wrapper
      params = server_call("get_bufkit_sounding", self.bufkit_standby_label, *args_list)

    else:
      args_list = [
        self.bufkit_model.selected_value.split(" ", 1)[0],
        self.bufkit_site_id.text,
        self.bufkit_fhour.text,
        settings["color_blind"],
        settings["dark_mode"],
        settings["show_hodo"],
        settings["storm_motion"],
        settings["modify_sfc"],
        settings["special_parcels"],
        settings["map_zoom"],
        settings["radar"],
        settings["radar_time"],
        settings["hodo_boundary"],
      ]

      # call server call wrapper
      params = server_call(
        "get_latest_bufkit_sounding", self.bufkit_standby_label, *args_list
      )

    if params is not None:
      self.bufkit_image_display.source = params[0]
      self.bufkit_plot_label.text = params[1]
      self.file_download_panel.visible = True
      files = params[2]
      print("FILES RETURNED =", params[2])

  # def download_button_click(self, **event_args):
  #   # get figure settings
  #   settings = self.fig_settings_comp_1.get_settings()
  #   media_file = server_call('get_latest_bufkit_sounding', self.bufkit_standby_label, *args_list)
  #   anvil.media.download(media_file)

  # if len(self.bufkit_direction.text) > 0:
  #   storm_motion = [int(self.bufkit_direction.text), int(self.bufkit_speed.text)]
  # else:
  #   storm_motion = self.bufkit_sm.selected_value

  # def check_for_vals(T_val, Td_val, ws_val, wd_val):
  #   modify_sfc = {}
  #   vals = [T_val, Td_val, ws_val, wd_val]
  #   keys = ["T", "Td", "ws", "wd"]

  #   for val, key in zip(vals, keys):
  #     if len(val) > 0:
  #       modify_sfc[key] = float(val)

  #   return modify_sfc

  # surface_mod_vals = check_for_vals(
  #   self.bufkit_temp.text,
  #   self.bufkit_dewp.text,
  #   self.bufkit_wspeed.text,
  #   self.bufkit_wdir.text,
  # )

  # if len(surface_mod_vals) > 0:
  #   modify_sfc = surface_mod_vals
  # else:
  #   modify_sfc = False

  # if self.bufkit_ecape_check.checked:
  #   special_parcels = None
  # else:
  #   special_parcels = "simple"

  # if len(self.bufkit_run_hour.text) > 0:
  #   params = anvil.server.call(
  #     "get_bufkit_sounding",
  #     self.bufkit_model.selected_value.split(" ", 1)[0],
  #     self.bufkit_site_id.text,
  #     self.bufkit_fhour.text,
  #     self.bufkit_run_date.date.strftime("%Y"),
  #     self.bufkit_run_date.date.strftime("%m"),
  #     self.bufkit_run_date.date.strftime("%d"),
  #     self.bufkit_run_hour.text,
  #     self.bufkit_color_blind_check.checked,
  #     self.bufkit_dark_mode_check.checked,
  #     self.bufkit_hodo_check.checked,
  #     storm_motion,
  #     modify_sfc,
  #     special_parcels,
  #     int(self.bufkit_map_zoom.text),
  #   )

  # else:
  #   params = anvil.server.call(
  #     "get_latest_bufkit_sounding",
  #     self.bufkit_model.selected_value.split(" ", 1)[0],
  #     self.bufkit_site_id.text,
  #     self.bufkit_fhour.text,
  #     self.bufkit_color_blind_check.checked,
  #     self.bufkit_dark_mode_check.checked,
  #     self.bufkit_hodo_check.checked,
  #     storm_motion,
  #     modify_sfc,
  #     special_parcels,
  #     int(self.bufkit_map_zoom.text),
  #   )
