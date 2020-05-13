#! /bin/bash
coverage erase
coverage run --source=problemas -m unittest discover -s tests/
coverage report
coverage html
