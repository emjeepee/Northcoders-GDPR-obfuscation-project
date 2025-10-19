terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 5.0"
          }
                     }


# Provision the S3 bucket that will
# contain Terraform state file.backend 
# (the 'x4bj13pa' in the bucket name 
# is a random 8-char substring to
# ensure name is unique worldwide
# within an AWS partition -- all 
# buckets in this project are 
# named this way):
  backend "s3" {
  bucket = "gdpr-obfus-state-bucket-x4bj13pa"
    key = "terraform/state.tfstate"
    region = "eu-west-2"
               }
         }


provider "aws" {
  region = "eu-west-2"
               }




# THE S3 BUCKETS, ETC
# ===================
# The bucket that will contain the
# code for the lambda handler:
resource "aws_s3_bucket" "code_bucket" {
  bucket = "gdpr-obfus-code-bucket-a1z3qs9n"

                                       }               

# The Bucket that will contain the
# .csv file of data that this project will 
# obfuscate:
resource "aws_s3_bucket" "ingestion_bucket" {
  bucket = "gdpr-obfus-my-ingestion-bucket-ga47fmw2"
  force_destroy = true # NOTE: AWS prevents non-empty buckets
                       # from being deleted, so if in the 
                       # command line you run terraform destroy, 
                       # then without this line you won't be 
                       # able to destroy this bucket if it 
                       # contains something 
                                            }                                                      


# Upload the csv file (that has no obfuscated data 
# in it) to the correct bucket:
resource "aws_s3_object" "csv_file" {
  # bucket = "gdpr-obfus-my-ingestion-bucket-ga47fmw2"
  bucket = aws_s3_bucket.ingestion_bucket.bucket
  key    = "new_data/file1.csv"       # fake folder / name of the file
  source = "${path.module}/file1.csv" # path to the file.
                                      # ${path.module} means 
                                      # the same directory as the 
                                      # current .tf file.    
                                      }




# THE LAMBDA FUNCTION
# ===================
resource "aws_lambda_function" "test1_lambda" {
  function_name = "gdpr-obfus-test1" # The name of the Lambda in AWS. 
                                     # It appears in the AWS console, 
                                     # the ARN and when you call it 
                                     # from other AWS services.
  role          = aws_iam_role.lambda_exec.arn
  runtime       = "python3.12"
  handler       = "lambda_handler.lambda_handler" # format is <filename>.<function_name>
  s3_bucket     = aws_s3_bucket.code_bucket.bucket # the code bucket 
  # s3_key        = "lambda_builds/lambda_code.zip" # site of zipped code
  s3_key        = aws_s3_object.first_lambda_zip.key

  timeout       = 30  # (optional) seconds before Lambda times out
  memory_size   = 128 # (optional) MB of memory. This is the minumum AWS allows 
                                              }



# IAM EXECUTION ROLE OF LAMBDA
# ============================
# NOTE: "lambda_exec" below cannot
# be dynamic, ie you cannot include 
# a variable value in that string!! 
# Instead use count or for each):
resource "aws_iam_role" "lambda_exec" {
  name = "gdpr-obfus-test1-IAM-exec-role"

# Define the trust policy to allow 
# lambda functions to assume this 
# role (could also be standalone 
# instead of inline):
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Principal = { Service = "lambda.amazonaws.com" },
      Action    = "sts:AssumeRole"
    }]
  })
                                      }

  

# POLICY TO LET THE LAMBDA
# READ FROM A SPECIFIC S3
# ========================
resource "aws_iam_policy" "lambda_get_policy" {
  name   = "gdpr-obfus-test1-read-S3-policy" # AWS name
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect   = "Allow",
      Action   = ["s3:GetObject"],
      Resource = "arn:aws:s3:::gdpr-obfus-my-ingestion-bucket-ga47fmw2/*" # '*' means all objects 
                                                                          # in the ingestion bucket.
    # Remember that gdpr-obfus-my-ingestion-bucket-ga47fmw2 is the AWS name (NOT the Terraform name)                                                                          
    }]
  })                                      
}



# ATTACHMENT TO ATTACH THE 
# POLICY ABOVE TO THE LAMBDA 
# EXECUTION ROLE
# ==========================
resource "aws_iam_role_policy_attachment" "lambda_get_attach" {
  role       = aws_iam_role.lambda_exec.name 
  policy_arn = aws_iam_policy.lambda_get_policy.arn
                                                              }



# POLICY TO LET CODE BUCKET BE 
# READ BY THE AWS LAMBDA SERVICE 
# =============================
resource "aws_s3_bucket_policy" "AWS_lambda_SERVICE_access" {
  bucket = aws_s3_bucket.code_bucket.id

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Sid: "AllowLambdaServiceToReadCode",
        Effect: "Allow",
        Principal: {
          Service: "lambda.amazonaws.com"
        },
        Action: [
          "s3:GetObject"
        ],
        Resource: "${aws_s3_bucket.code_bucket.arn}/*"
      }
    ]
  })
}                                                              



# LOAD THE ZIPPED LAMBDA FUNCTION 
# HANDLER INTO THE CODE BUCKET
#================================

# zipped handler for the Lambda function: 
resource "aws_s3_object" "first_lambda_zip" {
  bucket = "gdpr-obfus-code-bucket-a1z3qs9n"
  key    = "zipped/lambda_deploy.zip"
  source = "../zipped_files/lambda_deploy.zip" # must be relative to terraform dir
                                            }




