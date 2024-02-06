import tkinter as tk

window = tk.Tk()
window.config(bg="black")

def toggleLightSwitch():
	button.config(text="Switch light on" if button.lightOn else "Switch light off")
	window.config(bg="yellow" if button.lightOn else "black")

	print("light is on" if button.lightOn else "light is off")

	button.lightOn = not button.lightOn

button = tk.Button(text="Switch light on", bg="white", fg="black", command=toggleLightSwitch)
button.pack(pady = 20, padx = 20)
button.lightOn = False

window.mainloop()