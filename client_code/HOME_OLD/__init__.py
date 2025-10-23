from ._anvil_designer import HOME_OLDTemplate
from anvil import *
import anvil.server

from new_raob_form import new_raob_form
from new_acars_form import new_acars_form
from new_bufkit_form import new_bufkit_form
from new_reanl_form import new_reanl_form
from about_form import about_form
from Form2 import Form2
#from composite_form import composite_form
#from test_form import test_form

class HOME_OLD(HOME_OLDTemplate):
  def __init__(self, **properties):
    # Set Form Properties and Data Bindings.
    self.init_components(**properties)

  def raob_tab_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.tab_panel.clear()
    self.tab_panel.add_component(new_raob_form())
    pass

  def acars_tab_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.tab_panel.clear()
    self.tab_panel.add_component(new_acars_form())
    pass

  def bufkit_tab_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.tab_panel.clear()
    self.tab_panel.add_component(new_bufkit_form())
    pass

  def reanl_tab_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.tab_panel.clear()
    self.tab_panel.add_component(new_reanl_form())
    pass

  def about_tab_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.tab_panel.clear()
    self.tab_panel.add_component(about_form())
    pass

  def test_tab_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.tab_panel.clear()
    self.tab_panel.add_component(Form2())
    pass

