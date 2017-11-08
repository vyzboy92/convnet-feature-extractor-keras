#!/bin/bash
# Get width and height of base image
w=512;
h=512;

# Generate infinite (well, 10) patches
for k in *.png; do
  for ((i=0;i<10;i++)) ; do
    ((x=RANDOM % (w-1) ))
    ((y=RANDOM % (h-1) ))
    convert "$k" -crop 20x20+${x}+${y} cropped-${k}-${i}.jpg;
  done
done
