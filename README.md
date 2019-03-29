# get_weather_script
This script prints current temperature in a particular city with openwearthmap.org API.

To run the script:
<ul>
<li>get your APPID from http://openweathermap.org/appid and assign it to the <code>key</code> variable in the script,</li>
<li>type in terminal:
<code>python get_weather_script.py <i>[city]</i></code>.</li>
</ul>

<p>If a given city exists in the database, you'll obtain temperature in Centigrade degrees, e.g.: <code>12&deg;C</code>.</p>
<p>Or else, if a city doesn't exist in the database or for example you forget to paste your APPID, script will print suitable message from the server such a:</p>
<code>city not found</code><br/>
or<br/>
<code>Invalid API key. Please see http://openweathermap.org/faq#error401 for more info.</code><br/>
