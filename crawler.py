## this is a tester program
## written by Don Morretti
## September 1st, 2019

from bs4 import BeautifulSoup
import requests
import lxml
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Web:
    def __init__(self):
        self.url = input("Type URL: ")

    def soup(self):
        self.r = requests.get(self.url)
        print("\nStatus Code: {}".format(self.r.status_code))
        self.soup = BeautifulSoup(self.r.text,'lxml')
        return self.r,self.soup

    def htmlTags(self):
        self.htmlTags = [i.name for i in self.soup.find_all(True)]
        self.c = Counter(self.htmlTags)

        print("\nThis is the URL{}".format("---> " + self.url))
        return self.c

    def text(self):
        self.t = [i.get_text() for i in self.soup_find_all("p")]
        return self.t

    def results(self):
        #print(self.c.most_common(10))
        self.plotters = dict(self.c.most_common(10))
        print("\nLength of 10 most common items in container: " + str(len(self.plotters)))
        print("\nType of Plotters: " + str(type(self.plotters)))
        print("\nString of Plotters: " + str(self.plotters))

        self.k = [self.k for self.k in self.plotters.keys()]
        print("\nKeys---> " + str(self.k))
        self.v = [self.v for self.v in self.plotters.values()]
        print("\nValues---> " + str(self.v))

        return self.v, self.k
        

    def numpyPrinter(self):
        self.index = np.arange(len(self.k))
        print(f"Index: {self.index}")
        # self.plt.bar(self.index, self.v)
        # self.plt.xlabel("HTML Tags",fontsize=5)
        # self.plt.ylabel("Total Count",fontsize=5)
        # self.plt.xticks(self.index, self.htmlTags, fontsize=6,rotation=30)
        # self.plt.title("10 Most Used HTML Tags")
        # self.plt.show()

    def addToPandas(self):
        return "\nThis is pandas method"


def main():
    pass


if __name__ == '__main__':
    main()