#!/bin/bash
# Cria a role
aws iam create-role --role-name live-de-python --assume-role-policy-document file://policy.json

# 634468032295

# Cria ativa a policy
aws iam attach-role-policy \
    --role-name live-de-python \
    --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

# Criar zip
zip function.zip function.py

# Cria o lambda
aws lambda create-function \
    --function-name livedepython02 \
    --zip-file fileb://function.zip \
    --handler functio.lambda_handler \
    --runtime python3.8 \
    --role arn:aws:iam::634468032295:role/live-de-python

arn:aws:lambda:us-east-2:634468032295:function:livedepython02

# Criar API
aws apigateway create-rest-api --name 'Live de Python API'

# Listar endpoints
aws apigateway get-resources --rest-api-id vaz7da96z6

# Criar recurso
aws apigateway put-method --rest-api-id vaz7da96z6 --resource-id recurso --http-method GET --authorization-type NONE

# Lincar com o lambda
aws apigateway put-integration --rest-api-id vaz7da96z6 --resource-id cecurso
    --http-method POST --type AWS\
    --integration-http-method GET \
    --uri arn:aws:lambda:us-east-2:634468032295:function:my-function
