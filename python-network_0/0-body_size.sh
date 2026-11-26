#!/bin/bash
# Displays the size of the body of the response from the URL given as argument
curl -s "$1" | wc -c
