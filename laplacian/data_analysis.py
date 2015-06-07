import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    read_path = 'data/data.csv'
    write_path = 'data/data.png'

    df = pd.read_csv(read_path)

    del df['num_edges']
    del df['iter']

    df.plot()
    plt.savefig(write_path)
