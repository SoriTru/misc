import pandas as pd

if __name__ == '__main__':
    vaers_data_2020 = pd.read_csv('2020VAERSData/2020VAERSDATA.csv', low_memory=False, index_col=0)
    vaers_data_2021 = pd.read_csv('2021VAERSData/2021VAERSDATA.csv', low_memory=False, index_col=0)
    vax_data_2020 = pd.read_csv('2020VAERSData/2020VAERSVAX.csv')
    vax_data_2021 = pd.read_csv('2021VAERSData/2021VAERSVAX.csv')

    # get only covid vaccine data
    # NOTE: this is all covid vaccine VAERS data for 2020 and 2021 (as of 07/16/2021), not just since Dec 2020
    non_covid_ids_2020 = [id for id in vax_data_2020[vax_data_2020['VAX_TYPE'] != 'COVID19'].VAERS_ID]
    non_covid_ids_2021 = [id for id in vax_data_2021[vax_data_2021['VAX_TYPE'] != 'COVID19'].VAERS_ID]

    covid_df_2020 = vaers_data_2020.drop(non_covid_ids_2020)
    covid_df_2021 = vaers_data_2021.drop(non_covid_ids_2021)

    # save dataframe
    covid_df = pd.concat([covid_df_2020, covid_df_2021])
    covid_df.to_pickle('./covid_vax_data.pkl')
