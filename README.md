# ICP_Extractor
ICP Data_extractor

This is the stable version of the ICP Data Extractor. This application filters and processes data creating different types of reports based on CSV files exported from the ICP Machine.

# How to use

  1. Open the CSV file

  2. Check the Setup options you want 
    
    - noblk= remove the blank samples, nostd= remove the standard samples
    - nohno3= remove samples that have HNO in their label name
    - Selec. All Samples = Start the loading screen with all samples selected
    - Selec. All Samples = Start the loading screen with all elements selected

  3. Load the data

  4. Select the samples and the elements that you want in the final report

  5. Select the type of report and create the report ("Report" contains concentration column for each sample/element,"Full Report" include all columns, "Calc. Report" calculate the average and standard deviation of the samples by NIR)
  
  6. Check if the list of replicate names is working properly by clicking in preview. You should see the NIR numbers. If not, add the missing suffix in the list and click "Preview" again.
  
  7. After finish the setup just click in "Create report"

  The final document will be created in the same folder as the running program
  
