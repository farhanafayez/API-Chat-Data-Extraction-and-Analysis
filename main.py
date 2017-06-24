import requests
import sys
import xlwt
import csv
from datetime import datetime

def getInformationViaUrl(start_date, end_date, token):
    url = 'https://api.giosg.com/api/reporting/v1/rooms/84e0fefa-5675-11e7-a349-00163efdd8db/chat-stats/daily/?start_date={}&end_date={}'.format(start_date, end_date)
    response = requests.get(url, headers={'Authorization': 'Token {}'.format(token)})
    return response.json()

def get_top_three_conversation_count(by_date):
    list = []
    list2 = []
    for x in by_date:
        list.append(x['conversation_count'])
        list2.append(x['date'])
    top3counts = sorted(zip(list,list2), reverse=True)[:3]
    return top3counts

def get_hourly_presence_count(date, token):
    url = 'https://api.giosg.com/api/reporting/v1/rooms/84e0fefa-5675-11e7-a349-00163efdd8db/user-presence-counts/?start_date={}&end_date={}'.format(date, date)
    response = requests.get(url, headers={'Authorization': 'Token {}'.format(token)})
    return response.json()

def day_result(g_h_p_c):
    hourly = g_h_p_c['hourly']
    for hours in hourly:
        print('{}:00 there was {} users present'.format(hours['hour_of_day'],hours['user_count']))

def day_result2(g_h_p_c):
    hourly = g_h_p_c['hourly']
    list = []
    for hours in hourly:
        list.append([hours['hour_of_day'], hours['user_count']])
    return list

def run(start_date, end_date, token, excel):
    if(excel == 'empty'):
        # Lets call the url to get data
        information = getInformationViaUrl(start_date, end_date, token)

        #Lets get the by date from that information
        by_date = information['by_date']

        #Lets get the top three conversation counts
        top3ConversationCounts = get_top_three_conversation_count(by_date)

        # lets do a for loop and print all the results out at onces
        for x in top3ConversationCounts:
            print('On {} there was {} chats'.format(x[1], x[0]))
            print('-------------------------------------------')
            #lets call the url to get the hourly presence count
            g_h_p_c = get_hourly_presence_count(x[1],token)
            # lets print the hourly presense stuff with a function just like the design
            day_result(g_h_p_c)
            print()
            print()
    else:
        # Excel function
        information = getInformationViaUrl(start_date, end_date, token)
        by_date = information['by_date']
        top3ConversationCounts = get_top_three_conversation_count(by_date)

        # -------- excel file starts here -----------
        dict = {}
        for x in top3ConversationCounts:
            g_h_p_c = get_hourly_presence_count(x[1],token)
            #Another function recreated to get the result as a list
            result = day_result2(g_h_p_c)
            dict[x] =  result

        with open("busy_hours.csv", "w") as f:
            writer = csv.writer(f)
            for header, rows in dict.items():
                writer.writerow(header)
                writer.writerow(["hour_of_day", "user_count"])
                writer.writerows(rows)
        return print('result downloaded as CSV')

# RUN EVERYTHING
#run('2017-05-01','2017-06-15' ,'xxxx','excel')
run(sys.argv[2],sys.argv[4] ,sys.argv[6],sys.argv[8])
