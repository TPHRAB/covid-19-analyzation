import pandas as pd
import matplotlib.pyplot as plt


def covid_trend_log(covid_us):
    """
    Plot of the logarithmic trend of confirmed cases in US
    :param covid_us: covid data frame restricted to US
    """
    dates = covid_us['date']
    plt.plot(dates, covid_us['total_cases'])
    plt.xticks(rotation=45, ticks=[d for i, d in enumerate(dates)
                                   if i % (len(dates) // 12) == 0 and i > 0])  # format ticks
    plt.yscale('log')
    plt.show()


def main():
    covid_world = pd.read_csv('owid-covid-data.csv')
    covid_us = covid_world[covid_world['location'] == 'United States']
    covid_trend_log(covid_us)


if __name__ == '__main__':
    main()
