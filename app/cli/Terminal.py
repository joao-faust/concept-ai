from .Print import Print

class Terminal:
  @staticmethod
  def print(text: str) -> Print:
    return Print(text)
