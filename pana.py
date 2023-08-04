import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    # The link to the data source could be a comment above this function
    # https://www.moneydj.com/etf/x/basic/basic0011.xdjhtm?etfid=0050.tw

    data = {
        'Year': [2018, 2019, 2020, 2021, 2022],
        'StdDev': [15.15, 11.12, 28.88, 11.07, 26.43],
        'Beta': [1.08, 0.99, 1.03, 0.94, 0.94],
        'Sharpe': [-0.0871, 0.7586, 0.3079, 0.5267, -0.2332],
        'Treynor': [-0.3542, 2.4506, 2.4961, 1.7926, -1.9000],
        'Jensen': [0.3540, 0.3941, 0.1736, 0.2687, 0.2009],
        'Information': [-0.2444, -0.2758, 0.2772, -0.1518, 0.0149]
    }

    return pd.DataFrame(data)


def plot_stddev(df):
    plt.bar(df['Year'], df['StdDev'], alpha=0.7, color='blue')
    plt.title('Annual Standard Deviation')
    plt.xlabel('Year')
    plt.ylabel('StdDev')


def plot_beta(df):
    plt.plot(df['Year'], df['Beta'], color='red', marker='o')
    plt.title('Beta Over Years')
    plt.xlabel('Year')
    plt.ylabel('Beta')


def plot_risk_adjusted_performance(df):
    df.plot(x='Year', y=['Sharpe', 'Treynor', 'Jensen',
            'Information'], kind='bar', stacked=True, ax=plt.gca())
    plt.title('Risk Adjusted Performance Indicators')
    plt.ylabel('Value')


def display_table(df):
    # Create a table at the bottom left, below the subplots
    ax = plt.gca()
    rows = ['Year'] + list(df['Year'])
    cell_data = [df[column].tolist() for column in df.columns]
    cell_data = [[col] + data for col, data in zip(df.columns, cell_data)]

    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=cell_data, colLabels=None,
             cellLoc='center', loc='center')
    plt.title('Performance Metrics Table', fontsize=14, y=1.1)


def main():
    df = load_data()

    plt.figure(figsize=(14, 12))

    plt.subplot(2, 2, 1)
    plot_stddev(df)

    plt.subplot(2, 2, 2)
    plot_beta(df)

    plt.subplot(2, 2, 3)
    plot_risk_adjusted_performance(df)

    plt.subplot(2, 2, 4)
    display_table(df)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
