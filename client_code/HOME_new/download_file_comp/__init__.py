from ._anvil_designer import download_file_compTemplate
from anvil import *
import anvil.server


class download_file_comp(download_file_compTemplate):
  def __init__(self, files=None, **properties):
    """
        files: dict mapping file_type string -> anvil.media object
        Example: {'CSV': csv_file, 'TXT': txt_file, 'PDF': pdf_file}
        """
    self.init_components(**properties)
    self.files = files or {}

    # Update button visibility based on available files
    self.download_csv.visible = 'CSV' in self.files
    self.download_cm1.visible = 'CM1' in self.files
    self.download_sharppy.visible = 'SHARPPY' in self.files

  def csv_button_click(self, **event_args):
    if 'CSV' in self.files:
      anvil.media.download(self.files['CSV'])

  def cm1_button_click(self, **event_args):
    if 'CM1' in self.files:
      anvil.media.download(self.files['CM1'])

  def sharppy_button_click(self, **event_args):
    if 'SHARRPY' in self.files:
      anvil.media.download(self.files['SHARPPY'])