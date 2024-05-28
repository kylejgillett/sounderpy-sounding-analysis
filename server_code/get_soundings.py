# import anvil.server
# import sounderpy as spy
# import anvil.media
# from datetime import datetime as dt
# from urllib.request import urlopen
# import pandas as pd
# import pandas as pd
# import numpy as np

# # This is a server module. It runs on the Anvil server,
# # rather than in the user's browser.
# #
# import threading
# import queue

# # Lock to ensure thread-safe access to shared resources
# lock = threading.Lock()

# # Queue to store tasks (requests)
# task_queue = queue.Queue()

# def worker():
#     while True:
#         # Get a task from the queue
#         task = task_queue.get()

#         # Exit the loop if a sentinel value is received (indicating the worker should stop)
#         if task is None:
#             break

#         # Process the task based on the function name
#         if task["function"] == "raob_function":
#             result = process_raob_function(*task["args"])

#         elif task["function"] == "acars_list_function":
#             result = process_acars_list_function(*task["args"])

#         elif task["function"] == "acars_function":
#             result = process_acars_function(*task["args"])

#         elif task["function"] == "latest_bufkit_function":
#             result = process_bufkit_function(*task["args"])

#         elif task["function"] == "bufkit_function":
#             result = process_bufkit_function(*task["args"])

#         elif task["function"] == "reanl_function":
#             result = process_reanl_function(*task["args"])

#         # Mark the task as done
#         task_queue.task_done()

# # Start a worker thread
# worker_thread = threading.Thread(target=worker)
# worker_thread.start()





# # Example functions that may require different variables
# def process_raob_function(site_id, year, month, day, hour, color_blind, dark_mode, hodo, style, storm_motion, modify_sfc):
#     with lock:
#         clean_data = spy.get_obs_data(str(site_id), str(year), str(month), str(day), str(hour))

#         label_txt = f"{clean_data['site_info']['valid-time'][3]}Z RAOB for {clean_data['site_info']['site-id']}, {clean_data['site_info']['site-name']} at {clean_data['site_info']['valid-time'][1]}-{clean_data['site_info']['valid-time'][2]}-{clean_data['site_info']['valid-time'][0]}-{clean_data['site_info']['valid-time'][3]}Z"
        
#         if hodo == True:  
#              spy.build_hodograph(clean_data, dark_mode=dark_mode, storm_motion=storm_motion, save=True, filename='sounderpy_sounding')
#         else:
#              spy.build_sounding(clean_data, style=style, dark_mode=dark_mode, storm_motion=storm_motion, special_parcels='simple', color_blind=color_blind, save=True, map_zoom=0, modify_sfc=modify_sfc)
          
#         image = anvil.media.from_file('sounderpy_sounding.png', 'image/jpeg')

#         print(dt.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
#         print(dt.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

#         return image, label_txt






# def process_acars_all_list_function(year, month, day, hour):
#     with lock:

#        list_1 = spy.acars_data(str(year), str(month), str(day), str(hour)).list_profiles()

#        list_2 = [profile[0:3] for profile in list_1]
      
#        airports_csv = pd.read_csv(f'https://raw.githubusercontent.com/kylejgillett/sounderpy/main/src/AIRPORTS.csv',
#               skiprows=7, skipinitialspace = True)
      
#        list_3 = []
      
#        for arpt, profile in zip(list_2, list_1):
#           where = [np.where(airports_csv['IATA'].str.contains(arpt, na=False, case=True))[0]][0][0]
#           # ADD AIRPORT DATA INTO DICT
#           keys = ['Name', 'City', 'Country', 'Latitude', 'Longitude',]
#           airport_info = []
#           for key in keys:
#               airport_info.append(airports_csv[key][where])
          
#           list_3.append(f'{profile} | {airport_info[0]}, {airport_info[1]}') 

#        #print(dt.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

#        return "\n".join(list_3)



# def process_acars_airport_list_function(year, month, day, airport):
#     with lock: 
      
