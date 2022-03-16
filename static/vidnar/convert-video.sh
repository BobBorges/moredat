#!/bin/bash

# Use this script in case you want to batch convert videos in the `vid` dir to mp4.
# The script requires ffmpeg to be installed and on on the $PATH 


#set this $ext variable to the format of the videos you want to convert.
ext='.mpg'

for f in vid/*$ext ; do
    fbase=${f%.*}
    echo $f;
    echo $fbase

    ffmpeg -i $f -c:v libx264 -c:a aac -crf 20 -preset:v veryslow $fbase.mp4

done
