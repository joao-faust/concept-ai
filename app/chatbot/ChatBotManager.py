from .ChatBot import ChatBot

class ChatBotManager:
  def __init__(self, chat_bot: ChatBot):
    self.__chat_bot = chat_bot

  def get_concepts_response(self, concepts: list[str], lang: str) -> str:
    concepts_list = ', '.join(concepts)

    return self.__chat_bot.get_response(
      f'For each item in the list {concepts_list}, explain in {lang} in exactly one ' +
      'paragraph. Do not add extra information, do not mention unrelated topics, ' +
      'and reply strictly in the format: item:explanation\\n. No Markdown, no bullet ' +
      'points, no numbering.'
    )