#        profiles_list = []
#        dates_list = []

#        airports_csv = pd.read_csv(f'https://raw.githubusercontent.com/kylejgillett/sounderpy/main/src/AIRPORTS.csv',
#           skiprows=7, skipinitialspace = True)
      
#        for hour in range(0, 24):
          
#           if hour < 10:
#               hour = f'0{hour}'
          
#           try:
#               acars_conn = spy.acars_data(year, month, day, str(hour))
      
#               acars_list = acars_conn.list_profiles()
#               p_list = [item for item in acars_list if any(phrase in item for phrase in [str(airport)])]
#               d_list = [[year, month, day, hour] for item in acars_list if any(phrase in item for phrase in [str(airport)])]
            
#               profiles_list.extend(p_list)
#               dates_list.extend(d_list)
#           except:
#               pass
      
#        where = [np.where(airports_csv['IATA'].str.contains(airport, na=False, case=True))[0]][0][0]
#        # ADD AIRPORT DATA INTO DICT
#        airport_info = f"{airports_csv['Name'][where]}, {airports_csv['City'][where]}"

#        if len(profiles_list) >0: 
#         profile_ids = "\n".join(profiles_list)
#        else:
#          profile_ids = "No profiles found for given date & airport"

#        return profile_ids, airport_info, profiles_list, dates_list







# def process_acars_function(profile_id, year, month, day, hour, color_blind, dark_mode, hodo, style, storm_motion, modify_sfc):
#     with lock:
#         clean_data = spy.acars_data(str(year), str(month), str(day), str(hour)).get_profile(profile_id)

#         label_txt = f"{clean_data['site_info']['valid-time'][3]}Z flight from {clean_data['site_info']['site-id']}, {clean_data['site_info']['site-name']} at {clean_data['site_info']['valid-time'][1]}-{clean_data['site_info']['valid-time'][2]}-{clean_data['site_info']['valid-time'][0]}-{clean_data['site_info']['valid-time'][3]}Z"

#         if hodo == True:  
#              spy.build_hodograph(clean_data, dark_mode=dark_mode, storm_motion=storm_motion, save=True, filename='sounderpy_sounding')
#         else:
#              spy.build_sounding(clean_data, style=style, dark_mode=dark_mode, color_blind=color_blind, 
#                                 storm_motion=storm_motion, special_parcels='simple', save=True, map_zoom=0, modify_sfc=modify_sfc)

#         image =anvil.media.from_file('sounderpy_sounding.png', 'image/jpeg')

#         #print(dt.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

#         return image, label_txt

# def process_latest_bufkit_function(model, bufkit_site, fcst_hr, color_blind, dark_mode, hodo, style, storm_motion, modify_sfc):
#     with lock:
#         clean_data = spy.get_bufkit_data(str(model), str(bufkit_site), int(fcst_hr))

#         label_txt = f"{clean_data['site_info']['valid-time'][3]}Z forecast for {clean_data['site_info']['site-id']}, {clean_data['site_info']['site-name']} at {clean_data['site_info']['valid-time'][1]}-{clean_data['site_info']['valid-time'][2]}-{clean_data['site_info']['valid-time'][0]}-{clean_data['site_info']['valid-time'][3]}Z"

#         if hodo == True:  
#              spy.build_hodograph(clean_data, dark_mode=dark_mode, storm_motion=storm_motion, save=True, filename='sounderpy_sounding')
#         else:
#              spy.build_sounding(clean_data, style=style, dark_mode=dark_mode, storm_motion=storm_motion, special_parcels='simple', 
#                                 color_blind=color_blind, save=True, map_zoom=0, modify_sfc=modify_sfc)
#         image = anvil.media.from_file('sounderpy_sounding.png', 'image/jpeg')

#         #print(dt.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

#         return image, label_txt


# def process_bufkit_function(model, bufkit_site, fcst_hr, run_year, run_month, run_day, run_hour, color_blind, dark_mode, hodo, style, storm_motion, modify_sfc):
#     with lock:
#         clean_data = spy.get_bufkit_data(str(model), str(bufkit_site), int(fcst_hr), str(run_year), str(run_month), str(run_day), str(run_hour))

