#!/bin/bash
# Send a POST request with a few variables
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
