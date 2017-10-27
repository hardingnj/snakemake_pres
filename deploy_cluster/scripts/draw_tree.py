import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage        

dist = pd.read_table(snakemake.input.txt, index_col=0, header=None, comment="#")
# refer to variables defined outside
dist.columns = snakemake.params.samples
dist.index = snakemake.params.samples

d = np.array(dist)
z = linkage(d, method="complete")

r = dendrogram(
    z, labels=snakemake.params.samples, count_sort=True, 
    color_threshold=0, 
    above_threshold_color='k')
plt.savefig(output.png)

