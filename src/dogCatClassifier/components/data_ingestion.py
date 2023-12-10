import os
import urllib.request as request
from zipfile import ZipFile
from dogCatClassifier.entity import DataIngestionConfig
from pathlib import Path
from tqdm import tqdm

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )

    def _get_updated_list_of_files(self, list_of_files):
        return [f for f in list_of_files if f.endswith(".jpg") and ("Cat" in f or "Dog" in f)]
    
    def unzip_and_clean_file(self):
        with ZipFile(file=self.config.local_data_file, mode="r") as zf:
            list_of_files = zf.namelist()
            # Get only images in Dog and Cat folder
            updated_list_of_files = self._get_updated_list_of_files(list_of_files)
            
            for file_path in tqdm(updated_list_of_files):
                zf.extract(file_path, path=self.config.unzip_dir)
                new_file_path = Path(os.path.join(self.config.unzip_dir, file_path))

                if os.path.getsize(new_file_path) == 0:
                    print(f"Removing 0KB file in {new_file_path}")
                    os.remove(new_file_path)  