# escrever passo a passo sempre
import time
import pyautogui
pyautogui.PAUSE = 0.7
# passo 1: entrar no sistema da empresa
pyautogui.press("win")
pyautogui.write('chrome')
pyautogui.press('enter')

# entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press('enter')

#pausa pro site carregar
time.sleep(3)

# passo 2: fazer login
pyautogui.click(x=775, y=397)
pyautogui.write("gabrielpenisgrande@hotmail.com")
pyautogui.press("tab")
pyautogui.write("teste")
pyautogui.press("tab")
pyautogui.press('enter')

# passo 3: importar a base de dados do produto >>>>> pip install pandas numpy openpyxl
import pandas
tabela = pandas.read_csv("produtos.csv")
for linha in tabela.index:

# passo 4: cadastrar 1 produto
    pyautogui.click(x=707, y=278)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.press("tab")
    pyautogui.press('enter')
    
# passo 5: repetir o cadastro para todos os produtos
    pyautogui.scroll(50000)