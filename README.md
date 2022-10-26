# SACLA_2022B8033
Analysis tools for the experiment 2022B8033 at SACLA XFEL (BL3, EH2)


-----------------------------

### Useful links 

manual http://xfel.riken.jp/users/pdf/hpc_startup_manual_ver1.8.pdf

install VPN https://hpc.spring8.or.jp 

analysis software http://xhpcfep.hpc.spring8.or.jp/manuals/modules  

new user hpc account http://xhpcelog.hpc.spring8.or.jp/account/login 

-----------------------------

### Connecting and transfering 

Here replace "fperakis" with your user name.
```bash
ssh -X fperakis@xhpcfep.hpc.spring8.or.jp
```

```bash
scp local_file fperakis@xhpcfep.hpc.spring8.or.jp:/home/fperakis
```

-----------------------------
### Setting up procedure 

activate SACLA tools
```bash
ml python/SACLA_python-3.7/offline
which python
```

create a virtual environment 
```bash
python -m venv venv
source venv/bin/activate
which python
```

add to your ~/.bashrc the following 
```bash
source env/bin/activate
export PIP_PROXY=http://proxy.hpc.spring8.or.jp:3128
export HTTPS_PROXY=http://proxy.hpc.spring8.or.jp:3128
```

-----------------------------
### Running Jupiter lab

run on terminal on remote computer (here port number 8887 is chosen randonmly)
```bash
jupyter lab --no-browser --port 8887 &
```

run on terminal on local computer 
```bash
ssh -N -L localhost:8887:localhost:8887 fperakis@xhpcfep.hpc.spring8.or.jp
```

open in browser
http://localhost:8887

copy paste “token” and you are good to go.

-----------------------------

### setting up GitHub repo
configure 
```bash
git config --global user.name fperakis
git config --global color.ui auto
git config --global user.email f.perakis@fysik.su.se
git config --global http.proxy http://proxy.hpc.spring8.or.jp:3128
```

standard git commands
```bash
git clone https://github.com/fperakis/SACLA_2022B8033.git
git status
git add [file]
git commit -m “[message]”
git push
git pull
```
note that to be able to push you will need to create a PAT (instead of password), I used the classic token
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token 

-----------------------------
### Converting data to h5

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
