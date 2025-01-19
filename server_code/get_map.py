import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.server

@anvil.server.callable
def get_folium_map_html():
    # Read the content of the Folium-generated HTML file
    with open("/standard-page.html", "r") as f:
        html_content = f.read()

    return html_content
