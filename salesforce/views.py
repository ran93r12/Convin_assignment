from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import mysql.connector
from salesforce.models import Users_Table, Account_Table, Contact_Table

conn = mysql.connector.MySQLConnection(host='127.0.0.1',port='3306',
                                       database='salesforce',
                                       user='root',
                                       password='')


def home(request):
	return render(request,'home.html')




def sf_api_call(access_token,instance_url,action, parameters = {}, method = 'get', data = {}):
    """
    Helper function to make calls to Salesforce REST API.
    Parameters: action (the URL), URL params, method (get, post or patch), data for POST/PATCH.
    """
    headers = {
        'Content-type': 'application/json',
        'Accept-Encoding': 'gzip',
        'Authorization': 'Bearer %s' % access_token
    }
    if method == 'get':
        r = requests.request(method, instance_url+action, headers=headers, params=parameters, timeout=30)
    elif method in ['post', 'patch']:
        r = requests.request(method, instance_url+action, headers=headers, json=data, params=parameters, timeout=10)
    else:
        # other methods not implemented in this example
        raise ValueError('Method should be get or post or patch.')
    print('Debug: API %s call: %s' % (method, r.url) )
    if r.status_code < 300:
        if method=='patch':
            return None
        else:
            return r.json()
    else:
        raise Exception('API error when calling %s : %s' % (r.url, r.content))



def get_query(access_token,instance_url,conn):

	data_Users = json.dumps(sf_api_call(access_token,instance_url,'/services/data/v39.0/query/', {
		    'q': "SELECT Id, Name FROM User Where Name != ''"
		}), indent=2)
	data_Account = json.dumps(sf_api_call(access_token,instance_url,'/services/data/v39.0/query/', {
		    'q': "SELECT Id, Name FROM Account Where Name != ''"
		}), indent=2)
	data_Contact = json.dumps(sf_api_call(access_token,instance_url,'/services/data/v39.0/query/', {
		    'q': "SELECT Id, Name, Email FROM Contact "
		}), indent=2)
	User_dic = json.loads(data_Users)
	Account_dic = json.loads(data_Account)
	Contact_dic = json.loads(data_Contact)
	for record in User_dic['records']:
		cursor = conn.cursor()
		cursor.execute("""INSERT INTO Users_Table (id,Name) VALUES(%s,%s)""",(record['Id'],record['Name']))
		conn.commit()
	for record in Account_dic['records']:
		cursor = conn.cursor()
		cursor.execute("""INSERT INTO Account_Table (id,AccountHolderName) VALUES(%s,%s)""",(record['Id'],record['Name']))
		conn.commit()
	for record in Contact_dic['records']:
		cursor = conn.cursor()
		cursor.execute("""INSERT INTO Contact_Table (id,Name,Email) VALUES(%s,%s,%s)""",(record['Id'],record['Name'],record['Email']))
		conn.commit()



def display(request):
	Users = Users_Table.objects.all()
	Account = Account_Table.objects.all()
	Contact = Contact_Table.objects.all()
	return render(request, 'result.html',{'User_Table':Users,'Account_Table':Account,'Contact_Table':Contact})




def search(request):
	print("afdafdea")
	if request.method == 'GET':
		print("DOne1")
		if 'customsearch' in request.GET:
			print("1step DONE")
			Client_ID = request.GET.get('Consumer_ID')
			Client_Key = request.GET.get('Consumer_Key')
			Username = request.GET.get('username')
			Password = request.GET.get('password')
			params = {
			    "grant_type": "password",
			    "client_id": Client_ID, # Consumer Key
			    "client_secret":Client_Key, # Consumer Secret
			    "username": Username, # The email you use to login
			    "password": Password # Concat your password and your security token
			}
			oauth_url="https://login.salesforce.com/services/oauth2/token"
			r = requests.post(oauth_url,headers={"Content-Type":"application/x-www-form-urlencoded"}, params=params)
			access_token = r.json().get("access_token")
			instance_url = r.json().get("instance_url")
			print("Access Token:",'Bearer'+ access_token)
			print("Instance URL", instance_url)
		elif 'defaultsearch' in request.GET:
			params = {
			    "grant_type": "password",
			    "client_id": "xxxxxxxxx", # Consumer Key
			    "client_secret":"xxxxxxx", # Consumer Secret
			    "username": "xxxxxx", # The email you use to login
			    "password": "xxxxxxxxx" # Concat your password and your security token
			}
			oauth_url="https://login.salesforce.com/services/oauth2/token"
			r = requests.post(oauth_url,headers={"Content-Type":"application/x-www-form-urlencoded"}, params=params)
			access_token = r.json().get("access_token")
			instance_url = r.json().get("instance_url")
			print("Access Token:",'Bearer'+ access_token)
			print("Instance URL", instance_url)

	get_query(access_token,instance_url,conn)
	display()
	return 
	
 


