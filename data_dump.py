import pandas as pd
import pymongo
import json



client = pymongo.MongoClient("mongodb+srv://Mukul:12345@cluster0.daqxmxi.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH=(r"C:\Users\Mukul\Insurance\Insurance-premium-prediction\insurance.csv")

DATABASE_NAME='insurance'
COLLECTION_NAME='insurance_project'


if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    df.reset_index(drop = True, inplace = True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)