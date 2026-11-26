#!/bin/bash
# Displays all HTTP methods the server at the URL will accept
curl -sI -X OPTIONS "$1" | grep "Allow" | cut -d " " -f 2- | tr -d '\r'
