import pyautogui
import pyperclip
import time
import pandas as pd

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")
time.sleep(5)

pyautogui.click(x=983, y=441)
pyautogui.write("email@email.com")
pyautogui.click(x=912, y=529)
pyautogui.write("123456")
pyautogui.click(x=91, y=529)

time.sleep(3)
pyautogui.click(x=-2422, y=496)
pyautogui.click(x=-2124, y=253)
time.sleep(3)
pyautogui.click(x=-264, y=1514)

time.sleep(3)
table = pd.read_csv(r"C:\Users\user\Downloads\Compras.csv", sep=";")
valor_final = table["ValorFinal"].sum()
quantidade = table["Quantidade"].sum()
media = valor_final / quantidade

pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com")
pyautogui.press("enter")
time.sleep(2)

pyautogui.click(x=-2752, y=247)
pyautogui.write("mayndi15@gmail.com")
pyautogui.press("enter")

pyautogui.press("tab")
pyautogui.write("assunto")

pyautogui.press("tab")
pyperclip.copy("body")
pyautogui.hotkey("ctrl", "v")

pyautogui.hotkey("ctrl", "enter")
