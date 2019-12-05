[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Generic badge](https://img.shields.io/badge/Version-.1-<COLOR>.svg)](https://shields.io/) [![Generic badge](https://img.shields.io/badge/PYTHON-3-<COLOR>.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/MAINTAINABILITY-ACTIVE-<COLOR>.svg)](https://shields.io/) [![Generic badge](https://img.shields.io/badge/Dependencies-Python-<COLOR>.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Contributions-WELCOMED-<COLOR>.svg)](https://shields.io/)





# Description

Retrieve database tables from a SQL dump file (e.g: dump.sql) and write each table into a csv file

# Install
```ps
git clone https://github.com/alguindi/sql_dump_to_csv.git
cd sql_dump_to_csv
```
# Usage
run:
```ps
> python ./sql_dump_to_csv.py ./example_dump.sql
```
output
```ps
Initializing
output directory: ./example_dump_csv_output
Wrote table: accounts to ./example_dump_csv_output/accounts.csv file
Wrote table: bank_add to ./example_dump_csv_output/bank_add.csv file
Wrote table: ci_sessions to ./example_dump_csv_output/ci_sessions.csv file                                                                                                                                

     Job Done, Chief!                                                                                

>                         
```