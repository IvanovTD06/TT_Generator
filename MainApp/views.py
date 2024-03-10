from django.shortcuts import render, redirect

import psycopg2

from MainApp.forms import *

def main_page(request):
    return render(request, "Main page.html") 

def user_reg_page(request):
    user_reg_form = UserRegistration()
    
    return render(request, "Registration page.html", {"form": user_reg_form})

def user_reg_submit(request):
    if request.method == "POST":
        user_reg_form = UserRegistration(request.POST)
        if user_reg_form.is_valid():
            connection = create_connection("db", "student", "123456", "localhost", "5432")
            print(user_reg_form.cleaned_data.get(all))
            try:
                user_reg_form.save()
            except psycopg2.Error as psycopg2_err:
                print(psycopg2_err)
    return redirect("http://127.0.0.1:8000")
        
        

def authorisation(request):
    return redirect("/")





def create_connection(db_name, db_user, db_password, db_host, db_port):
        connection = None
        try:
            connection = psycopg2.connect(
                database=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
            )
            print("Connection to PostgreSQL DB successful")
        except psycopg2.Error as e:
            print(f"The error '{e}' occurred")
        return connection
def execute(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except psycopg2.Error as e:
        print(f"The error '{e}' occurred")
def reader(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except psycopg2.Error as e:
        print(f"The error '{e}' occurred")