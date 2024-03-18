import anvil.server
import sounderpy as spy
import anvil.media
from datetime import datetime as dt
from urllib.request import urlopen

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
import threading
import queue

# Lock to ensure thread-safe access to shared resources
lock = threading.Lock()

# Queue to store tasks (requests)
task_queue = queue.Queue()

def worker():
    while True:
        # Get a task from the queue
        task = task_queue.get()

        # Exit the loop if a sentinel value is received (indicating the worker should stop)
        if task is None:
            break

        # Process the task based on the function name
        if task["function"] == "raob_function":
            result = process_raob_function(*task["args"])

        elif task["function"] == "acars_list_function":
            result = process_acars_list_function(*task["args"])

        elif task["function"] == "acars_function":
            result = process_acars_function(*task["args"])

        elif task["function"] == "bufkit_function":
            result = process_bufkit_function(*task["args"])

        elif task["function"] == "reanl_function":
            result = process_reanl_function(*task["args"])

        # Mark the task as done
        task_queue.task_done()

# Start a worker thread
worker_thread = threading.Thread(target=worker)
worker_thread.start()





# Example functions that may require different variables
def process_raob_function(site_id, year, month, day, hour, color_blind, dark_mode, hodo, style, storm_motion):
    with lock:
        clean_data = spy.get_obs_data(str(site_id), str(year), str(month), str(day), str(hour))

        label_txt = f"{clean_data['site_info']['valid-time'][3]}Z Launch for {clean_data['site_info']['site-id']}, {clean_data['site_info']['site-name']} at {clean_data['site_info']['valid-time'][1]}-{clean_data['site_info']['valid-time'][2]}-{clean_data['site_info']['valid-time'][0]}-{clean_data['site_info']['valid-time'][3]}Z"
        
        if hodo == True:  
             spy.build_hodograph(clean_data, dark_mode=dark_mode, storm_motion=storm_motion, save=True, filename='sounderpy_sounding')
        else:
             spy.build_sounding(clean_data, style=style, dark_mode=dark_mode, storm_motion=storm_motion, special_parcels='simple', color_blind=color_blind, save=True)
          
        image = anvil.media.from_file('sounderpy_sounding.png', 'image/jpeg')

        print(dt.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

        return image, label_txt

def process_acars_list_function(year, month, day, hour):
    with lock:

        profiles_list = spy.acars_data(str(year), str(month), str(day), str(hour)).list_profiles()

        print(dt.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

        return profiles_list

def process_acars_function(profile_id, year, month, day, hour, color_blind, dark_mode, hodo, style, storm_motion):
    with lock:
        clean_data = spy.acars_data(str(year), str(month), str(day), str(hour)).get_profile(profile_id)

        label_txt = f"{clean_data['site_info']['valid-time'][3]}Z Launch for {clean_data['site_info']['site-id']}, {clean_data['site_info']['site-name']} at {clean_data['site_info']['valid-time'][1]}-{clean_data['site_info']['valid-time'][2]}-{clean_data['site_info']['valid-time'][0]}-{clean_data['site_info']['valid-time'][3]}Z"

        if hodo == True:  
             spy.build_hodograph(clean_data, dark_mode=dark_mode, storm_motion=storm_motion, save=True, filename='sounderpy_sounding')
        else:
             spy.build_sounding(clean_data, style=style, dark_mode=dark_mode, color_blind=color_blind, storm_motion=storm_motion, special_parcels='simple', save=True)

        image =anvil.media.from_file('sounderpy_sounding.png', 'image/jpeg')

        print(dt.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

        return image, label_txt

def process_bufkit_function(model, bufkit_site, fcst_hr, color_blind, dark_mode, hodo, style, storm_motion):
    with lock:
        clean_data = spy.get_bufkit_data(str(model), str(bufkit_site), int(fcst_hr))

        label_txt = f"{clean_data['site_info']['valid-time'][3]}Z Launch for {clean_data['site_info']['site-id']}, {clean_data['site_info']['site-name']} at {clean_data['site_info']['valid-time'][1]}-{clean_data['site_info']['valid-time'][2]}-{clean_data['site_info']['valid-time'][0]}-{clean_data['site_info']['valid-time'][3]}Z"

        if hodo == True:  
             spy.build_hodograph(clean_data, dark_mode=dark_mode, storm_motion=storm_motion, save=True, filename='sounderpy_sounding')
        else:
             spy.build_sounding(clean_data, style=style, dark_mode=dark_mode, storm_motion=storm_motion, special_parcels='simple', color_blind=color_blind, save=True)
        image = anvil.media.from_file('sounderpy_sounding.png', 'image/jpeg')

        print(dt.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

        return image, label_txt


def process_reanl_function(latlon, year, month, day, hour, color_blind, dark_mode, hodo, style, storm_motion):
    with lock:
        clean_data = spy.get_model_data('rap-ruc', latlon, str(year), str(month), str(day), str(hour))

        label_txt = f"{clean_data['site_info']['valid-time'][3]}Z  Reanalysis for {clean_data['site_info']['site-latlon']} at {clean_data['site_info']['valid-time'][1]}-{clean_data['site_info']['valid-time'][2]}-{clean_data['site_info']['valid-time'][0]}-{clean_data['site_info']['valid-time'][3]}Z"

        if hodo == True:  
             spy.build_hodograph(clean_data, dark_mode=dark_mode, storm_motion=storm_motion, save=True, filename='sounderpy_sounding')
        else:
             spy.build_sounding(clean_data, style=style, dark_mode=dark_mode, storm_motion=storm_motion, special_parcels='simple', color_blind=color_blind, save=True)

        image = anvil.media.from_file('sounderpy_sounding.png', 'image/jpeg')

        print(dt.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

        return image, label_txt


#####################
# GET RAOB FUNCTION #
#####################
@anvil.server.callable
def get_raob_sounding(site_id, year, month, day, hour, color_blind, dark_mode, hodo, style, storm_motion):
    # Add the task (request) to the queue
    task_queue.put({"function": "raob_function", "args": (site_id, year, month, day, hour, color_blind, dark_mode, hodo, style, storm_motion)})

    image, label_txt = process_raob_function(site_id, year, month, day, hour, color_blind, dark_mode, hodo, style, storm_motion)

    return image, label_txt


###########################
# GET ACARS LIST FUNCTION #
###########################
@anvil.server.callable
def get_acars_profile_list(year, month, day, hour):
    # Add the task (request) to the queue
    task_queue.put({"function": "acars_list_function", "args": (year, month, day, hour)})

    acars_list = process_acars_list_function(year, month, day, hour)

    return acars_list


######################
# GET ACARS FUNCTION #
######################
@anvil.server.callable
def get_acars_sounding(profile_id, year, month, day, hour, color_blind, dark_mode, hodo, style, storm_motion):
    # Add the task (request) to the queue
    task_queue.put({"function": "acars_function", "args": (profile_id, year, month, day, hour, color_blind, dark_mode, hodo, style, storm_motion)})

    image, label_txt = process_acars_function(profile_id, year, month, day, hour, color_blind, dark_mode, hodo, style, storm_motion)

    return image, label_txt


#######################
# GET BUFKIT FUNCTION #
#######################
@anvil.server.callable
def get_bufkit_sounding(model, bufkit_site, fcst_hr, color_blind, dark_mode, hodo, style, storm_motion):
    # Add the task (request) to the queue
    task_queue.put({"function": "bufkit_function", "args": (model, bufkit_site, fcst_hr, color_blind, dark_mode, hodo, style, storm_motion)})

    image, label_txt = process_bufkit_function(model, bufkit_site, fcst_hr, color_blind, dark_mode, hodo, style, storm_motion)

    return image, label_txt


#######################
# GET REANL FUNCTION #
#######################
@anvil.server.callable
def get_reanl_sounding(latlon, year, month, day, hour, color_blind, dark_mode, hodo, style, storm_motion):
    # Add the task (request) to the queue
    task_queue.put({"function": "reanl_function", "args": (latlon, year, month, day, hour, color_blind, dark_mode, hodo, style, storm_motion)})

    image, label_txt = process_reanl_function(latlon, year, month, day, hour, color_blind, dark_mode, hodo, style, storm_motion)

    return image, label_txt


###########################
# GET MODEL RUNS FUNCTION #
###########################
@anvil.server.callable
def get_latest_run():
    
    # make sure variables are in the correct case
    text_list = []
    station = 'KMOP'
    
    for model in ['gfs', 'nam', 'namnest', 'rap', 'hrrr', 'sref', 'hiresw']: 
        if model == 'gfs':
            model3 = 'gfs3' 
        else:
            model3 = model
        data_conn = f'http://www.meteo.psu.edu/bufkit/data/{model.upper()}/{model3}_{station.lower()}.buf'

        # GET BUFKIT FILE 
        # CONVERT LINES OF BYTES TO STRINGS 
        buf_file = urlopen(data_conn)
        buf_file = [str(line).replace("b'", "").replace("\\r\\n'", "") for line in buf_file]

        # SET UP DATE / TIME OBJECTS FROM THE BUFKIT FILE
        run_time = buf_file[4][buf_file[4].index('TIME') + 7:(buf_file[4].index('TIME')+9)+9]
        
        text_list.append(f'{str.upper(model)}: {run_time[2:4]}/{run_time[4:6]} {run_time[7:9]}Z')
      
        final_str = ''
        for i, string in enumerate(text_list):
          final_str += string
          if i < len(text_list) - 1:
              final_str += " | "
    
    return final_str