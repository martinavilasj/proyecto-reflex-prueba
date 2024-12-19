#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

cd $SCRIPT_DIR

source $SCRIPT_DIR/.venv/bin/activate

pip install --upgrade pip
pip install -r $SCRIPT_DIR/requirements.txt

reflex run
