from ._anvil_designer import test_formTemplate
from anvil import *
import anvil.server
from anvil import GoogleMap
from anvil.js import import_from


MarkerClusterer = import_from("https://cdn.skypack.dev/@googlemaps/markerclusterer").MarkerClusterer


# class test_form(test_formTemplate):
#     def __init__(self, **properties):
#         self.init_components(**properties)
#         self.setup_map()

#     def setup_map(self):
#         self.map.center = {"lat":-28.024, "lng":140.887 }
#         infoWindow = GoogleMap.InfoWindow(disable_auto_pan=True)

#         locations = anvil.server.call('get_location_data')

#         marker_list = []
#         label_list = []

#         for location in locations:
#             lat = location['LAT']
#             lon = location['LON']
#             name = location['NAME']
#             marker_list.append({"lat": lat, "lng": lon})
#             label_list.append(name)
      
#         markers = [GoogleMap.Marker(position=p, label=l) for p, l in zip(marker_list, label_list)]

#         def click(sender, **event_args):
#             infoWindow.content = sender.label
#             infoWindow.open(self.map, sender)

#         for mark in markers:
#             mark.add_event_handler("click", click)

#         MarkerClusterer({"markers": markers, "map": self.map})


      
# class test_form(test_formTemplate):
#   def __init__(self, **properties):
#           self.init_components(**properties)
  
#           # Initial setup
#           self.map.center = GoogleMap.LatLng(37.7749, -122.4194)  # San Francisco
#           self.map.zoom = 10
      
#           # Call the server-side function to get the location data
#           locations = anvil.server.call('get_location_data')
          
#           # Iterate over each location and plot it on the map
#           for location in locations:
#               lat = location['LAT']
#               lon = location['LON']
#               name = location['NAME']

#               marker = GoogleMap.Marker(
#                       position=GoogleMap.LatLng(lat, lon)
#                   )
#               # Plot the marker on the map (adjust for your map component)
#               self.map.add_component(marker)
