from ._anvil_designer import HOMETemplate
from anvil import *
import anvil.server

from raob_form import raob_form
from acars_form import acars_form
from bufkit_form import bufkit_form
from reanl_form import reanl_form
from about_form import about_form

class HOME(HOMETemplate):
  def __init__(self, **properties):
    # Set Form Properties and Data Bindings.
    self.init_components(**properties)

  def raob_tab_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.tab_panel.clear()
    self.tab_panel.add_component(raob_form())
    pass

  def acars_tab_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.tab_panel.clear()
    self.tab_panel.add_component(acars_form())
    pass

  def bufkit_tab_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.tab_panel.clear()
    self.tab_panel.add_component(bufkit_form())
    pass

  def reanl_tab_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.tab_panel.clear()
    self.tab_panel.add_component(reanl_form())
    pass

  def about_tab_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.tab_panel.clear()
    self.tab_panel.add_component(about_form())
    pass

  # def test_tab_click(self, **event_args):
  #   """This method is called when the button is clicked"""
  #   self.tab_panel.clear()
  #   self.tab_panel.add_component(acars_form_copy())
  #   pass