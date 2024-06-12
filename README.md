Yeslamov Temirlan, 22200836

Aldanbergen Zholdas, 22211514

# RASA bot - Bavarian Guide

Link to Wikis: 
https://github.com/teewhymagg/Chatbot-RASA/wiki

# Project description

This myGit project is assistance system, specifically rasa bot with the theme of Bavarian Guide. Rasa is an open source machine learning framework that was used to create a Bot that is a Travel Guide in Bavaria. Right fit, Persona, Use cases, Technical prerequisites, Example dialogs, Dialog flow are shown in wiki. We implemented 5 use cases based on different personas. Bot is able to understand the inputs of the user and print the outputs based on the stories that are written in stories.yml. All of the intents and examples of possible inputs of the user are written inside the file nlu.yml. All of the intents, actions, entities, responses and slots are written in domain.yml. The actions.py consists all of the functions that are triggered throughout the conversation. They are important for the correct work of the bot. Api for weather, info about the city was implemented. The city that was entered by the user will output the weather in this city and also the information about it from wikipedia. Bot also offers to book the accommodation by outputing the website url with the city that user entered. It also offers the Deutsche Bahn website url, specifically BayernTicket webpage.  

# Prerequisites

rasa = 3.6.15

python = 3.10.10

# Installation

To install this project the repository needs to be cloned. 

You can create virtual environment:

```bash
python -m venv venv_name
```

Activate the virtual environment: Windows

```bash
venv_name\Scripts\activate
```

MacOs/Linux:

```bash
source venv_name/bin/activate
```

To deactivate it, run:

```bash
deactivate
```

To install rasa run the following command: 
```bash
pip3 install rasa
```
or 
```bash
pip install rasa
```
To be able to execute the program rasa should be trained, run the following command:
```bash
rasa train
```
Also the following command should be entered
```bash
rasa run action -p 5056
```

After the rasa is trained, it has to be exectuted, following command:
```bash
rasa shell
```

# Basic usage

After executing the program the console bot will be opened. 

This is the example of a typical conversation:

**Your input** ->  Hello                                                 

Hey! How are you?

**Your input** -> Good

Great! Carry on!

**Your input** -> what can i do in Bavaria?                                       

I can suggest you several things like nature in Bavaria or description of major cities in Bavaria and also i can tell you the weather in a specific state in Bavaria

**Your input** -> lets see cities                                               

Interested in cities? Choose a city in Bavaria.

**Your input** -> Deggendorf                                       

Deggendorf (Bavarian: Degndorf, Deggndorf) is a town in Bavaria, Germany, capital of the Deggendorf district.
It is located on the left bank approximately in the middle between the Danube cities of Regensburg and Passau. The Danube forms the town's natural border towards the south. Towards the west, north and east the town is surrounded by the foothills of the central Bavarian Forest.
Near the southwestern rim of the town, the railway bridge crosses the Danube at river-kilometer 2286 ||| The current weather in Deggendorf is scattered clouds with a temperature of -4.22°C.
 You can book an accommodation here: https://www.booking.com/city/de/Deggendorf.html?aid=1610684

**Your input** -> lets see nature                                               

You've chosen to explore nature. Would you like mountains, forests, or lakes?  

**Your input** -> lakes              

Bavaria's lakes are stunning. Would you like to hear about Chiemsee, Starnberger See, or Ammersee?

**Your input** -> chiemsee        
                                                
Chiemsee (German pronunciation: [ˈkiːmzeː] ) is a freshwater lake in Bavaria, Germany, near Rosenheim. It is often called "the Bavarian Sea". The rivers Tiroler Achen and Prien flow into the lake from the south, and the river Alz flows out towards the north | You can buy Bavarian Ticket here: https://www.bahn.de/angebot/regio/laender-tickets/bayern-ticket

Want to get info about something else? Just type 'nature' or 'cities'.

# Implementation of the Requests

In this project we have 5 requests with slots and entities to process user messages. 

- resetting slots - **ActionResetSlots**, resets nature_slot

- choosing city - **ActionChooseCity**, requests information from wikipedia and weather websites using API key and presents information about the city the user specified

- choosing specific nature - **ActionChooseSpecificNature**, requests information from wikipedia, presents information, sends the link to buy Bayern ticket

- processing category choice - **ActionProcessCategoryChoice**, processes category choice (nature or city). Based on user response, provide bot response for nature or city.

- choosing nature - **ActionChooseNature**, processes the actions need to be taken based on nature_slot, to output specific information based on "forests", "mountains", "lakes"

# Work done

Zholdas performed tasks:

1) Persona (no. 2 in previous list)
2) Example dialogs (3)
3) Implementation yml-files (domain, data/nlu)

Temirlan perfomed tasks:

4) Use cases (1)
5) Dialog flow (4)
6) Implementation yml-files (data/stories data/rules)

However, we completed every task together, so there were practically no devisions to the roles in completing tasks.
