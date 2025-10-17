class Print:
  RED = '\033[91m'
  GREEN = '\033[92m'
  RESET = '\033[0m'

  def __init__(self, text: str) -> None:
    self.__text = text

  def default(self) -> None:
    print(self.__text)

  def red(self) -> None:
    print(f'{Print.RED}{self.__text}{Print.RESET}')

  def green(self) -> None:
    print(f'{Print.GREEN}{self.__text}{Print.RESET}')
