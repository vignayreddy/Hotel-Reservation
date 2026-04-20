Hotel Reservation


DATABASE SETUP
create a bucket in some project adn store the hotel resrrvation dataset in it

Project SETUP
Command Used 
python -m venv venv -> for virtual environment
venv\Scripts\activate -> for using this venv
pip install -e . -> Automatically checks setup.py

we use google service account for data ingestion
we will install and use google cloud client
gcloud --version  to check the version

    Go toIAM AND then go to  service account and then check the role as Storage Admin and also add another role as Storage Object Viewer

Then after go to buckets and in princioles go to hotel reservation add it 

hotel-reservation@project-82ee730d-c76d-4cc9-b7b.iam.gserviceaccount.com

and in assigned roles add the same roles assigned in the service account..

Then go to service accounts adn add key to the service account we juct created .
Key generation was giving an error so ensure to run command  
<!-- gcloud auth application-default login -->
<!-- C:\Users\vigna\AppData\Roaming\gcloud\application_default_credentials.json. -->