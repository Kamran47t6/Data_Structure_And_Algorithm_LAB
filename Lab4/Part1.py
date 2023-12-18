# bar chart

import matplotlib.pyplot as plt 
import pandas as pd
df = pd.read_csv('dailySteps_merged.csv' ) 
print(df.dtypes)
list1 = df['Id'].values.tolist() 
list2 = df['StepTotal' ].values.tolist() 
plt.bar(list1, list2,width = 1, color = ['red', 'green'])
plt.show()


# scatter chart
import matplotlib.pyplot as plt 
import pandas as pd
df = pd.read_csv('hourlySteps_merged.csv' ) 
print(df.dtypes)
list1 = df['ActivityHour'].values.tolist() 
list2 = df['StepTotal' ].values.tolist() 
plt.scatter(list1, list2)
plt.show()
