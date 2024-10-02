file="risk"

if [[ $1 == "clean" ]]; then 
  rm ./$file.bit
  rm ./$file.fasm
  rm ./$file.json
  rm ./$file.frames
  exit 0
fi

make
openFPGALoader --board arty --bitstream cpu.bit
