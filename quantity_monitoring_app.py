import streamlit as st
import pandas as pd


uploaded_file = st.file_uploader("Upload excel file with participant results")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

output = {}
users = df['user'].unique().tolist()
for user in users:
    is_user = (df.user == user)
    dayCounts = {user: (df[is_user]['surveystartdate'].value_counts())}
    output.update(dayCounts)

output_df = pd.DataFrame.from_dict(output).T.drop(columns=['######'])
output_df.sort_index()

days_passed = output_df.columns.tolist

# Morning thought survey
MTH = 40
MTH_daily = MTH
# Thought survey
THO = 36
THO_daily = THO*5

daily_total = MTH_daily + THO_daily
daily_per_survey = daily_total / 6
days_passed = len(output_df.columns.tolist())
total_surveys_expected = 6 * days_passed

survey_sum = round(output_df.div(daily_per_survey), 0)
survey_sum['surveys_filled'] = survey_sum.sum(axis=1)
survey_sum['percentage_filled'] = survey_sum['surveys_filled'] / total_surveys_expected

survey_sum["Credits"] = [4 if value >= 0.7
                         else 3 if value >= 0.5
                         else 2 if value >= 0.2
                         else 1
                         for value in survey_sum['percentage_filled']]

st.dataframe(survey_sum)
