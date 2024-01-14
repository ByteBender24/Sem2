import tkinter as tk

def convert():
    try:
        # Get the value from the input entry
        liters = float(entry.get())
        
        # Convert liters to gallons
        gallons = liters * 0.264172
        
        # Update the result label
        result.config(text=f"{liters} liters is equal to {gallons:.2f} gallons.")
        
    except ValueError:
        result.config(text="Invalid input!")

# Create the main window
window = tk.Tk()
window.title("Litre to Gallon Converter")

# Create the input label and entry
label = tk.Label(window, text="Enter liters:")
label.pack()
entry = tk.Entry(window)
entry.pack()

# Create the convert button
button = tk.Button(window, text="Convert", command=convert)
button.pack()

# Create the result label
result = tk.Label(window, text="")
result.pack()

# Start the main event loop
window.mainloop()
