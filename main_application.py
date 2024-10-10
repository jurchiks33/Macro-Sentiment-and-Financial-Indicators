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

