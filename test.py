from data_summarization.input_processing import *
from data_summarization.summarised_txt import *
from data_summarization.processing import *


import pandas as pd
import numpy as np


file = open("sample_data.csv")
df = pd_dataframe(file)
df = final_long_boi(df , ["ExperienceInCurrentDomain", "Age"])
op = get_summarised_txt(df)
print(op)


