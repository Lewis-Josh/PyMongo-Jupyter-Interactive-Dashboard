Project Overview:
This project provides a modular implementation of CRUD operations for MongoDB. It leverages PyMongo and Jupyter Notebook/Dashboard to facilitate the creation, reading, updating, and deletion of documents within a database collection. The CRUD module is designed to be easily adaptable and implemented within other applications.

Key Features:
Modular Design: All methods are contained within the AnimalShelter class. Import and create an instance of this class within your application to access these methods.
Adaptable: This module can be modified to suit a variety of databasing needs for MongoDB.
JSON Input: Inputs can be passed in JSON format, allowing for specific or generic retrieval or modification of database documents from other web sources.

Data Visualization:
The client, Grazioso Salvare, had specific requests for data visualization in the dashboard. End users needed to be able to filter and sort information, as well as view graphs and a map widget. The Grazioso Dashboard is a simple implementation of these requests. Using Jupyter Dash, the data retrieved from the CRUD module is passed to a dataframe which then generates a sortable, user-interactive table. Filters are auto-generated based on the keys from the documents. Interacting and filtering the data will also update the map/graph widgets.

Testing and Confirmation:
Included is a Jupyter Notebook testing script that demonstrates the implementations of the various methods, data that can be passed, and parameters. Additionally, within the testing script is an implementation of a confirmation method that can be used to prevent unintentional modifications to the database.

Logging:
The CRUD module comes with logging implementation to assist in development and testing.

Future Considerations:
The approach to this project differed from other projects with the addition of the data visualization widgets using HTML. These strategies are essential to future projects as companies such as Grazioso Salvare rely on data and information to effectively make decisions and plan for the future. Having data displayed that is easily searchable, sortable, and able to be filtered is invaluable to companies. Additionally, having widgets for visualization allows for a faster, deeper understanding of the data set as a whole.

As a computer scientist, my goal is to address the clients’ specific needs, and provide them a solution to their problem using methods that are easily adaptable, scalable, and reusable, while considering technical performance, data security, and ease of interaction with the end user.
