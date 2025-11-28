
import json
import requests
from config.settings import pushover_user , pushover_token, pushover_url

# --- FUNÇÕES INTERNAS (Backend) ---

def _push_notification(message: str) -> bool:
    """Função interna segura para enviar push."""
    try:
        payload = {"user": pushover_user, "token": pushover_token, "message": message}
        response = requests.post(pushover_url, data=payload, timeout=5) # Timeout evita travamento
        response.raise_for_status()
        return True
    except Exception as e:
        print(f"Erro ao enviar push: {e}")
        return False

# --- TOOLS DO AGENTE (Expostas para a IA) ---

def record_user_details(email: str, name: str = "Não informado", notes: str = "N/A", role: str = "general") -> str:
    """
    Registra um contato interessado (recrutador ou geral) e notifica o Guilherme.
    """
    msg = f"NOVO LEAD ({role.upper()}): {name} | Email: {email} | Notas: {notes}"
    print(msg) # Log local
    
    success = _push_notification(msg)
    if success:
        return json.dumps({"status": "success", "message": "Interesse registrado e notificado."})
    else:
        return json.dumps({"status": "error", "message": "Falha na notificação, mas dados salvos localmente."})

def record_unknown_question(question: str) -> str:
    """
    Registra uma pergunta que o agente não soube responder com base no perfil.
    """
    msg = f"PERGUNTA DESCONHECIDA: {question}"
    print(msg)
    _push_notification(msg)
    return json.dumps({"status": "logged", "message": "Pergunta enviada para análise do Guilherme."})

# JSON Schema para as ferramentas

# Definição da ferramenta record_user_details
record_user_details_json = {
    "name": "record_user_details",
    "description": "Use this tool to record that a user is interested in being in touch and provided an email address",
    "parameters": {
        "type": "object",
        "properties": {
            "email": {
                "type": "string",
                "description": "The email address of this user"
            },
            "name": {
                "type": "string",
                "description": "The user's name, if they provided it"
            }
            ,
            "notes": {
                "type": "string",
                "description": "Any additional information about the conversation that's worth recording to give context"
            }
        },
        "required": ["email"],
        "additionalProperties": False
    }
}

# Definição da ferramenta record_unknown_question
record_unknown_question_json = {
    "name": "record_unknown_question",
    "description": "Always use this tool to record any question that couldn't be answered as you didn't know the answer",
    "parameters": {
        "type": "object",
        "properties": {
            "question": {
                "type": "string",
                "description": "The question that couldn't be answered"
            },
        },
        "required": ["question"],
        "additionalProperties": False
    }
}
      

# --- 1. MAPEAMENTO DE EXECUÇÃO (Python) ---
# Dicionário que conecta o "nome da ferramenta" à "função real"
available_functions = {
    "record_user_details": record_user_details,
    "record_unknown_question": record_unknown_question
}

# --- 2. LISTA DE DEFINIÇÕES (OpenAI) ---
# Isso é o que enviamos para o GPT saber o que existe
tools_list = [
    {"type": "function", "function": record_user_details_json, "strict": True},          # "strict": True Garante adesão 100% ao schema
    {"type": "function", "function": record_unknown_question_json, "strict": True}
]