import datetime
import numpy as np

start = datetime.date(2022, 3, 15)
end = datetime.date(2022, 4, 16)

days = np.busday_count(start, end)
print('Number of business days is:', days)
