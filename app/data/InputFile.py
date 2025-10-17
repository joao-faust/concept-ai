from abc import ABC, abstractmethod

class InputFile(ABC):
  @abstractmethod
  def get_data(self) -> list[str]:
    pass

  @abstractmethod
  def get_filepath(self) -> str:
    pass
