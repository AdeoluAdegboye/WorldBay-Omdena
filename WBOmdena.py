from modulefinder import Module
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import base64
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import json 
import time 
from streamlit_option_menu import option_menu
#from featuresel import feature_sel
#from process import process_x, process_y
#from classifiermodule import classifiers 
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle
from sklearn.tree import DecisionTreeClassifier
with open('Final_Final.pkl','rb') as f:
    clf = pickle.load(f)




st.set_page_config(layout="wide") 
# [theme]
base="light"
secondaryBackgroundColor="#ea1fca"
#<img src="https://i.im.ge/2022/06/15/rJfCpG.png" alt="rJfCpG.png" border="0">
#Logo in navbar

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #2F3D60; padding: 8px;">



  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  
	
  <img src="https://img.icons8.com/cute-clipart/64/undefined/instagram-new.png" style="margin-top:40px">
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#" style="margin-top:40px;">Connect on instagram <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://www.onhealth.com/content/1/breast_cancer" target="_blank" style="margin-top:40px;">Top Analytics Services</a>
      </li>
      <img src="https://img.icons8.com/fluency/48/undefined/twitter.png" style="margin-top:40px">
	  <li class="nav-item">
		<a class="nav-link" href="https://twitter.com/ThePinkCaravan" target="_blank" style="margin-top:40px;">Twitter</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

st.markdown("""
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)


# st.title("Welcome to Pathomed")

# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions -add more columns to the table
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

# MAIN 

def main():
	"""Credit Scoring System for WorldBay Technologies"""
	
	choice = option_menu(
			menu_title =None, 
			options = ["Home","Login","SignUp"], 
			icons = ["house", "books", "envelope"],
			menu_icon="cast", 
			default_index=0,
			orientation= "horizontal",
			)
	image = Image.open('worldbay logo.jpg')
	st.image(image, width = 100)
	st.title("Credit Scoring System for WorldBay Technologies")
			# st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		# st.subheader("Welcome")
		photo = Image.open('grocedy.jpg')
		st.image(photo, width = 1500)
		st.write('')

	elif choice == "Login":
		st.subheader(" User Login ")
		photo = Image.open('login1.png')
		st.image(photo, width = 250)
		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Logged In as {}".format(username))
				photo = Image.open('postlogin.jpg') 
				st.image(photo, width = 1600)
				task = st.selectbox("Task",["Select an option","Predict your Credit Score","Explore and gain Insights to Various Data","Explore and gain Insights to Various Data"])
				if task == "Select an option":
					st.write("You can choose to input customer data and derive a CLV, or visualize uploaded datasets")
				elif task == "Predict your Credit Score":
					st.title('Customer Lifetime Value is generated via a series of inputs below')
					st.subheader("Enter the list of Customer features")
					NI = st.number_input('No of Invoices')
					DSR = st.number_input('days_since_registration')
					f = st.number_input('frequency')
					r = st.number_input('recency')
					T = st.number_input('T')
					inc = st.number_input('income')
					rmod = st.number_input('recency_mod')
					fmod = st.number_input('freq_mod')
					ppp = st.number_input('prob_of_predicted_purchases_30d')
					pia = st.number_input('prob_is_active_30d')
					days = st.number_input('4. 91 - 180 days')
					mv = st.number_input('monetary_value')
					ce = st.number_input('cond_expected_avg_profit')					
					PT = st.number_input('Payment Terms_0')
					PT2 = st.number_input('Payment Terms_27')
					PT3 = st.number_input('Payment Terms_30')
					PT4 = st.number_input('Payment Terms_40')
					Age5 = st.number_input('Age in Days_5')
					Age4 = st.number_input('Age in Days_4')
					Age3 = st.number_input('Age in Days_3')
					Age2 = st.number_input('Age in Days_2')
					Age1 = st.number_input('Age in Days_1')
					ssc = st.number_input('Subscriptions.Subscription Status_cancelled')
					sse = st.number_input('Subscriptions.Subscription_Status_expired')
					ssl = st.number_input('Subscriptions.Subscription_Status_live')
					ssp = st.number_input('Subscriptions.Subscription_Status_paused')
					sp1 = st.number_input('Subscriptions.Period Active in Months_1')
					sp2 = st.number_input('Subscriptions.Period Active in Months_2')
					sp3 = st.number_input('Subscriptions.Period Active in Months_3')
					sp4 = st.number_input('Subscriptions.Period Active in Months_4')
					sp5 = st.number_input('Subscriptions.Period Active in Months_5')
					Dp5 = st.number_input('Days Past Due Date_5')
					Dp4 = st.number_input('Days Past Due Date_4')
					Dp3 = st.number_input('Days Past Due Date_3')
					Dp2 = st.number_input('Days Past Due Date_2')
					Dp1 = st.number_input("Days Past Due Date_1")
					
					if st.button('Predict'):
						result = clf.predict([[NI,DSR,f,r,T,inc,rmod,fmod,ppp,pia,days,mv,ce,PT,PT2,PT3, PT4, Age5, Age4, Age3, Age2, Age1,ssc, sse,ssl,ssp,sp1,sp2,sp3,sp4,sp5,Dp5,Dp4,Dp3,Dp2,Dp1]])
						st.write(result)
						st.write(" Model Predictive Composition")
						image = Image.open('modelsummary.png')
						st.image(image, width = 1150)
						# uploaded_file = st.file_uploader("Choose a file")
					
					
				elif task == "Explore and gain Insights to Various Data":
					st.header("DATA VISUALIZATIONS FOR INSIGHTS")	
					st.subheader("Pick Up and Delivery Tasks")
					st.write("Bar plot displaying the layout of tasks across several months from 2019 to 2022")
					image = Image.open('EDA bar plot.png')
					st.image(image, width = 1150)
					

					st.write("Monthly spread of pick up and delivery trips ")
					image = Image.open('MagMonthly.png')
					st.image(image, width = 1150)
					

					st.write("Monthly spread of pick up and delivery trips ")
					image = Image.open('MagMonthly.png')
					st.image(image, width = 1150)
					

					st.write("Trips spread across top branch locations")
					image = Image.open('branches.png')
					st.image(image, width = 1150)

					st.write("Top Agents responsible for most trips")
					image = Image.open('Agentsoverview.png')
					st.image(image, width = 1150)

					st.write("Most Frequent Amounts")
					image = Image.open('amounts.png')
					st.image(image, width = 1150)
					
					

				elif task == "View Log in history":
					st.subheader("User Profiles")
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
					st.dataframe(clean_db)
			else:
				st.warning("Incorrect Username/Password")

	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")





if __name__ == '__main__':
	main()
