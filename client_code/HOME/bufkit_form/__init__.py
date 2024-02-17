from ._anvil_designer import bufkit_formTemplate
from anvil import *
import anvil.server

class bufkit_form(bufkit_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def bufkit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.bufkit_standby_label.text = "YOUR REQUEST IS PROCESSING, THIS MAY TAKE A MOMENT..."
    params = anvil.server.call('get_bufkit_sounding',
                               self.bufkit_model.text,
                               self.bufkit_site_id.text,
                               self.bufkit_fhour.text,
                               self.bufkit_dark_mode_check.checked,
                               self.bufkit_color_blind_check.checked,
                               self.bufkit_hodo_check.checked)
    self.bufkit_image_display.source = params[0]
    self.bufkit_plot_label.text = params[1]