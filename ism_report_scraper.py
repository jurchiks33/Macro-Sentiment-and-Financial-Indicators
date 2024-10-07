import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# helper function to convert text to float if needed
def convert_to_float(text):
    try:
        return float(text)
    except ValueError:
        return None

