#!/bin/bash

design="cpu.v"
output=${design%.*}
testbed="${output}_tb.v"

if [[ $1 == "clean" ]]; then 
  rm $output;
fi

iverilog -o $output $testbed $design 
vvp $output
