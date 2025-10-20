from ._anvil_designer import fig_settings_compTemplate
from anvil import *
import anvil.server


class fig_settings_comp(fig_settings_compTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def show_settings_panel_click(self, **event_args):
    current_state = self.settings_panel.visible
    self.settings_panel.visible = not current_state
    
    # Optional: Change the button text
    if self.settings_panel.visible:
      self.show_settings_panel.text = "Hide Figure Settings"
    else:
      self.show_settings_panel.text = "Show Figure Settings"


  
  def get_settings(self):
  
    # --- Storm Motion Logic ---
    if len(self.sm_direction.text) > 0:
      storm_motion = [int(self.sm_direction.text), int(self.sm_speed.text)]
    else:
      storm_motion = self.stormmotion.selected_value
  
      # --- Radar Data Logic ---
    if self.radar_type.selected_value == "None":
      radar = None
    else:
      radar = self.radar_type.selected_value
  
      # --- Radar Date Logic ---
    if self.radar_date.date is None:
      radar_date = "sounding"
    else:
      radar_date = self.radar_date.date
  
      # --- Hodo Boudnary Angle Logic ---
    hodo_boundary_angle = {'angle':[int(self.hodoboundary_angle.text)], 'color':['brown']} if len(self.hodoboundary_angle.text) > 0 else None
  
    # --- Surface Modification Logic ---
    def check_for_vals(T_val, Td_val, ws_val, wd_val):
      modify_sfc = {}
      vals = [T_val, Td_val, ws_val, wd_val]
      keys = ["T", "Td", "ws", "wd"]
  
      for val, key in zip(vals, keys):
        if len(val) > 0:
          modify_sfc[key] = float(val)
      return modify_sfc
  
    surface_mod_vals = check_for_vals(
      self.sfc_temp.text,
      self.sfc_dewp.text,
      self.sfc_wspeed.text,
      self.sfc_wdir.text,
    )
    modify_sfc = surface_mod_vals if len(surface_mod_vals) > 0 else False
  
  
    # --- Special Parcels Logic ---
    special_parcels = None if self.ecape_check.checked else "simple"
  
  
    # --- Return all settings ---
    return {
      'color_blind': self.color_blind_check.checked,
      'dark_mode': self.dark_mode_check.checked,
      'show_hodo': self.hodo_check.checked,
      'storm_motion': storm_motion,
      'modify_sfc': modify_sfc,
      'special_parcels': special_parcels,
      'map_zoom': int(self.map_zoom.text),
      'radar': radar,
      'radar_time': radar_date,
      'hodo_boundary': hodo_boundary_angle
    }


