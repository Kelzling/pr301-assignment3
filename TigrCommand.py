class TigrCommand:
    def __init__(self, drawer_command, args):
        self.__drawer_command = drawer_command
        self.__args = args

    def execute(self, data=None):
        args = self.__args.copy()
        if data:
            args.append(data)

        return self.__drawer_command(*args)
