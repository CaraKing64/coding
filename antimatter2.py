import keyboard, time

print("Waiting...")
time.sleep(5)
print("Pressing keys!")
keyboard.press("m")
while True:
  keyboard.press_and_release("r")
  time.sleep(0.1)