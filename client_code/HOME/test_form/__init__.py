from ._anvil_designer import test_formTemplate
from anvil import *
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

    if self.bufkit_simple_check.checked:
      style = "simple"
    else:
      style = "full"

    if len(self.bufkit_temp.text) > 0:
      modify_sfc = [self.bufkit_temp.text, self.bufkit_dewp.text]
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
        self.bufkit_model.text,
        self.bufkit_site_id.text,
        self.bufkit_fhour.text,
        self.bufkit_run_date.date.strftime("%Y"),
        self.bufkit_run_date.date.strftime("%m"),
        self.bufkit_run_date.date.strftime("%d"),
        self.bufkit_run_hour.text,
        self.bufkit_color_blind_check.checked,
        self.bufkit_dark_mode_check.checked,
        self.bufkit_hodo_check.checked,
        style,
        storm_motion,
        modify_sfc,
        special_parcels,
        map_zoom,
      )

    else:
      params = anvil.server.call(
        "get_latest_bufkit_sounding",
        self.bufkit_model.text,
        self.bufkit_site_id.text,
        self.bufkit_fhour.text,
        self.bufkit_color_blind_check.checked,
        self.bufkit_dark_mode_check.checked,
        self.bufkit_hodo_check.checked,
        style,
        storm_motion,
        modify_sfc,
        special_parcels,
        map_zoom,
      )

    self.bufkit_image_display.source = params[0]
    self.bufkit_plot_label.text = params[1]
    self.bufkit_cm1_button.visible = True
    
    def bufkit_cm1_button_click(self, **event_args):
        cm1_file = anvil.server.call(
            "get_cm1_file",
            self.bufkit_model.text,
            self.bufkit_site_id.text,
            self.bufkit_fhour.text,
          )
        anvil.media.download(cm1_file)
    
