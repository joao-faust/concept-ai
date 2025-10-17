from os import path
from .OutputFile import OutputFile

class OutputFileManager:
  def __init__(self, output_file: OutputFile) -> None:
    self.__output_file = output_file

  def validate_filepath(self) -> None:
    filepath = self.__output_file.get_filepath()
    directory, _ = path.split(filepath)

    if not path.exists(directory):
      raise ValueError('The output file path is invalid.')

  def set_data(self, data: list[str]) -> None:
    self.__output_file.set_data(data)
