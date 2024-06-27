# Chess Commentator Java Source

This directory contains the Java source code for the backend of the Chess Commentator application. The backend is a Spring Boot application that fetches popular chess games and their commentaries. It is deployed on AWS Lambda and uses API Gateway and DynamoDB to get the data.

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## Features

- **Fetch Popular Games**: Retrieve popular chess games and their commentaries.
- **AWS Integration**: Deployed on AWS Lambda with API Gateway and DynamoDB integration.
- **Spring Boot Application**: Built with Spring Boot for robust and scalable backend services.

## Architecture

The backend service is designed to be highly scalable and leverages several AWS services:

- **AWS Lambda**: For serverless computing.
- **API Gateway**: To expose RESTful APIs.
- **DynamoDB**: For data storage.

## Installation

### Prerequisites

- Java 11 or higher
- Maven
- AWS CLI (configured with appropriate permissions)

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/utkuaysev/ChessCommentator.git
    cd ChessCommentator/ChessCommentatorJavaSource
    ```

2. **Build the project**:
    ```bash
    mvn clean install
    ```

3. **AWS Configuration**:
    - Set the following configurations in your `application.properties` or `application.yml`:

      ```properties
      spring.application.name=ChessCommentator
      aws.auth.accessKeyId=<access_key>
      aws.auth.secretAccessKey=<secret_access_key>
      aws.auth.region=<region>
      spring.cloud.function.scan.packages=com.chesscommentary.awslambda
      ```

    - Replace `<access_key>`, `<secret_access_key>`, and `<region>` with your AWS credentials and region.

4. **Deploy to AWS**:
    - Package the Spring Boot application for deployment:
      ```bash
      mvn package
      ```
    - Deploy the packaged application to AWS Lambda using AWS CLI or through the AWS Management Console.

## Usage

1. **API Gateway Endpoints**:
    - Use the endpoints provided by API Gateway to interact with the backend service.

2. **Fetch Popular Games**:
    - Make a GET request to the appropriate API Gateway endpoint to fetch popular chess games and their commentaries.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please reach out to:

- Utku Aysev
- [GitHub Profile](https://github.com/utkuaysev)
