# MACS341FINALPROJECT

## Participants
- Johnathan Park ( PARKJX22@juniata.edu )
- Mansi Chandra ( CHANDMX20@juniata.edu )


## SIR model simulation for COVID-19 dynamics

### file : Changing the disease dynamics.py

This code simulates the spread of COVID-19 using the SIR (Susceptible-Infected-Recovered) model, which divides the population into three compartments: susceptible, infected, and recovered. The model assumes that people can transition between compartments based on certain parameters, such as the infection rate and recovery rate.
<br><br>
The simulation considers three different strategies for controlling the spread of COVID-19, each with different values for the infection rate and recovery rate. The strategies are:
<br>
<ol>
  <li>Strategy 1: lower infection rate (beta = 0.25) while keeping the recovery rate constant (gamma = 0.1)</li>
  <li>Strategy 2: lower recovery rate (gamma = 0.125) while keeping the infection rate constant (beta = 0.3)</li>
  <li>Strategy 3: increase the proportion of the population initially immune to the disease (by setting S0 to 90% of the population), while keeping the infection and recovery rates constant.</li>
</ol>
<br>
The code defines two functions:
<code>SIR_model</code> calculates the differential equations for the SIR model, and <code>simulate_SIR_model</code> runs the simulation for the given set of parameters and number of days.
<br>
The results of the simulation are plotted in two figures:

<br>

<ol>
<li>A line plot of the percentage of the population that is infectious over time for each strategy.</li>
<li>A line plot of the cumulative percentage of the population that has been infected over time for each strategy, scaled by a factor of 10.</li>
</ol>
<br>
The figures illustrate how different strategies can affect the spread of the disease, as well as the overall impact on the population.
<br>
<br>

<h2> Herd Immunity Plot </h2>
<h3> file: Herd immunity by R nought.py </h3>

This Python script produces a plot that shows the percentage of the population that needs to be immune in order to achieve herd immunity, as a function of the basic reproduction number (R0) of a disease. The plot is generated using the Matplotlib library and NumPy library.

<h3> Prerequisites </h3>

This script requires the following Python libraries to be installed:

<li>Matplotlib</li>
<li>numpy</li>
<br>
You can install these packages using pip: 

```bash
$ pip install numpy matplotlib
```

<h3> Getting Started </h3>

To run the script, simply execute the following command in your terminal:

```bash
python3 Herd_immunity_by_R_nought.py
```

<h3> Parameters </h3>

The script defines a single function<code>herd_immunity</code> that takes one parameter <code>r_0</code>, which represents the basic reproduction number of a disease. The function returns the fraction of the population that needs to be immune in order to achieve herd immunity.

<br>

The script also defines an array <code>r_0_vals</code> that contains a range of values for the basic reproduction number, and computes the corresponding values for the fraction of the population that needs to be immune using the <code>herd_immunity</code> function.

### Output

The script produces a plot that shows the percentage of the population that needs to be immune in order to achieve herd immunity as a function of the basic reproduction number of a disease. The plot has the following characteristics:
<li>The x-axis represents the basic reproduction number (R0).</li>
<li>The y-axis represents the fraction of the population that needs to be immune for herd immunity.</li>
<li>The title of the plot is "Percentage of Population Needed for Herd Immunity by R0".</li>
<li>The x-axis label is "R0".</li>
<li>The y-axis label is "Fraction Immune for Herd Immunity".</li>
<li>The y-axis limits are set to range from 0 to 1.</li>
<br>
<br>

## SIR Simulation - outputs CSV file and plots most infected day

### file : most infected date.py

This code simulates the spread of an infectious disease using the SIR (Susceptible-Infected-Recovered) model. The simulation calculates the number of susceptible, infected, and recovered individuals over time, assuming a fixed population size, transmission rate (beta), and recovery rate (gamma).

### Getting Started

To run the simulation, you need to have Python3 installed on your computer, as well as the following packages:

<li>numpy</li>
<li>pandas</li>
<li>matplotlib</li>

<br>

You can install these packages using pip: 

```bash
$ pip install numpy pandas matplotlib
```

To run the simulation, simply execute the following command in your terminal:

```bash
python3 most_infected _date.py
```

### Parameters

The simulation has the following parameters:

<br>

The script will save the results of the simulation to an Excel file named <code>sir_simulation_results.xlsx</code>, and will also generate a plot showing the most infected day as a function of the initial infected rate.

<ol>
<li><code>beta</code>: The transmissioin rate, representing the rate at which susceptible individuals become infected upon contact with infected individuals.</li>
<li><code>gamma</code>: The recovery rate, representing the rate at which infected individuals recover and become immune.</li>
<li><code>population</code>: The total size of the population.</li>
<li><code>days</code>: The number of days to simulate.</li>
<li><code>initial_infection_rates</code>: An array of initial infection rates to simulate, expressed as a percentage of the population.</li>
</ol>

### Output
The simulation outputs a DataFrame containing the following columns:
<ol>
<li><code>Initial Infected Rate</code>: The initial infection rate used in the simulation, expressed as a percentage of the population.</li>
<li><code>Most Infected Day</code>: The day with the highest number of infected individuals.</li>
<li><code>Infected Cases Per Day</code>: An array of the number of infected individuals per day.</li>
</ol>
The results are saved to an Excel file named <code>sir_simulation_results.xlsx</code>.

### Plot
The simulation also generates a plot showing the most infected day as a function of the initial infected rate. The plot has the following axis labels:
<li>x-axis: Initial Infected Rate (%)</li>
<li>y-axis: Most Infected Day</li>
<li>title: Most Infected Day vs. Initial Infected Rate</li>
<br><br>

## Standard SIR model simulator GUI

### file : SIRtest.py

SIRtest.py is a GUI file that allows you to check various results with graphs while modifying various parameters of the SIR standard model.

The tkinter, matplotlib, and numpy packages are required to run this file. numpy and matplotlib are installed by default with Python installed, so no other additional work is required, but tkinter must be installed separately.
The tkinter can be installed in the following ways.

#### Step 1: Check Python Installation
Make sure you have Python installed on your computer. You can download Python from the official Python website at https://www.python.org/downloads/. Follow the installation instructions for your operating system.

#### Step 2: Open a Command Prompt or Terminal
Open a command prompt (on Windows) or terminal (on macOS or Linux) on your computer. You can do this by searching for "Command Prompt" or "Terminal" in the search bar or by navigating to the appropriate application in your system's programs.

#### Step 3: Install tkinter
Enter the following command in the command prompt or terminal to install tkinter using the Python package manager pip:
</br>For Windows:
```
  $ pip install tk
```
</br>For macOS/Linux:
```
  $ pip3 install tk
```
Note: If you're using a virtual environment, make sure it's activated before running the above command.

#### Step 4: Verify tkinter Installation
After the installation is complete, you can verify that tkinter is installed by opening a Python interactive shell or an Integrated Development Environment (IDE) that supports Python, and then typing the following command:
  import tkinter
If you don't see any errors, then tkinter is successfully installed on your system.

<br><br>
## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
