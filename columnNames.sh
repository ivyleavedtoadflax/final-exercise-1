#!\bin\bash

python print_col_names.py > columnNames
python print_col_names.py | sort > sortedColumnNames
