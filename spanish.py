import os 
import shutil
import requests 
import subprocess
from bs4 import BeautifulSoup


base_url = "https://es.enduringword.com/comentario-biblico/"

books_es = {
    "genesis": 50,
    "exodo": 40,
    "levitico": 27,
    "numeros": 36,
    "deuteronomio": 34,
    "josue": 24,
    "jueces": 21,
    "rut": 4,
    "1-de-samuel": 31,
    "2-de-samuel": 24,
    "1-de-reyes": 22,
    "2-de-reyes": 25,
    "1-cronicas": 29,
    "2-cronicas": 36,
    "esdras": 10,
    "nehemias": 13,
    "ester": 10,
    "job": 42,
    "salmo": 150,
    "proverbios": 31,
    "eclesiastes": 12,
    "cantar de los cantares": 8,
    "isaias": 66,
    "jeremias": 52,
    "lamentaciones": 5,
    "ezequiel": 48,
    "daniel": 12,
    "oseas": 14,
    "joel": 3,
    "amos": 9,
    "abdias": 1,
    "jonas": 4,
    "miqueas": 7,
    "nahum": 3,
    "habacuc": 3,
    "sofonias": 3,
    "hageo": 2,
    "zacarias": 14,
    "malaquias": 4,
    "mateo": 28,
    "marcos": 16,
    "lucas": 24,
    "juan": 21,
    "hechos": 28,
    "romanos": 16,
    "1-corintios": 16,
    "2-corintios": 13,
    "galatas": 6,
    "efesios": 6,
    "filipenses": 4,
    "colosenses": 4,
    "1-tesalonicenses": 5,
    "2-tesalonicenses": 3,
    "1-timoteo": 6,
    "2-timoteo": 4,
    "tito": 3,
    "filemon": 1,
    "hebreos": 13,
    "santiago": 5,
    "1-pedro": 5,
    "2-pedro": 3,
    "1-juan": 5,
    "2-juan": 1,
    "3-juan": 1,
    "judas": 1,
    "apocalipsis": 22
}

def does_page_exists (url):
    r = requests.get(url)
    
    if r.status_code == 200:
        if "Nothing Found" in r.text:
            return False
        else: 
            return True
    else:
        print(f"ERROR: Connection to {url} failed with status code {r.status_code}")
        return False

def determine_numeration_style (book):
    url = base_url + book + "-01"
    if does_page_exists (url):
        return "leading_zero"
    else:
        return "no_leading_zero"

def html_from_url (url, path): 
    r = requests.get(url)
    with open (path, "w", encoding="utf-8") as file:
        file.write (r.text)

def verify_integrity (path):
    pending_books = {}
    for book, chapter_limit in books_es.items(): 

        if book not in os.listdir (path):
            os.mkdir(path+os.sep+book)

        if len (os.listdir(path+os.sep+book)) < chapter_limit:
            #print (f"INTEGRITY: {book}  ({chapter_limit}) != {len (os.listdir(path+os.sep+book))}")
            pending_books[book] = chapter_limit

    return pending_books

if os.path.exists("html"):
    response = input("There is already a download started, do you want to continue it? (Y/n): ").strip().lower()
    
    if response == 'y' or response == 'yes':
        books_es = verify_integrity ("html")
        for book in books_es: 
            try:
                shutil.rmtree('html'+os.sep+book)
            except: 
                print (f"WARNING: '{book}' was not found in the html directory.  ")
    elif response == 'n' or response == 'no':
        print("Download canceled.")
    else:
        print("Invalid response. Please enter 'Y' or 'n'.")
else:
    print("No download in progress. Starting a new download...")
    if os.path.exists("html"):
        shutil.rmtree('html')
    os.mkdir("html")

counter_of_downloaded_books = 1

for book, chapter_limit in books_es.items(): 
    os.mkdir("html"+os.sep+book)

    url = base_url + book 
    numeration_style = determine_numeration_style (book)  

    print (f"Downloading {book} ({counter_of_downloaded_books}/{len(books_es)}):") 
    counter_of_downloaded_books+=1

    for chapter in range (1,chapter_limit+1):

        print (f"\t-chapter ({chapter}/{chapter_limit})") 
        
        if numeration_style == "leading_zero" and chapter < 10: 
            str_chapter= "-0" + str(chapter)
        else:
            str_chapter = "-"+str(chapter)

        url = base_url + book + str_chapter

        if (does_page_exists(url)):
            while True:
                try:
                    html_from_url (url, "html"+os.sep+book+os.sep+str(chapter)+".html")
                    break
                except:
                    pass

if (not os.path.exists("html"+os.sep+"galatas"+os.sep+"6"+".html")):

    print ("Downloading exceptions")
    while True:
        try:
            #html_from_url ("https://es.enduringword.com/comentario-biblico/josue-15-16-17/", "html"+os.sep+"josue"+os.sep+"15-16-17"+".html")
            #html_from_url ("https://es.enduringword.com/comentario-biblico/josue-18-19/", "html"+os.sep+"josue"+os.sep+"18-19"+".html")
            #html_from_url ("https://es.enduringword.com/comentario-biblico/1-cronicas-4-8/", "html"+os.sep+"1-cronicas"+os.sep+"4-8"+".html")
            html_from_url ("https://es.enduringword.com/comentario-biblico/galatans-6/", "html"+os.sep+"galatas"+os.sep+"6"+".html")
            break
        except:
            pass

print ("Download complete") 

output_doc = BeautifulSoup ()
output_doc.append(output_doc.new_tag("html"))
output_doc.html.append(output_doc.new_tag("body"))

for book, chapter_limit in books_es.items(): 
    
    for chapter in range (1,chapter_limit+1):
        print (f"Converting all files into HTML, book: {book}, chapter: {chapter}")
        path = "html"+os.sep+book+os.sep+str(chapter)+".html"
        try: 
            with open(path, 'r', encoding='utf-8') as html_file:
                output_doc.body.extend(BeautifulSoup(html_file.read(), "html.parser").body)
        except: 
            print (f"WARNING: {book}, chapter: {chapter} not found")


with open("output.html", 'w', encoding='utf-8') as output_file:
    output_file.write(output_doc.prettify())
