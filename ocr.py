# Import libraries 
from PIL import Image 
import pytesseract 
import sys 
import os 
  
''' 
Part #2 - Recognizing text from the images using OCR 
'''

def OCR(filename):  
    # Creating a text file to write the output 
    outfile = os.path.splitext(filename,[0])
  
    # Open the file in write mode so that  
    # previous texts in file will be erased 
    f = open(outfile, "w") 
  
    image = Image.open(filename)
    text =''
    for frame in range (image.n_frames):
	    image.seek(frame)
          
    	# Recognize the text as string in image using pytesserct 
	    try:
		    text += str(((pytesseract.image_to_string(image,lang="Malayalam"))))
	    except RuntimeError as timeout_error:
    		print("terminated")	
    		# Tesseract processing is terminated
    		pass 
  
    # The recognized text is stored in variable text 
    # Any string processing may be applied on text 
    # Here, basic formatting has been done: 
    # In many PDFs, at line ending, if a word can't 
    # be written fully, a 'hyphen' is added. 
    # The rest of the word is written in the next line 
    # Eg: This is a sample text this word here Mala- 
    # yalam is half on first line, remaining on next. 
    # To remove this, we replace every '-\n' to ''. 
    text = text.replace('-\n', '')     
  
    # Finally, write the processed text to the file. 
    f.write(text) 
  
    # Close the file after writing all the text. 
    f.close() 

