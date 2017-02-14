from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import HttpResponse
import re
import os
import decimal
from datetime import datetime
from django.db.models import Q

from models import *
import urllib2



def add_fighter(request):
    url = "http://www.sherdog.com/fighter/"
    array = ""
    # dir = os.path.dirname(__file__)
    for j in xrange(1,99999):


        print '------------------------------------------------------'
        print '---------------------NEW FIGHTER----------------------'
        print '------------------------------------------------------'

        response = urllib2.urlopen(url + str(i))
        lines = response.read()

        text_file = open("fighter.html", "w")
        text_file.write(lines)
        text_file.close()

        file = open("fighter.html", 'rb')
        lines = file.readlines()

        for i in range(0, len(lines)):
            lines[i] = lines[i]

            code = i

            # name and nickname
            str_match = r'<h1 itemprop="name"><span class="fn">'
            match_begining = re.search(str_match, lines[i])
            if match_begining != None:
                match_end = re.search(r'</span>', lines[i])
                name = lines[i][match_begining.end():match_end.start()]
                name_array = []
                name_array = name.split(' ')

                print 'Name: '+ name

                # nickname
                nick_name = ''
                str_match = r'<span class="nickname">"<em>'
                match_begining = re.search(str_match, lines[i])
                if match_begining != None:
                    match_end = re.search(r'</em>"</span>', lines[i])
                    nick_name = lines[i][match_begining.end():match_end.start()]

                print 'Nickname: '+ nick_name

                continue
            #
            #  PICTURE DOWNLOAD
            #

            # birthdate
            str_match = r'<span itemprop="birthDate">'
            match_begining = re.search(str_match, lines[i])
            if match_begining != None:
                match_end = re.search(r'</span><br', lines[i])
                birth_date = lines[i][match_begining.end():match_end.start()]

                print 'Birth date: '+ birth_date

                continue

            # locality
            str_match = r'itemprop="addressLocality" class="locality">'
            match_begining = re.search(str_match, lines[i])
            if match_begining != None:
                match_end = re.search(r'</span></span>', lines[i])
                locality = lines[i][match_begining.end():match_end.start()]

                print 'Locality: '+locality
                continue


            # country
            str_match = r'<strong itemprop="nationality">'
            match_begining = re.search(str_match, lines[i])
            if match_begining != None:
                match_end = re.search(r'</strong>', lines[i])
                country = lines[i][match_begining.end():match_end.start()]

                print 'Country: '+ country
                continue


            # height
            str_match = r'Height<br />'
            match_begining = re.search(str_match, lines[i])
            if match_begining != None:
                i += 2
                lines[i] = lines[i]
                str_match = r' cm'
                match_begining = re.search(str_match, lines[i])
                height = str(lines[i][:match_begining.start()-1])

                print 'Height: '+height.strip()

                continue

            # weight
            str_match = r'Weight<br />'
            match_begining = re.search(str_match, lines[i])
            if match_begining != None:
                i += 2
                lines[i] = lines[i]
                str_match = r' kg'
                match_begining = re.search(str_match, lines[i])
                weight = str(lines[i][:match_begining.start()-1])

                print 'Weight: '+weight.strip()
                continue



            # # association
            # str_match = r'<span itemprop="birthDate">'
            # match_begining = re.search(str_match, lines[i])
            # if match_begining != None:
            #     begining = match_begining.start()+len(str_match)-1
            #     match_end = re.search(r'</span><br', lines[i])
            #     association = lines[i][begining:match_end.start()]
            #
            #     print association
            #     continue
            #

            # class
            str_match = r'weightclass='
            match_begining = re.search(str_match, lines[i])
            if match_begining != None:
                begining = match_begining.start()+len(str_match)
                match_end = re.search(r'">', lines[i])
                weight_class = lines[i][begining:match_end.start()]

                print 'Weight Class: '+weight_class
                continue



            # team
            str_match = r'<span itemprop="name">'
            match_begining = re.search(str_match, lines[i])
            if match_begining != None:
                begining = match_begining.start()+len(str_match)
                try:
                    match_end = re.search(r'</span></a>', lines[i])
                    team = lines[i][begining:match_end.start()]
                except AttributeError:
                    team = 'No Team'
                print 'Team: '+team
                continue


            # win counter
            str_match = r'<span class="result">Wins</span>'
            match_begining = re.search(str_match, lines[i])
            if match_begining != None:
                i += 1
                lines[i] = lines[i]
                str_match = r'<span class="counter">'
                match_begining = re.search(str_match, lines[i])
                match_end = re.search(r'</span>', lines[i])
                win_counter = lines[i][match_begining.end():match_end.start()]

                i += 5
                lines[i] = lines[i]
                str_match = r'<span class="graph_tag">'
                match_begining = re.search(str_match, lines[i])
                match_end = re.search(r' KO/TKO', lines[i])
                w_kos_tkos = lines[i][match_begining.end():match_end.start()]

                i += 4
                lines[i] = lines[i]
                str_match = r'<span class="graph_tag">'
                match_begining = re.search(str_match, lines[i])
                match_end = re.search(r' SUBMISSIONS', lines[i])
                w_submissions = lines[i][match_begining.end():match_end.start()]

                i += 4
                lines[i] = lines[i]
                str_match = r'<span class="graph_tag">'
                match_begining = re.search(str_match, lines[i])
                match_end = re.search(r' DECISIONS', lines[i])
                w_decisions = lines[i][match_begining.end():match_end.start()]


                print 'Wins: '+ win_counter
                print 'Wins by KO TKO: '+ w_kos_tkos
                print 'Wins by SUBMISSION: '+ w_submissions
                print 'Wins by DECISION: '+ w_decisions

                continue

            # loss counter
            str_match = r'<span class="result">Losses</span>'
            match_begining = re.search(str_match, lines[i])
            if match_begining != None:
                i += 1
                lines[i] = lines[i]
                str_match = r'<span class="counter">'
                match_begining = re.search(str_match, lines[i])
                match_end = re.search(r'</span>', lines[i])
                loss_counter = lines[i][match_begining.end():match_end.start()]

                i += 5
                lines[i] = lines[i]
                str_match = r'<span class="graph_tag">'
                match_begining = re.search(str_match, lines[i])
                match_end = re.search(r' KO/TKO', lines[i])
                l_kos_tkos = lines[i][match_begining.end():match_end.start()]

                i += 4
                lines[i] = lines[i]
                str_match = r'<span class="graph_tag">'
                match_begining = re.search(str_match, lines[i])
                match_end = re.search(r' SUBMISSIONS', lines[i])
                l_submissions = lines[i][match_begining.end():match_end.start()]

                i += 4
                lines[i] = lines[i]
                str_match = r'<span class="graph_tag">'
                match_begining = re.search(str_match, lines[i])
                match_end = re.search(r' DECISIONS', lines[i])
                l_decisions = lines[i][match_begining.end():match_end.start()]

                print 'Losses: '+ loss_counter
                print 'Losses by KO TKO: '+ l_kos_tkos
                print 'Losses by SUBMISSION: '+ l_submissions
                print 'Losses by DECISION: '+ l_decisions

                continue

            # fights
            str_match = r'<td><span class="final_result '
            match_begining = re.search(str_match, lines[i])

            ufc_fighter = False

            if match_begining != None:
                match_begining = re.search(str_match, lines[i])
                match_end = re.search(r'">', lines[i])
                final_result = lines[i][match_begining.end():match_end.start()]

                i += 1
                lines[i] = lines[i]
                str_match = r'href="/fighter/'
                match_begining = re.search(str_match, lines[i])
                match_end = re.search(r'">', lines[i])
                fighter_identifier = lines[i][match_begining.end():match_end.start()]
                array_fighter_id = []
                array_fighter_id = fighter_identifier.split('-')
                #fighter_id
                fighter_id = array_fighter_id[-1]

                str_match = r'class="sub_line">'
                match_begining = re.search(str_match, lines[i])
                match_end = re.search(r'</span></td>', lines[i])
                try:
                    fight_date = lines[i][match_begining.end():match_end.start()].replace(' ', '')
                except:
                    fight_date = '2000-01-01'
                fight = Fight.objects.filter(fighter1 = j).filter(fighter2 = fighter_id) or Fight.objects.filter(fighter2 = j).filter(fighter1 = fighter_id)
                # fight2 =
                print fight

                if fight.count() > 0:
                    continue

                i += 1
                lines[i] = lines[i]
                str_match = r'href="/events/'
                match_begining = re.search(str_match, lines[i])
                match_end = re.search(r'">', lines[i])
                event_identifier = lines[i][match_begining.end():match_end.start()]
                array_event_id = []
                array_event_id = event_identifier.split('-')
                #event_id
                event_id = array_event_id[-1]
                #event_name
                event_name_array = array_event_id[:-1]
                event_name = ''
                for evname in event_name_array:
                    event_name += evname
                if 'UFC' in event_name:
                    ufc_fighter = True

                # type of win or loss and referee
                i += 1
                lines[i] = lines[i]
                str_match = r'<td>'
                match_begining = re.search(str_match, lines[i])
                match_end = re.search(r'<br />', lines[i])
                fight_result_type = lines[i][match_begining.end():match_end.start()]

                str_match = r'class="sub_line">'
                match_begining = re.search(str_match, lines[i])
                match_end = re.search(r'</span></td>', lines[i])
                referee = lines[i][match_begining.end():match_end.start()]

                # round
                i += 1
                lines[i] = lines[i]
                str_match = r'<td>'
                match_begining = re.search(str_match, lines[i])
                match_end = re.search(r'</td>', lines[i])
                round = lines[i][match_begining.end():match_end.start()]

                # time
                i += 1
                lines[i] = lines[i]
                str_match = r'<td>'
                match_begining = re.search(str_match, lines[i])
                match_end = re.search(r'</td>', lines[i])
                time = lines[i][match_begining.end():match_end.start()]


                print 'Fight info: '
                print 'Fighter id: '+ fighter_id
                print 'Final result: '+ final_result
                print 'Event id: '+ event_id
                print 'Fight date: ' + fight_date
                print 'Fight result type: '+ fight_result_type
                print 'Referee: '+ referee
                print 'Round: '+ round
                print 'Time: '+ time

                to_add_fight = Fight()

                to_add_fight.fighter1 = j
                to_add_fight.fighter2 = int(fighter_id)
                to_add_fight.event_id = int(event_id)
                try:
                    to_add_fight.fight_date = datetime.strptime(fight_date, '%b/%d/%Y')
                except ValueError:
                    to_add_fight.fight_date = datetime.strptime('Jan/01/2000', '%b/%d/%Y')
                to_add_fight.fight_result_type = fight_result_type
                to_add_fight.referee = referee
                to_add_fight.round = int(round)
                to_add_fight.time = time
                if final_result == 'win':
                    to_add_fight.fighter_winner = j
                elif final_result == 'loss':
                    to_add_fight.fighter_winner = int(fighter_id)
                else:
                    to_add_fight.fighter_winner = 0
                to_add_fight.save()

                continue

        to_add_fighter = Fighter()
        to_add_fighter.code = j
        to_add_fighter.name = name
        to_add_fighter.nick_name = nick_name
        try:
            to_add_fighter.birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
        except ValueError:
            to_add_fighter.birth_date = datetime.strptime('Jan/01/2000', '%b/%d/%Y')
        to_add_fighter.locality = locality
        to_add_fighter.country = country
        try:
            to_add_fighter.height = decimal.Decimal(height.strip())
        except:
            to_add_fighter.height = decimal.Decimal(0)
        try:
            to_add_fighter.weight = decimal.Decimal(weight.strip())
        except:
            to_add_fighter.weight = decimal.Decimal(0)
        to_add_fighter.weight_class = weight_class
        to_add_fighter.win_counter = int(win_counter)
        to_add_fighter.w_kos_tkos = int(w_kos_tkos)
        to_add_fighter.w_submissions = int(w_submissions)
        to_add_fighter.w_decisions = int(w_decisions)
        to_add_fighter.l_kos_tkos = int(l_kos_tkos)
        to_add_fighter.l_submissions = int(l_submissions)
        to_add_fighter.l_decisions = int(l_decisions)
        to_add_fighter.ufc = ufc_fighter
        to_add_fighter.save()



    # return render_to_response('fighterdb/templates/addfighter.html',
    #                       locals(),
    #                       context_instance=RequestContext(request))

    return HttpResponse(array)



