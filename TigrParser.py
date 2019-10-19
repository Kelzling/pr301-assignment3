from TIGr import AbstractParser
from RegexLineParser import RegexLineParser

"""
Uses Regular Expressions in Parser, Parsed from Configurable Lookup Table
Written by Kelsey Vavasour and Thomas Baines
Refactored by Kelsey Vavasour
"""


class TigrParser(AbstractParser):
    def __init__(self, command_factory, line_parser, exception_handler):
        super().__init__()
        self.__line_parser = line_parser
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
            self.__line_parser.set_line(current_line)
            if self.__line_parser.is_line_blank():
                continue

            try:
                command, data = self.__line_parser.parse_line()

                prepared_command = self.__command_factory.get_command(command)

                output = prepared_command.execute(data)
                self._log_drawer_output(output)
            except Exception as e:
                self.__exception_handler.display_and_exit(e, line_number=line_number, line=current_line)

    def _log_drawer_output(self, output):
        self.__output_log.append(output)
