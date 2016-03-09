from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
import re

def add_fighter(request):
    array = ""
    for i in xrange(1,60):
        file = open('C:/Users/Paulo/Documents/Python/mmastats/mmastats/files/'+str(i)+'.html', 'rb')
        lines = file.readlines()

        for i in range(0, len(lines)):
            line = lines[i]

            # name and nickname
            str_match = r'<h1 itemprop="name"><span class="fn">'
            match_begining = re.search(str_match, line)
            if match_begining != None:
                begining = match_begining.start()+len(str_match)-1
                match_end = re.search(r'</span>', line)
                name = line[begining:match_end.start()]
                name_array = []
                name_array = name.split(' ')

                print name

                # nickname
                str_match = r'<span class="nickname">"<em>'
                match_begining = re.search(str_match, line)
                if match_begining != None:
                    begining = match_begining.start()+len(str_match)-1
                    match_end = re.search(r'</em>"</span>', line)
                    nick_name = line[begining:match_end.start()]

                print nick_name

                continue
            #
            #  PICTURE DOWNLOAD
            #

            # birthdate
            str_match = r'<span itemprop="birthDate">'
            match_begining = re.search(str_match, line)
            if match_begining != None:
                begining = match_begining.start()+len(str_match)-1
                match_end = re.search(r'</span><br', line)
                birth_date = line[begining:match_end.start()]

                print birth_date

                continue

            # locality
            str_match = r'itemprop="addressLocality" class="locality">'
            match_begining = re.search(str_match, line)
            if match_begining != None:
                begining = match_begining.start()+len(str_match)-1
                match_end = re.search(r'</span></span>', line)
                locality = line[begining:match_end.start()]

                print locality
                continue


            # country
            str_match = r'<strong itemprop="nationality">'
            match_begining = re.search(str_match, line)
            if match_begining != None:
                begining = match_begining.start()+len(str_match)-1
                match_end = re.search(r'</strong>', line)
                country = line[begining:match_end.start()]

                print country
                continue


            # height
            str_match = r'Height<br />'
            match_begining = re.search(str_match, line)
            if match_begining != None:
                i += 2
                line = lines[i]
                str_match = r' cm'
                match_begining = re.search(str_match, line)
                height = str(line[:match_begining.start()-1])

                print height

                continue

            # weight
            str_match = r'Weight<br />'
            match_begining = re.search(str_match, line)
            if match_begining != None:
                i += 2
                line = lines[i]
                str_match = r' kg'
                match_begining = re.search(str_match, line)
                weight = str(line[:match_begining.start()-1])

                print weight
                continue



            # # association
            # str_match = r'<span itemprop="birthDate">'
            # match_begining = re.search(str_match, line)
            # if match_begining != None:
            #     begining = match_begining.start()+len(str_match)-1
            #     match_end = re.search(r'</span><br', line)
            #     association = line[begining:match_end.start()]
            #
            #     print association
            #     continue
            #

            # class
            str_match = r'Class: <strong class="title">'
            match_begining = re.search(str_match, line)
            if match_begining != None:
                begining = match_begining.start()+len(str_match)-1
                match_end = re.search(r'</strong>', line)
                weight_class = line[begining:match_end.start()]

                print weight_class
                continue



            # team
            str_match = r'<span itemprop="name">'
            match_begining = re.search(str_match, line)
            if match_begining != None:
                begining = match_begining.start()+len(str_match)-1
                try:
                    match_end = re.search(r'</span></a>', line)
                    team = line[begining:match_end.start()]
                except AttributeError:
                    team = 'No Team'
                print team
                continue


            # # birthdate
            # str_match = r'<span itemprop="birthDate">'
            # match_begining = re.search(str_match, line)
            # if match_begining != None:
            #     begining = match_begining.start()+len(str_match)-1
            #     match_end = re.search(r'</span><br', line)
            #     birth_date = line[begining:match_end.start()]
            #     continue
            #
            #
            # # birthdate
            # str_match = r'<span itemprop="birthDate">'
            # match_begining = re.search(str_match, line)
            # if match_begining != None:
            #     begining = match_begining.start()+len(str_match)-1
            #     match_end = re.search(r'</span><br', line)
            #     birth_date = line[begining:match_end.start()]
            #     continue
            #
            #
            # # birthdate
            # str_match = r'<span itemprop="birthDate">'
            # match_begining = re.search(str_match, line)
            # if match_begining != None:
            #     begining = match_begining.start()+len(str_match)-1
            #     match_end = re.search(r'</span><br', line)
            #     birth_date = line[begining:match_end.start()]
            #     continue
            #
            #
            # # birthdate
            # str_match = r'<span itemprop="birthDate">'
            # match_begining = re.search(str_match, line)
            # if match_begining != None:
            #     begining = match_begining.start()+len(str_match)-1
            #     match_end = re.search(r'</span><br', line)
            #     birth_date = line[begining:match_end.start()]
            #     continue
            #
            #
            # # birthdate
            # str_match = r'<span itemprop="birthDate">'
            # match_begining = re.search(str_match, line)
            # if match_begining != None:
            #     begining = match_begining.start()+len(str_match)-1
            #     match_end = re.search(r'</span><br', line)
            #     birth_date = line[begining:match_end.start()]
            #     continue
            #
            #
            #
            # # birthdate
            # str_match = r'<span itemprop="birthDate">'
            # match_begining = re.search(str_match, line)
            # if match_begining != None:
            #     begining = match_begining.start()+len(str_match)-1
            #     match_end = re.search(r'</span><br', line)
            #     birth_date = line[begining:match_end.start()]
            #     continue
            #
            #
            # # birthdate
            # str_match = r'<span itemprop="birthDate">'
            # match_begining = re.search(str_match, line)
            # if match_begining != None:
            #     begining = match_begining.start()+len(str_match)-1
            #     match_end = re.search(r'</span><br', line)
            #     birth_date = line[begining:match_end.start()]
            #     continue



            # match_end = re.search(r'</span><br /><span class="nickname">"<em>', line)
            # if match_end != None:
            #     print match_end.end()
            #     continue


        # array += " - "
    # return render_to_response('fighterdb/templates/addfighter.html',
    #                       locals(),
    #                       context_instance=RequestContext(request))

    return HttpResponse(array)