from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import re
import time
from datetime import datetime

def fazer_login_e_extrair_bio(usuario, senha):
    """Faz login no Instagram e extrai apenas a bio do perfil @computacaounifavip_."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    chromedriver_path = r'C:\Users\fernn\Raspagem\chromedriver.exe'
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        print("[INFO] Abrindo página de login...")
        driver.get("https://www.instagram.com/accounts/login/")
        WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.NAME, "username")))

        print("[INFO] Preenchendo usuário e senha...")
        driver.find_element(By.NAME, "username").send_keys(usuario)
        driver.find_element(By.NAME, "password").send_keys(senha)
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        # Aguarda que não estejamos mais na página de login (evita confundir com url que já contém instagram.com)
        WebDriverWait(driver, 40).until(lambda d: '/accounts/login' not in d.current_url)
        time.sleep(1)

        # Ir direto para o perfil
        perfil = "computacaounifavip_"
        print(f"[INFO] Acessando perfil {perfil}...")
        driver.get(f"https://www.instagram.com/{perfil}/")

        # Espera o header do perfil carregar
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "header")))
        time.sleep(1)

        # Coleta possíveis blocos com texto dentro do header/section
        header = driver.find_element(By.TAG_NAME, "header")
        candidate_elements = header.find_elements(By.XPATH, ".//section//div//span | .//section//div//div | .//section//a")

        # Junta linhas únicas, mantendo ordem
        lines = []
        for el in candidate_elements:
            txt = el.text.strip()
            if not txt:
                continue
            for line in txt.splitlines():
                s = line.strip()
                if s and s not in lines:
                    lines.append(s)

        # Heurística para remover nomes, contagens e ruidos:
        cleaned = []
        username_plain = usuario.lstrip("@").strip().lower()
        for ln in lines:
            low = ln.lower()

            # remove o próprio username (aparece como primeira linha às vezes)
            if ln.strip().lower() == username_plain:
                continue

            # remove linhas que falam de publicações/seguidores/seguindo ou que são só números
            if re.search(r'publicaç|publicaç|publications|posts|seguidores|seguindo|followers|following', low):
                continue
            if re.fullmatch(r'[\d\.,\s]+', ln):
                continue

            # ignora pequenos ruidos
            if len(ln) <= 1:
                continue

            cleaned.append(ln)

        # Se o cleaned tem conteúdo, é provavel que seja a bio desejada
        if cleaned:
            # Junta mantendo quebras de linha (bio multiline)
            bio_texto = "\n".join(cleaned)
            print("[INFO] Bio reconstruída por heurística:")
            print(bio_texto)
        else:
            # fallback: tentar seletores conhecidos mais específicos
            bio_texto = None
            xpaths = [
                "//header//section//div[contains(@class,'-vDIg')]/span",
                "//header//section//div[2]//span",
                "//header//section//div//span"
            ]
            for xp in xpaths:
                try:
                    el = driver.find_element(By.XPATH, xp)
                    t = el.text.strip()
                    if t and not re.search(r'publicaç|seguidores|seguindo', t.lower()):
                        bio_texto = t
                        print(f"[INFO] Bio encontrada por XPath fallback ({xp}):")
                        print(bio_texto)
                        break
                except Exception:
                    continue

            if not bio_texto:
                # nada funcionou: salva page_source pra debug e reporta erro
                fname = "instagram/profile_page_source.html"
                with open(fname, "w", encoding="utf-8") as f:
                    f.write(driver.page_source)
                print(f"[WARN] Não foi possível encontrar a bio automaticamente. Page source salvo em '{fname}' para debug.")
                # informa quais linhas foram capturadas (útil para ajustar regras)
                bio_texto = "Bio não encontrada automaticamente. Linhas capturadas: " + "; ".join(lines[:10])

        # Monta dicionário e salva
        dados = {
            'perfil': f'@{perfil}',
            'bio': bio_texto,
            'data_extracao': datetime.now().isoformat()
        }
        salvar_json_bio(dados)

    except Exception as e:
        print(f"[ERRO] Exceção durante execução: {e}")
    finally:
        driver.quit()


def salvar_json_bio(dados):
    """Salva os dados da bio em um arquivo JSON."""
    try:
        with open('instagram/bio.json', 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        print("[INFO] Dados da bio salvos com sucesso em instagram/bio.json.")
    except Exception as e:
        print(f"[ERRO] Falha ao salvar JSON: {e}")


if __name__ == "__main__":
    import getpass
    usuario = input("Digite seu nome de usuário do Instagram (com ou sem @): ")
    senha = getpass.getpass("Digite sua senha do Instagram (oculta): ")
    fazer_login_e_extrair_bio(usuario, senha)
