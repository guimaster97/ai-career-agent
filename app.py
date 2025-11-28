

from ui.layout import demo
import gradio as gr


# --- RODAR APLICATIVO ---

if __name__ == "__main__":
    # Controle de Concorrência (Fila)
    # Isso impede que 50 pessoas usem a função 'chat' ao mesmo tempo e estoure sua memória/limite
    demo.queue(default_concurrency_limit=5)
    
    # Launch
    demo.launch(
        server_name="0.0.0.0", # Necessário para deploy em container/nuvem
        server_port=7860, 
        
        share=False            # Mude para True se quiser um link temporário para testar agora
    )