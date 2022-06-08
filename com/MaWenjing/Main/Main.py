import pandas as pd
from com.MaWenjing.Graphics.Histogram import historgram
from com.MaWenjing.Graphics.LineChart import lineChart
from com.MaWenjing.Graphics.PieCharts import generate_population_pies
from com.MaWenjing.Graphics.ScatterPlot import scatterChart


if __name__ == '__main__':
    datafile = '七次人口普查数据.xlsx'
    data = pd.read_excel(datafile)

    historgram()
    lineChart()
    generate_population_pies(datafile)
    scatterChart()
