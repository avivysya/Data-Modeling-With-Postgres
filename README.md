Data Modeling Project
This is my solution for the first project in the Data Engineering Nanodegree at Udacity . The goal was to design a star schema data warehouse and implement ETL processes for a music streaming startup.

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. The following steps are tested only for Ubuntu 18.04.

Docker
This project comes with a docker container with PostgreSQL and the necessary user (student) and database (studentdb). To get the container up and running, please execute:

docker-compose up
Virtual Environment
All necessary packages are listed in the requirements.txt file and can be installed by executing:

bin/setup
Running the ETL Process
To create and populate the database, execute the following commands:

source env/bin/activate   # activate the virtual environment
cd data_modeling          # move into the source folder
python create_tables.py   # create database and empty tables
python etl.py             # populate tables
You can validate that everything went well with the following commands:

cd ..                    # move back to the root folder
bin/pytest               # test that all tables have been populated properly.
This will create a virtual environment env in your root folder.

Data Warehousing at Sparkify
Sparkify is a music streaming startup that provides free and premium plans and aims to convert more free users to paid customers. For this purpose, they seek to get to know more about their songs, artists and especially - their customers and their usage patterns.

Currently, Sparkify is storing the majority of their data in .json files, which is tedious to work with, inefficient when the amount of data grows and prone to data loss. Therefore, they have decided to implement a more sophisticated data warehouse and the corresponding ETL processes.

Database Schema
The database schema follows the Snowflake style, with one fact table (songplays) and four dimension tables (time, users, songs and artists).

Database schema

The songplays table has foreign key constraints to all dimensions and well as a composite primary key, made out of all foreign keys.

ETL Processes
The implemented ETL process follows the project instructions and adds upon that by:

1.Using object-oriented programming principles to improve code efficiency and re-usability.
2.Separating source code from credentials.

Object-Oriented Preparation
The most relevant step in the ETL pipeline is to convert raw data into a format that is compatible with the database tables. This involves three steps:

1.Select relevant columns, generate new columns and rename columns.
2.Convert all values to native data types.
3.Convert to a list of dictionaries data structure.
