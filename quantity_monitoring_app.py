import streamlit as st
import pandas as pd

st.markdown("Credits calculator for eMoodie/UCL study")

with st.form(key='form'):
    # days_passed = st.slider("How many days have passed since start of the study?", 1, 14, 1)
    uploaded_file = st.file_uploader("Upload excel file with participant results")
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:

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

            output_df.reindex(sorted(output_df.columns), axis=1)

            # Morning thought survey
            MTH = 40
            MTH_daily = MTH
            # Thought survey
            THO = 36
            THO_daily = THO*5

            # Days passed
            days_passed = len(output_df.columns)

            daily_total = MTH_daily + THO_daily
            daily_per_survey = daily_total / 6
            total_surveys_expected = 6 * days_passed

            survey_sum = round(output_df.div(daily_per_survey), 0)
            survey_sum['surveys_filled'] = survey_sum.sum(axis=1)
            survey_sum['percentage_filled'] = survey_sum['surveys_filled'] / total_surveys_expected

            survey_sum["Credits for surveys"] = [3 if value >= 0.7
                                     else 2 if value >= 0.5
                                     else 1 if value >= 0.2
                                     else 0
                                     for value in survey_sum['percentage_filled']]

            st.dataframe(survey_sum)

            st.session_state['csv'] = survey_sum.to_csv(index=False).encode('utf-8')


if 'csv' in st.session_state:

    st.download_button(
        "Press to Download",
        st.session_state['csv'],
        "file.csv",
        "text/csv",
        key='download-csv')