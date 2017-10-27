import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage        
from scipy.spatial.distance import squareform

dist = pd.read_table(input.txt, index_col=0, header=None, comment="#")
# refer to variables defined outside
dist.columns = SAMPLES
dist.index = SAMPLES
        
d = squareform(np.array(dist))
z = linkage(d, method="complete")

r = dendrogram(
    z, labels=snakemake.params.samples, count_sort=True, 
    color_threshold=0, 
    above_threshold_color='k')
plt.savefig(output.png)

