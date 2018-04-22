import csv
import json
import requests
import re
import sys
firebase_url =  "https://inf551-project-10723.firebaseio.com"
def readFromFile():
    f = open('./data/dc.json')
    data = f.read()
    js = json.loads(data)
    return js
def a_1_save():
    rows = readFromFile()

    for row in rows:
        for key in row:
            if key in ["YEAR", "APPEARANCES", "page_id"]:
                print(key, row[key])
                if row[key] != "":
                    row[key] = int(row[key].strip())
        row["lower_case_name"] = row["name"].lower()

    response = requests.put(firebase_url + "/dc.json", json=rows)
    print(response.status_code)

    print("total data saved to firebase")

def a_2_save():
    rows = readFromFile()
    jsonfile = open('index.json', 'w')
    events = {}
    delims = ['&', '/']
    for obj in rows:
        event = obj['event']
        tokens = re.split(r'[^a-zA-z0-9]', event)
        for token in tokens:
            token = token
            token = token.strip()
            token = token.lower()
            if len(token) == 0:
                continue
            id = obj['id']
            if token in events:
                if id not in events[token]:
                    events[token].append(id)
            else:
                events[token] = [id]
    json.dump(events, jsonfile, indent=2)
    response = requests.put(firebase_url+"/index.json", json=events)
    print(response.status_code)
    print("inverted indexed data saved to firebase")

def getJSON():
    jsonfile = open('file.json', 'w')

    rows = []
    #fileUrl = './data/menu-136.csv'
    fileUrl = sys.argv[1]
    with open(fileUrl, 'r') as csvfile:
        dictcsv = csv.DictReader(csvfile)
        for row in dictcsv:
            #print(row)
            rows.append(row)
        json.dump(rows, jsonfile, indent=2)
        jsonfile.close()
        print("done")
    print("finished reading json and saved to file.json")
    return rows

if __name__ == '__main__':
    a_1_save()