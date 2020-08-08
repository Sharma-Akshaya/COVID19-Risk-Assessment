import db2
import json
import ibm_db
import ibm_db_dbi
#connecting to db
ibmDB= ibm_db.connect("DATABASE=BLUDB;HOSTNAME=dashdb-txn-sbox-yp-dal09-11.services.dal.bluemix.net;PORT=50001;PROTOCOL=TCPIP;UID=kpg48221;PWD=s8lg350w5wv+jbdh;Security=SSL;","ssljdbcurl","")
#curser= ibmDB.cursor()
conn = ibm_db_dbi.Connection(ibmDB)

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
            sql = "INSERT INTO Heartrates VALUES (jsonData['userid'],k2['heartrate'],k2['timestamp'])"
            stmt =ibm_db.exec_immediate(ibmDB, sql)
            
    risk_percentageVal= risk_calcuation(jsonData)
    sql = "INSERT INTO PATIENTS (userid,firstname,lastname,dob,gender,lung_issues,hypertension,heartdisease,hiv,diabetes,cancer,age,fever,drycough,fatigue,trouble_breathing,muscle_pain,sore_throat,heart_rate,headache,runnynose,diarrhea,zipcode,latitude,longitude,risk_percentage,bloodtype) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(str(jsonData['userid']),str(jsonData['firstname']),str(jsonData['lastname']),str(jsonData['dob']),str(jsonData['gender']),str(jsonData['lung_issues']),str(jsonData['hypertension']),str(jsonData['heartdisease']),str(jsonData['hiv']),str(jsonData['diabetes']),str(jsonData['cancer']),str(jsonData['age']),str(jsonData['fever']),str(jsonData['drycough']),str(jsonData['fatigue']),str(jsonData['trouble_breathing']),str(jsonData['muscle_pain']),str(jsonData['sore_throat']),null,str(jsonData['headache']),str(jsonData['runnynose']),str(jsonData['diarrhea']),str(jsonData['zipcode']),str(jsonData['latitude']),str(jsonData['longitude']),risk_percentageVal,str(jsonData['bloodtype']))
    stmt =ibm_db.exec_immediate(ibmDB, sql)