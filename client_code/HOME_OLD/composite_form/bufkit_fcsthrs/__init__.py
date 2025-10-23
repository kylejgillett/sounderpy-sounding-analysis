from ._anvil_designer import bufkit_fcsthrsTemplate
from anvil import *
import anvil.server


class bufkit_fcsthrs(bufkit_fcsthrsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.fhrs = []
    self.fhrs = [item.strip() for item in self.bufkit_fhour.split(",")]
    self.fhrs = [int(item) for item in self.fhrs]
    
    data_dict = anvil.server.call('fetch_bufkit_composite_data',
                                  self.bufkit_model.text,
                                  self.bufkit_site_id.text,
                                  self.fhrs)

    params = anvil.server.call('build_composite_sounding',
                              data_dict)
    
    # if len(self.bufkit_run_hour.text) > 0:
      
    #   params = anvil.server.call('get_composite_sounding',
    #                            self.bufkit_model.text,
    #                            self.bufkit_site_id.text,
    #                            self.bufkit_fhour.text,
    #                            self.bufkit_run_date.date.strftime('%Y'),
    #                            self.bufkit_run_date.date.strftime('%m'),
    #                            self.bufkit_run_date.date.strftime('%d'),
    #                            self.bufkit_run_hour.text,
    #                            self.bufkit_color_blind_check.checked,
    #                            self.bufkit_dark_mode_check.checked,
    #                            self.bufkit_hodo_check.checked,
    #                            storm_motion,
    #                            modify_sfc,
    #                            special_parcels,
    #                            map_zoom)
      
    # else:
      # params = anvil.server.call('get_latest_bufkit_sounding',
      #                          self.bufkit_model.text,
      #                          self.bufkit_site_id.text,
      #                          self.bufkit_fhour.text,
      #                          self.bufkit_color_blind_check.checked,
      #                          self.bufkit_dark_mode_check.checked,
      #                          self.bufkit_hodo_check.checked,
      #                          storm_motion,
      #                          modify_sfc,
      #                          special_parcels, 
      #                          map_zoom)

  
    self.bufkit_image_display.source = params[0]
    self.bufkit_plot_label.text = params[1]