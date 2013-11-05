Hey Adam,

First, spin up some clusters in the IPython Dashboard.

In the first part, I was just testing out things and printing the results. I found that you can either do the apply_async or the pool.map, so I tried both. In the end, pool.map looked a bit faster and the code was a bit cleaner so I used that for the formal analyses.

After this I clear the namespace, and redefine my pi finder functions to return tuples of the values I am interested in, and then I pull these into a pandas dataframe, and then pull from the dataframe to plot. 