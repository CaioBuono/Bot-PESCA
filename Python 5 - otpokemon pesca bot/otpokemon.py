import pyautogui
import keyboard
import time

# Define as coordenadas dos ícones de pesca, monstro e água
pesca_icon_coords = (603, 445)
monstro_coords = (464, 144)
agua_coords = (250, 245)

# Define a cor do ícone de pesca quando a isca é mordida
pesca_mordida_cor = (65, 163, 48)  # Verde

while True:
    # Clica no ícone de pesca e joga a isca na água
    pyautogui.click(pesca_icon_coords)
    pyautogui.click(agua_coords, duration=1.5)
    pyautogui.moveTo(pesca_icon_coords, duration=1)

    # Aguarda até que a isca seja mordida
    while True:
        # Verifica a cor do ícone de pesca para saber se a isca foi mordida
        tela = pyautogui.screenshot()
        if tela.getpixel(pesca_icon_coords) == pesca_mordida_cor:
            break
        time.sleep(1)  # Espera 1 segundo antes de verificar novamente

    # Clica no ícone de pesca para pegar o peixe
    pyautogui.click(pesca_icon_coords)

    # Clica no monstro para derrotá-lo
    pyautogui.moveTo(monstro_coords, duration=1)
    pyautogui.click()

    keyboard.press('f5')
    keyboard.release('f5')

    keyboard.press('f4')
    keyboard.release('f4')

    keyboard.press('f3')
    keyboard.release('f3')

    keyboard.press('f2')
    keyboard.release('f2')

    keyboard.press('f1')
    keyboard.release('f1')

    # retorna ao icone de pesca
    pyautogui.moveTo(pesca_icon_coords, duration=1.5)
