import requests
import csv
import requests
import logging








def fetch_data(api):
    try:
        response = requests.get(api, timeout=10)  
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data from {api}: {e}")
        return None



def contest_data(url):
    return fetch_data(url)






print("Enter No of organizations")
number=int(input())




inp=[]
print("Enter Organizations names")
for i in range(number):
    o=input()
    inp.append(o)    

for i in range(len(inp)):
    inp[i]=inp[i].lower().replace(" ","")



print("Enter Contest Id")
c_id=input()

    
def string_matching(a,b):
    if(b in a):
        return True
    return False



def upadated_standings(contestid):
    
    contest_url = f"https://codeforces.com/api/contest.standings?contestId={contestid}&from=1&count=9000&showUnofficial=false"
    contest_standings = contest_data(contest_url)

    if contest_standings is None:
        return None

    #return contest_standings  


    contestant=contest_standings['result']['rows']

    no_of_contestant=len(contestant)
    #print(no_of_contestant)
    start=1
    cont_lis=[]
    while start <= no_of_contestant:
        handle_url = "https://codeforces.com/api/user.info?handles="
        for i in range(start, min(start + 500, no_of_contestant)):
            handle = contestant[i]['party']['members'][0]['handle']
            handle_url += f"{handle};"

        cont_data = fetch_data(handle_url)

        if cont_data is None:
            break

        sz = len(cont_data['result'])

        for i in range(sz):
            cont_org = cont_data['result'][i]

            if cont_org.get('organization') is None:
                continue

            cont_org1 = cont_org['organization'].lower().replace(" ", "")
            for j in range(len(inp)):
                if string_matching(cont_org1, inp[j]):
                    cont_lis.append(contestant[i + start])
                    break

        start += 500

    contest_standings['result']['rows'] = cont_lis



    


   

    with open('results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Rank", "Global Rank", "User ID"])

        for i, item in enumerate(cont_lis):
            writer.writerow([i + 1, item['rank'], item['party']['members'][0]['handle']])

    
upadated_standings(c_id)