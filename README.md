# read_n42

This repository contains the file necessary to convert N42 NIST files to friendlier format, CSV. More specifically, the .py file was develop with the goal to facilitate the data analysis of gamma-rays spectrometry spectra obtained with a H3D M400 CZT detector. 

The generated N42 contain a large amount of data (calibration equation, measurement time, detected radionuclides, spectra, etc.) but our focus is solely in the spectra. Each file contains 3 spectra, namely: PUR, INDIV and SINGLE. Since I'm not quite sure on what is the difference between those three, the convertion file gets these three spectra and adds each one of them to a column of the CSV file.

In order to use the convertion tool, one must have Python 3 installed. Alongside Python, the libraries "os", "pandas", "numpy" and "BeatifulSoup" are necessary. The file works by acessing all the N42 files inside a folder and converting it to a CSV with the same name.

For more info, contact: lopes.joaomarcos@uel.br
