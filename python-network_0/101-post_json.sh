#!/bin/bash
# Sends a JSON POST request to a URL using the contents of a file and displays the body
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
