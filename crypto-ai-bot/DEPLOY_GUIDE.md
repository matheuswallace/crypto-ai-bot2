# DEPLOY_GUIDE — crypto-ai-bot (modo simulação)

Este guia explica passo-a-passo como colocar o repositório no GitHub e realizar o deploy no Render usando Docker (ideal para rodar apenas com o celular ou PC).

1) Criar repositório no GitHub (nome sugerido: crypto-ai-bot).
2) Subir todos os arquivos e pastas do projeto (veja estrutura).
3) Criar conta no Render.com e conectar o repositório GitHub.
4) Criar Web Service → escolher Docker → Deploy.
5) Configurar variáveis de ambiente no painel do Render conforme .env.example.
6) Acessar a URL do serviço e abrir /docs para testar o endpoint POST /process.

OBS: O decisor via GPT está desativado por padrão (modo simulação). Para ativar futuramente, adicione OPENAI_API_KEY nas variáveis de ambiente e faça as alterações no controller se desejar.
