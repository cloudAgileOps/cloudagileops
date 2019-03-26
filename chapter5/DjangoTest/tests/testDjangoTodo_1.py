# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class DjangoTODOListTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print "setupClass\n"        

    @classmethod
    def tearDownClass(cls):
        print "tearDownClass\n"


    def setUp(self):
        print "setUp"
    
    def login(self):
        print "login method has not implemented\n"

    def test01TaskList(self):
        self.fail("testTaskList has not implemented\n") 



    def test20UpdateTask(self):
        self.fail("testUpdateTask has not implemented\n") 


    def test30CreateTask(self):
        self.fail("testCreateTask has not implemented\n") 


    def test40DeleteTask(self):
        self.fail("testDeleteTask has not implemented\n")
   
    def tearDown(self):
        print "tearDown\n"

if __name__ == "__main__":
    unittest.main()
