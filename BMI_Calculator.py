import tkinter as tk


#Windows screen
window = tk.Tk()
window.geometry("600x300")
window.title("BMI Calculator")

#Weight
tk.Label(window, text="Weight (kg):").pack(pady=5)
entry_weight=tk.Entry(window, width=20).pack(pady=5)


#Height
tk.Label(window, text="Height (kg):").pack(pady=5)
entry_height=tk.Entry(window, width=20).pack(pady=5)

#Button
tk.Button(window, text="Calculate").pack(pady=5)

window.mainloop()