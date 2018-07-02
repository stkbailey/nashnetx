Overall Thoughts:
- What worked: 
	- Making it relatable 
		- Telling PyNash who the most central people were
		- Highlighting which groups were most "central" to the overall MeetUp fabric
		- Spiral outward
			- Toy example - can you go to all the food stations?
			- Anatomy of a MeetUp group - members (nodes) attending previous events together (edges)
			- Anatomy of a MeetUp city - groups(nodes) that share members with each other (edges)
	- Emphasize how great NetworkX is for working with -- 
		- pure Python
		- open source
		- just released new version recently
		- Plays well with Pandas 
		- Can generate other graph formats very well! Even if you just want to translate something so you can plot it, it can be a useful intermediary.
		- Fast
- Less important concepts from previous iterations
	- Bipartite graphs: Just focus on making graphs and measuring them
	- Adjacency plots
	- MeetUp data structures / scraping -- just a very brief overview will suffice
	- Graphing: wait until the end to discuss
- Keep in mind: last session of the weekend! Make it fun!
	- Funny toy example with food stations
	- 

- Clustering
- Centrality
- Degree
- Path length


Main takeaways
	- Making graphs
	- Measuring graphs
	- Exporting and Plotting graphs

**Learning goals**
	- Define what a "graph" is and why we would use them.
	- Describe what Degree, Path Length, Clustering and Centrality measure.
	- Build and describe a graph in NetworkX.
	- Leverage graph measures to answer a problem.
	- Plot a simple graph.


**New Outline**
1. What will we accomplish today?
	- Last session of the weekend. My goal is to equip you with enough know-how to take a dataset and create a graph of it. The data and several kernels I'm showing are on Kaggle - if you want to fork them and try it yourself, feel free to. 
	- You'll walk away knowing how to take a Pandas DataFrame, or a list  of relationships, make a graph object, plot it out, and make some simple measurements of it. 
2. "Important" example
	- Let's start out with a problem. It's one you might encounter at some of the bigger conferences. 
		- It's 3pm. You're tired. You're hungry. You're thirsty. And they've just put food out in the hallways. 
		- There's pizza in one hallway. Chips and dip in another. Ice cream sandwiches. Beer in a fourth. In fact, each hallway has a different delicious treat, and you want to get them all. 
		- BUT you don't want to go down the same hallway multiple times - because people will start to look at you funny. Question is, an you do it?
	- Answer is no. Why? Can you prove it?
	- The intuition is that you have to be able to go through each hallway once. 
	- Formally, we can say that we can traverse all edges once, if the number of odd nodes is 0 or 2.
3. Beyond the waistline...
	- This formalization led to a set of mathematics called graph theory. It goes far beyond that, as we'll see. But it starts with Nodes and Edges. 
	- NetworkX is a package that lets you perform graph theory analyses. It is quite good...
		- pure Python
		- open source
		- just released new version recently
		- Plays well with Pandas 
		- Can generate other graph formats very well! Even if you just want to translate something so you can plot it, it can be a useful intermediary.
		- Fast
	- Let's make our example to get you familiarized with the core concepts.
		- `g = nx.Graph()`
		- `g.add_node()`
		- `g.add_edge()`
	- We can access some basic attributes:
		- `g.degree`
	- We can add attributes, or weights. For example, we can say that this is the pizza hallway, or this has a ton of food on it. 
	- Finally, let's plot it. 
4. Influencers: 
	- We're going to look at users across the MeetUp world that have attended the same events. 
		- We will look at two measures: degree and centrality. 
		- This is the total number of people they have "interacted" with, or co-attended events with. 
		- Centrality is how much of a "connector" a person is. That is, if we want to go from any one person to another, how often do we go trhough this person?
	- Display the data
	- Load the data using `nx.from_dataframe...`
	- The people with the highest degree belong to big groups.
	- BUT the most central people are active in some big groups and some niche groups. 
	- To give you a sense of who is coming up on this measure...
		- Pablo, a DJ from Santiago, Chile
5. MeetUp groups: what "clusters" of groups are there?
	- Similar groups will attract the same people.
	- Clustering by category
	- Visualize it...
6. Some takeaways...
	- `nx.draw`
		- Spring graphs, circular graphs, eigengraphs
	- `nx.to_pajak...`
	- Using d3.js to draw graphs -- a great tool
	- Practice on the Kaggle kernel, or fork the repo on Github




**Detailed Outline**

1. Pose the networking problem
	- You're new to Nashville. You're ready to start meeting people, making friends, expanding your network. But you don't want to get pigeon-holed into just one group, i.e. the people you might already know / are comfortable with. Maybe you're trying to market yourself / a product.
	- What groups should you join? Who should you talk to in those groups? Wouldn't you rather be invited into a group than just show up at one?
2. Agenda
	- Netwhat?
	- Making networks
	- Describing networks
	- Drawing networks
3. Netwhat?
	- Simple problem: can you go to all of the conference rooms w/ food, without crossing the same hallway?
		- Display picture of bridges, pose problem: can you walk across all bridges once? Have group take a minute to ponder: how is it possible to solve this?
		- Why or why not?
		- Walk through Euler's thinking...
	- GT describes relationships
		- Examples of usefulness: Internet, Social networks, Brain
4. NetworkX
	- Vocabulary: Nodes, edges, communities, hubs
	- Build conference problem
		- Add nodes
		- Add edges
		- Add attributes
	- Discuss data structure: dict-of-dicts-of-dicts
		- Building MeetUp graph

Orient to available data: member data, group data, events attended data
Build bipartite graph from DataFrame
Make group and member graphs from bipartite graph
Describing networks
Orient to the members graph - each edge represents a shared group membership
Degree: the people with a lot of connections
But maybe they just join big groups? Theyre "mainstream"
Path Length: on average, how far is this person from some other person?
7 degress of separation
Interesting anecodote about mailers to NY
Centrality: how are the people who are "connectors"?
Creating a "scorecard" for individuals, then picking out individuals w/ the highest centrality
Big reveal: who are the most "central" people in PyNash?
Drawing networks
Basics: nodes plotted to points, edges drawn between
Gets tricky with larger data
Variable sizing of nodes, colors of edges
Credits and point to source code