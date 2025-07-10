import keyboard, time



time.sleep(5)





for i in range(53):
  a = 7*i+2
  b = 7*i+8
  #keyboard.write(f"=COUNTIF('2024 Data'!C{a}:C{b}, TRUE)")
  keyboard.write(f"='2024 Data'!S{b}")
  time.sleep(0.2)
  keyboard.press_and_release("enter")



""" for i in range(53):
  keyboard.press("ctrl")
  keyboard.press("shift")
  keyboard.press_and_release("right")
  keyboard.release("ctrl")
  keyboard.press_and_release("left")
  keyboard.release("shift")
  keyboard.press_and_release("ctrl + r")
  keyboard.press_and_release("down")
 """