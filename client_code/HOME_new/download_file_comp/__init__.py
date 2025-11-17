from ._anvil_designer import download_file_compTemplate
from anvil import *
import anvil.server


class download_file_comp(download_file_compTemplate):
  
  def __init__(self, files=None, **properties):
    self.init_components(**properties)
    self.set_files(files or {})

  def set_files(self, files):
    self.files = files

  def csv_button_click(self, **event_args):
    if 'CSV' in self.files:
      anvil.media.download(self.files['CSV'])

  def cm1_button_click(self, **event_args):
    if 'CM1' in self.files:
      anvil.media.download(self.files['CM1'])

  def sharppy_button_click(self, **event_args):
    if 'SHARPPY' in self.files:
      anvil.media.download(self.files['SHARPPY'])