# def add_fighter(request):
#     array = ""
#     dir = os.path.dirname(__file__)
#     for j in xrange(1,100):
#         print '------------------------------------------------------'
#         print '---------------------NEW FIGHTER----------------------'
#         print '------------------------------------------------------'
#         filename = os.path.join(dir, '../files/fighter'+str(j)+'.html')
#         file = open(filename, 'rb')
#         lines = file.readlines()
#
#         for i in range(0, len(lines)):
#             lines[i] = lines[i]
#
#             code = i
#
#             # name and nickname
#             str_match = r'<h1 itemprop="name"><span class="fn">'
#             match_begining = re.search(str_match, lines[i])
#             if match_begining != None:
#                 match_end = re.search(r'</span>', lines[i])
#                 name = lines[i][match_begining.end():match_end.start()]
#                 name_array = []
#                 name_array = name.split(' ')
#
#                 print 'Name: '+ name
#
#                 # nickname
#                 nick_name = ''
#                 str_match = r'<span class="nickname">"<em>'
#                 match_begining = re.search(str_match, lines[i])
#                 if match_begining != None:
#                     match_end = re.search(r'</em>"</span>', lines[i])
#                     nick_name = lines[i][match_begining.end():match_end.start()]
#
#                 print 'Nickname: '+ nick_name
#
#                 continue
#             #
#             #  PICTURE DOWNLOAD
#             #
#
#             # birthdate
#             str_match = r'<span itemprop="birthDate">'
#             match_begining = re.search(str_match, lines[i])
#             if match_begining != None:
#                 match_end = re.search(r'</span><br', lines[i])
#                 birth_date = lines[i][match_begining.end():match_end.start()]
#
#                 print 'Birth date: '+ birth_date
#
#                 continue
#
#             # locality
#             str_match = r'itemprop="addressLocality" class="locality">'
#             match_begining = re.search(str_match, lines[i])
#             if match_begining != None:
#                 match_end = re.search(r'</span></span>', lines[i])
#                 locality = lines[i][match_begining.end():match_end.start()]
#
#                 print 'Locality: '+locality
#                 continue
#
#
#             # country
#             str_match = r'<strong itemprop="nationality">'
#             match_begining = re.search(str_match, lines[i])
#             if match_begining != None:
#                 match_end = re.search(r'</strong>', lines[i])
#                 country = lines[i][match_begining.end():match_end.start()]
#
#                 print 'Country: '+ country
#                 continue
#
#
#             # height
#             str_match = r'Height<br />'
#             match_begining = re.search(str_match, lines[i])
#             if match_begining != None:
#                 i += 2
#                 lines[i] = lines[i]
#                 str_match = r' cm'
#                 match_begining = re.search(str_match, lines[i])
#                 height = str(lines[i][:match_begining.start()-1])
#
#                 print 'Height: '+height.strip()
#
#                 continue
#
#             # weight
#             str_match = r'Weight<br />'
#             match_begining = re.search(str_match, lines[i])
#             if match_begining != None:
#                 i += 2
#                 lines[i] = lines[i]
#                 str_match = r' kg'
#                 match_begining = re.search(str_match, lines[i])
#                 weight = str(lines[i][:match_begining.start()-1])
#
#                 print 'Weight: '+weight.strip()
#                 continue
#
#
#
#             # # association
#             # str_match = r'<span itemprop="birthDate">'
#             # match_begining = re.search(str_match, lines[i])
#             # if match_begining != None:
#             #     begining = match_begining.start()+len(str_match)-1
#             #     match_end = re.search(r'</span><br', lines[i])
#             #     association = lines[i][begining:match_end.start()]
#             #
#             #     print association
#             #     continue
#             #
#
#             # class
#             str_match = r'weightclass='
#             match_begining = re.search(str_match, lines[i])
#             if match_begining != None:
#                 begining = match_begining.start()+len(str_match)
#                 match_end = re.search(r'">', lines[i])
#                 weight_class = lines[i][begining:match_end.start()]
#
#                 print 'Weight Class: '+weight_class
#                 continue
#
#
#
#             # team
#             str_match = r'<span itemprop="name">'
#             match_begining = re.search(str_match, lines[i])
#             if match_begining != None:
#                 begining = match_begining.start()+len(str_match)
#                 try:
#                     match_end = re.search(r'</span></a>', lines[i])
#                     team = lines[i][begining:match_end.start()]
#                 except AttributeError:
#                     team = 'No Team'
#                 print 'Team: '+team
#                 continue
#
#
#             # win counter
#             str_match = r'<span class="result">Wins</span>'
#             match_begining = re.search(str_match, lines[i])
#             if match_begining != None:
#                 i += 1
#                 lines[i] = lines[i]
#                 str_match = r'<span class="counter">'
#                 match_begining = re.search(str_match, lines[i])
#                 match_end = re.search(r'</span>', lines[i])
#                 win_counter = lines[i][match_begining.end():match_end.start()]
#
#                 i += 5
#                 lines[i] = lines[i]
#                 str_match = r'<span class="graph_tag">'
#                 match_begining = re.search(str_match, lines[i])
#                 match_end = re.search(r' KO/TKO', lines[i])
#                 w_kos_tkos = lines[i][match_begining.end():match_end.start()]
#
#                 i += 4
#                 lines[i] = lines[i]
#                 str_match = r'<span class="graph_tag">'
#                 match_begining = re.search(str_match, lines[i])
#                 match_end = re.search(r' SUBMISSIONS', lines[i])
#                 w_submissions = lines[i][match_begining.end():match_end.start()]
#
#                 i += 4
#                 lines[i] = lines[i]
#                 str_match = r'<span class="graph_tag">'
#                 match_begining = re.search(str_match, lines[i])
#                 match_end = re.search(r' DECISIONS', lines[i])
#                 w_decisions = lines[i][match_begining.end():match_end.start()]
#
#
#                 print 'Wins: '+ win_counter
#                 print 'Wins by KO TKO: '+ w_kos_tkos
#                 print 'Wins by SUBMISSION: '+ w_submissions
#                 print 'Wins by DECISION: '+ w_decisions
#
#                 continue
#
#             # loss counter
#             str_match = r'<span class="result">Losses</span>'
#             match_begining = re.search(str_match, lines[i])
#             if match_begining != None:
#                 i += 1
#                 lines[i] = lines[i]
#                 str_match = r'<span class="counter">'
#                 match_begining = re.search(str_match, lines[i])
#                 match_end = re.search(r'</span>', lines[i])
#                 loss_counter = lines[i][match_begining.end():match_end.start()]
#
#                 i += 5
#                 lines[i] = lines[i]
#                 str_match = r'<span class="graph_tag">'
#                 match_begining = re.search(str_match, lines[i])
#                 match_end = re.search(r' KO/TKO', lines[i])
#                 l_kos_tkos = lines[i][match_begining.end():match_end.start()]
#
#                 i += 4
#                 lines[i] = lines[i]
#                 str_match = r'<span class="graph_tag">'
#                 match_begining = re.search(str_match, lines[i])
#                 match_end = re.search(r' SUBMISSIONS', lines[i])
#                 l_submissions = lines[i][match_begining.end():match_end.start()]
#
#                 i += 4
#                 lines[i] = lines[i]
#                 str_match = r'<span class="graph_tag">'
#                 match_begining = re.search(str_match, lines[i])
#                 match_end = re.search(r' DECISIONS', lines[i])
#                 l_decisions = lines[i][match_begining.end():match_end.start()]
#
#                 print 'Losses: '+ loss_counter
#                 print 'Losses by KO TKO: '+ l_kos_tkos
#                 print 'Losses by SUBMISSION: '+ l_submissions
#                 print 'Losses by DECISION: '+ l_decisions
#
#                 continue
#
#             # fights
#             str_match = r'<td><span class="final_result '
#             match_begining = re.search(str_match, lines[i])
#             if match_begining != None:
#                 match_begining = re.search(str_match, lines[i])
#                 match_end = re.search(r'">', lines[i])
#                 final_result = lines[i][match_begining.end():match_end.start()]
#
#                 i += 1
#                 lines[i] = lines[i]
#                 str_match = r'href="/fighter/'
#                 match_begining = re.search(str_match, lines[i])
#                 match_end = re.search(r'">', lines[i])
#                 fighter_identifier = lines[i][match_begining.end():match_end.start()]
#                 array_fighter_id = []
#                 array_fighter_id = fighter_identifier.split('-')
#                 #fighter_id
#                 fighter_id = array_fighter_id[-1]
#
#                 str_match = r'class="sub_line">'
#                 match_begining = re.search(str_match, lines[i])
#                 match_end = re.search(r'</span></td>', lines[i])
#                 try:
#                     fight_date = lines[i][match_begining.end():match_end.start()].replace(' ', '')
#                 except:
#                     fight_date = '2000-01-01'
#                 fight = Fight.objects.filter(fighter1 = j).filter(fighter2 = fighter_id) or Fight.objects.filter(fighter2 = j).filter(fighter1 = fighter_id)
#                 # fight2 =
#                 print fight
#
#                 if fight.count() > 0:
#                     continue
#
#                 i += 1
#                 lines[i] = lines[i]
#                 str_match = r'href="/events/'
#                 match_begining = re.search(str_match, lines[i])
#                 match_end = re.search(r'">', lines[i])
#                 event_identifier = lines[i][match_begining.end():match_end.start()]
#                 array_event_id = []
#                 array_event_id = event_identifier.split('-')
#                 #event_id
#                 event_id = array_event_id[-1]
#
#                 # type of win or loss and referee
#                 i += 1
#                 lines[i] = lines[i]
#                 str_match = r'<td>'
#                 match_begining = re.search(str_match, lines[i])
#                 match_end = re.search(r'<br />', lines[i])
#                 fight_result_type = lines[i][match_begining.end():match_end.start()]
#
#                 str_match = r'class="sub_line">'
#                 match_begining = re.search(str_match, lines[i])
#                 match_end = re.search(r'</span></td>', lines[i])
#                 referee = lines[i][match_begining.end():match_end.start()]
#
#                 # round
#                 i += 1
#                 lines[i] = lines[i]
#                 str_match = r'<td>'
#                 match_begining = re.search(str_match, lines[i])
#                 match_end = re.search(r'</td>', lines[i])
#                 round = lines[i][match_begining.end():match_end.start()]
#
#                 # time
#                 i += 1
#                 lines[i] = lines[i]
#                 str_match = r'<td>'
#                 match_begining = re.search(str_match, lines[i])
#                 match_end = re.search(r'</td>', lines[i])
#                 time = lines[i][match_begining.end():match_end.start()]
#
#
#                 print 'Fight info: '
#                 print 'Fighter id: '+ fighter_id
#                 print 'Final result: '+ final_result
#                 print 'Event id: '+ event_id
#                 print 'Fight date: ' + fight_date
#                 print 'Fight result type: '+ fight_result_type
#                 print 'Referee: '+ referee
#                 print 'Round: '+ round
#                 print 'Time: '+ time
#
#                 to_add_fight = Fight()
#
#                 to_add_fight.fighter1 = j
#                 to_add_fight.fighter2 = int(fighter_id)
#                 to_add_fight.event_id = int(event_id)
#                 try:
#                     to_add_fight.fight_date = datetime.strptime(fight_date, '%b/%d/%Y')
#                 except ValueError:
#                     to_add_fight.fight_date = datetime.strptime('Jan/01/2000', '%b/%d/%Y')
#                 to_add_fight.fight_result_type = fight_result_type
#                 to_add_fight.referee = referee
#                 to_add_fight.round = int(round)
#                 to_add_fight.time = time
#                 if final_result == 'win':
#                     to_add_fight.fighter_winner = j
#                 elif final_result == 'loss':
#                     to_add_fight.fighter_winner = int(fighter_id)
#                 else:
#                     to_add_fight.fighter_winner = 0
#                 to_add_fight.save()
#
#                 continue
#
#         # to_add_fighter = Fighter()
#         # to_add_fighter.code = j
#         # to_add_fighter.name = name
#         # to_add_fighter.nick_name = nick_name
#         # try:
#         #     to_add_fighter.birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
#         # except ValueError:
#         #     to_add_fighter.birth_date = datetime.strptime('Jan/01/2000', '%b/%d/%Y')
#         # to_add_fighter.locality = locality
#         # to_add_fighter.country = country
#         # try:
#         #     to_add_fighter.height = decimal.Decimal(height.strip())
#         # except:
#         #     to_add_fighter.height = decimal.Decimal(0)
#         # try:
#         #     to_add_fighter.weight = decimal.Decimal(weight.strip())
#         # except:
#         #     to_add_fighter.weight = decimal.Decimal(0)
#         # to_add_fighter.weight_class = weight_class
#         # to_add_fighter.win_counter = int(win_counter)
#         # to_add_fighter.w_kos_tkos = int(w_kos_tkos)
#         # to_add_fighter.w_submissions = int(w_submissions)
#         # to_add_fighter.w_decisions = int(w_decisions)
#         # to_add_fighter.l_kos_tkos = int(l_kos_tkos)
#         # to_add_fighter.l_submissions = int(l_submissions)
#         # to_add_fighter.l_decisions = int(l_decisions)
#         # to_add_fighter.save()
#
#
#
#     # return render_to_response('fighterdb/templates/addfighter.html',
#     #                       locals(),
#     #                       context_instance=RequestContext(request))
#
#     return HttpResponse(array)




