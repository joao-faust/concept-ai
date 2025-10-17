from .InputFile import InputFile

class InputTextFile(InputFile):
  def __init__(self, filepath: str) -> None:
    self.__filepath = filepath

  def get_data(self) -> list[str]:
    filtered_data = []

    with open(self.__filepath, 'r') as file:
      lines = file.readlines()

      for line in lines:
        line = line.replace('\n', '')

        if line in filtered_data:
          continue

        filtered_data.append(line)

    return filtered_data

  def get_filepath(self) -> str:
    return self.__filepath
