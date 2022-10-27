# script to process a run: converts data from detector format to h5 file
# variables: run number, dark h5 file
# REMEMBER TO CHANGE THE PATHS TO THE DIRECTORIES WHERE THE FILES ARE SAVED
# CHECK ALSO THE DETECTOR NAME

# make the tag list
MakeTagList -b 3 -r $1 -det 'MPCCD-8-2-002' -out /UserData/maddalena/sacla2018/01-tag-lists/"$1".lst
#MakeTagList -b 3 -r $1 -det 'MPCCD-8-2-002' -starttag 486976704 -endtag 486978704 -out /UserData/maddalena/sacla2018/01-tag-lists/"$1".lst

# convert data into h5 file
DataConvert4 -l /UserData/maddalena/sacla2018/01-tag-lists/"$1".lst -dir /UserData/maddalena/sacla2018/02-h5compression/ -o "$1".h5 -bkg /UserData/maddalena/sacla2018/02-h5compression/"$2".h5

echo ##########################
echo END OF THE SCRIPT
echo run "$1" saved as h5 file in /UserData/maddalenasacla2018/02-h5compression/"$1".h5
echo background run used is "$2"
echo ##########################