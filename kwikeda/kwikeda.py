import pandas as pd
import numpy as np

class openProcess:
    """
    This will load the given file and do the Exploratory data analysis

    """
    def __inti__(self):
        pass

    def load_output(self,filename):
        # EDA Step 2:
        # loading data
        try:
            df = pd.read_csv(filename)
            # number of rows
            total_rows = df.shape[0]
            # number of columns
            total_columns = df.shape[1]

            # Number of missing values per column and their percentage
            missing_data = df.isnull().sum()
            columns_with_missing_data = pd.DataFrame()
            columns_with_missing_data['Columns'] = missing_data.index
            columns_with_missing_data['Missing_Count'] = [data if data == 0 else data for data in missing_data]
            columns_with_missing_data['% Missing'] = np.round(
                columns_with_missing_data['Missing_Count'] / total_rows * 100, 2).astype(str) + ' %'
        except:
            return ("Something is wrong")
        return columns_with_missing_data