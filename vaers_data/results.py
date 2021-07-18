import pandas as pd
from datetime import datetime

if __name__ == '__main__':
    vax_data = pd.read_pickle('covid_vax_data.pkl')

    reported_deaths = vax_data[vax_data['DIED'].notna()]

    reported_deaths_count = len(reported_deaths)

    uncountable = []
    time_diffs_days = []

    for index in reported_deaths.index:
        vax_date = reported_deaths['VAX_DATE'][index]
        death_date = reported_deaths['DATEDIED'][index]

        if pd.isna(vax_date) or pd.isna(death_date):
            uncountable.append({'vax_date': vax_date, 'death_date': death_date})
            continue

        received = datetime.strptime(vax_date, '%m/%d/%Y').timestamp()
        died = datetime.strptime(death_date, '%m/%d/%Y').timestamp()
        time_diff = (died - received)/(60*60*24)
        time_diffs_days.append(time_diff)

        if time_diff < 2:
            print({'HISTORY': reported_deaths['HISTORY'][index],
                   'LAB_DATA': reported_deaths['LAB_DATA'][index],
                   'SYMPTOM_TEXT': reported_deaths['SYMPTOM_TEXT'][index],
                   'CUR_ILL': reported_deaths['CUR_ILL'][index]})
            print()

    print(f'Number of records with either vax date or death date not included: {len(uncountable)}')

    count_one_day = 0
    count_two_days = 0
    for time in time_diffs_days:
        if time <= 1:
            count_one_day += 1

        if time <= 2:
            count_two_days += 1

    num_time_diffs = len(time_diffs_days)
    print(f'Percentage died within 24 hrs: {(count_one_day/num_time_diffs)*100}')
    print(f'Percentage died within 48 hrs: {(count_two_days/num_time_diffs)*100}')


