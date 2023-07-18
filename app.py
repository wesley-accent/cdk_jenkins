#!/usr/bin/env python3

import aws_cdk as cdk

from jenkinscdk.jenkinscdk_stack import JenkinscdkStack


app = cdk.App()
JenkinscdkStack(app, "jenkinscdk")

app.synth()
