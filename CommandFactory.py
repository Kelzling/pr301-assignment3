import json

class CommandFactory(object):
    def __init__(self, drawer, lookup_file_name="command_lookup.json"):
        self.__drawer = drawer
        self.__command_pool = {}
        self.__command_lookup = self.__load_command_lookup(lookup_file_name)

    def __load_command_lookup(self, file_name):
        try:
            with open(file_name, 'r') as json_file:
                # load configurable language reference from file
                return json.load(json_file)  # convert to dict
        except (IOError, FileNotFoundError):
            raise FileNotFoundError(f"Command Lookup {file_name} not found")

    def get_command(self, command_text):
        if command_text in self.__command_pool:
            command = self.__command_pool[command_text]
        else:
            command = self.__create_command(command_text)
            self.__command_pool[command_text] = command

        return command

    def __create_command(self, command_text):
        pass
