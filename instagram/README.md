# Bot do Instagram

## Descrição
Script que automatiza o login no Instagram, acessa um perfil e extrai a bio, salvando em `bio.json`.

## Como Usar
1. Instale as dependências:
   ```bash
   pip install selenium
   ```
2. Baixe o ChromeDriver compatível com seu Chrome e coloque na pasta do projeto.
3. Execute:
   ```bash
   python bot_instagram.py
   ```
   Ou pelo menu principal:
   ```bash
   python ../main.py
   ```

## Dependências
- selenium

## Exemplo de Saída (bio.json)
```json
{
    "perfil": "@computacaounifavip_",
    "bio": "Aqui estará o texto da bio do perfil."
}
```

## Print do JSON
Adicione aqui o print da tela do arquivo `bio.json` gerado.

## Vídeo de Funcionamento
Adicione aqui o link do vídeo no YouTube mostrando o funcionamento do bot.