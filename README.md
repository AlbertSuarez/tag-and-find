# Tag & Find

Project built in JacobsHack 2018

Who knows better than people? Find what you are looking for thanks to the users reviews in just three steps

## Requirements

- Python 3.6+

## Recommendations

Usage of [virtualenv](https://realpython.com/blog/python/python-virtual-environments-a-primer/) is recommended for package library / runtime isolation.

## Usage

To run the server, please execute the following from the root directory:

1. Setup virtual environment

```bash
python3 -m venv env
source env/bin/activate
```

2. Install dependencies

```bash
pip3 install -r requirements.txt
```

3. Install `TextBlob` dependencies

```bash
python -m textblob.download_corpora
```

4. Run Startup server
    
```bash
python3 app.py
```

or via docker-compose

```bash
docker-compose up -d
```

## Inspiration
We like Google Maps, but we think that sometimes is not as accurate as it could be. That's why we have been thinking about developing a web app to find places with more specific parameters. e.g. Sometimes we want to go to a restaurant not only for its food, but also for the atmosphere (and that's not something Google Maps can give us, for that you should see the reviews :c, ain't nobody got for that!)

## What it does?
Our web app is used for finding places with special features you want to specify (maybe some clean toilets, a special restaurant with a astonishing atmosphere, a cozy bar for grabbing some beers with your friends...). All of this is based on the idea of finding that place you are looking for only in three steps:

- **First**: You say where do you want the place to be searched (it can be your university, next to your home, on the city of the next hackathon you are attending...). Also it has the possibility to indicate your geolocalization.
- **Second**: You indicate what you are looking for. You can select one of a variety of different things: bars, restaurants, museums, parks...
- **Third**: You select which features do you want your place to have (it can be more than one!): clean, comfortable, quiet, cheap, luxurious...

## How we built it
We focused in two different areas: the user interface and the natural language processing. Also, to get the information we needed we used the Here Geocoder API and the Google Places API.

- **User interface**: Everything has been made with HTML/CSS (also Bootstrap) and Javascript. We wanted to ensure that everything was intuitive, responsive and (of course) beautiful. It can be seen in the photos how the interface is.
- **Natural Language Processing**: We used the library called TextBlob based on the NLTK framework. Everything has been coded in python. The main idea of the algorithm is to get all the info of the places of the type selected nearer to the location (got with the Here API) used. Then, take their user reviews (we were about to do it also with the Here API, but we found that Google Places API had more results) and by Natural Language Processing analyze which of them accomplish the features selected.

## Challenges we ran into
When we started hacking, we had a lot of ideas that hasn't been able to be made reality. For instance, at final we couldn't make it possible to make that the parameters of the places and features were written by the user instead of selecting it of a limited set. Also we couldn't be able to deploy our flask app in the Google Cloud server :c so that's why we finally deployed it on Heroku (we were more familiar with this cloud service)

## Accomplishments that we're proud of
Nevertheless, we are really proud of the results we had. Everyone on the team has worked with technologies that never had experience of. We also are proud of being capable of working with a good team cooperation, parallelizing tasks and being efficient helping each other when was necessary. We also are happy to have worked with NLP and for having made our web responsive.

## What we learned
As it is said above, we all have had the opportunity to work with technologies that we never had used before. The use of Natural Language Processing has been a challenge that has made us learn a lot of concepts we didn't know. Also, two members of the team have worked with languages they never coded with, Javascript and Python respectively. And in spite of haven't accomplish the deployment of the web in Google Cloud, the one who tried to do it has learned a lot about Google Cloud, Flask and servers.

## What's next for Tag&Find
We would like to improve the searching of necessities and features, making it more customizable for the user to find more accurate places.

## Images

![](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/000/717/043/datas/gallery.jpg)
![](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/000/717/044/datas/gallery.jpg)

## License

MIT © Tag&Find