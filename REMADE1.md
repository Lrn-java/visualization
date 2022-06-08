# 人口普查数据时间轴散点图可视化项目文档

## 1. 文档标题
人口普查数据时间轴散点图可视化项目

## 2. 简介
本项目的目的是通过时间轴上的散点图来可视化不同年份的人口普查数据，以便观察和比较不同省份在不同时间点的人口数量。

## 3. 代码概述
项目使用了Pandas库来处理数据，Pyecharts库来创建图表，以及一个Excel文件作为数据源。

## 4. 数据加载
使用Pandas的`read_excel`函数加载名为'七次人口普查数据.xlsx'的Excel文件。

## 5. 数据预处理
从DataFrame中提取省份名称，并创建一个字典`census_data`来保存各个年份的人口普查数据。

## 6. 数据检查
通过打印语句对数据进行检查，确保数据加载正确。

## 7. 散点图生成函数
定义了一个名为`scatterChart`的函数，该函数使用Pyecharts创建时间轴散点图。

## 8. 时间轴设置
创建一个`Timeline`对象，用于管理不同年份的散点图。

## 9. 颜色设置
定义了一个颜色列表，用于为不同年份的散点图设置颜色。

## 10. 散点图配置
对于`census_data`字典中的每个年份，创建一个`Scatter`对象，并为它添加x轴（省份）和y轴（人口数量）的数据。

## 11. 图表全局选项设置
为每个散点图设置全局选项，包括图表标题、y轴和x轴的名称。

## 12. 时间轴添加散点图
使用`timeline.add`方法将每个年份的散点图添加到时间轴对象中，并以年份作为标签。

## 13. 渲染和输出
使用`timeline.render`方法将时间轴散点图渲染到一个名为'散点图-马文金.html'的HTML文件中。

## 14. 运行脚本
调用`scatterChart`函数以生成并渲染散点图。

## 15. 散点图数据点
散点图使用省份作为x轴，人口数量作为y轴，通过散点图可以直观地看到不同省份的人口数量对比。

## 16. 颜色应用
为每个年份的散点图数据点设置不同的颜色，以便于区分。

## 17. 图表标题
每个散点图都有与其年份对应的标题，方便用户识别。

## 18. 轴标签
设置了x轴和y轴的标签，分别代表“省份”和“人口数量”。

## 19. 渲染输出
最终的散点图将被保存为HTML文件，可以通过Web浏览器查看。