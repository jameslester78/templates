#!/bin/bash

username=test-user
groupname=test-group

echo "creating $username"

aws iam create-user --user-name $username

echo "creating $groupname"

aws iam create-group --group-name $groupname

echo "add $username to $groupname"

aws iam add-user-to-group --user-name $username --group-name $groupname

echo "create policy - policy1 from policy1.txt"
aws iam create-policy --policy-name policy1 --policy-document file://policy1.txt

echo "create policy - policy2 from policy2.txt"
aws iam create-policy --policy-name policy2 --policy-document file://policy2.txt

aws iam attach-group-policy --group-name $groupname  --policy-arn arn:aws:iam::999:policy/policy1

aws iam attach-group-policy --group-name $groupname  --policy-arn arn:aws:iam::999:policy/policy2

aws iam create-access-key --user $username