#!/bin/zsh
for test_file_buenos in ./codes/buenos/*.txt
do
  echo ------------------"Leyendo $test_file_buenos------------------"
  python main.py $test_file_buenos && python3 temp.py
done

# for test_file_malos in ./codes/malos/*.txt
# do
#   echo ------------------"Leyendo $test_file_malos------------------"
#   python3 main.py $test_file_malos && python3 temp.py
# done