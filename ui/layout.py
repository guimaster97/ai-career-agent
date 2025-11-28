

import gradio as gr
from core.agent import chat_logic

# --- CONFIGURAÇÃO VISUAL (UI/UX) ---
# Criando um tema personalizado (Azul Profissional)
theme = gr.themes.Soft(
    primary_hue="blue",    # Cor dos botões e destaques (Tech)
    secondary_hue="slate", # Cor de fundo secundária (Sóbrio)
    neutral_hue="slate",   # Cor do texto e bordas
    font=[gr.themes.GoogleFont("Inter"), "ui-sans-serif", "system-ui"] # Fonte moderna
).set(
    button_primary_background_fill="*primary_600",
    button_primary_background_fill_hover="*primary_700",
    block_title_text_weight="600"
)

# CSS Customizado para centralizar e dar acabamento
custom_css = """
h1 {
    text-align: center;
    color: #1e293b; /* Slate 800 */
    font-weight: 800 !important;
}
.description {
    text-align: center;
    font-size: 1.1rem !important;
    color: #475569;
}
footer {
    display: none !important;
}
"""

# --- INTERFACE ---
with gr.Blocks(title="Agente de Carreira | Guilherme Ferreira") as demo:
    
    # Criamos uma linha para dividir a tela
    with gr.Row():
        
        # --- COLUNA DA ESQUERDA (BARRA LATERAL) ---
        # scale=1 significa que ela ocupa 1 parte da tela (menor)
        with gr.Column(scale=1):
            # Se você não tiver a foto ainda, comente a linha abaixo para não dar erro
            # gr.Image("me.png", show_label=False, show_download_button=False, show_fullscreen_button=False)
            
            gr.Markdown("### 🤖Agente de Carreira")
            gr.Markdown("""
            Este agente foi treinado com dados e informações sobre Guilherme Ferreira.
            
            **Estou aqui para responder suas dúvidas**
            
            """)
            
            # Botão de Link (Opcional)
            gr.Button("🔗 Ver meu LinkedIn", link="https://www.linkedin.com/in/guilherme-ferreira-971b46382")

        # --- COLUNA DA DIREITA (CHAT PRINCIPAL) ---
        # scale=4 significa que ela ocupa 4 partes da tela (maior)
        with gr.Column(scale=4):
            gr.ChatInterface(
                fn=chat_logic,
                title="", # Deixamos vazio pois já tem infos na barra lateral
                description="", 
                examples=[
                    "Como esse Agente foi construído?",
                    "Você aceita trabalhar remotamente?",
                    "Quais suas habilidades técnicas?",
                ],
                cache_examples=False,
                submit_btn="Enviar Pergunta",
                
                
                
                # Configuração do Chatbot (SEM o argumento type="messages")
                chatbot=gr.Chatbot(
                    height=500,
                    # Caminho das imagens: (Usuario, Bot)
                    # Coloque None no primeiro se não quiser ícone pro usuário
                    # Certifique-se que o arquivo 'me.png' existe na pasta!
                    avatar_images=("user_image.png", "me.png") 

                    
                )
            )


