# MzML2CSV Converter

## Introduction

The **MzML2CSV Converter** is a Python script that simplifies the process of converting Mass Spectrometry data files in the MzML format to Comma-Separated Values (CSV) format. This tool is designed to assist researchers and data scientists in extracting valuable information from MzML files, making it easier to analyze and manipulate Mass Spectrometry data for various applications.

## Features

- **Effortless Conversion**: Convert MzML files to CSV format with ease, reducing the complexity of data extraction.

- **Data Filtering**: Apply an intensity filter to specify the minimum intensity value required for data inclusion in the CSV output.

- **Data Retention**: Retain important scan information, including scan number, retention time, m/z values, and intensities.

- **Customizable**: Easily integrate the tool into your data processing pipelines and workflows.

## Prerequisites

Before using the MzML2CSV Converter, ensure that you have the following prerequisites installed on your computer:

- **Python**: Download and install Python from the official website: [Python Downloads](https://www.python.org/downloads/).

- **Required Python Libraries**: Install the necessary Python libraries using the following command:

  ```shell
  pip install pyteomics
  ```

## Getting Started

Follow these steps to convert your MzML files to CSV format:

### 1. Clone the Repository

Obtain the MzML2CSV Converter script by cloning the GitHub repository to your local machine. Use the following command to clone the repository:

```shell
git clone https://github.com/your-username/your-repository.git
```

Replace `your-username` and `your-repository` with your GitHub username and the name of your repository.

### 2. Organize Your Data

Place your MzML files that you want to convert into a dedicated folder on your local system. This folder will serve as the input folder for the conversion process.

### 3. Configure Input and Output Folders

Edit the `mzml.py` script to specify the paths for your input and output folders:

```python
# Specify the input folder containing mzML files and the output folder for CSV files
input_folder = 'input_mzML'  # Replace with the actual folder path containing mzML files
output_folder = 'output_csv'  # Replace with the desired folder path for CSV files
```

Replace `'input_mzML'` with the actual path to your input folder containing MzML files, and `'output_csv'` with the desired path for the output CSV files.

### 4. Set the Intensity Filter (Optional)

Optionally, you can set an intensity filter to control which data points are included in the CSV output. Modify the `intensity_threshold` variable in the script to specify the minimum intensity value required for data inclusion.

```python
# Intensity filter threshold
intensity_threshold = 1000  # Adjust this value as needed
```

### 5. Run the Script

Open your command prompt or terminal, navigate to the folder where the `mzml.py` script is located, and run the script:

```shell
python mzml.py
```

The script will process the MzML files in the input folder, apply the intensity filter (if specified), convert them to CSV format, and save the CSV files in the specified output folder.

### 6. Review the Output

The script will provide progress updates as it processes each file. Once the conversion is complete, you will see a message indicating that the data has been saved to the output folder.

## Conclusion

The MzML2CSV Converter simplifies the conversion of Mass Spectrometry data from MzML to CSV format, making it easier for you to work with the data in various data analysis and research applications. If you encounter any issues or have questions, feel free to reach out to the project's author or the GitHub community for assistance.

We hope you find this tool helpful for your Mass Spectrometry data analysis projects!
