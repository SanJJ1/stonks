import pandas as pd

x = [[[i for i in range(5 + j + k)] for j in range(15 + k)] for k in range(15)]

y = pd.DataFrame(x)

print(y)