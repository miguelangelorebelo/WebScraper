The Economist - WebScraper 🤖 V1.0.0

To run:

1. Set up the environment with `make build`
2. Run `make run` to run the project
3. Run `make watch` to see the terminal outputs
3. In order to reset you may run `make clean`

If you have the required packages installed you can run the `main.py` file

It dumps the extracted news to a local db

The jupyter notebooks contain the exploration phase of this project. There I go through my thought
process and you see the steps to create the functions, then the class, then the service.

The basic strategy is this:

 - build a function that extracts the contents of one url (news url)
 - collect all the urls present in the main page of economist.com
 - extract all of the urls using the function developed before, to a list
 of dicts.
 - The list of dicts is used then to feed a table that gathers the extracted information
 (title, description, body, image, url, date_published)
 - build the db model and create the db
 - build a class for extracting the content using the functions developed before
 - use a cronjob to schedule the extraction for 10am, each day. 
 - package in a docker container

It has a throtle on, waiting 1 to 2 seconds between each url. To speed up the process,
I could remove that, but this way the systems department of The Economist 
doesn't become mad at me.

I hope you like this project!