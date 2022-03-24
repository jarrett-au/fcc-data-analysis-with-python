import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv', index_col='id')

# Add 'overweight' column
df['overweight'] = 10000 * df['weight'] / np.square(df['height'])
df['overweight'] = df['overweight'].apply(lambda x: 1 if x > 25 else 0)


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
def norm_func(x):
    return 1 if x > 1 else 0


df['cholesterol'] = df['cholesterol'].apply(norm_func)
df['gluc'] = df['gluc'].apply(norm_func)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    columns = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=columns)

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.reset_index().groupby(['variable', 'cardio',
                                           'value']).count().reset_index()
    df_cat.rename(columns={'index': 'total'}, inplace=True)

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(data=df_cat,
                      x='variable',
                      y='total',
                      col='cardio',
                      hue='value',
                      kind='bar').fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])
                 & (df['height'] >= df['height'].quantile(0.025))
                 & (df['height'] <= df['height'].quantile(0.975))
                 & (df['weight'] >= df['weight'].quantile(0.025))
                 &
                 (df['weight'] <= df['weight'].quantile(0.975))].reset_index()

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 6))

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr,
                     mask=mask,
                     center=0,
                     vmin=-0.5,
                     vmax=0.5,
                     annot=True,
                     fmt='.1f',
                     square=True)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
