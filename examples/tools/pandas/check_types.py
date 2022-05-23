import pandas as pd
from convenient_datascience_tools.tools import pandas as pd_tools

df = pd.DataFrame({ 
    "ColunaInt": [1, 2, 3],
    "ColunaObject":  ["a", "b", "c"],
    "ColunaFloat": [1.2, 1.3, 1.4]
})

pd_tools.check_types(df)