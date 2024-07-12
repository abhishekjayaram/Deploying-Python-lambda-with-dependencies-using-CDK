#!/usr/bin/env python3
import os
import aws_cdk as cdk
from py_stack.py_stack import PyStack

app = cdk.App()

PyStack(app, "PyStack",
    env=cdk.Environment(
        account=os.getenv('CDK_DEFAULT_ACCOUNT'), 
        region=os.getenv('CDK_DEFAULT_REGION')
    )
)

app.synth()