def get_updated_hashers(request):
    url = "http://www.fightmetric.com/statistics/events/completed?page=all"


    print '------------------------------------------------------'
    print '------------------UPDATE HASHERS----------------------'
    print '------------------------------------------------------'

    dir = os.path.dirname(__file__)


    response = urllib2.urlopen(url)
    lines = response.read()


    text_file = open("event.html", "w")
    text_file.write(lines)
    text_file.close()

    file = open("event.html", 'rb')
    lines = file.readlines()

    str_match = r'fightmetric.com/event-details/'

    for i in range(0, len(lines)):
        lines[i] = lines[i]

        # event hasher
        match_begining = re.search(str_match, lines[i])
        if match_begining != None:

            match_end = re.search(r'" class', lines[i])
            hasher = lines[i][match_begining.end():match_end.start()]


            print 'Hasher: '+ hasher

            # event name
            i+=1
            event_name = lines[i].replace('  ', '').replace('\n', '')

            # event date
            i+=3
            event_date = lines[i].replace('  ', '').replace('\n', '')


            # event date
            i+=5
            event_location = lines[i].replace('  ', '').replace('\n', '')

            to_add_event = EventMetric()
            to_add_event.hasher = hasher
            to_add_event.name = event_name


            try:

                to_add_event.date = datetime.strptime(event_date, '%B %d, %Y')
            except ValueError:
                to_add_event.date = datetime.strptime('Jan/01/2000', '%b/%d/%Y')

            array_event_name = event_location.split(',')


            try:
                to_add_event.city = array_event_name[0]
            except:
                to_add_event.city = ''

            try:
                to_add_event.state = array_event_name[1]
            except:
                to_add_event.state = ''

            try:
                to_add_event.country = array_event_name[2]
            except:
                to_add_event.country = ''



            to_add_event.save()



