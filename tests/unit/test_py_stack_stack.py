import aws_cdk as core
import aws_cdk.assertions as assertions

from py_stack.py_stack_stack import PyStackStack

# example tests. To run these tests, uncomment this file along with the example
# resource in py_stack/py_stack_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PyStackStack(app, "py-stack")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
