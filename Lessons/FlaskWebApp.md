# Flask Web App Development

## Table of Contents <!-- omit in toc -->

1. [Activities](#activities)
1. [Objectives](#objectives)
1. [Challenges](#challenges)
1. [Stretch Challenges](#stretch-challenges)
1. [Resources](#resources)

## Activities

- Compare implementations for sampling words based on observed frequency
- Visualize how sampling algorithms work by drawing pictures with a number line
- Discuss tradeoffs of different sampling techniques based on histogram implementations

## Objectives

After completing this class session and the associated tutorial challenges, students will be able to ...

- Set up Python virtual environments for package isolation
- Properly ignore unnessessary Python files and corpus data

  - Set up gitignore.io command line tool and run `gi python > .gitignore`
  - Add `data` folder and move corpus to new location
  - Ignore `data` folder in `.gitignore`

- Set up a root route (`/`) that will serve a random word or sentence
- Build and test simple Flask web apps on local computers
- Deploy Flask web apps to Render cloud hosted servers

## Challenges

These challenges are the baseline required to complete the project and course. Be sure to complete these before next class session and before starting on the stretch challenges below.

- [Page 5: Flask Web App]

  - Set up an isolated virtual environment with `virtualenv`
  - Develop a Flask web app locally (access via `localhost`)
  - Push your Flask web app to Render servers (on the Web)

## Stretch Challenges

These challenges are more difficult and help you push your skills and understanding to the next level.

- [Page 5: Flask Web App]

  - Improve the style of your page with CSS
  - Display more than one generated word
  - Generate a specific number of words given in a URL query string parameter (like `/?num=10`)
  - Add a button to display a new word (i.e. refresh the page) when clicked
  - Add a button and route to store favorites (chosen by users) with a database

## Resources

- Read The Hitchhiker's Guide to Python's tutorial on [virtual environments]
- Consult documentation for Python's [`virtualenv` tool]
- Read the [Flask quickstart] to jump right in and follow the [Flask tutorial]
- Consult the [Flask documentation] to learn more and solve specific problems
- Read [Explore Flask], a book about best practices and patterns for developing web apps with Flask

[`virtualenv` tool]: https://virtualenv.pypa.io/en/stable/
[explore flask]: https://exploreflask.com/en/latest/
[flask]: http://flask.pocoo.org/
[flask documentation]: http://flask.pocoo.org/docs/0.11/
[flask quickstart]: http://flask.pocoo.org/docs/0.11/quickstart/
[flask tutorial]: http://flask.pocoo.org/docs/0.11/tutorial/
[page 5: flask web app]: https://bit.ly/tutorial-tweet-generator
[video of sampling algorithms whiteboard activity]: https://www.youtube.com/watch?v=C0jk6HLj6Tk
[virtual environments]: http://docs.python-guide.org/en/latest/dev/virtualenvs/
