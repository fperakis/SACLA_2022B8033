# Converting data to h5 interactively
-----------------------------

Here is an example of how to convert SACLA data to h5. 

Start the qsub used to interactively submit jobs to the queue. 
```bash
qsub -I -X
```
Load the offline SACLA tools modules
```bash
module load SACLA_tool
```
Check the run info and available detector ID for the desired run (-r) and beamline (-b):
```bash
ShowRunInfo -b 3 -r 739127
```
```bash
ShowDetIDList -b 3 -r 739127
```

Make the tag list that will be used for the conversion marking the beamline (-b), run (-r) and detector ID (-det)
```bash
MakeTagList -b 3 -r 739127 -det 'OPAL-234363' -out tag_739127.lst
```

You can also select start and end tag number 
```bash
MakeTagList -b 3 -r 739127 -det 'OPAL-234363' -starttag 850076252 -endtag 850076268 -out tag_739127.lst 
```

Run data convert
```bash
DataConvert4 -l tag_739127.lst -dir . -o 739127.h5
```

or you can use the image averarging tool
```bash
ImgAvg -l tag_739127.lst -out  739127.h5
```
