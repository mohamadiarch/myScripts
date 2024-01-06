import argparse
import re
import os

file_path = os.path.realpath(__file__)
folder_path = os.path.dirname(file_path)



parser=argparse.ArgumentParser(
        prog="srt_to_txt",
        description="convert srt to txt in command line with python"
)
parser.add_argument("path", help="Enter the path")
args=parser.parse_args()
fileName=args.path
fileSrt=open(fileName,"r")


# file=open("./GeekForGeeks/file/friends.srt")
fileTxt=open("./new.txt","w")
lines=fileSrt.readlines()
for  line in lines:
    number=re.match("^[0-9]*$",line)
    time=re.match("^[0-9]{2,3}:[0-9]{2}:[0-9]{2}",line)
    if number or time: 
        continue
    else:
        fileTxt.write(line)

print("convert successfull")