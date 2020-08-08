#!/usr/bin/env python3
#from cloudant import Cloudant
from flask import Flask, render_template, request, jsonify
import atexit
import os
import json
import csv
from werkzeug.utils import secure_filename
import dateutil.parser, time
import math    
# from flask_mysqldb import MySQL    

import logging
import ibm_db

application = Flask(__name__)

db_name = 'mydb'
client = None
db = None

db2conn = ibm_db.connect("DATABASE=BLUDB;HOSTNAME=dashdb-txn-sbox-yp-dal09-11.services.dal.bluemix.net;PORT=50000;PROTOCOL=TCPIP;UID=kpg48221;PWD=s8lg350w5wv+jbdh;","kpg48221","s8lg350w5wv+jbdh")

@application.route('/')
def root():
    return render_template('login.html')
    # return application.send_static_file('login.html')

@application.route('/register')
def register():
    return render_template('Register.html')


# def getRiskPatients():

# stmt="SELECT time,mag,place,locationSource FROM quakeData 
# WHERE mag>= %s AND mag<= %s AND date(time)>= %s AND date(time)<= %s"
#     cur.execute(stmt,(mag1,mag2,startDate,endDate,))


# @application.route('/dashboard', methods=['GET', 'POST'])
# def dashboard():
#     # x = [1,2,3,4,5,6,7,8,9,10]
#     x=[1,2,3]
#     y=["High","Medium","Low"]
#     return render_template('basic1.html',x1=x,y1=y)

@application.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    x = [1,2,3,4,5,6,7,8,9,10]

    sql = "SELECT FIRSTNAME,LASTNAME FROM PATIENTS WHERE RISK_PERCENTAGE>=?"
    stmt1 = ibm_db.prepare(db2conn, sql )
    ibm_db.bind_param(stmt1, 1, 65)
    ibm_db.execute(stmt1)
    rows1=[]
    result = ibm_db.fetch_assoc(stmt1)
    print(type(result))
    while result != False:
        rows1.append(result.copy())
        result = ibm_db.fetch_assoc(stmt1)


    sql = "SELECT FIRSTNAME,LASTNAME FROM PATIENTS WHERE RISK_PERCENTAGE>? AND RISK_PERCENTAGE<?"
    stmt2 = ibm_db.prepare(db2conn, sql )
    ibm_db.bind_param(stmt2, 1, 35)
    ibm_db.bind_param(stmt2, 2, 65)
    ibm_db.execute(stmt2)
    rows2=[]
    result = ibm_db.fetch_assoc(stmt2)
    print(type(result))
    while result != False:
        rows2.append(result.copy())
        result = ibm_db.fetch_assoc(stmt2)

    sql = "SELECT FIRSTNAME,LASTNAME FROM PATIENTS WHERE RISK_PERCENTAGE<=?"
    stmt3 = ibm_db.prepare(db2conn, sql )
    ibm_db.bind_param(stmt3, 1, 35)
    ibm_db.execute(stmt3)
    rows3=[]
    result = ibm_db.fetch_assoc(stmt3)
    print(type(result))
    while result != False:
        rows3.append(result.copy())
        result = ibm_db.fetch_assoc(stmt3)

   
    x=[1,2,3]
    # x=[len(rows1),len(rows2),len(rows3)]

    print("nos",x)

    y=["High","Medium","Low"]
    # return render_template('basic1.html',x1=x,y1=y)

    # print(rows)
    # print(type(rows))
    # print(rows[0]["FIRSTNAME"])
    return render_template('dashboard.html',value3=rows3, value2=rows2, value1=rows1 , x1=x,y1=y)

@application.route('/login')
def login():
    return render_template('login.html')

@application.route('/patient')
def patient():
    x = [[1,2,3,4,5,6,7,8]]
    return render_template('PatientDetails.html',value=x)


