## Identifying PyNash's Popular Pythonistas with NetworkX

Network analysis is a powerful and increasingly widespread way to analyze relational data, such as social networks. In this tutorial, audience members will learn how to use NetworkX, a popular open-source Python package, to perform network analysis. The learning will be embedded within we will walk through an analysis of data from MeetUp.com to determine which groups in each major Tennessee city are most likely to . 

### Questions for Bill
- What is the best way to present code?
	* Running Jupyter Notebooks vs. using PowerPoint?
- What angle(s) do you think people in PyNash are most interested in?
	* Capabilities, math, data structures, code samples - or information / results / seeing cool things?
- What's the max amount of time I should take (to keep interest)... 30 minutes?

- font: source code pro, consulus
- submit to PyTN tutorial

### Outline

1. Pose the networking problem
	* You're new to Nashville. You're ready to start meeting people, making friends, expanding your network. But you don't want to get pigeon-holed into just one group, i.e. the people you might already know / are comfortable with. Maybe you're trying to market yourself / a product. 
	* What groups should you join? Who should you talk to in those groups? Wouldn't you rather be invited into a group than just show up at one?
2. Agenda
	- Netwhat?
	- Making networks
	- Drawing networks (Should I include?)
	- Describing networks
3. Netwhat?
	- Konigberg bridge problem
		* Display picture of bridges, pose problem: can you walk across all bridges once? Have group take a minute to ponder: how is it possible to solve this?
			* Why or why not?
		* Walk through Euler's thinking...
		* GT describes *relationships*
	- Examples of usefulness
		- Internet
		- Social networks
		- Brain
	- Vocabulary
		* Nodes, edges, communities, hubs
4. Making networks
	- Build Konigberg bridge problem
		* Construct graph
			* Discuss different graphs
			* Add nodes
			* Add edges
			* Add attributes
		* Discuss data structure: dict-of-dicts-of-dicts 
	- Building MeetUp graph
		* Orient to available data: member data, group data, events attended data
		* Build bipartite graph from DataFrame
		* Make group and member graphs from bipartite graph
5. Drawing networks
	- Clustering
		* Let's look at the groups graph... we would expect many groups to share members -- what are these groups?
		* Color groups by topic
		* See if there are "clusters" of groups based on their members
	- Visualization
		* Basics: nodes plotted to points, edges drawn between
		* Gets tricky with larger data
		* Variable sizing of nodes, colors of edges
6. Describing networks
	- Orient to the members graph - each edge represents a shared group membership
	- Degree: the people with a lot of connections
		- But maybe they just join big groups? Theyre "mainstream"
	- Path Length: on average, how far is this person from some other person?
		- 7 degress of separation
		- Interesting anecodote about mailers to NY
	- Centrality: how are the people who are "connectors"?
	- Creating a "scorecard" for individuals, then picking out individuals w/ the highest centrality
		- Big reve
		al: who are the most "central" people in PyNash?
7. Credits and point to source code


## Personal