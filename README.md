# SACLA_2022B8033
Analysis tools for the experiment `2022B8033` at SACLA XFEL (BL3, EH2). The experiment uses SAXS/WAXS on droplets. This repo includes analysis scripts for:
* converting the data from `.json` to `.h5` file format
* performing angular integration 
* sorting data based on hits/miss, excluding shots with streaks, and identifying liquid/frozen shots.  

![](https://github.com/fperakis/SACLA_2022B8033/blob/main/examples/img.jpg?raw=true)

### Documentation:
* [Usage examples:](Documentation/usage.md)  Data process pipeline during beamtime
* [Configuration: ](Documentation/instructions.md) setting up of your system at SACLA servers
* [Testing:](Documentation/interactive_qsub.md) Submitting jobs interactively with `qsub -I` 
* [Scripts overview:](Documentation/pipeline.md) details on the scripts and data processing pipeline
* [Useful Links:](Documentation/links.md) from SACLA and other sources

