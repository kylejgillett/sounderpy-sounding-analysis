from ._anvil_designer import new_reanl_formTemplate
from anvil import *
import anvil.server
from datetime import datetime
from ...SHARED_UTILS import server_call


class new_reanl_form(new_reanl_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    ### SET DEFAULT DATE PARAMETERS ----------------------
    # set date mound city date haha
    self.reanl_date.date = datetime(2024, 8, 28)
    # set to 23z
    self.reanl_hour.text = "23"

  def reanl_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.reanl_standby_label.text = (
      "YOUR REQUEST IS PROCESSING, THIS MAY TAKE A MOMENT..."
    )

    # get figure settings
    settings = self.fig_settings_comp_1.get_settings()
    args_list = [
      [
        float(self.reanl_coords.text.split(",", 1)[0][0:6]),
        float(self.reanl_coords.text.split(",", 1)[1][0:6]),
      ],
      self.reanl_date.date.strftime("%Y"),
      self.reanl_date.date.strftime("%m"),
      self.reanl_date.date.strftime("%d"),
      self.reanl_hour.text,
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
    params = server_call("get_reanl_sounding", self.reanl_standby_label, *args_list)

    if params is not None:
      self.reanl_image_display.source = params[0]
      self.reanl_plot_label.text = params[1]
