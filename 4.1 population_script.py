import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_django_project.settings')    # It's name of the project not application

import django
django.setup()

# Fake population script
# Used Faker package for fake data
# Install it with - pip install Faker

import random
from faker import Faker
from polls.models import Topic, Web_page, AccessRecord

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]    # Here 'topic_name' is column name in Topic Model(Table), needs to be passed with same name
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

        # get the topic for the entry
        topic = add_topic()

        # create fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create the new webpage entry
        webpg = Web_page.objects.get_or_create(topic=topic, url=fake_url, name=fake_name)[0]    # Here 'topic','url','name' are column names in Web_page Model(Table), needs to be passed with same names

        # create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]    # Here 'name','date' are column names in AccessRecord Model(Table), needs to be passed with same names


if __name__ == '__main__':
    print("Populating")
    populate(20)                          # Will populate 20 records of fake data in the Web_page and AccessRecord, will add topic in Topic if not already present.
    print("Populated")
    
    
    # Run the file in the project - python population_script.py
    # Run server to see the changes. - python manage.py runserver 8080