# #Database Connection
# def connection():
#     # db2conn = ibm_db.connect("DATABASE=BLUDB;HOSTNAME=dashdb-txn-sbox-yp-dal09-11.services.dal.bluemix.net;PORT=50000;PROTOCOL=TCPIP;UID=kpg48221;PWD=s8lg350w5wv+jbdh;","kpg48221","s8lg350w5wv+jbdh")
#     try:
#         db2conn = ibm_db.connect("DATABASE=BLUDB;HOSTNAME=dashdb-txn-sbox-yp-dal09-11.services.dal.bluemix.net;PORT=50000;PROTOCOL=TCPIP;UID=kpg48221;PWD=s8lg350w5wv+jbdh;","kpg48221","s8lg350w5wv+jbdh")
#     except:     
#         print("no connection:", ibm_db.conn_errormsg())
#     else:
#         print("The connection was successful")
#     # conn_str="DATABASE=BLUDB;HOSTNAME=dashdb-txn-sbox-yp-dal09-11.services.dal.bluemix.net;PORT=50000;PROTOCOL=TCPIP;UID=kpg48221;PWD=s8lg350w5wv+jbdh;"

#     # db2conn = ibm_db.connect(conn_str,",")
#     sql = "SELECT * FROM PATIENTS"
#     stmt = ibm_db.exec_immediate(db2conn, sql)
#     #ibm_db.execute(sql)
#     rows=[]
#     # fetch the result
#     result = ibm_db.fetch_assoc(stmt)
#     while result != False:
#         rows.append(result.copy())
#         result = ibm_db.fetch_assoc(stmt)
#         print(result)
#     # close database connection
#     ibm_db.close(db2conn)



# jsonData={"userid":"1ID2012","firstname":"Odele","lastname":"Syrett","dob":"1954-12-13","gender":"female","bloodtype":"B-","lung_issues":False,"hypertension":False,"heartdisease":False,"hiv":False,"diabetes":True,"cancer":False,"age":23,"fever":4,"drycough":6,"fatigue":0,"trouble_breathing":0,"muscle_pain":0,"sore_throat":0,"heart_rate":[{"heartrate": 0, "timestamp": "2019-08-24 22:05:09"},{"heartrate": 0, "timestamp": "2019-08-24 22:05:09"},{"heartrate": 0, "timestamp": "2019-08-24 22:05:09"},{"heartrate": 0, "timestamp": "2019-08-24 22:05:09"}],"headache":0,"runnynose":0,"diarrhea":0,"zipcode":76204,"latitude":-6.7594317,"longitude":111.4484559,"risk_percentage":4.9851563425}
jsonData = 'sample.json'

json_data=open(jsonData).read()
json_obj = json.loads(json_data)

#connecting to db
# ibmDB= ibm_db.connect("DATABASE=BLUDB;HOSTNAME=dashdb-txn-sbox-yp-dal09-11.services.dal.bluemix.net;PORT=50001;PROTOCOL=TCPIP;UID=kpg48221;PWD=s8lg350w5wv+jbdh;Security=SSL;","ssljdbcurl","")
#curser= ibmDB.cursor()
conn = ibm_db_dbi.Connection(db2conn)

