from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import HttpResponse
import re
import os
import decimal
from datetime import datetime
from django.db.models import Q

from models import Fighter, Fight

def add_fighter(request):
    array = ""
    dir = os.path.dirname(__file__)
    for i in xrange(1,100):
        print '------------------------------------------------------'
        print '---------------------NEW FIGHTER----------------------'
        print '------------------------------------------------------'
        filename = os.path.join(dir, '../files/'+str(i)+'.html')
        file = open(filename, 'rb')
        lines = file.readlines()

        for i in range(0, len(lines)):
            line = lines[i]

            # name and nickname
            str_match = r'<h1 itemprop="name"><span class="fn">'
            match_begining = re.search(str_match, line)
            if match_begining != None:
                match_end = re.search(r'</span>', line)
                name = line[match_begining.end():match_end.start()]
                name_array = []
                name_array = name.split(' ')

                print 'Name: '+ name

                # nickname
                nick_name = ''
                str_match = r'<span class="nickname">"<em>'
                match_begining = re.search(str_match, line)
                if match_begining != None:
                    match_end = re.search(r'</em>"</span>', line)
                    nick_name = line[match_begining.end():match_end.start()]

                print 'Nickname: '+ nick_name

                continue
            #
            #  PICTURE DOWNLOAD
            #

            # birthdate
            str_match = r'<span itemprop="birthDate">'
            match_begining = re.search(str_match, line)
            if match_begining != None:
                match_end = re.search(r'</span><br', line)
                birth_date = line[match_begining.end():match_end.start()]

                print 'Birth date: '+ birth_date

                continue

            # locality
            str_match = r'itemprop="addressLocality" class="locality">'
            match_begining = re.search(str_match, line)
            if match_begining != None:
                match_end = re.search(r'</span></span>', line)
                locality = line[match_begining.end():match_end.start()]

                print 'Locality: '+locality
                continue


            # country
            str_match = r'<strong itemprop="nationality">'
            match_begining = re.search(str_match, line)
            if match_begining != None:
                match_end = re.search(r'</strong>', line)
                country = line[match_begining.end():match_end.start()]

                print 'Country: '+ country
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

                print 'Height: '+height.strip()

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

                print 'Weight: '+weight.strip()
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
                begining = match_begining.start()+len(str_match)
                match_end = re.search(r'</strong>', line)
                weight_class = line[begining:match_end.start()]

                print 'Weight Class: '+weight_class
                continue



            # team
            str_match = r'<span itemprop="name">'
            match_begining = re.search(str_match, line)
            if match_begining != None:
                begining = match_begining.start()+len(str_match)
                try:
                    match_end = re.search(r'</span></a>', line)
                    team = line[begining:match_end.start()]
                except AttributeError:
                    team = 'No Team'
                print 'Team: '+team
                continue


            # win counter
            str_match = r'<span class="result">Wins</span>'
            match_begining = re.search(str_match, line)
            if match_begining != None:
                i += 1
                line = lines[i]
                str_match = r'<span class="counter">'
                match_begining = re.search(str_match, line)
                match_end = re.search(r'</span>', line)
                win_counter = line[match_begining.end():match_end.start()]

                i += 5
                line = lines[i]
                str_match = r'<span class="graph_tag">'
                match_begining = re.search(str_match, line)
                match_end = re.search(r' KO/TKO', line)
                w_kos_tkos = line[match_begining.end():match_end.start()]

                i += 4
                line = lines[i]
                str_match = r'<span class="graph_tag">'
                match_begining = re.search(str_match, line)
                match_end = re.search(r' SUBMISSIONS', line)
                w_submissions = line[match_begining.end():match_end.start()]

                i += 4
                line = lines[i]
                str_match = r'<span class="graph_tag">'
                match_begining = re.search(str_match, line)
                match_end = re.search(r' DECISIONS', line)
                w_decisions = line[match_begining.end():match_end.start()]


                print 'Wins: '+ win_counter
                print 'Wins by KO TKO: '+ w_kos_tkos
                print 'Wins by SUBMISSION: '+ w_submissions
                print 'Wins by DECISION: '+ w_decisions

                continue

            # loss counter
            str_match = r'<span class="result">Losses</span>'
            match_begining = re.search(str_match, line)
            if match_begining != None:
                i += 1
                line = lines[i]
                str_match = r'<span class="counter">'
                match_begining = re.search(str_match, line)
                match_end = re.search(r'</span>', line)
                loss_counter = line[match_begining.end():match_end.start()]

                i += 5
                line = lines[i]
                str_match = r'<span class="graph_tag">'
                match_begining = re.search(str_match, line)
                match_end = re.search(r' KO/TKO', line)
                l_kos_tkos = line[match_begining.end():match_end.start()]

                i += 4
                line = lines[i]
                str_match = r'<span class="graph_tag">'
                match_begining = re.search(str_match, line)
                match_end = re.search(r' SUBMISSIONS', line)
                l_submissions = line[match_begining.end():match_end.start()]

                i += 4
                line = lines[i]
                str_match = r'<span class="graph_tag">'
                match_begining = re.search(str_match, line)
                match_end = re.search(r' DECISIONS', line)
                l_decisions = line[match_begining.end():match_end.start()]

                print 'Losses: '+ loss_counter
                print 'Losses by KO TKO: '+ l_kos_tkos
                print 'Losses by SUBMISSION: '+ l_submissions
                print 'Losses by DECISION: '+ l_decisions

                continue

            # fights
            str_match = r'<td><span class="final_result '
            match_begining = re.search(str_match, line)
            if match_begining != None:
                match_begining = re.search(str_match, line)
                match_end = re.search(r'">', line)
                final_result = line[match_begining.end():match_end.start()]

                i += 1
                line = lines[i]
                str_match = r'href="/fighter/'
                match_begining = re.search(str_match, line)
                match_end = re.search(r'">', line)
                fighter_identifier = line[match_begining.end():match_end.start()]
                array_fighter_id = []
                array_fighter_id = fighter_identifier.split('-')
                #fighter_id
                fighter_id = array_fighter_id[-1]

                str_match = r'class="sub_line">'
                match_begining = re.search(str_match, line)
                match_end = re.search(r'</span></td>', line)
                try:
                    fight_date = line[match_begining.end():match_end.start()].replace(' ', '')
                except:
                    fight_date = '2000-01-01'
                fight = Fight.objects.filter(fighter1 = i).filter(fighter2 = fighter_id) | Fight.objects.filter(fighter2 = i).filter(fighter1 = fighter_id)

                if fight.count() > 0:
                    continue

                i += 1
                line = lines[i]
                str_match = r'href="/events/'
                match_begining = re.search(str_match, line)
                match_end = re.search(r'">', line)
                event_identifier = line[match_begining.end():match_end.start()]
                array_event_id = []
                array_event_id = event_identifier.split('-')
                #event_id
                event_id = array_event_id[-1]

                # type of win or loss and referee
                i += 1
                line = lines[i]
                str_match = r'<td>'
                match_begining = re.search(str_match, line)
                match_end = re.search(r'<br />', line)
                fight_result_type = line[match_begining.end():match_end.start()]

                str_match = r'class="sub_line">'
                match_begining = re.search(str_match, line)
                match_end = re.search(r'</span></td>', line)
                referee = line[match_begining.end():match_end.start()]

                # round
                i += 1
                line = lines[i]
                str_match = r'<td>'
                match_begining = re.search(str_match, line)
                match_end = re.search(r'</td>', line)
                round = line[match_begining.end():match_end.start()]

                # time
                i += 1
                line = lines[i]
                str_match = r'<td>'
                match_begining = re.search(str_match, line)
                match_end = re.search(r'</td>', line)
                time = line[match_begining.end():match_end.start()]


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

                to_add_fight.fighter1 = i
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
                    to_add_fight.fighter_winner = i
                elif final_result == 'loss':
                    to_add_fight.fighter_winner = int(fighter_id)
                else:
                    to_add_fight.fighter_winner = 0
                to_add_fight.save()

                continue

        to_add_fighter = Fighter()
        to_add_fighter.id = i
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
        to_add_fighter.save()



    # return render_to_response('fighterdb/templates/addfighter.html',
    #                       locals(),
    #                       context_instance=RequestContext(request))

    return HttpResponse(array)