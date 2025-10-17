from os import path
from .InputFile import InputFile

class InputFileManager:
  def __init__(self, input_file: InputFile) -> None:
    self.__input_file = input_file

  def validate_filepath(self) -> None:
    filepath = self.__input_file.get_filepath()

    if not path.exists(filepath):
      raise ValueError('The input file path is invalid.')

  def get_data(self) -> str:
    return self.__input_file.get_data()
