#!/usr/bin/env python
# coding: utf-8

# In[77]:


# pip install pandas openpyxl plotly plotly.express


# In[90]:


import pandas as pd
import pprint

# df1 = pd.read_excel('AllSurveys_TextDATA_20221101083046.xlsx')
# df2 = pd.read_excel('AllSurveys_TextDATA_20221101080022.xlsx')
# df = pd.read_excel('AllSurveys_TextDATA_20221103125211.xlsx')

df = pd.read_excel('data/AllSurveys_TextDATA_20221107031144.xlsx') # Completed week 1

# df = pd.concat([df1,df2], axis=0)
df


# In[91]:


output = {}
users = df['user'].unique().tolist()
for user in users:
    is_user = (df.user == user)
    dayCounts = {user: (df[is_user]['surveystartdate'].value_counts())}
    output.update(dayCounts)
    
outputdf = pd.DataFrame.from_dict(output).T
outputdf.sort_index()


# In[92]:


outputdf=outputdf.drop(columns=['######'])
outputdf.columns.tolist()


# In[93]:


MTH = 40
MTH_daily = MTH
THO = 36
THO_daily = THO*5
daily_total = MTH_daily + THO_daily
daily_per_survey = daily_total /6 
daily_per_survey
total_surveys_expected = 6 * 14
total_surveys_expected


# In[94]:


outputdf


# In[95]:


survey_sum = round(outputdf.div(daily_per_survey),0)
survey_sum


# In[96]:


survey_sum['surveys_filled'] = survey_sum.sum(axis=1)
survey_sum


# In[99]:


survey_sum['percentage_filled'] = survey_sum['surveys_filled'] / total_surveys_expected
survey_sum


# In[101]:


for value in survey_sum['percentage_filled']:
    if value >= 0.7:
        credits.append(4)
    elif value >= 0.5:
        credits.append(3)
    elif value >= 0.2:
        credits.append(2)
    else:
        credits.append(0)
        
survey_sum["Credits"] = result  
print(survey_sum)


# In[106]:


survey_sum["Credits"] = [4 if value>=0.7 
                         else 3 if value>=0.5 
                         else 2 if value>=0.2 
                         else 1 
                         for value in survey_sum['percentage_filled']]
survey_sum


# In[107]:


survey_sum.to_csv("TotalSurveys_October20start.csv")


# In[ ]:





# In[ ]:





# In[ ]:





# In[11]:


import plotly.express as px

for user in users:
    fig = px.bar(outputdf, x='year', y='pop')
    fig.show()

import plotly.express as px
fig = px.histogram(outputdf, x="total_bill")
fig.show()


# In[ ]:





# In[33]:


df['missed_filled'] = df['surveytriggerdetails'].astype(str).str[0:13]

users = df['user'].unique().tolist()

output = {}

for user in users:
    is_user = (df.user == user)
    d1 = {user: (df[is_user]['missed_filled'].value_counts())}
    output.update(d1)
    
outputdf = pd.DataFrame.from_dict(output).T
outputdf.sort_index()


# In[34]:


outputdf.columns


# In[35]:


outputdf['Percentage flled (%)'] = (
    (outputdf['User Initiate'] + outputdf['Notification '])
     / ((outputdf['Missed Survey']) + outputdf['User Initiate'] + outputdf['Notification ']) * 100)

outputdf


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[27]:


nwdf = df.groupby(by=['user', 'surveystartdate']).count()

nwdf


# In[28]:


# question_codes = df['questioncode'].unique().tolist()

# responsetext != 999


# In[123]:


from datetime import date
today = date.today()


# In[221]:


df['missed_filled'] = df['surveytriggerdetails'].astype(str).str[0:13]

MTH = 40
MTH_daily = MTH
THO = 36
THO_daily = THO*5
daily_total = MTH_daily + THO_daily
daily_total
days_sinceStart = 6

# fltr = (df['surveytriggerdetails'] == "User Initiated")
df2 = df.loc[(df['surveytriggerdetails'] == "User Initiated")].groupby(by=['user','surveystartdate']).count()
df2["surveys_filled"] = round((df2["questioncode"] / daily_total * 6),0)
# pd.set_option("display.max_rows", None, "display.max_columns", None)
# df2 = df2['questioncode']
final_count = pd.DataFrame(df2["surveys_filled"])
final_count = final_count.reset_index()


# In[248]:





# In[222]:


final_count.columns.tolist()


# In[236]:





# In[223]:


import plotly.express as px
fig = px.bar(final_count, x='surveystartdate', y='surveys_filled', color='user')
fig.show()


# In[238]:


users = final_count['user'].unique().tolist()


# In[242]:


for user in users: 
    condition = (final_count.reset_index().user == user)
    fig = px.bar(final_count[condition], x='surveystartdate', y='surveys_filled', title=user)
    fig.show()

