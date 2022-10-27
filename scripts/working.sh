# test if a file exist in the directory
# argument: filename
FILE = "$1"
if test -f "$FILE",  
then 
  echo "$FILE already exists."
fi

# if TEST-COMMAND
# then
#   STATEMENTS1
# else
#   STATEMENTS2
# fi

# FILE = /etc/resolv.conf
# if test -f "$FILE"; then
#     echo "$FILE exists."
# fi