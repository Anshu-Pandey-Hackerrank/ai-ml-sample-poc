#!/bin/bash

sudo python3 -m venv venv
source venv/bin/activate

sudo pip install -r requirements.txt

sudo uvicorn app.main:app --reload
