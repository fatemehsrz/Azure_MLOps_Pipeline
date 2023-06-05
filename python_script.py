from datetime import dattime, date, timedelta
import numpy as np
import pandas as pd
import argparse

import azureml.core
from azureml.core.workspace import Workspace, Datastore, Data

from azureml.core import Run, Dataset

print("date of running pipleline:", date.today())




run_context = Run.get_context()


print("setting up the AML workspace")

ws= workspace(subscription_id="YOUR SUBSCRIPTION ID", resource_group="YOUR RESOURSE GROUP", workspace_name="YOUR WORK SPACE NAME")


print(ws.name, ws.subscription_id, ws.resource_group, ws.workspace_name, ws.location)



blob_store_name= "demostore"
container_name= os.getenv ("BLOB_CONTAINER_NAME", "YOUR BLOB CONTAINER NAME")
account_name= os.getenv("BLOB_ACCOUNT_NAME", "YOUR STORAGE ACCOUNT NAME")
account_key=os.getenv("BLOB_ACCOUNT_KEY", "YOUR ACCOUNT KEY")



datastore= Datastore.get(ws, "demostore")

print("setting up the blob store for reading the inputfile")

parser= argparse.ArgumentParser()
parser.add_argument("--input-data", type=str)
args=parser.parse_args()


traing_data= Dataset.Tabular.from_delimited_files( path= [( datastore, args.input-data)]).to_pandas_dataframe()


print("data shape:", str(training_data.shape))






