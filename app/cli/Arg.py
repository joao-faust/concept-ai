class Arg:
  def __init__(self, key: str, value: str) -> None:
    self.__key = key
    self.__value = value

  def get_key(self) -> str:
    return self.__key

  def get_value(self, normalize=True) -> str:
    if normalize:
      return self.__value.strip().lower()
    return self.__value
