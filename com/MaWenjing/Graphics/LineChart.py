import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Line, Timeline

datafile = '七次人口普查数据.xlsx'
data = pd.read_excel(datafile)

# 从DataFrame中提取省份和人口普查数据
provinces = [i.replace("\u3000", "") for i in data['省份'].tolist()[1:]]

# 创建一个字典来保存各个年份的人口普查数据
census_data = {year: data[year].tolist()[1:] for year in data.columns if year.startswith('20') or year.startswith('19')}

# 检查数据是否正确
for year, value in census_data.items():
    print(f"{year}: {value}")

##折线图
def lineChart():
    timeline = Timeline()

    # 定义颜色列表
    colors = ["lightsalmon", "mediumpurple", "lightblue", "gold", "lightgreen", "orange", "springgreen", "skyblue", "red", "yellowgreen"]

    # 遍历每个年份的人口普查数据
    for year, value in census_data.items():
        line_chart = (
            Line()
            .add_xaxis(provinces)  # 添加省份作为x轴
            .add_yaxis("人口数量", value, itemstyle_opts=opts.ItemStyleOpts(color=colors.pop(0)))  # 添加y轴数据，并设置颜色
            .set_global_opts(
                title_opts=opts.TitleOpts(title=f"{year}年不同省份总人口"),
                yaxis_opts=opts.AxisOpts(name="人口数量"),
                xaxis_opts=opts.AxisOpts(name="省份"),
            )
        )
        timeline.add(line_chart, year)

    # 渲染时间轴折线图到HTML文件
    timeline.render(path="折线图-马文金.html")

##运行并生成折线图
lineChart()