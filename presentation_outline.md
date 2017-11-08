## Identifying PyNash's Popular Pythonistas with NetworkX

Network analysis is a powerful and increasingly widespread way to analyze relational data, such as social networks. In this tutorial, we will learn the basics of graph theory and how to use NetworkX, a popular open-source Python package. We'll then apply this knowledge to extract insights about the social fabric of Tennessee MeetUp groups.

#### Abstract
Network analysis is a powerful and increasingly widespread way to analyze relational data, such as social networks. In this tutorial, we will learn the basics of graph theory and how to use NetworkX, a popular open-source Python package. We'll then apply this knowledge to extract insights about the social fabric of Tennessee MeetUp groups.

#### Learning goals
1. Define what a "graph" is and why we would use them.
2. Describe what Degree, Path Length, Clustering and Centrality measure.
3. Build and describe a graph in NetworkX.
4. Leverage graph measures to answer a problem.
5. Plot a simple graph.

#### Detailed Outline
1. Pose the networking problem
	* You're new to Nashville. You're ready to start meeting people, making friends, expanding your network. But you don't want to get pigeon-holed into just one group, i.e. the people you might already know / are comfortable with. Maybe you're trying to market yourself / a product. 
	* What groups should you join? Who should you talk to in those groups? Wouldn't you rather be invited into a group than just show up at one?
2. Agenda
	- Netwhat?
	- Making networks
	- Describing networks
        - Drawing networks
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
5. Describing networks
	- Orient to the members graph - each edge represents a shared group membership
	- Degree: the people with a lot of connections
		- But maybe they just join big groups? Theyre "mainstream"
	- Path Length: on average, how far is this person from some other person?
		- 7 degress of separation
		- Interesting anecodote about mailers to NY
	- Centrality: how are the people who are "connectors"?
	- Creating a "scorecard" for individuals, then picking out individuals w/ the highest centrality
	- Big reveal: who are the most "central" people in PyNash?
6. Drawing networks
	* Basics: nodes plotted to points, edges drawn between
	* Gets tricky with larger data
	* Variable sizing of nodes, colors of edges
7. Credits and point to source code


I am a PhD student at Vanderbilt, and I enjoy speaking. Although I have never given a large tutorial, I have experience teaching adults in classroom settings, as well as giving lectures to mid-size audiences (30-60). A couple years ago, I attended Toastmasters and got to practice on my fundamental public speaking skills.

I have some expertise in the subject matter from my research, which uses graph theory to analyze brain networks. I have also completed an online course - [Applied Social Network Analysis in Python](https://www.coursera.org/learn/python-social-network-analysis) - which has given me some thoughts on how to present the material cogently. 

I'll be presenting a brief talk on the proposed material at PyNash on 11/16, which will provide a good opportunity to vet and refine the basic idea. For the tutorial, I would expand the topic a bit and set up a Jupyter Notebook server so that people can follow along and also practice on their own (although I haven't done this before). If I can get that to work, then my actual talk might be a mix of presentation + pseudo-live coding (indexing the graph in different ways, showing how different tweaks can change network properties, etc.).

Data and code would be made available on Github of course. I would also be open to making this a two-hour tutorial and adding in another dataset (brain data) and/or a problem that leverages using graph theory to answer a machine learning problem. 


### Questions for Bill
- What is the best way to present code?
	* Running Jupyter Notebooks vs. using PowerPoint?
- What angle(s) do you think people in PyNash are most interested in?
	* Capabilities, math, data structures, code samples - or information / results / seeing cool things?
- What's the max amount of time I should take (to keep interest)... 30 minutes?

- font: source code pro, consulus
- submit to PyTN tutorial
