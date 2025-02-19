# Serverless URL Shortener

This project demonstrates a simple URL shortening service built using AWS Lambda, API Gateway, DynamoDB, and S3 for static website hosting.  The infrastructure is provisioned and managed using Terraform.

## Table of Contents

- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [Implementation](#implementation)
- [Deployment](#deployment)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Screenshots (Optional)](#screenshots-optional)
- [Future Enhancements](#future-enhancements)
- [Author](#author)
- [License](#license)

## Project Overview

This project provides a user-friendly way to shorten long URLs. Users can submit a long URL through a simple web interface, and the application generates a shortened URL that redirects to the original link.  The backend logic is implemented using serverless functions (AWS Lambda), and the data is stored in a NoSQL database (DynamoDB).  The frontend is a static website hosted on S3.

## Architecture

The architecture consists of the following components:

1. **Frontend (Static Website):** Hosted on S3, provides a form for users to submit long URLs.  Uses JavaScript to interact with the API Gateway.

2. **Backend (API):**
   - API Gateway: Handles incoming requests and routes them to the Lambda function.
   - Lambda Function (Python): Generates short codes, stores mappings in DynamoDB, and returns shortened URLs.

3. **Data Store:** DynamoDB: Stores the short code and long URL mappings.

4. **Redirection:** Route 53 (or S3 redirect rule): Redirects users from the shortened URL to the original URL.  (Could also be a Lambda function if you want to get more advanced).

5. **Infrastructure as Code:** Terraform: Provisions and manages all AWS resources.

## Implementation

The project is implemented as follows:

1. **Frontend (S3):**  HTML, CSS, and JavaScript are used to create the user interface.
2. **Backend (Lambda & API Gateway):** Python is used for the Lambda function. API Gateway is configured to trigger the Lambda function on POST requests.
3. **Data Store (DynamoDB):** A DynamoDB table stores the short code and long URL mappings.
4. **Infrastructure as Code (Terraform):** Terraform scripts define and create all necessary AWS resources.

## Deployment

The deployment process involves the following steps:

1. **Terraform Deployment:**  Use Terraform to create the infrastructure: `terraform apply`
2. **Frontend Deployment:** Upload the static website files to the S3 bucket.

## Technologies Used

* **AWS:** S3, API Gateway, Lambda, DynamoDB, Route 53 (optional), IAM
* **Programming Languages:** Python (Lambda), JavaScript (Frontend)
* **Infrastructure as Code:** Terraform
* **Other:** HTML, CSS

## Getting Started

1. **Clone the repository:** `git clone https://github.com/your-username/serverless-url-shortener.git`
2. **Install Terraform:** Follow the instructions on the Terraform website.
3. **Configure AWS Credentials:** Set up your AWS credentials.
4. **Navigate to the Terraform directory:** `cd terraform`
5. **Initialize Terraform:** `terraform init`
6. **Plan the infrastructure:** `terraform plan`
7. **Apply the infrastructure:** `terraform apply`
8. **Configure S3:** Upload the frontend files to the created S3 bucket.
9. **Access the application:** The shortened URLs will be accessible via your domain name (if configured) or the S3 website endpoint.

## Screenshots (Optional)

(Include screenshots of the frontend and any relevant parts of the AWS console)

## Future Enhancements

* **Custom Domain:** Configure Route 53 for a custom domain.
* **URL Validation:** Add validation to the Lambda function.
* **Analytics:** Implement click tracking and analytics.
* **Error Handling:** Improve error handling in the Lambda function.
* **CI/CD:** Implement a CI/CD pipeline for automated deployments.

## Author

Your Name

## License

(Choose a license, e.g., MIT)