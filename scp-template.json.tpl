{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "ec2:*",
      "Resource": "${resource_arn}",
      "Condition": {
        "StringNotLike": {
          "aws:PrincipalArn": "arn:aws:iam::${account_id}:role/${role_name}"
        }
      }
    }
  ]
}