def get_fights_metrics(request):
    url = "http://www.fightmetric.com/event-details/"


    events = EventMetric.objects.all()

    for event in events:


        response = urllib2.urlopen(url + event.hasher)
        lines = response.read()

        text_file = open("event.html", "w")
        text_file.write(lines)
        text_file.close()

        file = open("event.html", 'rb')
        lines = file.readlines()

        for i in range(0, len(lines)):

            code = i

            # name and nickname
            str_match = r'    <td style="width:100px" class="b-fight-details__table-col l-page_align_left">'
            match_begining = re.search(str_match, lines[i])
            if match_begining != None:
                i+=4
                match_begining = re.search('/fighter-details/', lines[i])
                match_end = re.search(r'">', lines[i])
                winner_hasher = lines[i][match_begining.end():match_end.start()]
                print 'Winner hasher: '+winner_hasher

                i += 1
                winner_name = lines[i]
                print 'Winner name: ' + winner_name

                i += 7
                match_begining = re.search('/fighter-details/', lines[i])
                match_end = re.search(r'">', lines[i])
                loser_hasher = lines[i][match_begining.end():match_end.start()]
                print 'Loser hasher: ' + loser_hasher

                i += 1
                loser_name = lines[i]
                print 'Loser name: ' + loser_name

                i += 12
                winner_str = int(lines[i].replace(' ',''))
                print 'Winner STR: ' + str(winner_str)

                i += 7
                loser_str = int(lines[i].replace(' ', ''))
                print 'Loser STR: ' + str(loser_str)

                i += 9
                winner_td = int(lines[i].replace(' ', ''))
                print 'Winner TD: ' + str(winner_td)

                i += 5
                loser_td = int(lines[i].replace(' ', ''))
                print 'Loser TD: ' + str(loser_td)

                i += 9
                winner_sub = int(lines[i].replace(' ', ''))
                print 'Winner SUB: ' + str(winner_sub)

                i += 5
                loser_sub = int(lines[i].replace(' ', ''))
                print 'Loser SUB: ' + str(loser_sub)

                i += 9
                winner_pass = int(lines[i].replace(' ', ''))
                print 'Winner PASS: ' + str(winner_pass)

                i += 5
                loser_pass = int(lines[i].replace(' ', ''))
                print 'Loser PASS: ' + str(loser_pass)

                i += 6
                weight_category = lines[i].replace(' ', '')
                print 'Weight Category: ' + weight_category

                i += 10
                method = lines[i].replace(' ', '')
                print 'Method: ' + method

                i += 5
                method_2 = lines[i].replace(' ', '')
                print 'Method2: ' + method_2

                i += 6
                round = lines[i].replace(' ', '')
                print 'Round: ' + round

                i += 6
                time = lines[i].replace(' ', '')
                print 'Time: ' + time

                fight = FightMetric()

                fight.event = event
                fight.fighter1 = winner_hasher
                fight.fighter2 = loser_hasher
                fight.str1 = winner_str
                fight.str2 = loser_str
                fight.td1 = winner_td
                fight.td2 = loser_td
                fight.sub1 = winner_sub
                fight.sub2 = loser_sub
                fight.pass1 = winner_pass
                fight.pass2 = loser_pass
                fight.round = round
                fight.time = time

                fight.save()


                continue


