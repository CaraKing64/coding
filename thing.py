import keyboard as kb
import time

time.sleep(2)


for i in range (14, 397):
    st = ""
    if i < 10:
        st = "00"
    if 10 <= i < 100:
        st = "0"
    if 100 <= i:
        st = ""
    st = st + str(i) + ".jpg"
    url = "https://multporn.net/sites/default/files/comics/pokemon/kinkymation_pokemusu_dex_-_gotta_fuck_039em_all/" + st

    
    kb.press_and_release("ctrl + t")
    time.sleep(0.5)
    kb.press_and_release("ctrl + l")
    time.sleep(0.5)
    kb.write(url)
    time.sleep(1)
    kb.press_and_release("return")
    time.sleep(3)
    kb.press_and_release("ctrl + s")
    time.sleep(0.75)
    kb.press_and_release("return")
    time.sleep(0.75)
    kb.press_and_release("escape")
    time.sleep(0.75)
    