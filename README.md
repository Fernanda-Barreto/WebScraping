


# Projeto de Web Scraping

Este projeto contém dois scripts principais:

## 1. Scraper de Notícias (G1)
Extrai manchetes, links e resumos de notícias do portal G1 e salva em `manchetes.json`.

## 2. Bot do Instagram
Faz login no Instagram, acessa um perfil e extrai a bio, salvando em `bio.json`.

---

## Dependências utilizadas
- requests
- beautifulsoup4
- selenium

Instale todas as dependências com:
```bash
pip install -r requirements.txt
```

Para o bot do Instagram, baixe o ChromeDriver compatível com sua versão do Chrome e coloque na pasta do projeto.

---

## Como executar

### Menu principal
Execute:
```bash
python main.py
```
Escolha a opção desejada para rodar cada script.

### Executar individualmente
- Scraper de notícias:
  ```bash
  python ./noticias/scraper_noticias.py
  ```
- Bot do Instagram:
  ```bash
  python ./instagram/bot_instagram.py
  ```

---

## Prints dos JSON gerados

### Scraper de Notícias
![manchetes.json](./docs/imgs/noticias.png)

### Bot do Instagram
![bio.json](./docs/imgs/bio.png)
---

## Vídeo de Funcionamento

Grave um vídeo mostrando a aplicação funcionando, suba no YouTube e coloque o link abaixo:

**Link do vídeo:** [Cole aqui o link do vídeo no YouTube]

## Link do Vídeo de Demonstração

