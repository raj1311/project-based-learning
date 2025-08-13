import pandas as pd
import requests
from pathlib import Path


def download_from_drive(file_id: str, dest_path: str = "options_data.csv") -> pd.DataFrame:
    """Download CSV options data from Google Drive.

    Args:
        file_id: Google Drive file ID of the CSV file.
        dest_path: Destination path to save the CSV locally.

    Returns:
        DataFrame loaded from the downloaded CSV file.
    """
    url = f"https://drive.google.com/uc?id={file_id}"
    dest = Path(dest_path)
    response = requests.get(url)
    response.raise_for_status()
    dest.write_bytes(response.content)
    return pd.read_csv(dest)
