# VesselWatch - Unlocking Insights from Maritime Data

## Table of Contents
- [Project Description](#project-description)
- [Technical Specifications](#technical-specifications)
- [Working with the Code](#working-with-the-code)
- [Future Plans](#future-plans)
- [Queries and Related Components](#queries-and-related-components)
- [Files and Their Roles](#files-and-their-roles)

## Project Description

VesselWatch empowers users to extract valuable insights from maritime data, including risk assessments and vessel activities. By leveraging GraphQL queries and robust security measures, the system facilitates efficient monitoring and analysis of vessel-related information.

## Technical Specifications

### Backend Development
- **Python**: The backbone of the backend development.
- **Requests Library**: Powering seamless HTTP requests to the GraphQL endpoint.
- **GraphQLClient**: Custom-built for smooth interaction with GraphQL endpoint.
- **Asyncio**: Fueling high-performance asynchronous programming.
- **Tokenization**: Ensuring secure authentication and access control.
- **Logging**: Keeping track of crucial events and errors for monitoring and debugging.
- **Datetime**: Managing date and time data efficiently.
- **JSON**: Serialization and deserialization of data in JSON format.
- **Environment Variables**: Safely storing sensitive information for enhanced security.

### Code Structure
- **Query Class**: Contains methods for sending requests to the GraphQL endpoint, including `convert_to_iso_format`, `check_risk`, and `activities`.
- **GraphQLClient Class**: A custom-built class for managing GraphQL requests, including token management, request timing, and logging.

## Working with the Code

To work with the VesselWatch code, you'll need to set up your development environment with Python and ensure you have the necessary libraries installed. Familiarize yourself with the structure of the project, particularly the `Query` class and its methods, to understand how data is fetched and processed.

## Future Plans

Looking ahead, the integration with LLM (Language Model) frameworks, such as Instructor, is planned to democratize access to maritime data. By simplifying data retrieval processes, VesselWatch aims to make vessel monitoring more accessible to a wider audience, thereby promoting safer and more efficient maritime operations.

## Queries and Related Components

The VesselWatch project is structured around several key files that work together to facilitate its operation:

- **main.py**: This is the main business model file where the core logic of the application resides. It orchestrates the flow of data through the system, including fetching and processing data from the GraphQL endpoint.

- **tokenizer.py**: This file is responsible for renewing tokens. It contains the `GraphQLClient` class, which manages the authentication process with the GraphQL endpoint, ensuring that requests are made securely and that tokens are refreshed as needed.

- **queries.py**: This file holds the query strings used to interact with the GraphQL endpoint. It includes functions like `risk_assessment_query_string()` and `activities_query_string()`, which return the query strings for fetching risk assessments and vessel activities. These queries are constructed to retrieve specific data from the GraphQL API, tailored to the needs of the VesselWatch application.

## Files and Their Roles

The VesselWatch project is structured around several key files that work together to facilitate its operation:

- **main.py**: This is the main business model file where the core logic of the application resides. It orchestrates the flow of data through the system, including fetching and processing data from the GraphQL endpoint.

- **tokenizer.py**: This file is responsible for renewing tokens. It contains the `GraphQLClient` class, which manages the authentication process with the GraphQL endpoint, ensuring that requests are made securely and that tokens are refreshed as needed.

- **queries.py**: This file holds the query strings used to interact with the GraphQL endpoint. It includes functions like `risk_assessment_query_string()` and `activities_query_string()`, which return the query strings for fetching risk assessments and vessel activities. These queries are constructed to retrieve specific data from the GraphQL API, tailored to the needs of the application.

 Each of these components plays a crucial role in the operation.

 Each of these components plays a crucial role in the operation. Each of these components plays a crucial role in the operation. Each of these components plays a crucial role in the operation. Each of these components plays a crucial role in the operation. Each of these components plays a crucial role in the operation.Components play a crucial role in the operation. Each of these components plays a crucial role in the operation..swing a crucial role in the operation..swing a crucial role in the operation..swing a crucial role in the operation.Components play a crucial role in the operation.Components play a crucial role in the operation.The Vessel play a crucial role in the operation.Components play a crucial role in the operation. Each of these components play a crucial role in the operation..swing a crucial role in the operation. Each of these components play a crucial role in the operation.```


