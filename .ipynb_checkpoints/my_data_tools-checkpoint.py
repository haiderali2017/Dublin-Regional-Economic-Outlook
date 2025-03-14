import missingno as msno
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

def data_clean(df, transformations):
    """
    This function cleans datasets.

    Parameters used:
    -----------------
    df - DataFrame
    transformations - applies transformations to the dataframe
    """
    # If the column has only missing values, then drop the entire column
    df.dropna(axis=1, how='all', inplace=True) # how='all' → Drops columns only if all values are NaN.
        
    # Removing leading and trailing spaces in column names
    cleaned_col_names = df.columns.str.strip()
    for i in range(len(df.columns)):
        df = df.rename(columns={df.columns[i]:cleaned_col_names[i]})

    # Remove '\n'
    df.columns = df.columns.str.replace('\n', ' ', regex=True)
    

    # Applying transformations - dropping selective columns in a pandas DataFrame
    for column, rules in transformations.items():
        if column not in df.columns:
            raise ValueError(f"Column '{column}' not found in dataframe.")

        # Drop columns
        if 'drop' in rules and rules['drop'] == True:
            df.drop(column, axis=1, inplace=True)

        
    # Drop missing values
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True) 

    
    # Applying transformations - (character replacements and typecasting) to specified columns in a pandas DataFrame
    for column, rules in transformations.items():
        # Skip the columns that are already dropped
        if 'drop' not in rules:         
            
            # Apply replacements
            if 'replace' in rules:
                for old_char, new_char in rules['replace'].items():
                    df[column] = df[column].astype(str).str.replace(old_char, new_char)
            
            # Apply typecasting
            if 'typecast' in rules:
                df[column] = df[column].astype(rules['typecast'])


    # Applying transformations - renaming columns
    for column, rules in transformations.items():
        
        if 'rename' in rules:
            df = df.rename(columns={column:rules['rename']})
    
    # return the processed dataset
    return df

def missingno_plot(df):
    msno.matrix(df)
    plt.show()

def visualize_data(df, x, y, chart_type, title, y_axis_label):
    """
    Creates a Plotly visualization for the given dataset.

    Parameters:
    df (pd.DataFrame): The dataset to visualize.
    x (str): Column name for the x-axis.
    y (str): Column name for the y-axis.
    chart_type (str): Type of chart ('line', 'bar', 'scatter').
    title (str, optional): Title of the chart.

    Returns:
    plotly.graph_objects.Figure: The generated figure.
    """
    
    # Choose the correct chart type
    if chart_type == "line":
        fig = px.line(df, x=x, y=y, title=title)
    elif chart_type == "bar":
        fig = px.bar(df, x=x, y=y, title=title)
    elif chart_type == "scatter":
        fig = px.scatter(df, x=x, y=y, title=title)
    else:
        raise ValueError("Invalid chart_type. Choose from 'line', 'bar', or 'scatter'.")

    if y_axis_label:
        # Update layout for y-axis label
        fig.update_layout(
            yaxis_title=y_axis_label
        )
    
    return fig

def create_heatmap(df, metrics, columns, x):
    """
    This function generates a heatmap.

    Parameters used:
    -----------------
    df - DataFrame
    metrics - the metrics that are being gauged.
    x - x-axis column
    columns - columns against which the metrics are being gauged.
    """

    metric_values = [df[columns[0]],df[columns[1]]]
    
    fig = px.imshow(metric_values,
                    labels=dict(x=x, y=f"{metrics[0]} vs {metrics[1]}", color="Intensity"),
                    x=df[x],
                    y=metrics
                   )
    # Adjust layout to ensure all labels are visible
    fig.update_layout(
        yaxis=dict(tickmode='array', tickvals=list(range(len(metrics))), ticktext=metrics)
    )
    
    return fig

def get_df(*args):
    df = args[0]
    quarter = args[1]
    column1 = args[2]
    column2 = args[3]
    var_name = args[4]
    value_name = args[5]
    
    df = df.loc[df['Quarter']==quarter, [column1,column2]]
    # Reshaping the data
    df_melted = df.melt(var_name=var_name, value_name=value_name)
    
    return df_melted