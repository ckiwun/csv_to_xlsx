#!/usr/bin/env python3

import csv
import xlsxwriter
import os
import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', '--inputs', dest='inputs', default=None, type=str,
                      help='Input filenames, separate with comma(,)')
  parser.add_argument('-o', '--output', dest='output', default='foo', type=str,
                      help='Output filename prefix, will be postfixed with .xlsx')
  parser.add_argument('-d', '--delimiter', dest='delimiter', default=',', type=str,
                      help='Delimiter used in csv file')
  args = parser.parse_args()

  if args.inputs is None:
    print('please specify input csv files')
    parser.print_help()

  csv_files = list(i for i in args.inputs.split(','))

  output_dir = os.path.dirname(args.output)
  output_filename = os.path.basename(args.output)

  if not os.path.exists(output_dir):
    os.makedirs(output_dir)

  workbook = xlsxwriter.Workbook(os.path.join(output_dir, '{}.xlsx'.format(output_filename)))

  for filename in csv_files:
    with open(filename, newline='') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=args.delimiter, quotechar='|')

      worksheet = workbook.add_worksheet()

      for i, row in enumerate(csv_reader):
        for j, col in enumerate(row):
          worksheet.write(i, j, col)

  workbook.close()

if __name__ == '__main__':
  main()
