# JAddleseeSQL-Python-Project
A small SQL/Python project using a mock dataset modeled around a subscription service and its customer base

Using python and SQL in conjuction I've created a pipeline wherein the raw csv file will get read by Python, validated and cleaned up for analysis before sending it to the MySQL server that I was running. Where I've got two tables one containing customer information another containing details on the different tiers of membership, linked together by a foreign key.


## Technologies

- Python
- Pandas
- MySQL

## Pipeline

   <img width="174" height="662" alt="pipeline" src="https://github.com/user-attachments/assets/fb0ba55b-fc5b-471e-bd47-a6d5e8077620" />


## Database Design

<img width="501" height="225" alt="databasedesign" src="https://github.com/user-attachments/assets/21b625ee-2f8a-4a04-81bb-92a0e73f8969" />


## SQL Analysis

[Members By Tier](https://github.com/Jaddlesee/JAddleseeSQL-Python-Project/blob/main/QueryResults/membersByTier.csv)

[Active Subscriptions and Estimated Monthly Income](https://github.com/Jaddlesee/JAddleseeSQL-Python-Project/blob/main/QueryResults/activeMembersAndExpectedIncome.csv)

[Oldest 10 Members](https://github.com/Jaddlesee/JAddleseeSQL-Python-Project/blob/main/QueryResults/oldestMembers.csv)
