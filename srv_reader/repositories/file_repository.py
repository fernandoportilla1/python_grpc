import json


class FileRepository():
    __file_path = ''
    __file_open = None

    def __init__(self, file_path):
        self.__file_path = file_path

    def __open_file(self) -> None:
        if (self.__file_open == None):
            self.__file_open = open(self.__file_path, 'r')

    def __close_file(self) -> None:
        if (self.__file_open):
            self.__file_open.close()
            self.__file_open = None

    def read_data(self):
        try:
            data_read = []

            self.__open_file()
            data_read = json.load(self.__file_open)
            return data_read
        except Exception as exception:
            raise Exception('Error reading data: ' + str(exception))
        finally:
            self.__close_file()
