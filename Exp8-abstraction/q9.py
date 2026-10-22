# Q9. Create an abstract class CloudStorage with abstract methods upload_file(), download_file(), and delete_file(). Create subclasses representing different storage services and implement the operations.

from abc import ABC, abstractmethod

class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self):
        pass

    @abstractmethod
    def download_file(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass

class GoogleDrive(CloudStorage):
    def upload_file(self):
        print("File uploaded to Google Drive")

    def download_file(self):
        print("File downloaded from Google Drive")

    def delete_file(self):
        print("File deleted from Google Drive")

class OneDrive(CloudStorage):
    def upload_file(self):
        print("File uploaded to OneDrive")

    def download_file(self):
        print("File downloaded from OneDrive")

    def delete_file(self):
        print("File deleted from OneDrive")

class Dropbox(CloudStorage):
    def upload_file(self):
        print("File uploaded to Dropbox")

    def download_file(self):
        print("File downloaded from Dropbox")

    def delete_file(self):
        print("File deleted from Dropbox")

drive = GoogleDrive()
one_drive = OneDrive()
dropbox = Dropbox()

storage_services = [drive, one_drive, dropbox]

for storage in storage_services:
    storage.upload_file()
    storage.download_file()
    storage.delete_file()