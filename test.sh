#!/usr/bin/env bash

vagrant up --destroy-on-error
python test-templates.py
python update-build-icon.py
vagrant destroy -f