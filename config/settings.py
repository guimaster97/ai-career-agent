
import os
from dotenv import load_dotenv
from openai import OpenAI

# Carrega variáveis de ambiente
load_dotenv()

# Configurações da API
openai_key = os.getenv("OPENAI_API_KEY")
pushover_user = os.getenv("PUSHOVER_USER")
pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_url = "https://api.pushover.net/1/messages.json"
         

# Inicializa o cliente OpenAI (Singleton)
client = OpenAI(api_key=openai_key)

