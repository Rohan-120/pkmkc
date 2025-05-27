#!/bin/bash

echo "Setting up environment"

python3 -m venv myenv

source ./myenv/bin/activate

pip install flask

echo "Environment setup is complete now run the app with :python3 app.py"
