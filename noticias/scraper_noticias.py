import requests
from bs4 import BeautifulSoup
import json

def extrair_noticias():
    """Extrai títulos, links e resumos do site G1 ou Books to Scrape."""
    import sys
    url = input("Digite a URL do site de notícias (padrão G1): ") or 'https://www.g1.globo.com/'
    headers = {'User-Agent': 'Mozilla/5.0'}
    print(f"Acessando {url}...")
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
        return None
    soup = BeautifulSoup(response.text, 'html.parser')
    manchetes = []
    if 'g1.globo.com' in url:
        noticias = soup.find_all('div', class_='feed-post-body')
        for noticia in noticias:
            titulo_tag = noticia.find('a', class_='feed-post-link')
            resumo_tag = noticia.find('div', class_='feed-post-body-resumo')
            titulo = titulo_tag.text.strip() if titulo_tag else 'Título não encontrado'
            link = titulo_tag['href'] if titulo_tag else 'Link não encontrado'
            resumo = resumo_tag.text.strip() if resumo_tag else 'Resumo não disponível'
            manchetes.append({
                'titulo': titulo,
                'link': link,
                'resumo': resumo,
                'data_extracao': __import__('datetime').datetime.now().isoformat()
            })
    elif 'books.toscrape.com' in url:
        livros = soup.select('article.product_pod')
        for livro in livros:
            titulo_tag = livro.h3.a
            titulo = titulo_tag['title'] if titulo_tag else 'Título não encontrado'
            link = 'http://books.toscrape.com/' + titulo_tag['href'] if titulo_tag else 'Link não encontrado'
            resumo = livro.p['class'][0] if livro.p else 'Resumo não disponível'
            manchetes.append({
                'titulo': titulo,
                'link': link,
                'resumo': resumo,
                'data_extracao': __import__('datetime').datetime.now().isoformat()
            })
    else:
        print("Site não suportado para extração automática.")
        return None
    print(f"Extraídas {len(manchetes)} manchetes/livros.")
    return manchetes

def salvar_json(dados):
    """Salva os dados em um arquivo JSON."""
    if dados:
        try:
            with open('noticias/manchetes.json', 'w', encoding='utf-8') as f:
                json.dump(dados, f, indent=4, ensure_ascii=False)
            print("Dados salvos com sucesso em manchetes.json.")
        except Exception as e:
            print(f"Erro ao salvar JSON: {e}")

if __name__ == "__main__":
    manchetes_extraidas = extrair_noticias()
    salvar_json(manchetes_extraidas)