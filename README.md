# AWS WorkSpaces Images and Bundles Info Generator

This script generates an Excel workbook containing information about AWS WorkSpaces images and bundles. The workbook consists of three sheets: "Images", "Bundles", and "Bundles_With_Images".

## Features

- The "Images" sheet lists the details of all available WorkSpaces images, including image ID, name, description, and creation time.
- The "Bundles" sheet lists the details of all available WorkSpaces bundles, including bundle ID, name, description, image ID, compute type, and creation time.
- The "Bundles_With_Images" sheet provides a merged view of the bundles and their associated images.
- The script accepts command-line arguments for the AWS profile, region, and output filename, with default values provided.
- Columns in the Excel workbook are auto-sized for better readability.

## Usage

To use the script, run the following command:

python3 excel-gather-image-bundle-data.py [--profile AWS_PROFILE] [--region AWS_REGION] [--output OUTPUT_FILENAME]

### Command-line Arguments

- `--profile AWS_PROFILE`: Specify the AWS profile to use. Default: `"massdot-workspace-admins-603512801773"`.
- `--region AWS_REGION`: Specify the AWS region to use. Default: `"us-east-1"`.
- `--output OUTPUT_FILENAME`: Specify the output Excel file name. Default: `"{current_date}-workspaces_info.xlsx"`, where `{current_date}` is the current date in the format YYYYMMDD.

## Requirements

- Python 3
- boto3
- pandas
- openpyxl
- argparse

Please ensure that the AWS CLI is configured with the necessary credentials and region settings before running the script.

## License

[MIT License](LICENSE)

