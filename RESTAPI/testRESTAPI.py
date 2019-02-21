import unittest
import requests
import os, sys, time, datetime, json, random
import pdb
import requests
from requests.auth import HTTPBasicAuth
import json_tools



class FlaskRestApiTestCase(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://localhost:5000/todo/api/v1.0/tasks"
        self.basic_auth = HTTPBasicAuth('tester', 'flask')
        print '\nEnter setUp of %s\n' % self._testMethodName
        sys.stdout.flush()

    def tearDown(self):
        print "\nEnter tearDown of %s\n" % self._testMethodName


    def test00Tasklist(self):
        rest_url = self.base_url
        r = requests.get(rest_url,auth=self.basic_auth)

        target_result = {
 "tasks":
 [
    {
        'uri': u"http://localhost:5000/todo/api/v1.0/tasks/1",
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'uri': u"http://localhost:5000/todo/api/v1.0/tasks/2",
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]
}       
        real_result = r.json() 
        diff_result = json_tools.diff(target_result, real_result)
        self.assertEquals([], diff_result)


    def test10TaskSpecific(self):
        rest_url = self.base_url + "/2"
        r = requests.get(rest_url,auth=self.basic_auth)

        target_result =  {
"task": {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
}
         
        print r.content
        real_result = r.json()
        diff_result = json_tools.diff(target_result, real_result)
        self.assertEquals([], diff_result)

    def test20CreateTask(self):
        rest_url = self.base_url

        headers = {"Content-Type":"application/json"}

        data={"title":"Read a new Book"}
        
        r = requests.post(rest_url, headers=headers, json=data, auth=self.basic_auth)


        target_result = {
  "task": {
    "description": u"",
    "done": False,
    "id": 3,
    "title": u"Read a new Book"
  }
}

        print r.content
        real_result = r.json()
        diff_result = json_tools.diff(target_result, real_result)
        self.assertEquals([], diff_result)



    def test30UpdateTask(self):
       rest_url = self.base_url + "/2"
       headers = {"Content-Type":"application/json"}
       data ={"done":True}

       r = requests.put(rest_url, headers=headers, json=data, auth=self.basic_auth)

       target_result = {
  "task": {
    "description": u"Need to find a good Python tutorial on the web",
    "done": True,
    "id": 2,
    "title": u"Learn Python"
  }
}
       print r.content
       real_result = r.json()
       diff_result = json_tools.diff(target_result, real_result)
       self.assertEquals([], diff_result)

       data = {"done":False}
       r = requests.put(rest_url, headers=headers, json=data, auth=self.basic_auth)
 

    def test40DeleteTask(self):

        rest_url = self.base_url + "/3"

        r = requests.delete(rest_url, auth=self.basic_auth)

        target_result = {
  "result": True
}


        real_result = r.json()
        diff_result = json_tools.diff(target_result, real_result)
        self.assertEquals([], diff_result)

if __name__ == "__main__":
    unittest.main()

