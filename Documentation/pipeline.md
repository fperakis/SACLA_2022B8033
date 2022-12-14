## Script Overview

### Step 1: process darks
> Creates h5 files based on dark runs. This script does the following:

    job_darks.sh                              # defines parameters for the job submission and runs process_darks.sh
          └──process_darks.sh                 # runs MakeTagList, ImgAvg and then saves an h5 file 
                  ├── MakeTagList             # generates a list of numbers for the given run number 
                  └── ImgAvg                  # averages the images of a given run specified specified by the MakeTagList

### Step 2: compress data
> Creates h5 files based on given runs and calcualte the I(q) for each shot. It compresses the data from the original .json files which contains 2D images of all shots into the final h5 file which containes I(q) of each run. 

    compress.py                               # finds the first and last tag number and splits the run into 10 jobs using process_all.sh 
       └──process_all.sh                      # defines parameters for the job submission and runs process_run.sh
             └──process_run.sh                # runs MakeTagList, runs DataConvert4 and then saves an h5 file 
                  ├── MakeTagList             # generates a list of numbers for the given run number 
                  └── DataConvert4            # generates an h5 file containing the images of a given run/tags specified specified by the MakeTagList
             └──IqPhi.py                      # Calculates the Iq of the given run/tags and generates an h5 file with the Iqs for each shot
          
### Step 3: analyse data
> Use jupyter notebooks to load h5 file with I(q) data and analyse the data including filtering for:
> - find hit/misses 
> - excludes shots with streaks 
> - distinguish between shots with liquids or ice 
