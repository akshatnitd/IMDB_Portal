import requests
import os
import sys
import json
import bs4

if(sys.version[0] == '3'):
    raw_input = input

os.system('clear')


status=open('info.txt','a')



def info_movie():
    name = raw_input('\nEnter the title of the movie: ')
    t = name.replace(' ','%20')
    url = 'https://api.themoviedb.org/3/search/movie?api_key=ffb07b773769d55c36ccd83845385205&language=en-US&query='+str(t)+'&page=1&include_adult=false'
    response = requests.get(url)
    u = json.loads(response.text)
    results  = u['results']
    id = results[0]['id']
    url2 = 'https://api.themoviedb.org/3/movie/'+str(id)+'?api_key=ffb07b773769d55c36ccd83845385205&language=en-US'
    response = requests.get(url2)
    w = json.loads(response.text)
    try:
        title = w['title']
        imdb_id = w['imdb_id']
        year = w['release_date']
        genre = w['genres']
        language = w['spoken_languages']
        duration = w['runtime']
        plot = w['overview']

        url3 = 'http://www.imdb.com/title/'+str(imdb_id)
        response = requests.get(url3)
        html = response.text
        soup = bs4.BeautifulSoup(html,"lxml")
        data = soup.select('.ratingValue')
        rating = data[0].get_text('',strip=True)

        print ("\n\n----------------------------MOVIE INFORMATION-------------------------\n")
        print ("\n\t TITLE       : \t\t"+title)
        print ("\n\t IMDB RATING : \t\t"+rating)
        print ("\n\t RELEASED ON : \t\t"+year)
        print ("\n\t DURATION    : \t\t"+str(duration)+" mins")
        # print ("\n\t LANGUAGE    : \t\t"+language[0]['name'])
        print ("\n\t GENRE       : \t\t"+genre[0]['name'])
        print ("\n\t PLOT        : \t\t"+plot)

        status.write ("\n\n--------------------------------------MOVIE INFORMATION---------------------------------\n")
        status.write ("\n\t TITLE       : \t\t"+title)
        status.write ("\n\t IMDB RATING : \t\t"+rating)
        status.write ("\n\t RELEASED ON : \t\t"+year)
        status.write ("\n\t DURATION    : \t\t"+str(duration)+" mins")
        # status.write ("\n\t LANGUAGE    : \t\t"+language[0]['name'])
        status.write ("\n\t GENRE       : \t\t"+genre[0]['name'])
        status.write ("\n\t PLOT        : \t\t"+plot)

    except KeyError:
        print ("\nNo such movie titled '"+name+"' found!\n")
        status.write ("\nNo such movie titled '"+name+"' found!\n")
    
    
def top_movies():
    x = int(raw_input("\nEnter n, to display Top 'n' movies: " ))
    url = 'http://www.imdb.com/chart/top'
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html,"lxml")
    rows = soup.select('.lister-list tr')
    print ("\n"+"----------------------------------TOP "+str(x)+" MOVIES ACCORDING TO IMDB RATINGS---------------------------------"+"\n\n")
    print (" \t   TITLE\t\t\t\t\t\t\t\t\t\t   IMDB RATING\n\n")
    status.write ("\n"+"---------------------------TOP "+str(x)+" MOVIES ACCORDING TO IMDB RATINGS-----------------------------"+"\n\n")
    status.write (" \t   TITLE\t\t\t\t\t\t\t\t\t\t   IMDB RATING\n\n")
    
    for row in range(0,x):
        tdata=rows[row].select('td')
        name=tdata[1].get_text(' ',strip=True)
        rating=tdata[2].get_text(' ',strip=True)
        ans=("\n "+name.ljust(75,' ')+"\t\t\t\t"+rating+"\n")
        status.write (ans)
        if(sys.version[0] != '3'):
            ans=ans.encode('ascii','ignore')
        print (ans)
        
        
def folder():
    path = raw_input("\n\nEnter the complete path of the directory where your movies are present: ")
    dirs = os.listdir(path)
    print ("Showing results for the path: "+path+"\n")
    status.write ('Showing results for the path: '+path+'\n')
    
    for i in range(len(dirs)):
        x = dirs[i]
        if(x == '.DS_Store'):
            continue
        t = x.replace(' ','%20')
        url = 'https://api.themoviedb.org/3/search/movie?api_key=ffb07b773769d55c36ccd83845385205&language=en-US&query='+str(t)+'&page=1&include_adult=false'
        response = requests.get(url)
        u = json.loads(response.text)
        results  = u['results']
        id = results[0]['id']
        url2 = 'https://api.themoviedb.org/3/movie/'+str(id)+'?api_key=ffb07b773769d55c36ccd83845385205&language=en-US'
        response = requests.get(url2)
        w = json.loads(response.text)

        try:
            title = w['title']
            year = w['release_date']
            imdb_id = w['imdb_id']

            url3 = 'http://www.imdb.com/title/'+str(imdb_id)
            response = requests.get(url3)
            html = response.text
            soup = bs4.BeautifulSoup(html,"lxml")
            data = soup.select('.ratingValue strong span')
            rating = data[0].get_text('',strip=True)

            if(sys.version[0] != '3'):
                x = x.encode('ascii','ignore')
            y = "["+rating+"] "+title+" ("+year+")"
            if(sys.version[0] != '3'):
                y = y.encode('ascii','ignore')
            print ("\n"+y)
            status.write ("\n"+y)
            os.rename(os.path.join(path, x), os.path.join(path, y))			
            print ("Renaming Done\n")
            status.write ('Renaming Done\n')
        except KeyError:
            print ("\nNo such movie titled '"+x+"' found or else read the instructions before using this feature!\n")
            status.write ("\nNo such movie titled '"+x+"' found else read the instructions before using this feature!\n")


def driver():
    print ("\n\n\t\t\t\t\t----------------IMDB PORTAL--------------------")
    status.write("\\\n\n\t\t\t\t\t---------------------IMDB PORTAL----------------------")
    choice = int(raw_input('Enter your choice:\n\n1) Search movie information by title\n2) Show top rated movies\n3) Rename folder with IMDB rating and year of release added to it\n\nInput: '))
    
    if(choice == 1):
        info_movie()
    elif(choice == 2):
        top_movies()
    else:
            folder()
            
        
driver()
while (1>0) :
    repeat = raw_input("\n\nDo you want to try again?(type 'Yes'/'Y'/'y' or else press anything) ")
    if (repeat == 'Yes') or (repeat == 'Y') or (repeat == 'y'):
        os.system('clear')
        driver()
    else:
        print ("\nThank you for using!")
        status.write("\nThank you for using!")
        break

status.close()