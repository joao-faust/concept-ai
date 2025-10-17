from sys import argv
from .Arg import Arg

class Args:
  def __init__(self, args: list[Arg]=[]) -> None:
    self.__args: list[Arg] = args

  def add(self, key: str, value: str) -> None:
    self.__args.append(Arg(key.replace('--', ''), value))

  def populate(self) -> None:
    args: list[str] = argv[1:]

    for arg in args:
      if arg.find('=') != -1:
        key, value = arg.split('=')
        self.add(key, value)

  def get(self, key: str) -> Arg | None:
    for arg in self.__args:
      if arg.get_key() == key:
        return arg
    return None
