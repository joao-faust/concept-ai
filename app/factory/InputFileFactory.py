from os import path

from ..data.InputTextFile import InputTextFile
from ..data.InputFile import InputFile

class InputFileFactory:
  @staticmethod
  def build(filepath: str) -> InputFile:
    _, filename_ext = path.splitext(filepath)

    match filename_ext:
      case '.txt':
        return InputTextFile(filepath)
      case _:
        raise ValueError('The input file extension is invalid.')
