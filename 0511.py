import pandas as pd
from collections import Counter
###画图
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar, Pie, Timeline
from pyecharts.faker import Faker


datafile = u'七次人口普查数据-李运辰.xlsx'
data = pd.read_excel(datafile)


###第七次不同省份总人口-李运辰
def an1():
    name = data['省份'].tolist()[1:]
    value = data['2020年第七次人口普查'].tolist()[1:]
    provinces = [i.replace("\u3000","") for i in name]
    #value = [int(int(i)/10000) for i in value]
    print(provinces)
    print(value)
    c = (
        Map()
            .add("", [list(z) for z in zip(provinces, value)], "china")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="第七次不同省份总人口"),
            visualmap_opts=opts.VisualMapOpts(max_=130000000, split_number=8, is_piecewise=True),
        )
    ).render(path="第七次不同省份总人口-李运辰.html")

###1953~2021年不同省份总人口-李运辰
def an2():
    name = data['省份'].tolist()[1:]
    value1 = data['1953年第一次人口普查'].tolist()[1:]
    value2 = data['1964年第二次人口普查'].tolist()[1:]
    value3 = data['1982年第三次人口普查'].tolist()[1:]
    value4 = data['1990年第四次人口普查'].tolist()[1:]
    value5 = data['2000年第五次人口普查'].tolist()[1:]
    value6 = data['2010年第六次人口普查'].tolist()[1:]
    value7 = data['2020年第七次人口普查'].tolist()[1:]
    provinces = [i.replace("\u3000","") for i in name]
    #value = [int(int(i)/10000) for i in value]
    print(provinces)


    t = Timeline()
    c1 = (
        Map()
            .add("", [list(z) for z in zip(provinces, value1)], "china")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="第一次人口普查不同省份总人口"),
            visualmap_opts=opts.VisualMapOpts(max_=130000000, split_number=8, is_piecewise=True),
        )
    )
    t.add(c1, "第一次人口普查不同省份总人口")

    c2 = (
        Map()
            .add("", [list(z) for z in zip(provinces, value2)], "china")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="第二次人口普查不同省份总人口"),
            visualmap_opts=opts.VisualMapOpts(max_=130000000, split_number=8, is_piecewise=True),
        )
    )
    t.add(c2, "第二次人口普查不同省份总人口")

    c3 = (
        Map()
            .add("", [list(z) for z in zip(provinces, value3)], "china")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="第三次人口普查不同省份总人口"),
            visualmap_opts=opts.VisualMapOpts(max_=130000000, split_number=8, is_piecewise=True),
        )
    )
    t.add(c3, "第三次人口普查不同省份总人口")

    c4 = (
        Map()
            .add("", [list(z) for z in zip(provinces, value4)], "china")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="第四次人口普查不同省份总人口"),
            visualmap_opts=opts.VisualMapOpts(max_=130000000, split_number=8, is_piecewise=True),
        )
    )
    t.add(c4, "第四次人口普查不同省份总人口")

    c5 = (
        Map()
            .add("", [list(z) for z in zip(provinces, value5)], "china")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="第五次人口普查不同省份总人口"),
            visualmap_opts=opts.VisualMapOpts(max_=130000000, split_number=8, is_piecewise=True),
        )
    )
    t.add(c5, "第五次人口普查不同省份总人口")

    c6 = (
        Map()
            .add("", [list(z) for z in zip(provinces, value6)], "china")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="第六次人口普查不同省份总人口"),
            visualmap_opts=opts.VisualMapOpts(max_=130000000, split_number=8, is_piecewise=True),
        )
    )
    t.add(c6, "第六次人口普查不同省份总人口")

    c7 = (
        Map()
            .add("", [list(z) for z in zip(provinces, value7)], "china")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="第七次人口普查不同省份总人口"),
            visualmap_opts=opts.VisualMapOpts(max_=130000000, split_number=8, is_piecewise=True),
        )
    )
    t.add(c7,"第七次人口普查不同省份总人口")

    t.render(path="1953~2021年不同省份总人口-李运辰.html")




an2()