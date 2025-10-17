from .OutputFile import OutputFile

class OutputTextFile(OutputFile):
  def __init__(self, filepath: str) -> None:
    self.__filepath = filepath

  def set_data(self, data: list[str]) -> None:
    with open(self.__filepath, 'a') as file:
      for row in data:
        question, response = row.split(':')
        capitalized_question = question.upper()
        formatted_row = f'{capitalized_question} => {response}\n\n'
        file.write(formatted_row)

  def get_filepath(self) -> str:
    return self.__filepath
