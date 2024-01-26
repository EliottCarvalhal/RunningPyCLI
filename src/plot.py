import matplotlib.pyplot as plt
import numpy as np
from db import query_all
from data import calculate_pace
from datetime import datetime

runs = query_all()

import matplotlib.pyplot as plt
from datetime import datetime

runs = query_all()

def scatter_plot_runs():
    dates = []
    paces = []

    # Filter and sort runs by date
    filtered_runs = sorted([run for run in runs if 5.2 > run.dist > 4.90], key=lambda run: run.date)

    for run in filtered_runs:
        dates.append(datetime.strptime(run.date, '%d/%m/%Y'))  # Convert date string to datetime object
        pace = calculate_pace(run.dist, run.time)
        paces.append(pace)

    # Sort paces from shortest to longest time
    sorted_indices = sorted(range(len(paces)), key=lambda k: datetime.strptime(paces[k], '%M:%S'))
    sorted_dates = [dates[i] for i in sorted_indices]
    sorted_paces = [paces[i] for i in sorted_indices]

    fig, ax = plt.subplots()
    ax.plot(sorted_dates, sorted_paces, marker='o', linestyle='-')

    # Format x-axis labels as dates
    plt.gcf().autofmt_xdate()

    plt.xlabel('Date')
    plt.ylabel('Pace (min/km)')
    plt.title('Pace Over Date for 5k Runs')
    plt.show()
