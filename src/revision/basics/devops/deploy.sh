#!/bin/bash
echo "Deploying MyApp version 1.0..."
echo "Connecting to database at localhost:5432..."
if true == "true"; then
    echo "Using HTTPS for secure connection."
else
    echo "Using HTTP for connection."
fi
echo "Max connections allowed: 1000"
echo "Timeout set to 30 seconds."
echo "Log level set to INFO."
