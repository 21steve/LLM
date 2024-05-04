# VesselWatch - Unlocking Insights from Maritime Data

## Table of Contents
- [Project Description](#project-description)
- [Technical Specifications](#technical-specifications)
- [Working with the Code](#working-with-the-code)
- [Usage](#usage)

## Project Description

VesselWatch empowers users to extract valuable insights from maritime data, including risk assessments and vessel activities. By leveraging GraphQL queries and robust security measures, the system facilitates efficient monitoring and analysis of vessel-related information.

## Tech used

- **Python**: The backbone of the backend development.
- **Requests Library**: Powering seamless HTTP requests to the GraphQL endpoint.
- **GraphQLClient**: Custom-built for smooth interaction with GraphQL endpoint.
- **Asyncio**: Fueling high-performance asynchronous programming.
- **Tokenization**: Ensuring secure authentication and access control.
- **Logging**: Keeping track of crucial events and errors for monitoring and debugging.
- **Datetime**: Managing date and time data efficiently.
- **JSON**: Serialization and deserialization of data in JSON format.
- **Environment Variables**: Safely storing sensitive information for enhanced security.

## Technical Specifications

### Backend Development
- **Python**: The primary language used for backend development.
- **Requests Library**: Utilized for making HTTP requests to the GraphQL endpoint.
- **GraphQLClient**: A custom-built module for smooth interaction with the GraphQL endpoint.
- **Asyncio**: Employed for asynchronous programming, enabling high-performance operations.
- **Tokenization**: Implemented for secure authentication and access control.
- **Logging**: Integrated for tracking crucial events and errors.
- **Datetime**: Used for managing date and time data efficiently.
- **JSON**: Utilized for serialization and deserialization of data in JSON format.
- **Environment Variables**: Employed for safely storing sensitive information.

### Code Structure
- **Query Class**: Contains methods for sending requests to the GraphQL endpoint, including `convert_to_iso_format`, `check_risk`, and `activities`.

## Working with the Code

To work with the VesselWatch code, you'll need to set up your development environment with Python and ensure you have the necessary libraries installed. Familiarize yourself with the structure of the project, particularly the `Query` class and its methods, to understand how data is fetched and processed.

## Usage

To use VesselWatch, you need to initialize the `GraphQLClient` with your credentials and endpoint URL. Then, you can use the `Query` class to fetch risk assessments and vessel activities. Here's a brief example:

