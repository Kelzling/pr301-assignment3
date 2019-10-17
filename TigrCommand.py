class TigrCommand:
    def __init__(self, drawer_command, args):
        self.__drawer_command = drawer_command
        self.__args = args

    def execute(self, data=None):
        if data:
            self.__args.append(data)

        return self.__drawer_command(self.__args)
