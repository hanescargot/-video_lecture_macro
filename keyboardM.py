import keyboard
import mouse
import time



def doSpacebar():
    while True:
        x,y = mouse.get_position()
        mouse.move(-424, 171)
        mouse.click()
        keyboard.press("enter")
        mouse.move(x,y)
        print("run")
        time.sleep(5)

if __name__ == "__main__":
    doSpacebar();
