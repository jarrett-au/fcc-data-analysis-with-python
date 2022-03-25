import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = df = pd.read_csv('fcc-forum-pageviews.csv',
                      index_col='date',
                      parse_dates=True)

# Clean data
df = df[(df['value'] <= df['value'].quantile(0.975))
        & (df['value'] >= df['value'].quantile(0.025))]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='date', y='value')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.strftime('%B')
    df_bar = df_bar.groupby(by=['year', 'month']).mean().reset_index()

    # Draw bar plot
    months = pd.date_range('2022-01', '2023-01',
                           freq='M').strftime('%B').tolist()
    fig = plt.figure(figsize=(12, 6))
    sns.barplot(data=df_bar,
                x='year',
                y='value',
                hue='month',
                hue_order=months)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    months = pd.date_range('2022-01', '2023-01',
                           freq='M').strftime('%b').tolist()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 6))

    # ax1
    sns.boxplot(data=df_box, x='year', y='value', ax=ax1)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.set_title('Year-wise Box Plot (Trend)')

    # ax2
    sns.boxplot(data=df_box, x='month', y='value', ax=ax2, order=months)
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
