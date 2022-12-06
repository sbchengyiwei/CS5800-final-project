<h1>Genshin Speedrun Contest: Dijkstra's algorithm Solver</h1>
<p>Calculate the shortest path within the map.
Our project focuses on finding the shortest path in a given map. The idea comes from a speedrun contest of a video game, Genshin Impact. The contest requires players to get to the destination as fast as possible using combined methods given in the game: running, sprinting and wind glider.

In this project, we will first implement the shortest path finding algorithm on the base scenario where the only method allowed is running. Then we will bring in more moving methods, sprinting and wind glider, to enrich our model.
After applying the different method, the shortest path will be the fastest way from the source point to the destination. Here we will use the time-distance function: **Time = Distance / Speed(factor)** .

You can save the graph as an SVG file.</p>

This is the demo video link: https://youtu.be/mxyS_octKrI

<h2>Files</h2>
<ul>
<li>./dijkstra.js contains the JavaScript code</li>
<li>./dijkstra.html contains a demo page</li>
<li>./dijkstra.css contains the stylesheet</li>
<li>./image contains the background pictures</li>
<li>./distance contains the data of points and their transit time(calculate by distance/speed)</li>
</ul>

<h2>References</h2>
<ol>
<li>Computer Networks, 5E, by Andrew S. Tanenbaum</li>
<li>https://developer.mozilla.org/en/docs/Web/SVG/Element/textPath</li>
<li>http://stackoverflow.com/questions/24045673/reorder-elements-of-svg-z-index-in-d3-js</li>
<li>https://developer.mozilla.org/en-US/docs/Web/API/XMLSerializer</li>
<li>http://stackoverflow.com/questions/2897619/using-html5-javascript-to-generate-and-save-a-file</li>
<li>http://stackoverflow.com/questions/27098373/saving-xml-filen-in-node-js</li>
</ol>
