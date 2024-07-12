from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from typing import Sequence
from aws_cdk.aws_apigatewayv2 import HttpApi
from aws_cdk.aws_lambda import Function, Runtime, Code, AssetCode
from aws_cdk.aws_lambda_python_alpha import PythonFunction, BundlingOptions
from constructs import Construct
import os
from pathlib import Path
import shutil

assetFolderPrefix = 'assets'

def buildAsset(folder_name, PY_EXECUTABLE) -> AssetCode:
    assetFolder = f'{assetFolderPrefix}/{folder_name}'
    folder = Path(assetFolderPrefix)
    folder.mkdir(parents=True, exist_ok=True)
    shutil.copytree(folder_name, assetFolder, dirs_exist_ok=True)
    return Code.from_custom_command(
                output= assetFolder,
                command=[PY_EXECUTABLE, '-m' ,'pip', 'install', '-r', f'{assetFolder}/requirements.txt', '--target', assetFolder],
                exclude= ['requirements.txt']
            )

def pyExecutable() -> str:
    if os.name == 'nt':
        return "python"
    else:
        return "python3"

PY_EXECUTABLE = pyExecutable()

class PyStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        directory = Path('assets')
        if directory.exists() and directory.is_dir():
            shutil.rmtree(directory)

        pyfunc = Function(
            self, 
            'pyfuncbundle',
            handler='index.handler',
            runtime= Runtime.PYTHON_3_10,
            code= buildAsset('src', PY_EXECUTABLE)
        )