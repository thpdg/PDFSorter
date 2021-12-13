# PDFSorter
Attempts to identify key concepts in a folder of PDF documents

For all PDF files in a folder
  Determine "frequent" word threshold based on number of pages
  Count each word in document, storing counts in a temporary array
  Display words as frequent if they occur more often than the threshold
  Display words if they appear in the important word list at top of code
  Ignore words if they appear in the common word list at top of code
  
Display report of all frequent and important words for all documents. Words that appear in the frequent list may need to be added to either important words or common words list.

TODO:
- Move word lists to external resource for easier maintenance
- Create file report that's easier to read (Been just piping for now)
- 