def risk_calcuation(user_details):
    """
    values: json input from app
    """
    pre_existing = ["lung_issues","hypertension","heartdisease","hiv","diabetes","cancer"]
    weights = {"age":0.02,"fever":0.2,"drycough":0.19,"fatigue":0.16,"trouble_breathing":0.15,"muscle_pain":0.0225,"sore_throat":0.015,"heart_rate":0.0125,"headache":0.01,"runnynose":0.01,"diarrhea":0.005,"gender":0.005}
    constant_values = {"male":5.5,"female":4.5,"lung_issues":2.2,"hypertension":2,"heartdisease":1.8,"hiv":1.6,"diabetes":1.4,"cancer":1}
    symptoms_list = ["gender","lung_issues","hypertension","heartdisease","hiv","diabetes","cancer","age","fever","drycough","fatigue","trouble_breathing","muscle_pain","sore_throat","heart_rate","headache","runnynose","diarrhea"]
    
    #updating raw_score to pre_exisiting conditions
    for condition in pre_existing:
        if user_details[condition]:
            if condition == "lung_issues":
                user_details[condition] = 5
            elif condition == "hypertension":
                user_details[condition] = 5.5
            elif condition == "heartdisease":
                user_details[condition] = 5
            elif condition == "hiv":
                user_details[condition] = 4.5
            elif condition == "diabetes":
                user_details[condition] = 4
            elif condition == "cancer":
                user_details[condition] = 3.5
        else:
            user_details[condition] = 0
            
    
    #updating raw_score to gender
    sex = user_details["gender"].lower()
    if sex == "male":
        user_details["gender"] = 5.5
    elif sex == "female":
        user_details["gender"] = 4.5
    
    #updating raw_score to age
    age = user_details["age"]
    if age >= 75:
        user_details["age"] = 6
    elif(age>=65 and age<=74):
        user_details["age"] = 5.5
    elif(age>=45 and age<=64):
        user_details["age"] = 5
    elif(age>=18 and age<=44):
        user_details["age"] = 4
    elif(age>=1 and age<=17):
        user_details["age"] = 3
    
    #updating heart_rate value
    rate_sum = 0
    rate_count = 0
    for ht_rate in user_details["heart_rate"]:
        rate_sum += ht_rate['heartrate']
        rate_count += 1
    avg_rate = rate_sum/rate_count
    if(avg_rate >= 130 or avg_rate <= 50):
        user_details["heart_rate"] = 3
    elif((avg_rate >= 50 or avg_rate <= 60) or
         (avg_rate >= 120 or avg_rate <= 130)):
        user_details["heart_rate"] = 2
    elif((avg_rate >= 60 or avg_rate <= 65) or
         (avg_rate >= 110 or avg_rate <= 120)):
        user_details["heart_rate"] = 1     
    elif(avg_rate >= 65 or avg_rate <= 110):
        user_details["heart_rate"] = 0
    
    risk_value = 0
    weight = 0
    for symptom in symptoms_list:
        if symptom in weights.keys():
            weight = weights[symptom]
        elif symptom in pre_existing:
            #pre-existing weights
            weight = 0.2
        risk_value += (user_details[symptom]*weight)
        
    return (risk_value*10)


def load_data(user_details):
    for k2 in jsonData["heart_rate"]:
        for k,v in jsonData["heart_rate"]:
            # sql = "INSERT INTO Heartrate VALUES (jsonData['userid'],k2['heartrate'],k2['timestamp'])"
            sql = "INSERT INTO Heartrate VALUES (?,?,?)"
            stmt = ibm_db.prepare(db2conn, sql )
            # print(type(jsonData['userid']))
            ibm_db.bind_param(sql, 1, str(jsonData['userid']))
            ibm_db.bind_param(sql, 2, str(k2['heartrate']))
            ibm_db.bind_param(sql, 3, str(k2['timestamp']))
            sibm_db.execute(stmt)


            # stmt =ibm_db.exec_immediate(ibmDB, sql)
            
    risk_percentageVal= risk_calcuation(jsonData)
    sql = "INSERT INTO PATIENTS (userid,firstname,lastname,dob,gender,lung_issues,hypertension,heartdisease,hiv,diabetes,cancer,age,fever,drycough,fatigue,trouble_breathing,muscle_pain,sore_throat,heart_rate,headache,runnynose,diarrhea,zipcode,latitude,longitude,risk_percentage,bloodtype) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    stmt = ibm_db.prepare(ibmDB, sql )
            # print(type(jsonData['userid']))
    ibm_db.bind_param(sql, 1, str(jsonData['userid']))
    ibm_db.bind_param(sql, 2,  str(jsonData['firstname']))
    ibm_db.bind_param(sql, 3, str(jsonData['lastname']))
    ibm_db.bind_param(sql, 4,  str(jsonData['dob']))
    ibm_db.bind_param(sql, 5,  str(jsonData['gender']))
    ibm_db.bind_param(sql, 6,  str(jsonData['lung_issues']))
    ibm_db.bind_param(sql, 7,  str(jsonData['hypertension']))
    ibm_db.bind_param(sql, 8,  str(jsonData['heartdisease']))
    ibm_db.bind_param(sql, 9,  str(jsonData['hiv']))
    ibm_db.bind_param(sql, 10,  (jsonData['diabetes']))
    ibm_db.bind_param(sql, 11,  str(jsonData['cancer']))
    ibm_db.bind_param(sql, 12,  str(jsonData['age']))
    ibm_db.bind_param(sql, 13,  str(jsonData['fever']))
    ibm_db.bind_param(sql, 14,  str(jsonData['drycough']))
    ibm_db.bind_param(sql, 15,  str(jsonData['fatigue']))
    ibm_db.bind_param(sql, 16,  str(jsonData['trouble_breathing']))
    ibm_db.bind_param(sql, 17,  str(jsonData['muscle_pain']))
    ibm_db.bind_param(sql, 18,  str(jsonData['sore_throat']))
    ibm_db.bind_param(sql, 19,  null,str(jsonData['headache']))
    ibm_db.bind_param(sql, 20,  str(jsonData['runnynose']))
    ibm_db.bind_param(sql, 21,  str(jsonData['diarrhea']))
    ibm_db.bind_param(sql, 22,  str(jsonData['zipcode']))
    ibm_db.bind_param(sql, 23,  str(jsonData['latitude']))
    ibm_db.bind_param(sql, 24,  str(jsonData['longitude']))
    ibm_db.bind_param(sql, 25,  risk_percentageVal)
    ibm_db.bind_param(sql, 26,  str(jsonData['bloodtype']))      
    
    sibm_db.execute(stmt)
    # stmt =ibm_db.exec_immediate(ibmDB, sql)


