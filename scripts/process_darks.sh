# script to process a dark: converts data from detector format to h5 file
# variables: dark run number
# REMEMBER TO CHANGE THE PATHS TO THE DIRECTORIES WHERE THE FILES ARE SAVED

# make the tag list
MakeTagList -b 3 -r $1 -out /UserData/maddalena/sacla2018/01-tag-lists/"$1".lst

# convert data into h5 file
ImgAvg -l /UserData/maddalena/sacla2018/01-tag-lists/"$1".lst -out /UserData/maddalena/sacla2018/02-h5compression/"$1".h5 

echo ##########################
echo END OF THE SCRIPT
echo run "$1" saved as h5 file in /UserData/maddalena/sacla2018/02-h5compression/"$1".h5
echo ##########################
