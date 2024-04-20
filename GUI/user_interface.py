import tkinter as tk
from tkinter import ttk
from sklearn.svm import SVR
import pickle


with open('../Train_Model/model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Create a list to store the values from sliders
values = [0] * 30

def update_value(slider_value, index):
    rounded_value = "{:.4f}".format(float(slider_value)) # Round the slider value to 4 decimal places
    values[index] = rounded_value
    value_boxes[index].config(text=rounded_value)  # Update the value in the corresponding box


features = ['Alcoholic Beverages', 'Animal Products', 'Animal fats',
            'Aquatic Products, Other', 'Cereals - Excluding Beer', 'Eggs',
            'Fish, Seafood', 'Fruits - Excluding Wine', 'Meat', 'Miscellaneous',
            'Milk - Excluding Butter', 'Offals', 'Oilcrops', 'Pulses', 'Spices',
            'Starchy Roots', 'Stimulants', 'Sugar Crops', 'Sugar & Sweeteners',
            'Treenuts', 'Vegetal Products', 'Vegetable Oils', 'Vegetables',
            'Obesity', 'Undernourished', 'Confirmed', 'Deaths', 'Recovered',
            'Active', 'Population']

# Create the Tkinter application window
root = tk.Tk()
root.title("Slider Demo")

# Create a frame to hold the sliders and value boxes
frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

# Create lists to store sliders and value boxes
sliders = []
value_boxes = []

# Create 30 sliders and add them to the frame
for i in range(30):
    value_box = ttk.Label(frame, text="0.0000")
    value_box.grid(row=i % 15, column=(i // 15) * 3 + 2, padx=50, pady=5)
    value_boxes.append(value_box)

    slider_label = ttk.Label(frame, text=f"{features[i]}")
    slider_label.grid(row=i % 15, column=(i // 15) * 3, padx=5, pady=5, sticky="w")

    slider = ttk.Scale(frame, from_=0, to=50, length=200, orient="horizontal", command=lambda value, i=i: update_value(value, i))
    slider.set(float(0.0000))
    slider.grid(row=i % 15, column=(i // 15) * 3 + 1, padx=5, pady=5)
    sliders.append(slider)

    # Adjust the layout to ensure proper spacing
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    

# Run the Tkinter event loop
root.mainloop()
