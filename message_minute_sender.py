import keyboard, datetime, time




time.sleep(10)

while True:

    currentDT = datetime.datetime.now()
    now_time = f"{currentDT.hour}:{currentDT.minute}"

    keyboard.write(f"This is an automated message that will type send every so often. The time is currently {now_time}")
    keyboard.press_and_release('return')

    time.sleep(60)
