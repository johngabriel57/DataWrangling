import pandas as pd
data1= {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'Math': [80, 95, 79]}
data2= {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'Electronics': [85, 81, 83]}
data3= {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'GEAS': [90, 79, 93]}
data4= {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'ESAT': [93, 89, 88]}

math= pd.DataFrame(data1, columns= ['Student', 'Math'])
electronics= pd.DataFrame(data2, columns= ['Student', 'Electronics'])
esat= pd.DataFrame(data4, columns= ['Student', 'ESAT'])
geas= pd.DataFrame(data3, columns= ['Student', 'GEAS'])

merge= pd.merge(math,electronics, on='Student')
merge1= pd.merge(merge, esat, on='Student')
bear_grades= pd.merge(merge1, geas, on='Student')

longbear = pd.melt(bear_grades, id_vars= 'Student', value_vars= ['Math','Electronics','ESAT','GEAS'])
newbear_grades = longbear.rename(columns= {'variable':'Subject', 'value':'Grades'})
