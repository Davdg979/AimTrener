import tkinter as tk
import threading
import pyautogui
import win32api, win32con
import keyboard
import time

print('Hello World!')

cheat_on = False
running = True
hits = 0

def click(x, y):
    global hits
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    hits += 1

def aimbot_loop():
    global running, cheat_on
    while running:
        if cheat_on:
            sc = pyautogui.screenshot(region=(400, 150, 798, 593))
            width, height = sc.size
            found = False
            for x in range(0, width, 12):
                for y in range(0, height, 12):
                    r, g, b = sc.getpixel((x, y))
                    if r == 255 and g == 0 and b == 0:
                        click(400 + x, 150 + y)
                        found = True
                        time.sleep(0.01)
                        break
                if found:
                    break
        time.sleep(0.01)

def keyboard_loop():
    global cheat_on, running
    while running:
        if keyboard.is_pressed('c'):
            cheat_on = not cheat_on
            status_label.config(text=f"Aimbot {'Ativo' if cheat_on else 'Desativado'}")
            time.sleep(0.3)
        if keyboard.is_pressed('z'):
            running = False
            root.destroy()
        time.sleep(0.01)

root = tk.Tk()
root.title("Aimbot_AimTrener")
root.geometry("300x180")

status_label = tk.Label(root, text="Aimbot Desativado", font=("Arial", 16))
status_label.pack(pady=20)

hits_label = tk.Label(root, text=f"Hits: {hits}", font=("Arial", 12))
hits_label.pack(pady=5)

label = tk.Label(root, text="ligar/desligar (c) fecha janela (z)", font=("Arial", 14))
label.pack(pady=20)

def update_hits():
    hits_label.config(text=f"Hits: {hits}")
    if running:
        root.after(100, update_hits)

update_hits()

threading.Thread(target=aimbot_loop, daemon=True).start()
threading.Thread(target=keyboard_loop, daemon=True).start()

root.mainloop()
