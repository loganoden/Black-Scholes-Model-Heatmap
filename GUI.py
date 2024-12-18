import fix_tcl
fix_tcl.fix_tcl_paths()

from blackScholesModel import BlackScholesModel
import numpy
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Black Scholes Model: Heatmap")

        # Initialize class variables
        self.labels = ["Time to Maturity", "Strike", "Current Price", "Volatility", "Interest Rate"]
        self.canvas = None
        
        # Create GUI elements
        self.create_input_fields()
        self.create_buttons()

    def create_input_fields(self):
        self.entries = {}

        for i, label in enumerate(self.labels):
            ttk.Label(self.root, text=label).grid(row=i, column=0)
            entry = ttk.Entry(self.root)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries[label] = entry

    def create_buttons(self):
        generate_button = ttk.Button(self.root, text="Generate Heatmap", command=self.generate_heatmap)
        generate_button.grid(row=len(self.labels), column=0, columnspan=2)

    def generate_heatmap(self):
        # Get the values from the input fields
        S = float(self.entries["Current Price"].get())
        K = float(self.entries["Strike"].get())
        T = float(self.entries["Time to Maturity"].get())
        r = float(self.entries["Interest Rate"].get())
        v = float(self.entries["Volatility"].get())

        # Generate the grid of prices and volatilities
        prices = numpy.linspace(S - 10, S + 10, 100)
        volatilities = numpy.linspace(v - 0.1, v + 0.1, 100)
        option_prices = numpy.zeros((100, 100))

        # Create the model & calculate the option prices
        for i, price in enumerate(prices):
            for j, vol in enumerate(volatilities):
                model = BlackScholesModel(price, K, T, r, vol)
                option_prices[i, j] = model.calculate()

        # Plot the heatmap
        self.plot_heatmap(prices, volatilities, option_prices)

    def plot_heatmap(self, prices, volatilities, option_prices):
        fig, ax = plt.subplots(figsize=(6, 4))
        heatmap = ax.imshow(option_prices, 
                           extent=(volatilities[0], volatilities[-1], prices[0], prices[-1]),
                           origin="lower",
                           cmap="coolwarm",
                           aspect="auto")
        
        ax.set_xlabel("Volatility")
        ax.set_ylabel("Price")
        fig.colorbar(heatmap, ax=ax, label="Option Price")

        if hasattr(self, 'canvas') and self.canvas:
            self.canvas.get_tk_widget().destroy()

        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=len(self.labels) + 1, column=0, columnspan=2, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()