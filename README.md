# read_n42

This repository contains the file necessary to convert N42 NIST files to a friendlier format, CSV. More specifically, the .py file was developed to facilitate the data analysis of gamma-ray spectrometry spectra obtained with an H3D M400 CZT detector. 

The generated N42 contains a large amount of data (calibration equation, measurement time, detected radionuclides, spectra, etc.) but our focus is solely on the spectra. Each file contains 3 spectra, namely: PUR, INDIV, and SINGLE. Since I'm not quite sure on what is the difference between those three, the conversion file gets these three spectra and adds each one of them to a column of the CSV file.

To use the conversion tool, one must have Python 3 installed. Alongside Python, the libraries "os", "pandas", "numpy" and "BeatifulSoup" are necessary. The file works by accessing all the N42 files inside a folder and converting it to a CSV with the same name. The repository also contains a test file (the spectrum of measuring a Cs-137 and a Co-60 source for 10 minutes) both in N42 and CSV.

For more info, contact: lopes.joaomarcos@uel.br