@atexit.register
def shutdown():
    if client:
        client.disconnect()

if __name__ == '__main__':
    application.run(host='127.0.0.1', port=8000, debug=True)


# @application.route('/uploadData')
# def uploadData():
#     return render_template("uploadData.html")

# #THIS LOADS FILE (LOCALLY) INTO DATABASE
# def _get_col_datatypes(fin):
#     dr = csv.DictReader(fin) # comma is default delimiter
#     fieldTypes = {}
#     for entry in dr:
#         feildslLeft = [f for f in dr.fieldnames if f not in fieldTypes.keys()]
#         if not feildslLeft: break # We're done
#         for field in feildslLeft:
#             data = entry[field]
#             # Need data to decide
#             if len(data) == 0:
#                 continue
#             if data.isdigit():
#                 fieldTypes[field] = "INTEGER"
#             else:
#                 fieldTypes[field] = "TEXT"
#         # Currently there's no support for DATE in sqllite

#     if len(feildslLeft) > 0:
#         raise Exception("Failed to find all the columns data types - Maybe some are empty?")

#     return fieldTypes
	
	
# def escapingGenerator(f):
#     for line in f:
#         yield line.encode("ascii", "xmlcharrefreplace").decode("ascii")
		
		
# def csvToDb(csvFile, outputToFile = False):
#     # implement output to file

#     with open(csvFile,mode='r', encoding="ISO-8859-1") as fin:
#         dt = _get_col_datatypes(fin)

#         fin.seek(0)

#         reader = csv.DictReader(fin)

#         # To keep the order of the columns name just as in the CSV
#         fields = reader.fieldnames
#         cols = []

#         # Setting field and type
#         for f in fields:
#             cols.append("%s %s" % (f, dt[f]))

#         cur = mysql.connection.cursor()
#         #create table statement:
#         stmt = "CREATE TABLE if not exists quakeData (%s)" % ",".join(cols)
#         cur.execute(stmt)

#         fin.seek(0)

#         reader = csv.DictReader(fin,fieldnames = ("time","latitude","longitude","depth","locationSource","magSource"))
#         #cur = con.cursor()
#         cur = mysql.connection.cursor()
#         next(reader,None)

