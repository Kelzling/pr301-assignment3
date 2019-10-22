from TIGr import AbstractParser
import re

"""
Uses Regular Expressions in Parser, Parsed from Configurable Lookup Table
Written by Kelsey Vavasour and Thomas Baines
Refactored by Kelsey Vavasour
"""


class RegexParser(AbstractParser):
    def __init__(self, command_factory, exception_handler):
        super().__init__(command_factory, exception_handler)
        self.__command_pattern = r'(^[a-zA-Z]\b)\s+?(-?\b\d+\.?\d?\b)?\s*?((#|/{2}).*)?$'
        self.__blank_line_pattern = r'^\s*((#|/{2}).*)?$'

    def _skip_line(self, line) -> bool:
        return bool(re.search(self.__blank_line_pattern, line))

    def _parse_line(self, line) -> (str, int):
        match = re.findall(self.__command_pattern, line)
        if match:
            groups = match[0]
            command = groups[0].upper()
            if groups[1]:
                data = int(round(float(groups[1])))
                """ Parser accepts decimals but silently rounds them in the background - all numbers passed are
                stored as integers"""
            else:
                data = None

            return command, data
        else:
            raise ValueError(
                f"Line did not match expected syntax")
