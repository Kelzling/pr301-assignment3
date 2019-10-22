from abc import ABC, abstractmethod

""" Tiny Interpreted GRaphic = TIGR
Keep the interfaces defined below in your work.
 """


class AbstractDrawer(ABC):
    """ Responsible for defining an interface for drawing """

    @abstractmethod
    def select_pen(self, pen_num):
        pass

    @abstractmethod
    def pen_down(self):
        pass

    @abstractmethod
    def pen_up(self):
        pass

    @abstractmethod
    def go_along(self, along):
        pass

    @abstractmethod
    def go_down(self, down):
        pass

    @abstractmethod
    def draw_line(self, direction, distance):
        pass


class AbstractParser(ABC):
    def __init__(self, command_factory, exception_handler):
        self.__output_log = []
        self.__exception_handler = exception_handler
        self.__command_factory = command_factory

    @property
    def output_log(self):
        # readonly
        return self.__output_log

    def parse(self, raw_source):
        if type(raw_source) == str:  # defensively handles edge case where a single command was passed as a string
            raw_source = [raw_source]

        for line_number in range(0, len(raw_source) - 1):
            current_line = raw_source[line_number]

            if self._skip_line(current_line):
                continue

            try:
                command, data = self._parse_line(current_line)

                prepared_command = self.__command_factory.get_command(command)

                output = prepared_command.execute(data)
                self._log_drawer_output(output)
            except Exception as e:
                self.__exception_handler.display_and_exit(e, line_number=line_number, line=current_line)

    @abstractmethod
    def _skip_line(self, line) -> bool:
        pass

    @abstractmethod
    def _parse_line(self, line) -> (str, int):
        pass

    def _log_drawer_output(self, output):
        self.__output_log.append(output)


class AbstractSourceReader(ABC):
    """ responsible for providing source text for parsing and drawing
        Initiates the Draw use-case.
        Links to a parser and passes the source text onwards
    """

    def __init__(self, parser, optional_file_name=None):
        self.parser = parser
        self.file_name = optional_file_name
        self.source = []

    @abstractmethod
    def go(self):
        pass
