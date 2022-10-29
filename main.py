
import pandas as pd
from src.preprocess import Preprocess, drop_columns
# from src.preprocess import load_transaction_data


DATA_PATH = "data/transaction.csv"


def main() -> None:

    # load the data and create the data manager
    data =  pd.read_csv(DATA_PATH , sep=';')
    output = Preprocess(data, data['NumberOfItemsPurchased'] , data['CostPerItem'] , data['SellingPricePerItem'])
    
    desc = output.describe()
    print('*******************************************DATA DESSCRIPTION*****************************************************\n')
    print(desc)
    output.cost_per_tranx()
    output.sale_per_tranx()
    output.profit_per_tranx()
    output.split_client_keywords()
    output.combine_date()
    output.lower_case()
    output.export_dataset_csv()
    drop_columns()
    print('*******************************************END*****************************************************')



if __name__ == "__main__":
    main()








# df = pd.read_csv('data/transaction.csv', sep=';')
# # print(data.head())
# val = Preprocess(df,df['NumberOfItemsPurchased'] , df['CostPerItem'] , df['SellingPricePerItem'] )
# print(val.describe())

# print('*************************************************************************************************************************************************')
# print(val.cost_per_tranx())
# print('**********************************************************************************************************************************************')
# print(val.sale_per_tranx())
# print('****************************************************************************************************************************************************')
# print(val.profit_per_tranx())
# print('****************************************************************************************************************************************************')
# print(val.split_client_keywords())
# print('*********i*******************************************************************************************************************************************')
# print(val.lower_case())
# print(val.combine_date())