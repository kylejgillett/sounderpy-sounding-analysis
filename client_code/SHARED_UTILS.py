import anvil.server
from anvil import alert 

def server_call(server_function_name, standby_label, *args, **kwargs):

  try:
    # Call the server function using its name and arguments
    result = anvil.server.call(server_function_name, *args, **kwargs)
    return result

  except anvil.server.UplinkDisconnectedError:
    # Handle server disconnection error
    standby_label.text = "SERVER ERROR: Connection to server was lost, but it's attempting to reconnect. Try again in 10 seconds"
    alert("Connection to server was lost, but it's attempting to reconnect. Try again in 10 seconds", title="Connection Error")
    return None

  except Exception as e:
    # Handle other unexpected errors (e.g., from server-side Python logic)
    standby_label.text = f"SERVER ERROR: {type(e).__name__}"
    print(f"Server call '{server_function_name}' failed with: {e}")
    return None