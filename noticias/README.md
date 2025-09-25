# Scraper de Notícias (G1)

## Descrição
Script que extrai manchetes, links e resumos de notícias do portal G1 e salva em `manchetes.json`.

## Como Usar
1. Instale as dependências:
   ```bash
   pip install requests beautifulsoup4
   ```
2. Execute:
   ```bash
   python scraper_noticias.py
   ```
   Ou pelo menu principal:
   ```bash
   python ../main.py
   ```

## Dependências
- requests
- beautifulsoup4

## Exemplo de Saída (manchetes.json)
```json
[
    {
        "titulo": "Exemplo de Título da Notícia",
        "link": "https://g1.globo.com/exemplo",
        "resumo": "Exemplo de resumo da notícia que será extraído."
    }
]
```

## Print do JSON
Adicione aqui o print da tela do arquivo `manchetes.json` gerado.

## Vídeo de Funcionamento
Adicione aqui o link do vídeo no YouTube mostrando o funcionamento do scraper.