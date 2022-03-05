
import pandas, numpy,pygal
from matplotlib import  pyplot as plt
from matplotlib import style
#from project_module import project

def main():
    data_frame = pandas.read_csv('D://UIT//2ndSemester//ObjectOrientedProgramming//OOP Final Project//vgsales.csv')
    NA_Sales = summed_sales(data_frame, 'NA_Sales')
    EU_Sales = summed_sales(data_frame, 'EU_Sales')
    JP_Sales = summed_sales(data_frame, 'JP_Sales')
    OT_Sales = summed_sales(data_frame, 'Other_Sales')
    GB_Sales = summed_sales(data_frame, 'Global_Sales')
    createPie(NA_Sales, EU_Sales, JP_Sales, OT_Sales, GB_Sales)

def summed_sales(data_frame, zone):
    return data_frame[zone].sum()

def createPie(NASales,EUSales,JPSales,OTSales,GBSales):
    pie_chart = pygal.Pie(inner_radius=.4)
    pie_chart.title = 'Overall Sales By Region'
    pie_chart.add('North America', NASales)
    pie_chart.add('Europe', EUSales)
    pie_chart.add('Japan', JPSales)
    pie_chart.add('Others', OTSales)
    pie_chart.add('Global', GBSales)
    pie_chart.render_in_browser()

main()
