# from operator import index
# import pandas as pd
# import numpy as np

# from handy_manny import HandyManny
# import data_toolkit as dtk


# data = dtk.read_jsnl(file="./data/export-HMMIL_DP_APOFRUIT_SOLARELLI_QUALITY SEEKERS 20_WR-22946204.json",
#                      keys=["profile", "events"],
#                      identifier="id",
#                      remove_void=True)

# manny = HandyManny(data)
# manny.map_refactors(replace_missing=0, inplace=True)
# manny.map_query(key_tree={
#     "profiles": "all"}, identifier="id", inplace=True)

# manny.map_apply(dtk.flatten_dict)
# manny.apply(lambda x: pd.DataFrame(x))
# manny.data.to_csv("./apofruit_quality_seekers_events2.csv", na_rep=np.nan, index=False)



