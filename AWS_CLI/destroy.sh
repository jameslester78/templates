#!/bin/bash

username=test-user
groupname=test-group


echo "remove $username to $groupname"

aws iam remove-user-from-group --user-name $username --group-name $groupname

echo "deleting $username"

aws iam delete-user --user-name $username

echo "detaching policies"

aws iam detach-group-policy --group-name $groupname  --policy-arn arn:aws:iam::999:policy/policy1
aws iam detach-group-policy --group-name $groupname  --policy-arn arn:aws:iam::999:policy/policy2

echo "deleting $groupname"

aws iam delete-group --group-name $groupname

echo "deleting policy"

aws iam delete-policy --policy-arn arn:aws:iam::999:policy/policy1
aws iam delete-policy --policy-arn arn:aws:iam::999:policy/policy2