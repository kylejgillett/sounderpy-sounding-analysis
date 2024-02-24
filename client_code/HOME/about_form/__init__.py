from ._anvil_designer import about_formTemplate
from anvil import *
import anvil.server
from anvil import open_form

class about_form(about_formTemplate):
    def __init__(self, **properties):
        # Set up the form
        self.init_components(**properties)

        # Call the server function to get the Folium-generated HTML content
        folium_html_content = anvil.server.call('get_folium_map_html')

        # Set the content of the HTML component to the Folium-generated HTML
        self.html_1.content = folium_html_content
