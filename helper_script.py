import csv
import settings


def get_edited_lines(file_path):
    lines = list()
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        head = next(reader)
        lines.append(head)
        for row in reader:
            for idx, field in enumerate(row):
                if (field == 'Â\xa0') or (field == '-') or (field == '0'):
                    row[idx] = ''
            lines.append(row)
    return lines


def write_edited_lines(file_path, edited_lines):
    with open(file_path, "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        for line in edited_lines:
            writer.writerow(line)


csv_file_path = settings.csv_main_file_path
columns_lst = settings.required_columns
lines = get_edited_lines(csv_file_path)
write_edited_lines(csv_file_path, lines)
