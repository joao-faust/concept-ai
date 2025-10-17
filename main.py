from traceback import print_exc
from dotenv import load_dotenv
from os import getenv

from app.factory.OutputFileFactory import OutputFileFactory
from app.factory.InputFileFactory import InputFileFactory
from app.data.OutputFileManager import OutputFileManager
from app.data.InputFileManager import InputFileManager
from app.chatbot.ChatBotManager import ChatBotManager
from app.chatbot.Gemini import Gemini
from app.cli.Terminal import Terminal
from app.cli.Args import Args

try:
  load_dotenv()

  CHAT_BOT_KEY = getenv('CHAT_BOT_KEY')

  Terminal.print('Processing...').default()

  args = Args()
  args.populate()

  lang = args.get('lang').get_value()
  input_path = args.get('input').get_value()
  output_path = args.get('output').get_value()

  gemini = Gemini('gemini-2.5-pro', CHAT_BOT_KEY)
  chat_bot_manager = ChatBotManager(gemini)

  input_file = InputFileFactory.build(input_path)
  input_file_manager = InputFileManager(input_file)
  output_file = OutputFileFactory.build(output_path)
  output_file_manager = OutputFileManager(output_file)

  input_file_manager.validate_filepath()
  output_file_manager.validate_filepath()

  concepts = input_file_manager.get_data()
  concepts_response = chat_bot_manager.get_concepts_response(concepts, lang)
  concepts_response_list = concepts_response.split('\n')

  output_file_manager.set_data(concepts_response_list)

  Terminal.print('The concepts have been generated.').green()
except ValueError as error:
  Terminal.print(f'[ERROR] {error}').red()
except Exception as error:
  if getenv('MODE') == 'dev':
    print_exc()
  else:
    msg = 'Run the script in dev mode to get more details.'
    Terminal.print(f'[UNEXPECTED ERROR] {msg}').red()
