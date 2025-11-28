
# 🤖 AI Career Agent | Guilherme Ferreira

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-green)
![Gradio](https://img.shields.io/badge/Frontend-Gradio-orange)

> **"Show, don't tell."**
> Este projeto é um Agente de IA autônomo projetado para atuar como minha primeira camada de contato com recrutadores. Ele substitui o currículo estático por uma experiência conversacional interativa.

---

## 🚀 Teste Agora (Live Demo)
Converse com meu agente em tempo real no Hugging Face Spaces:
👉 **[Clique aqui para acessar o Agente] https://huggingface.co/spaces/gui97/agente_de_carreira-gui_ferreira**

---

## 💡 Sobre o Projeto
Sou um profissional em transição de carreira (Indústria -> Engenharia de IA). Criei este projeto para aplicar na prática os conceitos que estudei nos cursos de **Agentic AI** e **Python** da DeepLearning.AI (Andrew Ng).

O objetivo do agente é:
1.  Responder perguntas sobre minha trajetória e habilidades 24/7.
2.  Filtrar oportunidades alinhadas com meu perfil (Cultura e Tech Stack).
3.  Demonstrar domínio sobre integração de LLMs e Engenharia de Prompt.

## 🛠️ Stack Tecnológica
O projeto foi construído com foco em **simplicidade** e **eficiência** (Clean Code), sem o uso excessivo de frameworks complexos para demonstrar entendimento dos fundamentos.

* **Linguagem:** Python puro.
* **Cérebro (LLM):** OpenAI GPT-4o-mini (via API).
* **Arquitetura:** RAG Estático (Context Injection via System Prompt).
* **Interface:** Gradio (Web Chat UI).
* **Deploy:** Hugging Face Spaces (Cloud).

## 📂 Estrutura do Projeto
* `app.py`: Lógica principal, configuração do cliente OpenAI e interface Gradio.
* `dados.py`: A "Base de Conhecimento" do agente. Contém meu perfil, skills e regras de negócio estruturadas.
* `requirements.txt`: Dependências necessárias para o deploy.

## 🧠 Desafios & Aprendizados
Durante o desenvolvimento, foquei em resolver problemas reais de IA:
* **Controle de Alucinação:** Implementação de um *System Prompt* robusto para impedir que o agente invente habilidades que não possuo.
* **Design de Persona:** Ajuste do tom de voz para ser profissional, mas refletir minha realidade de autodidata.
* **Segurança:** Gerenciamento de chaves de API usando variáveis de ambiente (`dotenv` e Secrets).

## 📚 Certificações Aplicadas
Este projeto materializa o conhecimento adquirido em:
* *Agentic AI* (DeepLearning.AI / Andrew Ng)
* *AI Python for Beginners* (DeepLearning.AI)
* *Engenharia de Prompts* (Udemy)

---

### 📫 Contato
* **LinkedIn:** [Guilherme Ferreira](https://www.linkedin.com/in/guilherme-ferreira-971b46382/)
* **Email:** www.guiferreira70@gmail.com

---
*Desenvolvido  por Guilherme Ferreira.*