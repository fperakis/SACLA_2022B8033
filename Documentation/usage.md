# Data process pipeline

### Step 1: process darks
> Creates `.h5` files based on dark runs. Example of use:
 ```bash
 qsub -v run=690007 job_darks.sh 
 ```
 
 ### Step 2: compress data
> Creates `.h5` files based on given runs and calcualte the I(q) for each shot. It compresses the data from the original `.json` files which contains 2D images of all shots into the final `.h5` file which containes I(q) of each run. The input is run number and dark number. 
> Example of use:
```bash
python compress.py -r 690006 -d 690007
```

### Step 3: analyse data
> Use jupyter notebooks to load `.h5` file with I(q) data and analyse the data including filtering for:
> - find hit/misses 
> - excludes shots with streaks 
> - distinguish between shots with liquids or ice 
