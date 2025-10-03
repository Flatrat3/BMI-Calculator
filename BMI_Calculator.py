import tkinter as tk

# Windows screen
window = tk.Tk()
window.geometry("600x300")
window.title("BMI Calculator")

def calculate_bmi():
    try:

        if not entry_weight.get() or not entry_height.get():
            result_label.config(text="Xahiş olunur hər iki xanaya dəyər daxil edin!", fg="red")
            return

        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100
        bmi = weight / (height ** 2)
        print("Your BMI is", bmi)


        if bmi < 18.5:
            result_text = f"BMI: {bmi:.2f} - Arıqlıq"
        elif 18.5 <= bmi < 24.9:
            result_text = f"BMI: {bmi:.2f} - Normal"
        elif 25 <= bmi < 29.9:
            result_text = f"BMI: {bmi:.2f} - Artıq çəki"
        else:
            result_text = f"BMI: {bmi:.2f} - Obez"

        result_label.config(text=result_text, fg="blue")

    except ValueError:
        result_label.config(text="Xahiş olunur düzgün rəqəm daxil edin!", fg="red")

# Weight
tk.Label(window, text="Weight (kg):").pack(pady=5)
entry_weight = tk.Entry(window, width=20)
entry_weight.pack(pady=5)

# Height
tk.Label(window, text="Height (cm):").pack(pady=5)
entry_height = tk.Entry(window, width=20)
entry_height.pack(pady=5)

# Button
btn_calculate = tk.Button(window, text="Calculate", command=calculate_bmi)
btn_calculate.pack(pady=5)

# Nəticə Label
result_label = tk.Label(window, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

window.mainloop()
