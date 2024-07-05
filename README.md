# NBU-TCMB029
New Bulgarian University<br />
Course: TCMB029 Introduction to Network Engineering - Part II<br />
Professor: Mr. Milovanov<br />
Name: malinka<br />
faculty number: F108682<br />

Project Condition:
- Install docker and familiarize yourself with it according to docker-ciriculum;
- Familiarize yourself with docker-compose and the ability to compose your application stack into containers;
- Familiarize yourself with the mininet;
- Familiarize yourself with the floodlight SDN controller;
- Make a repo in GitHub;
- Write a sample mininet Python script that creates a network with a topology of 812 switches and 18 hosts connected to your chosen topology;
- Demonstrate how you configure bidirectional traffic rules between the two farthest hosts on your network with a script to the floodlight API.<br />
You can find the video here.

----Commands used in the video----<br />
`sudo docker pull latarc/floodlight`<br />
`sudo docker run -d -p 6653:6653 -p 8080:8080 --name=floodlight latarc/floodlight`<br />
`sudo docker start floodlight`<br />
`sudo docker images`<br />
`sudo docker ps -a`<br />
(i already installed mininet, but you haven't, try `sudo apt install mininet`)<br />
`sudo mn --switch ovsbr --test pingall`<br />
`sudo mn --custom custom_topology.py --topo=mytopo --controller=remote`<br />
`h1 arp -a`<br />
`h2 arp -a`<br />
`dump`<br />
`h1 ping s1`<br />
`h2 ping s2`<br />
`net`<br />
