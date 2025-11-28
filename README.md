
# 🤖 Agente de Carreira | Guilherme Ferreira

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-API-green?style=for-the-badge&logo=openai&logoColor=white)
![Gradio](https://img.shields.io/badge/Frontend-Gradio-orange?style=for-the-badge&logo=gradio&logoColor=white)
![Status](https://img.shields.io/badge/Status-Production-success?style=for-the-badge)

> **"First Principles over Frameworks."**

Este projeto é um **Agente de IA Autônomo** projetado para atuar como meu representante profissional inicial. Ele conversa com recrutadores, tira dúvidas sobre minha trajetória e captura oportunidades de contato (Leads) em tempo real.

🔗 **[Acesse o Agente Online no Hugging Face](https://huggingface.co/spaces/gui97/agente-guilherme-ferreira)** 

---

## 🎯 Objetivo do Projeto

Diferente da maioria dos chatbots que utilizam frameworks de alto nível (como LangChain ou CrewAI), este agente foi construído em **Python Puro (Vanilla Python)**.

**Por quê?**
Como desenvolvedor em transição de carreira, meu objetivo foi demonstrar domínio sobre os fundamentos da Engenharia de IA:
1.  **Controle de Estado:** Gerenciamento manual do histórico de mensagens e contexto.
2.  **Function Calling (Tool Use):** Implementação da lógica de decisão e execução de ferramentas "na mão".
3.  **Loop de Agente (ReAct):** Construção da arquitetura de raciocínio (Thought -> Action -> Observation) sem abstrações.

---

## ⚙️ Arquitetura e Stack

O projeto segue uma arquitetura modular para facilitar manutenção e escalabilidade.

* **Core:** Python 3.x
* **LLM:** OpenAI GPT-4o-mini (Custo-eficiente e rápido).
* **Interface:** Gradio (Blocks & ChatInterface).
* **Notificações:** Pushover API (Notifica meu celular instantaneamente quando um recrutador deixa contato, ou quando faz uma pergunta que o agente não tem aresposta).
* **Deploy:** Hugging Face Spaces.

### Estrutura de Pastas
```text
projeto/
├── config/          # Gerenciamento de chaves e variáveis de ambiente
├── core/            # Cérebro do agente (Loop principal e Prompts)
├── data/            # Base de conhecimento (Perfil Profissional)
├── tools/           # Ferramentas (Funções Python + JSON Schemas)
├── ui/              # Camada visual (Gradio Layout & CSS)
├── app.py           # Ponto de entrada da aplicação
└── requirements.txt # Dependências

## 🛠️ Funcionalidades (Tools)

O agente possui acesso a ferramentas que ele decide usar autonomamente:

1. `record_user_details`:
    
    - **Gatilho:** Quando um recrutador demonstra interesse ou oferece uma vaga.
        
    - **Ação:** Captura Nome, Email e Notas, salva o lead e envia uma notificação Push para o meu celular.
        
2. `record_unknown_question`:
    
    - **Gatilho:** Quando o usuário faz uma pergunta que não consta na base de conhecimento.
        
    - **Ação:** Registra a dúvida para que eu possa responder pessoalmente depois.
        

---

## 🚀 Como Rodar Localmente

Siga os passos abaixo para clonar e executar o agente na sua máquina.

### 1. Clone o repositório

Bash

```
git clone [git clone https://huggingface.co/spaces/gui97/agente-guilherme-ferreira]
cd agente-guilherme-ferreira
```

### 2. Crie um ambiente virtual

Bash

```
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate
```

### 3. Instale as dependências

Bash

```
pip install -r requirements.txt
```

### 4. Configure as Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto e adicione suas chaves:

Snippet de código

```
OPENAI_API_KEY=sk-proj-sua-chave-aqui
PUSHOVER_USER=sua-user-key
PUSHOVER_TOKEN=seu-app-token
```

### 5. Execute

Bash

```
python app.py
```

O projeto estará rodando em `http://localhost:7860`.

---

## 👤 Sobre o Autor

**Guilherme Ferreira** _Desenvolvedor em Transição (Indústria -> Tech)_

Trago a disciplina e resiliência de 3+ anos na indústria para o mundo do desenvolvimento de software. Focado em Python, Automação e IA Agêntica.

- **LinkedIn:** [linkedin.com/in/seu-perfil](https://www.linkedin.com/in/guilherme-ferreira-971b46382)
    
- **GitHub:** [github.com/guimaster97](https://www.google.com/search?q=https://github.com/guimaster97)
- **Email:** www.guiferreira70@gmail.com  

---

_Este projeto é Open Source sob a licença MIT._