#         label_txt = f"{clean_data['site_info']['valid-time'][3]}Z forecast for {clean_data['site_info']['site-id']}, {clean_data['site_info']['site-name']} at {clean_data['site_info']['valid-time'][1]}-{clean_data['site_info']['valid-time'][2]}-{clean_data['site_info']['valid-time'][0]}-{clean_data['site_info']['valid-time'][3]}Z"

#         if hodo == True:  
#              spy.build_hodograph(clean_data, dark_mode=dark_mode, storm_motion=storm_motion, save=True, filename='sounderpy_sounding')
#         else:
#              spy.build_sounding(clean_data, style=style, dark_mode=dark_mode, storm_motion=storm_motion, special_parcels='simple', 
#                                 color_blind=color_blind, save=True, map_zoom=0, modify_sfc=modify_sfc)
#         image = anvil.media.from_file('sounderpy_sounding.png', 'image/jpeg')

#         #print(dt.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

#         return image, label_txt


# def process_reanl_function(latlon, year, month, day, hour, color_blind, dark_mode, hodo, style, storm_motion, modify_sfc):
#     with lock:
#         clean_data = spy.get_model_data('rap-ruc', latlon, str(year), str(month), str(day), str(hour))

#         label_txt = f"{clean_data['site_info']['valid-time'][3]}Z reanalysis for {clean_data['site_info']['site-latlon']} at {clean_data['site_info']['valid-time'][1]}-{clean_data['site_info']['valid-time'][2]}-{clean_data['site_info']['valid-time'][0]}-{clean_data['site_info']['valid-time'][3]}Z"

#         if hodo == True:  
#              spy.build_hodograph(clean_data, dark_mode=dark_mode, storm_motion=storm_motion, save=True, filename='sounderpy_sounding')
#         else:
#              spy.build_sounding(clean_data, style=style, dark_mode=dark_mode, storm_motion=storm_motion, special_parcels='simple', color_blind=color_blind, save=True, map_zoom=0, modify_sfc=modify_sfc)

#         image = anvil.media.from_file('sounderpy_sounding.png', 'image/jpeg')

#         #print(dt.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

#         return image, label_txt


# #####################
# # GET RAOB FUNCTION #
# #####################
# @anvil.server.callable
# def get_raob_sounding(site_id, year, month, day, hour, color_blind, dark_mode, hodo, style, storm_motion, modify_sfc):
#     # Add the task (request) to the queue
#     task_queue.put({"function": "raob_function", "args": (site_id, year, month, day, hour, color_blind, dark_mode, hodo, style, storm_motion, modify_sfc)})

#     image, label_txt = process_raob_function(site_id, year, month, day, hour, color_blind, dark_mode, hodo, style, storm_motion, modify_sfc)

#     return image, label_txt


# ###########################
# # GET ACARS LIST FUNCTION #
# ###########################
# @anvil.server.callable
# def get_acars_all_profile_list(year, month, day, hour):
#     # Add the task (request) to the queue
#     task_queue.put({"function": "acars_all_list_function", "args": (year, month, day, hour)})

#     acars_list = process_acars_all_list_function(year, month, day, hour)

#     return acars_list


# ###########################
# # GET ACARS LIST FUNCTION #
# ###########################
# @anvil.server.callable
# def get_acars_airport_profile_list(year, month, day, airport):
#     # Add the task (request) to the queue
#     task_queue.put({"function": "acars_airport_list_function", "args": (year, month, day, airport)})

#     acars_list, airport_info, profiles_list, dates_list = process_acars_airport_list_function(year, month, day, airport)

#     return acars_list, airport_info, profiles_list, dates_list

