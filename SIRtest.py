import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

class SIRModelGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SIR Model")
        
        # Parameters
        self.beta = tk.DoubleVar(value=0.5)  # init value 0.5
        self.gamma = tk.DoubleVar(value=0.1)  # init value 0.1
        self.initial_infected = tk.DoubleVar(value=0.01)  # init value 0.01
        self.total_population = tk.IntVar(value=1000)  # init value 1000
        self.days = tk.IntVar(value=100)  # init value 100
        
        # Input frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)  # How many pixels to pad widget, horizontally and vertically, outside v's borders, is 10
        
        tk.Label(input_frame, text="SIR Model Parameters").grid(row=0, column=0, columnspan=2, sticky=tk.W) # title
        tk.Label(input_frame, text="Beta (Infection rate):").grid(row=1, column=0, sticky=tk.W) # beta
        tk.Label(input_frame, text="Gamma (Recovery rate):").grid(row=2, column=0, sticky=tk.W) # gamma
        tk.Label(input_frame, text="Initial infected (%):").grid(row=3, column=0, sticky=tk.W) # inital infected
        tk.Label(input_frame, text="Total population:").grid(row=4, column=0, sticky=tk.W) # num of people
        tk.Label(input_frame, text="Days:").grid(row=5, column=0, sticky=tk.W) # days
        
        tk.Entry(input_frame, textvariable=self.beta).grid(row=1, column=1, sticky=tk.E)  # inputs
        tk.Entry(input_frame, textvariable=self.gamma).grid(row=2, column=1, sticky=tk.E)  # inputs
        tk.Entry(input_frame, textvariable=self.initial_infected).grid(row=3, column=1, sticky=tk.E)  # inputs
        tk.Entry(input_frame, textvariable=self.total_population).grid(row=4, column=1, sticky=tk.E)  # inputs
        tk.Entry(input_frame, textvariable=self.days).grid(row=5, column=1, sticky=tk.E)  # inputs
        
        tk.Button(input_frame, text="Simulate", command=self.simulate).grid(row=6, column=0, columnspan=2, pady=10) # make graph button
        
        # Output frame
        output_frame = tk.Frame(self.root)
        output_frame.pack(padx=10, pady=10)
        
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.plot = self.figure.add_subplot(111)
        self.plot.set_xlabel("Days")
        self.plot.set_ylabel("Population")
        self.canvas = FigureCanvasTkAgg(self.figure, output_frame)
        self.canvas.get_tk_widget().pack()
        
    def simulate(self):
        beta = self.beta.get()
        gamma = self.gamma.get()
        initial_infected = self.initial_infected.get() / 100 # cause its percentage
        total_population = self.total_population.get()
        days = self.days.get()
        
        # Initial conditions
        susceptible = total_population * (1 - initial_infected)
        infected = total_population * initial_infected
        recovered = 0
        
        # Lists to store results for plotting
        days_list = [0]
        susceptible_list = [susceptible]
        infected_list = [infected]
        recovered_list = [recovered]
        
        # Run simulation
        for day in range(1, days + 1):
            # Update SIR model equations
            new_infections = beta * susceptible * infected / total_population
            new_recoveries = gamma * infected
            susceptible -= new_infections
            infected += new_infections - new_recoveries
            recovered += new_recoveries
            
            # Append results to lists for plotting
            days_list.append(day)
            susceptible_list.append(susceptible)
            infected_list.append(infected)
            recovered_list.append(recovered)
        
        # Clear previous plot
        self.plot.clear()
        
        # Plot SIR model results
        self.plot.plot(days_list, susceptible_list, label="Susceptible")
        self.plot.plot(days_list, infected_list, label="Infected")
        self.plot.plot(days_list, recovered_list, label="Recovered")
        self.plot.legend()
        self.plot.set_xlabel("Days")
        self.plot.set_ylabel("Population")
        self.plot.set_title("SIR Model Simulation")
        
        # Update canvas
        self.canvas.draw()
        
if __name__ == "__main__":
    # Create main window
    root = tk.Tk()
    root.geometry("600x400")
    
    # Create SIRModelGUI object
    sir_model_gui = SIRModelGUI(root)
    
    # Start GUI event loop
    root.mainloop()


