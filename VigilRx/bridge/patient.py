import json
import os

from web3 import Web3

import errors


try:
    with open(os.path.join('build', 'Patient.abi'), 'r') as file:
        _PATIENT_ABI = json.load(file)
    with open(os.path.join('build', 'Patient.bin'), 'r') as file:
        _PATIENT_BIN = file.read()
except Exception as e:
    raise errors.NotCompiledException()


def view_history():
    pass


def add_permissioned():
    pass


def remove_permissioned():
    pass
