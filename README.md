# News-API

### 28th Feb. 2022

## Author

[Kiptoo Rugut](https://github.com/KiptooRugut)

# Description
This is a News Hub application that consumes News Api hence the user is able to read news from top news sources around the world by a click of a button. the user can choose from a wide range of sources, from general, entertainment, business and even sports.

## Live Link

https://news-hubs.herokuapp.com/

## Screenshot

<img src="app/static/images/HerokuNewsAPI.png">

## User Story

1. A user would see various news sources on the homepage of the application.
2. A user would also be able to select a news source and see all news articles from the selected news source in the application.
3. A user will be able to see the image, description and the time a news article was created from the News-Articles button.
4. A click on an article and read the full article on the source website.


## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  git clone https://github.com/KiptooRugut/News-API.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd News-Hub
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export API_KEY='{Enter your News Api Key}'
  ```
4. Running the application

  ```bash
  chmod a+x start.sh

  ./start.sh
  ```
5. Testing the application
  ```bash
  python3.8 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* [Python3.8](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)


## Known Bugs
* There are no known yet.

## Support and Contact Information 

To make a contribution to the code used or for any queries feel free to contact me via my email addresses mccrug97@gmail.com

## License

### MIT LICENCE

#### LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE).
