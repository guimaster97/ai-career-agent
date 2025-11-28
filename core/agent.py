

import json
from config.settings import client
from core.prompts import SYSTEM_PROMPT
from tools.manager import tools_list, available_functions


# Função para lidar com chamadas de ferramentas feitas pelo agente
def handle_tool_calls(tool_calls):
    results = []
    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        
        # 1. Segurança: Só executa se estiver na lista permitida
        if tool_name not in available_functions:
            results.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps({"error": f"Tool {tool_name} not found"})
            })
            continue

        # 2. Execução Segura
        try:
            arguments = json.loads(tool_call.function.arguments)
            print(f"🔧 Tool called: {tool_name} with args: {arguments}") # Log útil
            
            tool_function = available_functions[tool_name]
            result = tool_function(**arguments)
            
            # Garante que o resultado seja string (OpenAI exige content como string)
            content_str = json.dumps(result) if not isinstance(result, str) else result
            
        except Exception as e:
            print(f"❌ Erro na ferramenta {tool_name}: {e}")
            content_str = json.dumps({"error": f"Execution failed: {str(e)}"})

        results.append({
            "role": "tool",
            "content": content_str,
            "tool_call_id": tool_call.id
        })
        
    return results

def format_gradio_history(history):
    """
    Adaptador Universal: Funciona tanto para Gradio antigo (Listas) 
    quanto para Gradio novo (Dicionários).
    """
    if not history:
        return []
    
    # VERIFICAÇÃO INTELIGENTE:
    # Se o primeiro item já for um dicionário (Gradio 6.x), retorna como está.
    if isinstance(history[0], dict):
        return history

    # Se não for dicionário, assume que é o formato antigo (Lista de listas)
    # e faz a conversão manual.
    formatted_messages = []
    for item in history:
        # Garante segurança se a lista tiver tamanho diferente de 2
        if isinstance(item, (list, tuple)) and len(item) >= 2:
            user_msg, bot_msg = item[0], item[1]
            if user_msg:
                formatted_messages.append({"role": "user", "content": str(user_msg)})
            if bot_msg:
                formatted_messages.append({"role": "assistant", "content": str(bot_msg)})
                
    return formatted_messages

def chat_logic(message, history):
    """Função principal de chat que interage com o agente IA."""

    # 1. Converte o histórico antigo (formato de listas para formato OpenAI)
    history_openai = format_gradio_history(history)
    
    # 2. Monta a lista atual
    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history_openai + [{"role": "user", "content": message}]
    
    # 3. Loop principal para lidar com tool calls
    
    done = False
    attempts = 0
    
    while not done and attempts < 5:   # Limita a 5 tentativas
        attempts += 1
        
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                tools=tools_list, # Suas definições JSON
                tool_choice="auto", # Deixa a IA decidir
                max_tokens=350, # Limita a resposta para evitar custos altos, (aprox 300 palavras)
                temperature=0.7 # Um pouco de criatividade, mas sem alucinar muito
                
            )
        except Exception as e:
            return f"Erro de conexão com a OpenAI: {e}"

        response_message = response.choices[0].message
        finish_reason = response.choices[0].finish_reason

        # Se for apenas texto, retorna e encerra
        if finish_reason == "stop":
            return response_message.content

        # Se a IA quiser usar ferramentas
        elif finish_reason == "tool_calls":
            # 1. Adiciona a intenção da IA no histórico (Obrigatório pela OpenAI)
            messages.append(response_message)
            
            # 2. Executa as ferramentas
            tool_calls = response_message.tool_calls
            tool_results = handle_tool_calls(tool_calls)
            
            # 3. Adiciona os resultados no histórico
            messages.extend(tool_results)
            
            # O loop continua (while not done) para a IA ler o resultado e gerar a resposta final
        
        else:
            done = True # Outros motivos de parada

    return "Não consegui processar sua solicitação após várias tentativas."