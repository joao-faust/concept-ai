from .ChatBot import ChatBot
from google import genai

class Gemini(ChatBot):
  def __init__(self, model: str, key: str) -> None:
    self.__model = model
    self.__client = genai.Client(api_key=key)

  def get_response(self, msg: str) -> str:
    return self.__client.models.generate_content(model=self.__model, contents=msg).text
