import argparse
import pandas as pd
import datetime
import boto3
from openpyxl.utils import get_column_letter
import logging

# Function to auto-size columns in an Excel worksheet
def autosize_columns(worksheet):
    for col in worksheet.columns:
        max_length = 0
        column = col[0].column_letter
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = max_length + 2
        worksheet.column_dimensions[column].width = adjusted_width

# Define command-line arguments using argparse
parser = argparse.ArgumentParser(description='Generate WorkSpaces info in Excel file.')
parser.add_argument('--profile', default='default', help='AWS profile to use (default: default).')
parser.add_argument('--region', default='us-east-1', help='AWS region to use (default: us-east-1).')
parser.add_argument('--output', default='workspaces_info.xlsx', help='Output Excel file (default: workspaces_info.xlsx).')
parser.add_argument('--log', '-l', action='store_true', help='Enable logging to a file.')
parser.add_argument('--debug', '-d', action='store_true', help='Enable debug-level logging.')

# Parse command-line arguments
args = parser.parse_args()

# Set up logging
if args.log:
    log_filename = datetime.datetime.now().strftime('%Y%m%d') + '-' + args.output.split('.')[0] + '.log'
    log_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(filename=log_filename, level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info('Script started.')

# Set the AWS profile and region from command-line arguments
aws_profile = args.profile
aws_region = args.region

# Set the date format for file naming and format the output Excel file name
current_date = datetime.datetime.now().strftime('%Y%m%d')
excel_file = current_date + '-' + args.output

# Create an AWS session with the specified profile and region
session = boto3.Session(profile_name=aws_profile, region_name=aws_region)

# Create an AWS WorkSpaces client
workspaces_client = session.client('workspaces')

# List all Amazon WorkSpaces images and convert to DataFrame
response_images = workspaces_client.describe_workspace_images()
df_images = pd.DataFrame(response_images['Images'])
df_images = df_images[['ImageId', 'Name', 'Description', 'Created']]
df_images['Created'] = df_images['Created'].apply(lambda x: x.replace(tzinfo=None))

# List all Amazon WorkSpaces bundles and convert to DataFrame
response_bundles = workspaces_client.describe_workspace_bundles()
df_bundles = pd.DataFrame(response_bundles['Bundles'])
df_bundles = df_bundles[['BundleId', 'Name', 'Description', 'ImageId', 'ComputeType', 'CreationTime']]
df_bundles['CreationTime'] = df_bundles['CreationTime'].apply(lambda x: x.replace(tzinfo=None))
df_bundles['ComputeType'] = df_bundles['ComputeType'].apply(lambda x: x['Name'])

# Merge the images and bundles DataFrames based on the ImageId
df_merged = pd.merge(df_bundles, df_images, left_on='ImageId', right_on='ImageId', suffixes=('_Bundle', '_Image'))

# Create an Excel writer
writer = pd.ExcelWriter(excel_file, engine='openpyxl')

# Write each DataFrame to a separate sheet in the Excel file
df_images.to_excel(writer, sheet_name='Images', index=False)
df_bundles.to_excel(writer, sheet_name='Bundles', index=False)
df_merged.to_excel(writer, sheet_name='Bundles_With_Images', index=False)

# Auto-size columns for each sheet
for sheet_name in writer.sheets:
    worksheet = writer.sheets[sheet_name]
    autosize_columns(worksheet)

# Save the Excel file using the save method of the Workbook object
writer.book.save(excel_file)

# Log the completion of the script
if args.log:
    logging.info(f'The Excel file "{excel_file}" has been created with three sheets: Images, Bundles, and Bundles_With_Images.')
    logging.info('Script completed.')

print(f'The Excel file "{excel_file}" has been created with three sheets: Images, Bundles, and Bundles_With_Images.')

