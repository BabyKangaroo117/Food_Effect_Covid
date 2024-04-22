import tkinter as tk
from tkinter import ttk
from sklearn.svm import SVR
import pickle
import pandas as pd

with open('../Train_Model/model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Create a list to store the values from sliders
values = [0] * 23

def update_value(slider_value, index):
    rounded_value = "{:.4f}".format(float(slider_value)) # Round the slider value to 4 decimal places
    values[index] = rounded_value
    value_boxes[index].config(text=rounded_value)  # Update the value in the corresponding box
    prediction = make_prediction()
    rounded_value = "{:.8f}".format(float(prediction))
    prediction_box.config(text=f"{prediction}")


def make_prediction():
    # Make prediction
    data = pd.DataFrame([values], columns=list(features.keys()))
    prediction = loaded_model.predict(data)
    print(prediction)
    return prediction



# Includes the max percentage of each category
features = {'Alcoholic Beverages': 15.0, 'Animal fats': 1.0, 'Animal Products': 27.0, 
            'Cereals - Excluding Beer': 30.0, 'Eggs': 2.0, 'Fish, Seafood': 9.0, 
            'Fruits - Excluding Wine': 19.0, 'Meat': 8.0, 'Milk - Excluding Butter': 21.0, 
            'Offals': 1.0, 'Oilcrops': 12.0, 'Pulses': 3.0, 'Spices': 1.0, 'Starchy Roots': 28.0, 
            'Stimulants': 1.0, 'Sugar & Sweeteners': 10.0, 'Treenuts': 1.0, 'Vegetable Oils': 2.0, 
            'Vegetables': 19.0, 'Vegetal Products': 48.0, 'Obesity': 46.0, 'Undernourished': 60.0, 'Active': 8.0}

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
prediction_label = ttk.Label(frame, text=f"Prediction: ")
prediction_label.grid(row=6, column=3 * 3, padx=5, pady=5, sticky="w")
prediction_box = ttk.Label(frame, text="0.0000")
prediction_box.grid(row=6, column=3 * 3 + 2, padx=50, pady=5)

# Create 30 sliders and add them to the frame
for i in range(23):
    value_box = ttk.Label(frame, text="0.0000")
    value_box.grid(row=i % 13, column=(i // 13) * 3 + 2, padx=50, pady=5)
    value_boxes.append(value_box)

    slider_label = ttk.Label(frame, text=f"{list(features.keys())[i]}")
    slider_label.grid(row=i % 13, column=(i // 13) * 3, padx=5, pady=5, sticky="w")

    slider = ttk.Scale(frame, from_=0, to=list(features.values())[i], length=200, orient="horizontal", command=lambda value, i=i: update_value(value, i))
    slider.set(float(0.0000))
    slider.grid(row=i % 13, column=(i // 13) * 3 + 1, padx=5, pady=5)
    sliders.append(slider)

    # Adjust the layout to ensure proper spacing
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

# Run the Tkinter event loop
root.mainloop()
