import anvil.server

@anvil.server.callable
def get_folium_map_html():
    # Read the content of the Folium-generated HTML file
    with open("_/theme/folium_generated_map.html", "r") as f:
        html_content = f.read()

    return html_content
