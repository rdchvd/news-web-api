# news-web-api
It`s a simple news board API.

<h2>About</h2>
<div>
If you want to see API documentation:
<p><a href="https://documenter.getpostman.com/view/14195354/TVzVhakw">click here</a></p>
</div>

<h2>Getting Started</h2>

<h3>Prerequisites</h3>
<ul>
  <li>Python 3</li>
  <li>pip3 to install dependencies</li>
  <li>PostgreSQL</li>
  </ul>

<h3>Installing packages</h3>
<h4>Mac OS:</h4>
<ol>
 <li>Run <code>virtualenv env</code> to make virtual environment </li>
 <li>Activate it by <code>source env/bin/activate</code></li>
 <li>Run <code>pip3 install -r requirements.txt</code></li>
 </ol>
 <h4>Windows:</h4>
<ol>
 <li>Run <code>python3 -m venv venv</code> to make virtual environment </li>
 <li>Activate it by <code>venv\Scripts\activate.bat</code></li>
 <li>Run <code>pip3 install -r requirements.txt</code></li>
 </ol>
 

<h3>Setting up the local DB</h3>
<ol>
<li>Cd into the app directory</li>
<li>Run <code>python3 manage.py makemigrations</code></li>
<li><code>python3 manage.py migrate</code></li>
</ol>

<h3>Running the app</h3>
<p>Run using <code>python3 manage.py runserver</code></p>
