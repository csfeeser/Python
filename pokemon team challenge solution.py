#!/usr/bin/python3
import requests
import wget

# PLAYER 1 SOLUTION
def api_pull():
    while True:
        try:
            # Using the requests library, pull a Pokemon from the PokeAPI
            choice= input("What Pokemon would you like a picture of? ").lower()
            if choice == "":
                raise ValueError("Something bad done did happen!")
            poke_api = ('https://pokeapi.co/api/v2/pokemon/' + choice + '/')
            break
        except:
            print("That is not a valid Pokemon.")
    return poke_api


# PLAYER 2 SOLUTION
def json_conv(poke_api):
    json_object= requests.get(poke_api)
    json2python= json_object.json()
    return json2python


# PLAYER 3 SOLUTION
def api_slice(json2python):
    imagelink= json2python["sprites"]["front_default"]
    return imagelink


# PLAYER 4 SOLUTION
def wget_pic(imagelink):
    wget.download(imagelink, "/home/student/mycode/pokepic.png")


# THE FINAL TEST
def main():
    wget_pic(api_slice(json_conv(api_pull())))

main()
~       