def get_fighter_metrics(request):
    url = "http://www.fightmetric.com/fighter-details/"


    fighters1 = FightMetric.objects.all().values_list('fighter1', flat=True)
    fighters2 = FightMetric.objects.all().values_list('fighter2', flat=True)

    in_first = set(fighters1)
    in_second = set(fighters2)

    in_second_but_not_in_first = in_second - in_first

    filtered_fighters = fighters1 + list(in_second_but_not_in_first)

    for fighter in filtered_fighters:


        response = urllib2.urlopen(url + fighter.fighter)
        lines = response.read()

        text_file = open("fighter.html", "w")
        text_file.write(lines)
        text_file.close()

        file = open("fighter.html", 'rb')
        lines = file.readlines()

        for i in range(0, len(lines)):

            code = i

            # name and nickname
            str_match = r'            <span class="b-content__title-highlight">'
            match_begining = re.search(str_match, lines[i])
            if match_begining != None:
                i+=1
                # match_begining = re.search('/fighter-details/', lines[i])
                # match_end = re.search(r'">', lines[i])
                fighter_name = lines[i].replace(' ', '')
                print 'Fighter name: '+fighter_name

                i += 5
                match_begining = re.search('Record: ', lines[i])
                match_end = re.search(r'\n', lines[i])
                record = lines[i][match_begining.end():match_end.start()].split('-')
                wins = int(record[0])
                loses = int(record[1])
                draws = int(record[2])
                print 'Wins: ' + wins
                print 'Loses: ' + loses
                print 'Draws: ' + draws

            # name and nickname
            str_match = r'    <tr class="b-fight-details__table-row b-fight-details__table-row__hover js-fight-details-click"'
            match_begining = re.search(str_match, lines[i])
            if match_begining != None:
                i += 9
                match_begining = re.search('/fighter-details/', lines[i])
                match_end = re.search(r'">', lines[i])
                winner_hasher = lines[i][match_begining.end():match_end.start()]
                print 'Winner hasher: ' + winner_hasher

                i += 1
                winner_name = lines[i]
                print 'Winner name: ' + winner_name

                i += 7
                match_begining = re.search('/fighter-details/', lines[i])
                match_end = re.search(r'">', lines[i])
                loser_hasher = lines[i][match_begining.end():match_end.start()]
                print 'Loser hasher: ' + loser_hasher

                i += 1
                loser_name = lines[i]
                print 'Loser name: ' + loser_name

                i += 12
                winner_str = int(lines[i].replace(' ', ''))
                print 'Winner STR: ' + str(winner_str)

                i += 7
                loser_str = int(lines[i].replace(' ', ''))
                print 'Loser STR: ' + str(loser_str)

                i += 9
                winner_td = int(lines[i].replace(' ', ''))
                print 'Winner TD: ' + str(winner_td)

                i += 5
                loser_td = int(lines[i].replace(' ', ''))
                print 'Loser TD: ' + str(loser_td)

                i += 9
                winner_sub = int(lines[i].replace(' ', ''))
                print 'Winner SUB: ' + str(winner_sub)

                i += 5
                loser_sub = int(lines[i].replace(' ', ''))
                print 'Loser SUB: ' + str(loser_sub)

                i += 9
                winner_pass = int(lines[i].replace(' ', ''))
                print 'Winner PASS: ' + str(winner_pass)

                i += 5
                loser_pass = int(lines[i].replace(' ', ''))
                print 'Loser PASS: ' + str(loser_pass)

                i += 6
                weight_category = lines[i].replace(' ', '')
                print 'Weight Category: ' + weight_category

                i += 10
                method = lines[i].replace(' ', '')
                print 'Method: ' + method

                i += 5
                method_2 = lines[i].replace(' ', '')
                print 'Method2: ' + method_2

                i += 6
                round = lines[i].replace(' ', '')
                print 'Round: ' + round

                i += 6
                time = lines[i].replace(' ', '')
                print 'Time: ' + time

                fight = FightMetric()

                fight.event = event
                fight.fighter1 = winner_hasher
                fight.fighter2 = loser_hasher
                fight.str1 = winner_str
                fight.str2 = loser_str
                fight.td1 = winner_td
                fight.td2 = loser_td
                fight.sub1 = winner_sub
                fight.sub2 = loser_sub
                fight.pass1 = winner_pass
                fight.pass2 = loser_pass
                fight.round = round
                fight.time = time

                fight.save()

                continue


            continue


