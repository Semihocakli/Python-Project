import tkinter as tk

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = float(weight) / ((float(height) / 100) ** 2)
    result_label.config(text=write_result(bmi))

def write_result(bmi):
    result_string = f"Your BMI is {round(bmi, 2)}. You are "
    if bmi <= 16:
        result_string += "severely thin!"
    elif 16 < bmi <= 17:
        result_string += "moderately thin!"
    elif 17 < bmi <= 18.5:
        result_string += "mild thin!"
    elif 18.5 < bmi <= 25:
        result_string += "normal weight"
    elif 25 < bmi <= 30:
        result_string += "overweight"
    elif 30 < bmi <= 35:
        result_string += "obese class 1"
    elif 35 < bmi <= 40:
        result_string += "obese class 2"
    else:
        result_string += "obese class 3"
    return result_string

window = tk.Tk()
window.title("BMI Calculator")
window.geometry("400x200")

#ui
weight_label = tk.Label(window, text="Kilonuz (kg):")
weight_label.grid(row=0, column=0, padx=10, pady=10)

weight_entry = tk.Entry(window)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

height_label = tk.Label(window, text="Boyunuz (cm):")
height_label.grid(row=1, column=0, padx=10, pady=10)

height_entry = tk.Entry(window)
height_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(window, text="Hesapla", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
