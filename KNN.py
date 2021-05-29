import re
import csv
import json
from collections import Counter
import matplotlib.pyplot as plt


def readCsv(path):
    list=[]
    with open(path,"r",encoding="utf-8")as f:
        reader=csv.reader(f)
        for line in reader:
            title=line[1]
            list.append(normalize(title))
    return list

def readJson(path):
    list=[]
    with open(path,"r",encoding="utf-8")as f:
        jsonreader= json.load(f)
        for row in jsonreader.values():
           list.append(normalize(row))
    return list


def normalize(name):
    name = name.lower()
    name = re.sub(r"[.,/#!$%^*;:{}=_`~()@]", ' ', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name


def analyze(data,n):
    count=Counter(data)
    return count.most_common(n)


def plot_bar(data):
    names, values = zip(*data)
    plt.bar(names, values, width=0.55,
            color="#f9af2b", edgecolor="#f05131")
    plt.ylabel("Count")
    plt.xlabel("Playlist Titles")
    plt.title("Most Frequent Playlist Titles")



if __name__ == '__main__':

 path1 = input("Please enter the path to the csv file:")
 data1=readCsv(path1)
 path2 = input("Please enter the path to the json file:")
 data2=readJson(path2)
 data1.extend(data2)
 n1=int(input("Please enter the number of titles to be visualized:"))
 data3=analyze(data1,n1)
 print(data3)
 plot_bar(data3)
 plt.show()
