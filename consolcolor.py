C_END     = '\033[0m'
C_BOLD    = "\033[1m"
C_INVERSE = "\033[3m"

C_BLACK  = "\033[30m"
C_RED    = "\033[31m"
C_GREEN  = "\033[32m"
C_YELLOW = "\033[33m"
C_BLUE   = "\033[34m"
C_PURPLE = "\033[35m"
C_CYAN   = "\033[36m"
C_WHITE  = "\033[37m"

C_BGBLACK  = "\033[40m"
C_BGRED    = "\033[41m"
C_BGGREEN  = "\033[42m"
C_BGYELLOW = "\033[43m"
C_BGBLUE   = "\033[44m"
C_BGPURPLE = "\033[45m"
C_BGCYAN   = "\033[46m"
C_BGWHITE  = "\033[47m"

"""How to use?
print(C_YELLOW + "yellow" + C_END + C_Red + "red" + C_END) => (yellow)yellow(red)red
print(C_BOLD + C_BGBLUE + C_WHITE + "boldbluewhite" + C_END + C_Green + "g" + C_END) => (bold,background blue, white)boldbluewhite(green)g"""
