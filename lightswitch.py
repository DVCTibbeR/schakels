import tkinter as tk

window = tk.Tk()
window.config(bg="black")

lightOn = False

def toggleLightSwitch():
	global lightOn

	if lightOn:
		button.config(text="Switch light off")
		window.config(bg="black")
	else:
		button.config(text="Switch light on")
		window.config(bg="yellow")

	lightOn = not lightOn

button = tk.Button(text="Switch light on", bg="white", fg="black", command=toggleLightSwitch)
button.pack(pady = 20, padx = 20)

window.mainloop()