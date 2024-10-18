from ._anvil_designer import reanl_formTemplate
from anvil import *
import anvil.server

class reanl_form(reanl_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def reanl_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.reanl_standby_label.text = "YOUR REQUEST IS PROCESSING, THIS MAY TAKE A MOMENT..."

    if len(self.reanl_direction.text) > 0:
      storm_motion = [int(self.reanl_direction.text), int(self.reanl_speed.text)]
    else:
      storm_motion = self.reanl_sm.selected_value
    

    
    if self.reanl_ecape_check.checked:
      special_parcels = None
    else:
      special_parcels = 'simple'

    
    def check_for_vals(T_val, Td_val, ws_val, wd_val):
      modify_sfc = {}
      vals = [T_val, Td_val, ws_val, wd_val]
      keys = ["T", "Td", "ws", "wd"]
      
      for val, key in zip(vals, keys):
        if len(val) > 0:
          modify_sfc[key] = float(val)
    
      return modify_sfc 

    surface_mod_vals = check_for_vals(self.reanl_temp.text, self.reanl_dewp.text, self.reanl_wspeed.text, self.reanl_wdir.text)

    if len(surface_mod_vals) > 0:
      modify_sfc = surface_mod_vals 
    else:
      modify_sfc = False

    if self.reanl_map_check.checked:
      map_zoom = 2
    else:
      map_zoom = 0
    
    params = anvil.server.call('get_reanl_sounding',
                                [float(self.reanl_lat.text), float(self.reanl_lon.text)],
                                self.reanl_date.date.strftime('%Y'),
                                self.reanl_date.date.strftime('%m'),
                                self.reanl_date.date.strftime('%d'),
                                self.reanl_hour.text,
                                self.reanl_color_blind_check.checked,
                                self.reanl_dark_mode_check.checked,
                                self.reanl_hodo_check.checked,
                                storm_motion,
                                modify_sfc,
                                special_parcels, 
                                map_zoom)
    self.reanl_image_display.source = params[0]
    self.reanl_plot_label.text = params[1]