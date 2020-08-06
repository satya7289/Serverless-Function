# Description

- This contains the 3 serverless functions written to deploy it to as functions of the IBM cloud.
- First is Jokes.py -> Using the API http://api.icndb.com/jokes/random, the function returns a random joke. This serverless function can be triggered in chatbot after identifying user intention.
- Second is News.py -> We are using this API for news https://newsapi.org/. This function requires a parameter like a type, country, query. Types can be "top-headlines", "sources", "everything", Country can code the country and query if the user needs some specific topic of news. This function returns top news. This function can be triggered in chatbot after identifying user intention.
- Third is Weather.py -> We are using this API for weather https://openweathermap.org/. This function requires a parameter like 'latitude', 'longitude', 'city'. Latitude and longitude are used to get the user’s location to give the weather response of that location and the city parameter is used to 
get the status of the weather of that city. This function returns the weather report of the location or the specific issue. This function can be triggered in chatbot after identifying user intention.

# Locally Testing
- For the purpose of testing or localy check we can run the each program by `python <file_name>`
