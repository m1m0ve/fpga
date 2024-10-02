#!/bin/bash

design="risk.v"
output=${design%.*}
testbed="${output}_testbench.v"

if [[ $1 == "clean" ]]; then 
  rm $output;
 fi

iverilog -o $output $testbed $design 
vvp $output
