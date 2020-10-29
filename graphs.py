import pandas as pd
import matplotlib.pyplot as plt


PLOT_DIR = 'plots/'


def generate_date_ticks(dates):
    """
    Generate a list of 12 dates

    :param dates: a list of dates
    :return: 12 dates selected from dates that is equally distributed
    """
    return [d for i, d in enumerate(dates)
            if i % (len(dates) // 12) == 0]


def total_cases(covid_us):
    """
    Plot of the linear and logarithmic trend of confirmed cases in US

    :param covid_us: covid data frame restricted to US
    """
    plt.figure()  # create a figure
    dates = covid_us['date']
    us_total_cases = covid_us['total_cases']

    # plot logarithmic plot
    plt.plot(dates, us_total_cases, linewidth=3)
    plt.xticks(rotation=45, ticks=generate_date_ticks(dates))

    plt.xlabel('Date')
    plt.grid(color='grey', linestyle='--')

    # logarithmic plot
    plt.yscale('log')
    plt.title('US Total Cases (log)')
    plt.ylabel('Cases')
    plt.ylim(1, 10000000)
    plt.savefig(PLOT_DIR + 'total_cases_log.png', bbox_inches='tight')

    # generate linear plot
    plt.yscale('linear')
    plt.title('US Total Cases (linear)')
    plt.ylabel('Cases (millon)')
    plt.ylim(0, 9000000)
    plt.savefig(PLOT_DIR + 'total_cases_linear.png', bbox_inches='tight')



def new_cases(covid_us):
    """
    Plot of the linear and logarithmic trend of new cases in US

    :param covid_us: covid data frame restricted to US
    """
    plt.figure()
    dates = covid_us['date']
    us_new_cases = covid_us['new_cases']

    plt.plot(dates, us_new_cases)
    plt.xticks(rotation=45, ticks=generate_date_ticks(dates))

    plt.xlabel('Date')
    plt.ylabel('Cases')

    # linear plot
    plt.title('US New Cases (linear)')
    plt.yscale('linear')
    plt.savefig(PLOT_DIR + 'new_cases_linear.png', bbox_inches='tight')

    # logarithmic plot
    plt.title('US New Cases (log)')
    plt.yscale('log')
    plt.savefig(PLOT_DIR + 'new_cases_log.png', bbox_inches='tight')


def main():
    covid_world = pd.read_csv('owid-covid-data.csv')
    covid_us = covid_world[covid_world['location'] == 'United States']
    total_cases(covid_us)
    new_cases(covid_us)


if __name__ == '__main__':
    main()
