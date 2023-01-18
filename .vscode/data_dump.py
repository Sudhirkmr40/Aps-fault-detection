import pymongo
import pandas as pd
import json
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
data_file_path =  "/config/workspace/aps_failure_training_set1.csv"

database_name = "airpressuresystem"
collection_name = "sensor"

if __name__=="__main__":
   df = pd.read_csv(data_file_path)
   print(f"Rows and column : {df.shape}")

   
   #convert dataframe into json so tha we can dump records in mongo db 
   df.reset_index(drop = True,inplace = True)

   json_record = list(json.loads(df.T.to_json()).values())
   print(json_record[0])

# insert converted json record to mongodb
   client[database_name][collection_name].insert_many(json_record)



   



   

