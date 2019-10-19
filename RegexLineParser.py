import re


class RegexLineParser(object):
    def __init__(self):
        self.__line = ""
        self.__regex_pattern = r'(^[a-zA-Z]\b)\s+?(-?\b\d+\.?\d?\b)?\s*?([#|//].*)?$'
        # does not need to be compiled as it is the only pattern in use, python will cache it.

    def set_line(self, line):
        self.__line = line.strip()

    def is_line_blank(self):
        return not self.__line

    def parse_line(self):
        match = re.findall(self.__regex_pattern, self.__line)
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