#         for row in reader:
#             time = dateutil.parser.parse(row['time'])            
#             #time= get_timezone_date(row['longitude'],row['latitude'], mytime.strftime("%Y-%m-%d %H:%M:%S.%f"))
#             latitude = row['latitude'] if row['latitude'] else float (0)
#             longitude = row['longitude'] if row['longitude'] else float (0)
#             depth= row['depth'] if row['depth'] else float (0)
#             locationSource=row['locationSource'] if row['locationSource'] else ''
#             magSource=row['magSource'] if row['magSource'] else ''

#             cur = mysql.connection.cursor()           

#             cur.execute('INSERT INTO quakeData (time,latitude,longitude,depth,locationSource,magSource) VALUES (%s,%s,%s,%s,%s,%s)',(str(time),str(latitude),str(longitude),str(depth),status,locationSource,magSource))
#             mysql.connection.commit()

#     return "File has been uploaded!"


# # METHOD TO UPLOAD THE FILE
# @application.route("/upload", methods=['POST'])
# def upload():	

# 	files = request.files['data_file']
		
# 	files.save(os.path.join('static', files.filename))
# 	msg = csvToDb(os.path.join('static', files.filename))
			
# 	return render_template('display.html', msgRet=msg)


	
# #METHOD FOR QUERY 2
# @application.route("/display", methods=['POST'])
# def display():    
#     # #SQLITE Connection
#     # con = sqlite3.connect('earth.db')
#     # cur = con.cursor()
#     cur = mysql.connection.cursor()

#     mag1=request.form['mag1']
#     mag2=request.form['mag2']
#     startDate=request.form['startDate']
#     endDate=request.form['endDate']
    
#     stmt="SELECT time,mag,place,locationSource FROM quakeData WHERE mag>= %s AND mag<= %s AND date(time)>= %s AND date(time)<= %s"
#     cur.execute(stmt,(mag1,mag2,startDate,endDate,))
    
#     return render_template('displayData.html', result_set = cur.fetchall() )


	
# @application.route("/calculateRisk", methods=['POST'])
# def calculateRisk():    
#     # #SQLITE Connection
#     # con = sqlite3.connect('earth.db')
#     # cur = con.cursor()
#     cur = mysql.connection.cursor()

#     # mysql.connection.create_function("findacos", 1, findacos)
#     # mysql.connection.create_function("findsine", 1, findsine)
#     # mysql.connection.create_function("findcosine", 1, findcosine)
	
#     latDeg=float(request.form['lat'])
#     lonDeg=float(request.form['lon'])
#     dist=float(request.form['dist'])

#     R=6370
#     r= dist/R
#     lat = math.radians(latDeg)
#     lon = math.radians(lonDeg) 
    
#     #(lat,lon) in radians
#     lat_min = math.degrees(lat-r)
#     lat_max = math.degrees(lat+r)

#     del_lon= math.asin(math.sin(r)/math.cos(lat))

#     latT = math.asin(math.sin(lat)/math.cos(r)) 

#     lon_min = math.degrees(lon - del_lon)
#     lon_max = math.degrees(lon + del_lon)
    
#     #stmt= "SELECT time,mag,place,locationSource FROM quakeData WHERE (latitude >= %s AND latitude <= %s) AND ((longitude >= %s AND longitude <= %s) OR (longitude*(-1) >= %s AND longitude*(-1) <= %s )) AND findacos(findsine(%s) * findsine(latitude) + findcosine(%s) * findcosine(latitude) * findcosine(longitude - (%s))) <= %s"

#     #cur.execute(stmt,(lat_min,lat_max,lon_min,lon_max,lon_min,lon_max,lat,lat,lon,r,))

#     stmt= "SELECT time,mag,place,locationSource FROM quakeData WHERE (latitude >= %s AND latitude <= %s) AND ((longitude >= %s AND longitude <= %s) OR (longitude*(-1) >= %s AND longitude*(-1) <= %s )) "

#     cur.execute(stmt,(lat_min,lat_max,lon_min,lon_max,lon_min,lon_max,))

#     return render_template('displayData.html', result_set2 = cur.fetchall() )
