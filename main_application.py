import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# importing individual modules to the main file
import Benchmark_Yield_US
import ism_report_on_business_SERVICES
import ism_report_scraper
import M2_Money_Supply
import us_building_permits
import umsci_scrapper
import vix_analysis
import sp500_building_permits_ma
import Inflation_CPI_and_PPI

# function to display M2 Money Supply vs Stock Market Analysis
def display_m2_money_supply():
    clear_canvas()
    M2_Money_Supply.main()

# function to display U.S. buildng permits
def display_us_buildings_permits():
    clear_canvas()
    us_building_permits.main()

# function to display ISM report on business Services
def display_ism_services_report():
    clear_canvas()
    ism_report_on_business_SERVICES.main()

# function to display ISM manufacturing report
def display_ism_manufacturing_report():
    clear_canvas()
    ism_report_scraper.main()

# Function to display University of Michigan Sentiment Index
def display_umcsi():
    clear_canvas()
    umsci_scrapper.main()

# Function to display VIX Analysis
def display_vix_analysis():
    clear_canvas()
    vix_analysis.main()

# Function to display Benchmark Yield
def display_benchmark_yield():
    clear_canvas()
    Benchmark_Yield_US.main()

# function for inflation CPI and PPI display
def display_inflation_cpi_ppi():
    clear_canvas()
    Inflation_CPI_and_PPI.main()

# Function to clear the canvas area for new plots
def clear_canvas():
    for widget in right_frame.winfo_children():
        widget.destroy()

# creating main application window
root = tk.Tk()
root.title("Financial Data Dashboard")

# frame for buttons
left_frame = tk.Frame(root, width=200, bg='lightgray')
left_frame.pack(side=tk.LEFT, fill=tk.Y)

# frame for a data display
right_frame = tk.Frame(root, bg='white')
right_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# button styling
button_style = {
    'font': ('Arial', 12),
    'width': 25,        # for all buttons to have same width
    'bg': 'lightgrey',  # background for buttons
    'fg': 'black',      # text color
    'activebackground': 'grey',   # background on button press
    'activeforeground': 'white'   # text color on button press
}

# buttons for the left frame
btn_m2_money = tk.Button(left_frame, 
                         text="M2 Money Supply",
                         command=display_m2_money_supply,
                         **button_style)
btn_m2_money.pack(pady=10, padx=10)

btn_us_buildings = tk.Button(left_frame, 
                             text="U.S. Building Permits",
                             command=display_us_buildings_permits,
                             **button_style)
btn_us_buildings.pack(pady=10, padx=10)

btn_ism_manufacturing = tk.Button(left_frame,
                                  text="ISM Report - Manufacturing", 
                                  command=display_ism_manufacturing_report,
                                  **button_style)
btn_ism_manufacturing.pack(pady=10, padx=10)

btn_ism_services = tk.Button(left_frame,
                             text="ISM Report - Services",
                             command=display_ism_services_report,
                             **button_style)
btn_ism_services.pack(pady=10, padx=10)

btn_umsci = tk.Button(left_frame,
                      text="U. of Michigan Sentiment Index", 
                      command=display_umcsi,
                      **button_style)
btn_umsci.pack(pady=10, padx=10)

btn_vix_analysis = tk.Button(left_frame, 
                             text="VIX Analysis", 
                             command=display_vix_analysis,
                             **button_style)
btn_vix_analysis.pack(pady=10, padx=10)

btn_benchmark_yield = tk.Button(left_frame, 
                                text="Benchmark Yield", 
                                command=display_benchmark_yield,
                                **button_style)
btn_benchmark_yield.pack(pady=10, padx=10)

btn_sp500_permits_pct = tk.Button(left_frame, 
                                 text="SP500 & Building Permits MA",
                                 command=lambda: sp500_building_permits_ma.main(),
                                 **button_style)
btn_sp500_permits_pct.pack(pady=10, padx=10)

btn_inflation = tk.Button(left_frame, 
                          text="Inflation:CPI & PPI",
                          command=lambda: Inflation_CPI_and_PPI.main(),
                          **button_style)
btn_inflation.pack(pady=10, padx=10)

# starting main loop
root.mainloop()