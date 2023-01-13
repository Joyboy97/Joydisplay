from bs4 import BeautifulSoup

with open('cvexample.html','r') as html_file:
    content= html_file.read()
    #print(content) #print filr
    soup = BeautifulSoup(content,'lxml')
    #tags=soup.find('h5')#first h5 tag
    # job_tags=soup.find_all('h5')#first h5 tag
    job_tags=soup.find_all('div', class_='w3-container w3-card w3-white w3-margin-bottom')#first h5 tag
    for job in job_tags:
        print(job.h5.text)