#PROCESSO DE AUTOMAÇÃO
import pyautogui
import time
import pandas

pyautogui.PAUSE = 1 #a cada comando ele pausa 1s 
#bom para verificar se a automação tá funcionando de forma ok

pyautogui.press("win") #pressiona a tecla windows
pyautogui.write("chrome") #escreve o nome crhome na barra de pesquisa do windows
pyautogui.press("enter") 
#se tiver diferentes perfis no chrome, deve-se adiconar um passo aqui

time.sleep(2)
#selecionar um perfil no chrome
pyautogui.click(x=848,y=486)

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter") 
#espera específica de 5s nesse canto específico
time.sleep(5)

#clicar na tela no campo da senha
pyautogui.click(x=751,y=460)
#digitar o email
pyautogui.write("anandinha@gmail.com")
#pular para o próximo espaço
pyautogui.press("tab")
#clicar na tela no campo da senha
pyautogui.click(x=946,y=670)
time.sleep(3)

#armazenando a tabela de dados
tabelaDeDados = pandas.read_csv("produtos.csv")
print(tabelaDeDados)

#para cada item em um conjunto de itens
for linha in tabelaDeDados.index:
    pyautogui.click(x=725,y=323)

    #na tabela localiza a linha e a coluna com esse nome
    pyautogui.write(tabelaDeDados.loc[linha, "codigo"])
    pyautogui.press("tab")


    pyautogui.write(tabelaDeDados.loc[linha, "marca"])
    pyautogui.press("tab")


    pyautogui.write(tabelaDeDados.loc[linha, "tipo"])
    pyautogui.press("tab")

    
    pyautogui.write(str(tabelaDeDados.loc[linha, "categoria"]))
    pyautogui.press("tab")


    pyautogui.write(str(tabelaDeDados.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")


    pyautogui.write(str(tabelaDeDados.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabelaDeDados.loc[linha, "obs"]
    if not pandas.isna(obs): #se o valor não for o NaN = not a number
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter") 

    pyautogui.scroll(5000)
