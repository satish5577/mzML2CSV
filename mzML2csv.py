import csv
import os
from pyteomics import mzml

# Specify the input folder containing mzML files and the output folder for CSV files
input_folder = 'input_mzML'  # Replace with the actual folder path containing mzML files
output_folder = 'output_csv'  # Replace with the desired folder path for CSV files

# Intensity filter threshold
intensity_threshold = 1000

# Ensure the output folder exists, or create it if it doesn't
os.makedirs(output_folder, exist_ok=True)

# Iterate through files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.mzML'):
        input_mzml_file = os.path.join(input_folder, filename)
        output_csv_file = os.path.join(output_folder, f'{os.path.splitext(filename)[0]}.csv')

        # Open the mzML file for reading
        with mzml.read(input_mzml_file) as mzml_file:
            # Create a CSV file for writing
            with open(output_csv_file, mode='w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                
                # Write the header row
                csv_writer.writerow(['ScanNumber', 'RetentionTime', 'm/z', 'Intensity'])

                # Iterate through spectra in the mzML file
                for spectrum in mzml_file:
                    scan_number = spectrum['id']
                    retention_time = spectrum['scanList']['scan'][0]['scan start time']
                    mzs = spectrum['m/z array']
                    intensities = spectrum['intensity array']

                    # Filter data based on intensity threshold
                    filtered_data = [(mz, intensity) for mz, intensity in zip(mzs, intensities) if intensity >= intensity_threshold]

                    # Write the filtered data to the CSV file
                    for mz, intensity in filtered_data:
                        csv_writer.writerow([scan_number, retention_time, mz, intensity])

        print(f"Conversion completed for {filename}. Data saved to {output_csv_file}")
