import re, os, sys

## Regex patterns
table_info_ptn = re.compile(
    r'^INSERT INTO `(?P<table_name>.+)` \((?P<table_header>.+)\) VALUES'
    )

table_row_ptn = re.compile(
    r'\((?P<table_row>.+)\)[;,]'
    )

insertion_chunks_ptn = re.compile(
    r'INSERT INTO.+VALUES(\n\(.+)*\);$',
    re.MULTILINE
    )

## processing routines
def find_all_insert_chunks(sql_dump):
    ptn = insertion_chunks_ptn
    matches = re.finditer(ptn, sql_dump)
    return matches

def process_chunks(chunks):
    tables = {}
    for chunk in chunks:
        start, end = chunk.span()
        chunk_str = chunk.string[start:end]
        table_name, table_header, rows = process_chunk(chunk_str)
        if table_name in tables:
            # append to table content
            tables[table_name] += rows
        else:
            tables[table_name] = table_header + '\n' + rows
    return tables

def process_chunk(chunk):
    "a chunk is a string"
    chunk_lines = chunk.splitlines()
    table_name, table_header = extract_table_info(chunk_lines[0])
    rows = extract_rows(chunk_lines[1:])
    return table_name, table_header, rows

def extract_table_info(string):
    ptn = table_info_ptn
    match = re.search(ptn, string).groupdict()
    table_name = match['table_name']
    table_header = match['table_header'].replace('`', '')
    return table_name, table_header

def extract_rows(lines):
    rows = []
    ptn = table_row_ptn
    for l in lines:
        row = re.search(ptn, l).groupdict()['table_row']
        rows.append(row)
    return '\n'.join(rows)

def write_to_csv(table_name, table_content):
    file_name = table_name + '.csv'
    with open(file_name, 'w') as f:
        f.write(table_content)
        f.close()

def read_file(fn):
    with open(fn, 'r') as f:
        content = f.read()
        f.close()
    return content

##### Main function ########
def main():
    print('Initializing')
    file_name = sys.argv[1]
    file_text_str = read_file(file_name)
    chunks = find_all_insert_chunks(file_text_str)
    tables = process_chunks(chunks)
    directory_name = file_name.split('.')[-2]
    directory_path = f'./{directory_name}_csv_output'
    os.makedirs(directory_path, exist_ok=True)
    os.chdir(directory_path)
    print(f'output directory: {directory_path}')
    for table_name, table_content in tables.items():
        write_to_csv(table_name, table_content)
        print(f'Wrote table: {table_name} to {directory_path}/{table_name}.csv file')
    os.chdir('..')
    print('\n', 'Job Done, Chief!', '\n')

main()