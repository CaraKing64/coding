import keyboard, time, random

inps = ["w", "a", "s", "d", "space", "e"]

time.sleep(5)

while True:
    ck = random.choice(inps)
    t = random.random()*0.5
    keyboard.press(ck)
    time.sleep(t)
    keyboard.release(ck)