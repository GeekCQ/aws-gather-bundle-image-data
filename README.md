# AWS WorkSpaces Images and Bundles Info Generator

This script generates an Excel workbook containing information about AWS WorkSpaces images and bundles. The workbook consists of three sheets: "Images", "Bundles", and "Bundles_With_Images". The "Images" sheet lists the details of all available WorkSpaces images, including image ID, name, description, and creation time. The "Bundles" sheet lists the details of all available WorkSpaces bundles, including bundle ID, name, description, image ID, compute type, and creation time. The "Bundles_With_Images" sheet provides a merged view of the bundles and their associated images.

The script can accept command-line arguments for the AWS profile, region, output filename, logging, and debugging. If not provided, the script uses default values for these parameters.

## Usage

python3 excel-gather-image-bundle-data.py --profile <AWS_PROFILE> [--region AWS_REGION] [--output OUTPUT_FILENAME] [--log] [--debug]

### Command-line Arguments

- `--profile AWS_PROFILE`: Specify the AWS profile to use. Default: "default"
- `--region AWS_REGION`: Specify the AWS region to use. Default: "us-east-1".
- `--output OUTPUT_FILENAME`: Specify the output Excel file name. The script will prepend the current date to the file name. Default: "workspaces_info.xlsx".
- `--log` or `-l`: Enable logging to a file. The log file will be named similarly to the output file, with a ".log" extension.
- `--debug` or `-d`: Enable debug-level logging. Requires the `--log` option to be enabled.

## Requirements

- Python 3
- boto3
- pandas
- openpyxl
- argparse

Please ensure that the AWS CLI is configured with the necessary credentials and region settings before running the script.

## License

[MIT License](LICENSE)

