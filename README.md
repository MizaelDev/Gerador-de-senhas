# Gerador de Senhas

Projeto que fiz enquanto estudava cibersegurança. A ideia era juntar duas coisas que tava aprendendo ao mesmo tempo: como senhas são comprometidas em vazamentos, e como fazer uma interface web.

## O que faz

- Gera senhas com tamanho e complexidade configuráveis
- Verifica se a senha já apareceu em algum vazamento de dados, usando a API do [Have I Been Pwned](https://haveibeenpwned.com/)
- Calcula a entropia da senha (quanto mais bits, mais difícil de quebrar)

## A parte que achei mais interessante

A verificação usa uma técnica chamada **k-anonymity**. O problema era: como verificar se uma senha foi vazada sem enviar a senha pra nenhum servidor?

A solução é bem interessante:

1. A senha é convertida em hash SHA-1 localmente, no browser
2. Só os 5 primeiros caracteres do hash vão pra API
3. A API retorna todos os hashes que começam com esses 5 caracteres (~500 resultados)
4. A comparação final acontece localmente

Ou seja, nem o próprio HIBP sabe qual senha foi verificada. Aprendi isso pesquisando a documentação da API e achei que valia a pena implementar do jeito certo.

## Tecnologias

- HTML, CSS e JS puro no frontend
- `crypto.subtle` (Web Crypto API) para o SHA-1 no browser
- Python + Flask no backend
- API pública do Have I Been Pwned

## Como rodar o backend localmente

```bash
cd backend
pip install -r requirements.txt
python app.py
```

O `index.html` funciona sozinho sem o backend — a verificação HIBP é feita direto no browser.

## Status

Projeto de portfólio, feito enquanto me formava em cibersegurança. Ainda quero adicionar um histórico de senhas geradas (localStorage) e talvez uma estimativa de tempo para força bruta.
