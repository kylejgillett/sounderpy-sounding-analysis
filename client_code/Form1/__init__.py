from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form Properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.


  def raob_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.raob_standby_label.text = "YOUR REQUEST IS PROCESSING, THIS MAY TAKE A MOMENT..."
    params = anvil.server.call('get_raob_sounding',
                               self.raob_site_id.text,
                               self.raob_date.date.strftime('%Y'),
                               self.raob_date.date.strftime('%m'),
                               self.raob_date.date.strftime('%d'),
                               self.raob_hour.text,
                               self.raob_dark_mode_check.checked,
                               self.raob_color_blind_check.checked)
    self.raob_image_display.source = params[0]
    self.raob_plot_label.text = params[1]


  def acars_profiles_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.acars_profiles_list.text = anvil.server.call('get_acars_profile_list',
                               self.acars_date.date.strftime('%Y'),
                               self.acars_date.date.strftime('%m'),
                               self.acars_date.date.strftime('%d'),
                               self.acars_hour.text)
  
  def acars_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.acars_standby_label.text = "YOUR REQUEST IS PROCESSING, THIS MAY TAKE A MOMENT..."
    params = anvil.server.call('get_acars_sounding',
                               self.acars_site_id.text,
                               self.acars_date.date.strftime('%Y'),
                               self.acars_date.date.strftime('%m'),
                               self.acars_date.date.strftime('%d'),
                               self.acars_hour.text,
                               self.acars_dark_mode_check.checked,
                               self.acars_color_blind_check.checked)
    self.acars_image_display.source = params[0]
    self.acars_plot_label.text = params[1]




  def bufkit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.bufkit_standby_label.text = "YOUR REQUEST IS PROCESSING, THIS MAY TAKE A MOMENT..."
    params = anvil.server.call('get_bufkit_sounding',
                               self.bufkit_model.text,
                               self.bufkit_site_id.text,
                               self.bufkit_fhour.text,
                               self.bufkit_dark_mode_check.checked,
                               self.bufkit_color_blind_check.checked)
    self.bufkit_image_display.source = params[0]
    self.bufkit_plot_label.text = params[1]

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    anvil.server.call('timer_task')
    pass
