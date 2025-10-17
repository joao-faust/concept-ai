from abc import ABC, abstractmethod

class OutputFile(ABC):
  @abstractmethod
  def set_data(self, data: list[str]) -> None:
    pass

  @abstractmethod
  def get_filepath(self) -> str:
    pass
