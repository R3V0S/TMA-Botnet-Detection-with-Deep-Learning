In the Data folder you can find the processed .CSV files with the Scenario 10 and the Scenario 11 data. By using the OpenRefine tool (https://openrefine.org/), we can filter and clean the raw tracesets, which are obtained from https://www.stratosphereips.org/datasets-ctu13. More concretely, from:

>>> https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-51/detailed-bidirectional-flow-labels/ # For the Scenario 10
>>> https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-52/detailed-bidirectional-flow-labels/ # For the Scenario 11

Here, you cand find different jupyter notebooks. The complete version is the _1DCNN_CTU13_READY.ipynb_, which processes the both datasets.

In the notebook, you can find detailed information about the different code-lines, post-processing techniques and the model definition. Also, the training and testing phase are validated.
