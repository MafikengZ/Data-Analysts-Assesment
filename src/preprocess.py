# import i18n
from xmlrpc.client import DateTime
import pandas as pd

from typing import TypeVar
from typing import Callable
from functools import reduce
from dataclasses import dataclass
import datetime


PandasDataFrame = TypeVar('pandas.core.frame.DataFrame')
# Preprocessor = Callable[[PandasDataFrame], PandasDataFrame]

@dataclass
class Preprocess:
    data: PandasDataFrame
    item:pd.DataFrame.columns
    cost:pd.DataFrame.columns
    sale: pd.DataFrame.columns
    
    def describe(self)-> PandasDataFrame:
       '''
       Func returns statistical summery of your data
       Arg: pandas dataframe
       Return: dataframe
       '''
       return self.data.describe()
    
    def cost_per_tranx(self)-> PandasDataFrame:
        
        '''
        Create an additional column in the dataframe called
    
        '''
        self.data['CostPerTransaction'] = self.item * self.cost
        return self.data.head()

    def sale_per_tranx(self)-> PandasDataFrame:
        
        self.data['SalePerTransaction'] = self.item * self.sale
        return self.data.head()
        
    def profit_per_tranx(self)-> PandasDataFrame:
        
        self.data['ProfitPerTransaction'] = round(self.data['SalePerTransaction'] - self.data['CostPerTransaction'])
        return self.data.head()

    def combine_date (self)-> PandasDataFrame:
        
        self.data.Month = pd.to_datetime(self.data.Month, format="%b").dt.month
        self.data['Date'] =  pd.to_datetime(self.data[['Day','Month','Year']]).dt.strftime('%d-%b-%Y')
        
        # self.data.Date = self.data['Date'].dt.month_name().str.slice(stop=3)
        
        return self.data.head()

    def lower_case(self)->PandasDataFrame:
        lower= self.data['ItemDescription'].str.lower()
        return lower


    def split_client_keywords(self)-> PandasDataFrame:
        '''Func expand keyword column in to multiple columns'''
        
        # strip list brackets
        self.data['ClientKeywords'] = self.data['ClientKeywords'].str.strip('[]').astype(str)
        # split strings by colon
        new = self.data["ClientKeywords"].str.split(", ", n = 1, expand = True)
        self.data['ClientAge'] = new[0]
        self.data['ClientType1'] = new[1]
        new1 = self.data['ClientType1'].str.split(", ", n = 1, expand = True)
        self.data['ClientType'] = new1[0]
        self.data['LengthofContract'] = new1[1]
        # self.data.drop( self.data['ClientType1 pd.read_csv('data/transaction.csv', sep=';')'] ,axis=0, inplace=True)

        return self.data.head()
    
    def export_dataset_csv(self)->PandasDataFrame:
        '''Func export pandas dataframe to_csv'''
        
        return self.data.to_csv('data/output_dataframe.csv', index=False)
    
def drop_columns()-> None:
    '''Func drops redundant columns'''
    output_file=pd.read_csv('data/output_dataframe.csv')
    output_file.drop(['ClientKeywords' , 'ClientType1'], axis=1 , inplace=True)

# def compose(*functions: Preprocessor) -> Preprocessor:
#     return reduce(lambda f, g: lambda x: g(f(x)), functions)


# def load_transaction_data(path: str) -> PandasDataFrame:
#     # load the data from the CSV file
#     data = pd.read_csv(path, sep=';')

#     Preprocessor = compose(
#         Preprocess.describe,
#         Preprocess.cost_per_tranx,
#         Preprocess.sale_per_tranx,
#         Preprocess.profit_per_tranx,
#         Preprocess.combine_date,
#         Preprocess.lower_case,
#         Preprocess.export_dataset_csv,
#     )
#     return Preprocessor(data)