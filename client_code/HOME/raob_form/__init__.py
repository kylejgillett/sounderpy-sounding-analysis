from ._anvil_designer import raob_formTemplate
from anvil import *
import anvil.server

class raob_form(raob_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def raob_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.raob_standby_label.text = "YOUR REQUEST IS PROCESSING, THIS MAY TAKE A MOMENT..."


    if len(self.raob_direction.text) > 0:
      storm_motion = [int(self.raob_direction.text), int(self.raob_speed.text)]
    else:
      storm_motion = self.raob_sm.selected_value
    
    if self.raob_simple_check.checked:
      style = 'simple'
    else:
      style = 'full'

    if len(self.raob_temp.text) > 0:
      modify_sfc = [self.raob_temp.text, self.raob_dewp.text]
    else:
      modify_sfc = False

    if self.raob_ecape_check.checked:
      special_parcels = None
    else:
      special_parcels = 'simple'

    if self.raob_map_check.checked:
      map_zoom = 2
    else:
      map_zoom = 0
    params = anvil.server.call('get_raob_sounding',
                              self.raob_site_id.text,
                              self.raob_date.date.strftime('%Y'),
                              self.raob_date.date.strftime('%m'),
                              self.raob_date.date.strftime('%d'),
                              self.raob_hour.text,
                              self.raob_color_blind_check.checked,
                              self.raob_dark_mode_check.checked,
                              self.raob_hodo_check.checked,
                              storm_motion,
                              modify_sfc,
                              special_parcels, 
                              map_zoom)
    self.raob_image_display.source = params[0]
    self.raob_plot_label.text = params[1]