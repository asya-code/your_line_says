<h1 align="center">
  <a href="https://github.com/asya-code/your_line_says.git">
    <!-- Please provide path to your logo here -->
    <div style="font-family: 'Shadows Into Light', cursive; font-size: x-large; color: Black">Your line says...</div>
  </a>
</h1>

<div align="center">
<br />

[![code with love by asya_code](https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%99%A5%20by-asya_code-ff1414.svg?style=flat-square)](https://github.com/asya-code)

</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
  - [Built With](#built-with)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Launch your server](#launch-your-server)

- [Roadmap](#roadmap)


</details>

---

## About
<p>
You'r line says... is a cute little application which gives you inspiring citations by your favorite authors and offers it's own sugested citations.
</p>

<br>


<img src="static/images/1.png" title="First img readme" width="100%"> 
<br>


### Built With

Backend is powered by Python with Flask web framework and SQLAlchemy as its ORM, PostgreSQL for database. The front-end is written in HTML, Jinja and Javascript. Bootstrap and css were used to style the app.
<p>
<img src="static/images/code.png" title="code snippet" width="100%"> 

<p>

## Features
<p>
Guests can enter their favorite author's name in the search field to get his/her random citation.

<p>
<img src="static/images/search_author.png" title="search by author" width="100%"> 

<p>
Or give the choice to the app and get absolutely random citation! 
</p>
<br>

<img src="static/images/random.png" title="random citation" width="100%">


## Getting Started

### Installation

Retrieve an entire repository from a hosted location via URL
<br>
<p> &nbsp <b> git clone https://github.com/asya-code/your_line_says.git </b> </p>

You’d then create a virtual environment:

<p> &nbsp <b> virtualenv env </b> </p>

Next, you’d activate that environment:
<br>

<p> &nbsp <b> source env/bin/activate </b> </p>

Finally, you’d use pip3 to install all of the requirements:
<br>

<p> &nbsp <b> (env) $ pip3 install -r requirements.txt </b> </p>
The -r option lets you supply a text file in the format pip3 freeze produces. This command should install all of the listed libraries.

To confirm that the correct packages are installed, you’d just run:
<br>

<p> &nbsp <b> pip3 freeze </b> </p>

### Launch your server

Once you’ve set up your virtual environment, activated it, and installed Flask, you should just be able to type:
<br>
<p> &nbsp <b> python3 server.py </b> </p>


## Roadmap

Project started on 06.14.2022, ended on 06.18.2022

Steps:

MVP
- Users can search for the citation by their favorite author

2.0
- Users can get random citation chosen by the app's algorithm

Main data is coming from the static database.