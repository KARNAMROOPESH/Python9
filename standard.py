import pandas as pd
import plotly_express as pe
import statistics
import math

one = pd.read_csv('./class1.csv')
two = pd.read_csv('./class2.csv')

mean1 = statistics.mean(one['Marks'])
mean2 = statistics.mean(two['Marks'])

df1 = one['Marks'].tolist()
df2 = two['Marks'].tolist()
slist1 = []
slist2 = []

for i in df1:
    diff = mean1 - i
    mult = diff * diff
    slist1.append(mult)

for i in df2:
    diff = mean2 - i
    mult = diff*diff
    slist2.append(mult)

sum1 = sum(slist1)
sum2 = sum(slist2)

length1 = len(slist1) - 1
length2 = len(slist2) - 1

ans1 = sum1/length1
ans2 = sum2/length2

""" standard deviation = sqrt(sum(men-dataPoint)^2 / n-1) , n = total observation """
std1 = math.sqrt(ans1)
std2 = math.sqrt(ans2)

fig = pe.scatter(one,x = 'Student Number' , y = 'Marks')
fig.update_layout(shapes=[dict(type = 'line' , x0 = 0 , x1 = len(slist1) , y0 = mean1 , y1 = mean1),dict(type = 'line' , x0 = 0 , x1 = len(slist1), y0 = std1 , y1 = std1)])

fig2 = pe.scatter(two, x ='Student Number' , y='Marks')
fig2.update_layout(shapes=[dict(type='line',x0 = 0 , x1 = len(slist2 ) , y0 = mean2 , y1 = mean2 ), dict(type='line', x0=0 , x1 = len(slist2), y0 = std2 , y1 = std2)])
