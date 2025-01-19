from ._anvil_designer import test_formTemplate
from anvil import *
import anvil.server
from anvil import GoogleMap

class test_form(test_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Center map at a specific location
    self.map.center = GoogleMap.LatLng(40.477446, -96.090886)
    self.map.zoom = 40

    # Add markers to the map
    self.add_marker(37.7749, -122.4194, "San Francisco", "SF Marker")
    self.add_marker(34.0522, -118.2437, "Los Angeles", "LA Marker")
