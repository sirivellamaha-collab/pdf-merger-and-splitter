
1. INTRODUCTION

PDF files are widely used for storing and sharing documents because they preserve the original formatting across different devices and operating systems. 
In many situations, users need to combine multiple PDF files into a single document or split a large PDF into smaller files. 
Performing these tasks manually can be difficult and time-consuming.

PDF Merger & Splitter Pro is a desktop application developed using Python 3.10.11. The application provides a simple graphical user interface that allows users to merge PDF files and split PDF documents efficiently. This project was developed as part of the internship program to gain practical experience in Python programming, graphical user interface development, and file handling.

2. OBJECTIVES

The objectives of this project are:

* To develop a desktop application using Python.
* To implement PDF merging functionality.
* To implement PDF splitting functionality.
* To create a user-friendly graphical interface.
* To improve knowledge of file handling techniques.
* To gain practical experience in software development and project management.

3. PROJECT SCOPE

The scope of this project is limited to basic PDF management operations. 
The application allows users to merge multiple PDF files into a single PDF document and split PDF files into individual pages. 
The project is intended for students, office users, and anyone who works regularly with PDF documents.

4. SYSTEM REQUIREMENTS

Hardware Requirements

* Processor: Intel Core i3 or higher
* RAM: 4 GB or above
* Storage: Minimum 100 MB free space

Software Requirements

* Windows 10 or Windows 11
* Python 3.10.11
* CustomTkinter Library
* pypdf Library
* Visual Studio Code (Optional)

5. TECHNOLOGIES USED

Python 3.10.11: Python was used as the main programming language for developing the application.

CustomTkinter: CustomTkinter was used to design the graphical user interface and improve the overall appearance of the application.

pypdf: The pypdf library was used to perform PDF operations such as merging and splitting PDF files.

GitHub: GitHub was used to store, manage, and maintain the project repository.

6. PROJECT STRUCTURE

he project is organized into separate folders to improve readability and maintenance.

PDF_Merger_Splitter_Pro

src
* main.py
* pdf_operations.py
* logger.py
* config.py

logs

outputs

screenshots

documentation

README.md

requirements.txt

.gitignore

7. WORKING OF THE PROJECT

1. The application starts with a graphical user interface where users can select PDF files.
2. The Add PDFs option allows users to choose one or more PDF files from their computer.
3. The Merge option combines the selected PDF files into a single PDF document and saves it to the chosen location.
4. The Split option divides a PDF file into separate pages and saves each page as an individual PDF file.
5. The application also maintains a log file to record operations performed by the user.

8. FEATURES

The main features of the application include:

* Merge multiple PDF files into a single PDF.
* Split PDF files into individual pages.
* User-friendly graphical interface.
* Operation logging.
* Error handling and validation.
* Output file generation.

9. TESTING

Several tests were performed to ensure that the application works correctly.

Test 1:
Merged multiple PDF files and verified that a single PDF file was generated successfully.

Test 2:
Split a PDF file and verified that separate PDF pages were created successfully.

Test 3:
Selected invalid files and verified that the application handled errors properly.

Test 4:
Attempted operations without selecting files and verified that warning messages were displayed.

Test 5:
Checked generated output files and verified that they were saved correctly.

10. RESULTS

The application was successfully developed and tested. All core functionalities worked as expected. 
The merge and split operations were performed successfully, and the generated output files were created correctly.

11. LEARNING OUTCOMES

During the development of this project, I gained practical experience in:

* Python Programming
* GUI Development
* PDF Processing
* File Handling
* Error Handling
* Software Documentation
* GitHub Repository Management

The project also helped me understand how to organize code into modules and maintain a structured software project.

12. FUTURE ENHANCEMENTS

The following improvements can be added in future versions:

* Password-protected PDF support
* PDF watermarking
* PDF page rotation
* Drag and drop functionality
* Improved user interface
* Additional PDF editing features

13. CONCLUSION

PDF Merger & Splitter Pro is a simple and useful desktop application developed using Python.
The project successfully demonstrates PDF merging and splitting operations through an easy-to-use graphical interface. 
Through this project, I gained valuable practical experience in Python programming, GUI development, file handling, and project documentation.
