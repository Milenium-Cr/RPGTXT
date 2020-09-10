from colorama import init

init()

def redbg(text):
    return f"\033[41m{text}\033[0m"

def red(text):
    return f"\033[31m{text}\033[0m"

def greenbg(text):
    return f"\033[42m{text}\033[0m"

def green(text):
    return f"\033[32m{text}\033[0m"

def bluebg(text):
    return f"\033[44m{text}\033[0m"

def blue(text):
    return f"\033[34m{text}\033[0m"

def yellow(text):
    return f"\033[33m{text}\033[0m

def gray(text):
    return f"\033[1;30m{text}\033[0m"

def blackbg(text):
    return f"\033[30m{text}\033[0m"
