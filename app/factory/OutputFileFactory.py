from os import path

from ..data.OutputTextFile import OutputTextFile
from ..data.OutputFile import OutputFile

class OutputFileFactory:
  @staticmethod
  def build(filepath: str) -> OutputFile:
    _, filename_ext = path.splitext(filepath)

    match filename_ext:
      case '.txt':
        return OutputTextFile(filepath)
      case _:
        raise ValueError('The output file extension is invalid.')
