import colorama
print(dir(colorama))
# думаю что самые важные функции и методы в этой библиотеке это
# init() тк цвета без инициализации винды не будут работать
# fore, back и style тк это и есть функции для которых сделана colorama
# типа вот
from colorama import init, Fore, Back, Style

init(autoreset=True)

print(Fore.RED + "АШИБАЧКА")
print(Fore.GREEN + "йоу йоу йоу")
print(Back.BLUE + Style.BRIGHT + "веном")