# Some data and methods to help with the project

# https://stackoverflow.com/a/287944/2557030
class BColors:
    header = '\033[95m'
    ok_blue = '\033[94m'
    ok_cyan = '\033[96m'
    ok_green = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    end_dc = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'


class Console:
    def printHeader(self, text: str):
        print(f'{BColors.header}{text}{BColors.end_dc}')
