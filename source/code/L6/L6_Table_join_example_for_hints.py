# -*- coding: utf-8 -*-
"""

Table join example.

Created on Thu Oct 12 09:48:17 2017

@author: Henrikki Tenkanen
"""

import pandas as pd

# Joining data from one DataFrame to another
# ------------------------------------------

# One quite useful functionality in Pandas is the ability to conduct a **table join**
# where data from one DataFrame is merged with another DataFrame based on a common **key**.
# Hence, making a table join requires that you have at least one common variable in both
# of the DataFrames that can be used to combine the data together.

# Consider a following example.

# Let's create some test data to our DataFrames
data1 = pd.DataFrame(data=[['20170101', 'Pluto'], ['20170102', 'Panda'], ['20170103', 'Snoopy']], columns=['Time', 'Favourite_dog'])
data2 = pd.DataFrame(data=[['20170101', 1], ['20170101', 2], ['20170102', 3], ['20170104', 3], ['20170104', 8]], columns=['Time', 'Value'])

data1
data2

# As we can see here, there different number of rows in the DataFrames. Important thing to notice is that there seems to be a common column called ``Time`` that we can use to 
# join these DataFrames together. In Pandas we can conduct a table join with ``merge`` -function. Consider following example where we join the data **from** ``data2`` DataFrame **to** ``data1`` DataFrame. 

join1 = data1.merge(data2, on='Time')
join1

# Ahaa! Now we can see that we managed to get the ``Value`` column from ``data2`` in our ``data1`` DataFrame (here we just assigned those values to a new variable ``join1``)
# It is important to notice that there were more values in the ``data2`` DataFrame than in ``data1``. The result ``join1``, does not contain the values ``3 and 8`` that were from day ``20170104`` and they were omitted. 
# This might be okey, but in some cases it is useful to also bring **all** values from another DataFrame even though there would not be a matching value in the column that used for making the join (i.e. the ``key``). 
# We can bring all the values from another DataFrame by specifyin parameter ``how='outer'``, i.e. we will make an **outer** join. 
# Let's consider another example with the outer join.
join2 = data1.merge(data2, on='Time', how='outer')
join2

# Cool! Nowe we have all the values included from both DataFrames and if Pandas did not find a common value in the ``key`` column, it still kept them and inserted ``NaN`` values into ``Favourite_dog`` column and ``Value`` column.
# Overall, knowing how to conduct a table join can be really handy in many different situations. 
# See more examples and documentation from `official documentation of Pandas <https://pandas.pydata.org/pandas-docs/stable/merging.html>`__.
