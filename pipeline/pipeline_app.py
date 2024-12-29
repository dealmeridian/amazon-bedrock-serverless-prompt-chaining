import os

from aws_cdk import (
    App,
    Environment,
)
from pipeline_stack import PipelineStack

app = App()
env = Environment(account=os.environ["CDK_DEFAULT_ACCOUNT"], region="us-east-1")
PipelineStack(app, "PromptChainingPipeline", env=env)
app.synth()
