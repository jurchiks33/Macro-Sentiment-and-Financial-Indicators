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

# Function to clear the canvas area for new plots
def clear_canvas():
    for widget in right_frame.winfo_children():
        widget.destroy()