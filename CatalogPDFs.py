from PyPDF2 import PdfFileReader
from pathlib import Path
import os

counts = dict()
total_counts = dict()

common_words = ['//','.','level','1','2','3','4','over','text','key''b','their','hill','was','she','he','function','[',']','*','+','just','string','following','new','return','properties','also','from','than','image','tile','code','method','using','only','other','array','typeof','returns','chapter','the','=','but','with','are','for','our','not','by','use','have','be','of','or','if','which','your','value','some','do','has','we','about','we','when','look','see','one','all','much','very','used','var','so','into','these','to','a','is','and','in','that','you','this','it','as','will','can','{','}','how','more','i','on','at','an']
important_words = ['apple','usb','cable','pi','javascript','java','css','mongodb','python','database','trek','arduino','raspberry','angularjs','dom','html','lego','oriented','marketing','zoning''meeting','franchise','mdm','python','pygame','vision','learning','ct','simsbury','canton','farmington','hartford','probability','electrical','electronics','pdf','php','perl','stack','circuit','starship','torpedo','enterprise','starfleet','playmates','borg','alpha','voyager','defiant','picard','riker','worchester','kmart','sears','avenue','mall']

def word_count(str):
    words = str.split()
    for word in words:
        if word.lower() in counts:
            counts[word.lower()] += 1
            total_counts[word.lower()] += 1
        else:
            counts[word.lower()] = 1
            total_counts[word.lower()] = 1

    return counts

def process_pdf(str):
    
    print("\n\n Working on " + str)
    try:
        pdf = PdfFileReader(str)
    except:
        print("Unable to open file " + str)
        return

    try:
        print("Pages: {}".format(pdf.getNumPages()))
    except:
        print("Unable to get page count from " + str)
        return

    if pdf.getNumPages() > 20:
        word_threshold = 50
    else:
        word_threshold = 5

    for page in pdf.pages:
        try:
            word_count(page.extractText())
        except:
            print("Unable to extract text from " + str)
            return

    print("=========================================")
    print("===== Frequent Words ====================")
    print("=========================================")
    sort_orders = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    for i in sort_orders:
        if i[1] > word_threshold:
            if i[0].lower() not in common_words:
                try:
                    if i[0].lower() in important_words:
                        print("* ", end='')
                    print(i[0], i[1])
                except:
                    print("Unprintable word!")

    print("=========================================")
    print("===== Important Words ===================")
    print("=========================================")
    for i in sort_orders:    
            if i[0].lower() in important_words:
                print(i[0], i[1])

    # print(len(counts))

# Main() - In the currect directory, open each file that has a .pdf extension and count the words in it
for file in os.listdir("."):
    if file.endswith(".pdf"):
        process_pdf(file)
        counts = dict()

# After processing all files in folder, report what the frequent words were to consider adding to word lists above
print("=========================================")
print("===== Total Frequent Words ==============")
print("=========================================")
sort_orders = sorted(total_counts.items(), key=lambda x: x[1], reverse=True)
for i in sort_orders:
    if i[1] > 10:
        if i[0].lower() not in common_words:
            try:
                if i[0].lower() in important_words:
                    print("* ", end='')    
                print(i[0], i[1])
            except:
                print("Unprintable word!")