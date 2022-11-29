# ucl-emoodie

This is a streamlit-based calculator used for calculating filled survey % in the UCL/eMoodie study. 

You should upload the csv file downloaded from eMoodie backend with all of the participant survey data from a given batch. 

The calculator will then produce a table containing users as rows and columns as days where surveys in a given batch of participants were administered. The results are rounded to 1, i.e. when more than half of the questions from a given survey were answered, it will round it up to 1 (survey filled).

The total of surveys per day should be 6 per participant and the whole study period is 14 days. The calculator automatically checks how many days have passed based on the content of the dataframe and gives the total surveys filled score together with the percentage.

The credits are attributed on the following basis:
<20% - 0 credits
20-49% - 1 credit
50-70% - 2 credits
>70% - 3 credits

Please also give the participants an additional credits for the following:
1 credit for attending the sign up session
1 credit for over 50% of days where smartwatch data was collected (for those who were given a smarwatch). 

Please note the calculator does not take into account the number of questionnaires filled or the voice/video recordings. This calculator does not calculate the data quantity of smartwatch data. 

You can access the calculator by accessing this link: 
https://joannku-ucl-emoodie-quantity-monitoring-app-1dvu4t.streamlit.app/
