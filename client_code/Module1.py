import anvil.server

@anvil.server.callable
def anvil_uplink_heartbeat():
  """
  An empty function that is called by the Uplink server's Watchdog 
  thread to keep the network connection alive during long tasks.
  """
  pass