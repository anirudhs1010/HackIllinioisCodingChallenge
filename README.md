**Coding Challenge**

Your city, nestled at the base of Mount Olympus, is under siege by Typhon, the monstrous titan of storms and chaos. As the chosen hero, you have been tasked with seeking out the gods and heroes who might help defend your city.

To begin, you must retrieve your celestial JWT token to prove your worth. Make sure you use the same GitHub account as you did earlier!

Fetch JWT
For all future API calls, you will need to include the magical JWT token (exactly as you received it) in the request header. Don't forget to specify the required content-type header, or your plea for help will not be understood by the gods.

{"Authorization": <enter_token>}

{"Content-Type": "application/json"}

Problem Setup
In the ancient world, there are different pantheons of gods and heroes, each with their own distinct power. Some are benevolent, while others are malicious. You are provided with a dictionary of gods and heroes, with their divine power value.

You are also given a list of alliances, representing pairs of gods and heroes who are allies. These alliances connect the gods and heroes, making them part of the same pantheon. The nodes (gods and heroes) and edges (alliances) form an undirected graph, where each connected component represents a different pantheon.

You will receive these inputs by making a GET request to this endpoint (make sure to include the required headers).

GET https://adonix.hackillinois.org/registration/challenge/

Problem Statement
The King of your city has tasked you with finding the greatest divine power among all pantheons. In other words, determine the sum of divine power for each pantheon and return the greatest sum. If you succeed, the King will use this information to coordinate the defense of the city!

Submitting Your Solution
Make a POST request to this endpoint and include your max_divine_power in the request body as shown below:

POST https://adonix.hackillinois.org/registration/challenge/

{"solution": <calculated_max_divine_power>}

(Don't forget to include your headers!)

Example
Given this scenario, we have two pantheons:

Pantheon 1: Zeus, Apollo, Athena, with a total divine power of 102.
Pantheon 2: Hades, Hermes, and Artemis, with a total divine power of 87.
Inputs
alliances	people
[

["Zeus", "Apollo"],

["Apollo", "Athena"],

["Hades", "Hermes"]

["Hermes", "Artemis"]

["Hades", "Artemis"]

]

{
"Zeus": 36,

"Apollo": 32,

"Athena": 34,

"Hades": 28,

"Hermes": 29,

"Artemis": 30
}

Example
We have two pantheons: one consisting of Zeus, Apollo, and Athena; and the other consisting of Hades, Artemis, and Hermes. The first pantheon's sum is 102, and the second pantheon's sum is 87. Therefore, the max_divine_power is 102. 

Constraints
The input edges (alliances) and nodes (gods/heroes) will be valid.
Divine power values can be positive or negative integers, as gods and heroes can be either benevolent or malevolent.
The graph will contain cycles, so be careful not to be trapped in a loop of eternity.

**Solution**

Using a disjoint set union, we can find the sum of each connected component fast and then take the max by comparison using their parents. Used a GET request with the provided authentication and then a POST at the end for the solution as specified.
