#!/bin/bash

for i in 9 10 11 12; do
    echo 3.$i
    pyenv local 3.$i
    python erros.py
done
