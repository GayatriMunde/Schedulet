from bs4 import BeautifulSoup
import requests
import camelot

def get_vals(filename):
    HTMLFile = open('./data/outline2.html', "r", encoding="utf8")

    # read the HTML file
    index = HTMLFile.read()

    soup = BeautifulSoup(index, "html.parser")
    tables = camelot.read_pdf('./data/outline2.pdf')
    weight_table = tables[0]

    return soup, weight_table