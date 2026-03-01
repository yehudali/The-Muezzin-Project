import os

class FolderManege:
    def __init__(self, path_to_folder) -> None:
        self.path = path_to_folder

    def get_list_file(self)-> list[str]:
        return  os.listdir(self.path)
    