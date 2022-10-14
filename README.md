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

Here replace "fperakis" with your user name-
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

create virtual environment 
```bash
python -m venv venv
source venv/bin/activate
which python
```

add to the ~/.bashrc the following 
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
