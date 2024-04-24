import tkinter as tk
from tkinter import ttk
import xgboost as xgb
import pickle
import pandas as pd

with open('../Train_Model/model.pkl', 'rb') as file:
    loaded_model: xgb = pickle.load(file)

# Create a list to store the values from sliders
values = [0] * 20
update_counter = 0
# Includes the max percentage of each category
features = {'Alcoholic Beverages': 15.0, 'Animal fats': 1.0, 'Animal Products': 27.0, 
            'Cereals - Excluding Beer': 30.0, 'Eggs': 2.0, 'Fish, Seafood': 9.0, 
            'Fruits - Excluding Wine': 19.0, 'Meat': 8.0, 'Milk - Excluding Butter': 21.0, 
            'Offals': 1.0, 'Oilcrops': 12.0, 'Pulses': 3.0, 'Spices': 1.0, 'Starchy Roots': 28.0, 
            'Stimulants': 1.0, 'Sugar & Sweeteners': 10.0, 'Treenuts': 1.0, 'Vegetable Oils': 2.0, 
            'Vegetables': 19.0, 'Vegetal Products': 48.0}


def update_value(slider_value, index):
    global update_counter
    update_counter += 1
    rounded_value = "{:.4f}".format(float(slider_value)) # Round the slider value to 4 decimal places
    values[index] = float(rounded_value)
    value_boxes[index].config(text=rounded_value)  # Update the value in the corresponding box
    
    # Total percentage
    total = 0
    for value in values:
        total += float(value)
    rounded_value = "{:.4f}".format(float(total))
    percentage_box.config(text=f"{rounded_value}")

    # Limit number of times data is run through model for stability of program
    if update_counter % 10 == 0:
        update_counter = 0
        # Prediction
        prediction = make_prediction()
        rounded_value = "{:.7f}".format(float(prediction[0]))
        prediction_box.config(text=f"{rounded_value}")


def make_prediction():
    # Make prediction
    data = pd.DataFrame([values], columns=list(features.keys()))
    prediction = loaded_model.predict(data)
    return prediction

# Create the Tkinter application window
root = tk.Tk()
root.title("Slider Demo")

# Create a frame to hold the sliders and value boxes
frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

# Create lists to store sliders and value boxes
sliders = []
value_boxes = []

# Prediction label
prediction_label = ttk.Label(frame, text=f"Percentage Confirmed Covid: ")
prediction_label.grid(row=5, column=3 * 3, padx=2, pady=5, sticky="w")
prediction_box = ttk.Label(frame, text="0.00000000")
prediction_box.grid(row=5, column=3 * 3 + 2, padx=50, pady=5)

# Total Percentage of foods
percentage_label = ttk.Label(frame, text=f"Total Percentage Food: ")
percentage_label.grid(row=4, column=3 * 3, padx=2, pady=5, sticky="w")
percentage_box = ttk.Label(frame, text="0.0000")
percentage_box.grid(row=4, column=3 * 3 + 2, padx=50, pady=5)

# Create 30 sliders and add them to the frame
for i in range(20):
    value_box = ttk.Label(frame, text="0.0000")
    value_box.grid(row=i % 10, column=(i // 10) * 3 + 2, padx=50, pady=5)
    value_boxes.append(value_box)

    slider_label = ttk.Label(frame, text=f"{list(features.keys())[i]}")
    slider_label.grid(row=i % 10, column=(i // 10) * 3, padx=5, pady=5, sticky="w")

    slider = ttk.Scale(frame, from_=0, to=list(features.values())[i], length=200, orient="horizontal", command=lambda value, i=i: update_value(value, i))
    slider.set(float(0.0000))
    slider.grid(row=i % 10, column=(i // 10) * 3 + 1, padx=5, pady=5)
    sliders.append(slider)

    # Adjust the layout to ensure proper spacing
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

# Run the Tkinter event loop
root.mainloop()
