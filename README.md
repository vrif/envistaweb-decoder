# Envistaweb Decoder

This decoder is for converting Excel/CSV files that are downloaded from the [BC Air Data Archive](https://envistaweb.env.gov.bc.ca/DynamicTable2.aspx?G_ID=331) to a Pandas DataFrame.

1. First click on the desired monitoring station. eg. 'Vancouver International Airport #2'.
2. Click 'Station Report'.
3. A yellow box will appear, and choose 'Period'.
4. Please tick the desired variables, and your ''Start' and 'End Date Range.
5. Change the 'End Time' to 11:00PM. 
6. Keep 'Time Base' as 1 Hour.
7. Press 'Create Report' to generate the report and check that your desired date range has been generated. Note: The system can only generate reports in one year intervals.

For processing Excel file Export:

8. At the top, choose 'Excel' from the drop down menu and then click 'Export'.
9. Now open 'FileName.xls' file that you have just downloaded from the website. You should encounter an error on Excel saying: 'The file format and extension of 'FileName.xls' don't match. The file could be corrupted or unsafe. Unless you trust its source, don't open it. Do you want to open it anyway?'
10. Click 'Yes', then resave this file as a .xls. For some odd reason, the report generates the files as a .tsv wrapped in a .xls.
11. Then use `load_AQ_data_excel()` to load the data into a Pandas DataFrame.

For processing CSV file Export:

8. At the top, choose 'CSV' from the drop down menu and then click 'Export'.
9. Then use `load_AQ_data_csv()` to load the data into a Pandas DataFrame.
