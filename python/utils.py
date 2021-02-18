import json
import tempfile

def read_file(filepath):
  """ 
  Args:
  Returns:
  """

def read_values_from_json(filepath):
  """ 
  Args:
    filepath (str): The full path of the json file.
  Returns:
    data (dict): The dictionary from the file.
  """
  

def create_temp_json_file(data):
    """Create temp json file

    Args:
        data (dict): The new data dictionary to write in the temp json.
    Returns:
        temp_file (str): Full path to temp config.
    """
    # Write data to temp json.
    temp_cfg = tempfile.mktemp(suffix=".json")
    with open(temp_cfg, "w") as output_file:
        json.dump(data, output_file, indent=4)
    return temp_cfg

