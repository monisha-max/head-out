import pandas as pd
import matplotlib.pyplot as plt


def plot_graph2(df, x_column, y_columns):
    try:
        df.plot(x=x_column, y=y_columns, kind='bar')

        plt.title(f"bar plot")
        plt.xlabel(x_column)
        plt.ylabel(", ".join(y_columns))
        plt.savefig(f'pngs/plot1.png')

        df.plot(x=x_column, y=y_columns, kind='line')

        plt.title(f"line plot")
        plt.xlabel(x_column)
        plt.ylabel(", ".join(y_columns))
        plt.savefig(f'pngs/plot2.png')


        df.plot(x=x_column, y=y_columns, kind='scatter')

        plt.title(f"scatter plot")
        plt.xlabel(x_column)
        plt.ylabel(", ".join(y_columns))
        plt.savefig(f'pngs/plot3.png')



    except:
        print("Invalid graph type or data format.")
        return

def plot_graph(dataframe, x_column, y_columns):
    

    # Create a figure and axes
    fig, ax = plt.subplots()

    # Extract data from the DataFrame
    x_data = dataframe[x_column]
    y_data = dataframe[y_columns]

    # Create and save a bar plot
    ax.bar(x_data, y_data)
    plt.xlabel(x_column)
    plt.ylabel(', '.join(y_columns))
    plt.title(f'Bar Plot: {", ".join(y_columns)} vs. {x_column}')
    plt.savefig('pngs/' + '_bar.png')
    plt.close()

    
   #for column in y_columns:
   #     fig, ax = plt.subplots()
   #     ax.scatter(x_data, dataframe[column])
   #     plt.xlabel(x_column)
   #     plt.ylabel(column)
   #     plt.title(f'Scatter Plot: {column} vs. {x_column}')
   #     #plt.savefig('pngs/' + '_scatter.png')
   #    plt.close()
   

    # Create and save a line plot
    #fig, ax = plt.subplots()
    #for column in y_columns:
    #    ax.plot(x_data, dataframe[column], label=column)
    #plt.xlabel(x_column)
    #plt.ylabel(', '.join(y_columns))
    #plt.title(f'Line Plot: {", ".join(y_columns)} vs. {x_column}')
    #plt.legend()
    #plt.savefig('pngs/' + '_line.png')
    #plt.close()