# ######################
# # GET ACARS FUNCTION #
# ######################
# @anvil.server.callable
# def get_acars_sounding(profile_id, year, month, day, hour, color_blind, dark_mode, hodo, style, storm_motion, modify_sfc):
#     # Add the task (request) to the queue
#     task_queue.put({"function": "acars_function", "args": (profile_id, year, month, day, hour, color_blind, dark_mode, hodo, style, storm_motion, modify_sfc)})

#     image, label_txt = process_acars_function(profile_id, year, month, day, hour, color_blind, dark_mode, hodo, style, storm_motion, modify_sfc)

#     return image, label_txt


# #######################
# # GET BUFKIT FUNCTION #
# #######################
# @anvil.server.callable
# def get_bufkit_sounding(model, bufkit_site, fcst_hr, run_year, run_month, run_day, run_hour, color_blind, dark_mode, hodo, style, storm_motion, modify_sfc):
#     # Add the task (request) to the queue
#     task_queue.put({"function": "bufkit_function", "args": (model, bufkit_site, fcst_hr, run_year, run_month, run_day, run_hour, color_blind, dark_mode, hodo, style, storm_motion, modify_sfc)})

#     image, label_txt = process_bufkit_function(model, bufkit_site, fcst_hr, run_year, run_month, run_day, run_hour, color_blind, dark_mode, hodo, style, storm_motion, modify_sfc)

#     return image, label_txt


# ##############################
# # GET LATEST BUFKIT FUNCTION #
# ##############################
# @anvil.server.callable
# def get_latest_bufkit_sounding(model, bufkit_site, fcst_hr, color_blind, dark_mode, hodo, style, storm_motion, modify_sfc):
#     # Add the task (request) to the queue
#     task_queue.put({"function": "latest_bufkit_function", "args": (model, bufkit_site, fcst_hr, color_blind, dark_mode, hodo, style, storm_motion, modify_sfc)})

#     image, label_txt = process_latest_bufkit_function(model, bufkit_site, fcst_hr, color_blind, dark_mode, hodo, style, storm_motion, modify_sfc)

#     return image, label_txt


# #######################
# # GET REANL FUNCTION #
# #######################
# @anvil.server.callable
# def get_reanl_sounding(latlon, year, month, day, hour, color_blind, dark_mode, hodo, style, storm_motion, modify_sfc):
#     # Add the task (request) to the queue
#     task_queue.put({"function": "reanl_function", "args": (latlon, year, month, day, hour, color_blind, dark_mode, hodo, style, storm_motion, modify_sfc)})

#     image, label_txt = process_reanl_function(latlon, year, month, day, hour, color_blind, dark_mode, hodo, style, storm_motion, modify_sfc)

#     return image, label_txt


# ###########################
# # GET MODEL RUNS FUNCTION #
# ###########################
# @anvil.server.callable
# def get_latest_run():
    
#     # make sure variables are in the correct case
#     text_list = []
#     station = 'KMOP'
    
#     for model in ['gfs', 'nam', 'namnest', 'rap', 'hrrr', 'sref', 'hiresw']: 
#         if model == 'gfs':
#             model3 = 'gfs3' 
#         else:
#             model3 = model
#         data_conn = f'http://www.meteo.psu.edu/bufkit/data/{model.upper()}/{model3}_{station.lower()}.buf'

#         # GET BUFKIT FILE 
#         # CONVERT LINES OF BYTES TO STRINGS 
#         buf_file = urlopen(data_conn)
#         buf_file = [str(line).replace("b'", "").replace("\\r\\n'", "") for line in buf_file]

#         # SET UP DATE / TIME OBJECTS FROM THE BUFKIT FILE
#         run_time = buf_file[4][buf_file[4].index('TIME') + 7:(buf_file[4].index('TIME')+9)+9]
        
#         text_list.append(f'{str.upper(model)}: {run_time[2:4]}/{run_time[4:6]} {run_time[7:9]}Z')
      
#         final_str = ''
#         for i, string in enumerate(text_list):
#           final_str += string
#           if i < len(text_list) - 1:
#               final_str += " | "
    
#     return final_str