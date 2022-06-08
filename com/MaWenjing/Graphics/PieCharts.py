import pandas as pd
from pyecharts.charts import Pie, Timeline
from pyecharts import options as opts

datafile = '七次人口普查数据.xlsx'
data = pd.read_excel(datafile)
def generate_population_pies(datafile):
    data = pd.read_excel(datafile)

    # 提取省份名称和对应的人口普查数据
    name = data['省份'].tolist()[1:]
    value1 = data['1953年第一次人口普查'].tolist()[1:]
    value2 = data['1964年第二次人口普查'].tolist()[1:]
    value3 = data['1982年第三次人口普查'].tolist()[1:]
    value4 = data['1990年第四次人口普查'].tolist()[1:]
    value5 = data['2000年第五次人口普查'].tolist()[1:]
    value6 = data['2010年第六次人口普查'].tolist()[1:]
    value7 = data['2020年第七次人口普查'].tolist()[1:]
    provinces = [i.replace("\u3000", "") for i in name]

    # 创建时间线对象
    timeline = Timeline()

    # 为每个人口普查年份创建一个饼图并添加到时间线上
    years = ['1953年第一次人口普查', '1964年第二次人口普查', '1982年第三次人口普查',
             '1990年第四次人口普查', '2000年第五次人口普查', '2010年第六次人口普查', '2020年第七次人口普查']

    for i, year in enumerate(years):
        pie = (
            Pie()
            .add(
                series_name="Population",
                data_pair=list(zip(provinces, eval(f"value{i+1}"))),
                radius=["30%", "75%"],
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title=year),
                legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
            )
        )
        timeline.add(pie, year)

    # 渲染时间轴和饼图到HTML文件
    timeline.render(path="饼图-马文金.html")

# 调用方法，传入Excel文件路径
generate_population_pies("七次人口普查数据.xlsx")
