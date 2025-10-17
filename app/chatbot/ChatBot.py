from abc import ABC, abstractmethod

class ChatBot(ABC):
  @abstractmethod
  def get_response(self, msg: str) -> str:
    pass
