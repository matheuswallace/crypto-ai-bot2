# crypto-ai-bot

Esqueleto de bot de trading cripto para Binance Testnet, usando modelos dummy.

## Como usar no Render (ou Railway)
1. Crie repositório GitHub e cole os arquivos.
2. No Render, crie Web Service → Docker → conecte ao GitHub.
3. Configure variáveis de ambiente (veja `.env.example`).
4. Deploy → Render builda containers automaticamente.
5. Abra `/docs` para testar o endpoint `/process`.

## Segurança
- Use **Testnet** antes de qualquer operação real.
- Nunca exponha chaves.
- GPT está desativado no momento.
