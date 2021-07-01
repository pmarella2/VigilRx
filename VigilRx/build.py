import argparse
import json
import os
import time

import solc

# from bridge.registrar import new_registrar
# /home/user/Documents/reu/VigilRx/VigilRx 
# 

def clean() -> None:
    """Removes all files in the build directory.
    """
    files = os.listdir(os.path.join('build'))
    for file in files:
        os.remove(os.path.join('build', file))


def compile() -> None:
    """Compiles all Solidity contracts in the contracts directory.
    """
    if not os.path.exists('build'):
        os.mkdir(os.path.join('build'))

    standard_json = {
        'language': 'Solidity',
        'sources': {},
        'settings':
        {
            'outputSelection': {
                '*': {
                    '*': [
                        'metadata', 'evm.bytecode', 'evm.bytecode.sourceMap'
                    ]
                }
            }
        }
    }

    contracts = [f for f in os.listdir('contracts') if f.endswith('.sol')]
    for contract in contracts:
        with open(os.path.join('contracts', contract)) as file:
            source = file.read()
            standard_json['sources'][contract] = {'content': ''}
            standard_json['sources'][contract]['content'] = source

    compiled_sol = solc.compile_standard(standard_json)
    with open(os.path.join('build', 'contracts.json'), 'w') as file:
        json.dump(compiled_sol, file, indent=4)

    for contract in contracts:
        name = contract.replace('.sol', '')
        bytecode = compiled_sol['contracts'][contract][name]['evm']['bytecode']['object']
        abi = json.loads(compiled_sol['contracts'][contract][name]['metadata'])['output']['abi']

        with open(os.path.join('build', name + '.abi'), 'w') as file:
            json.dump(abi, file, indent=4)
        with open(os.path.join('build', name + '.bin'), 'w') as file:
            file.write(bytecode)


def run_ganache() -> None:
    """Runs the Ganache blockchain locally.
    """
    ganache_path = os.path.join('..', 'node_modules', '.bin', 'ganache-cli')
    os.system(f'gnome-terminal -- {ganache_path}')


def run_server() -> None:
    """Runs the VigilRx Django web server locally.
    """
    web_app_path = os.path.join('app', 'manage.py')
    os.system(f'gnome-terminal -- python3 {web_app_path} runserver')


def registrar() -> None:
    """Deploys a new registrar contract.
    """
    deploy_path = os.path.join('bridge', 'deploy.py')
    os.system(f'python {deploy_path}')


def deploy() -> None:
    """Deploys and runs the entire app.
    """
    compile()
    time.sleep(3)
    run_ganache()
    time.sleep(3)
    registrar()
    time.sleep(3)
    run_server()


if __name__ == '__main__':
    ACTIONS = {
        'clean': clean,
        'compile': compile,
        'ganache': run_ganache,
        'runserver': run_server,
        'registrar': registrar,
        'deploy': deploy,
    }

    argparser = argparse.ArgumentParser()
    argparser.add_argument('--action', choices=ACTIONS.keys(), required=True)
    args = argparser.parse_args()
    function = ACTIONS[args.action]
    function()
