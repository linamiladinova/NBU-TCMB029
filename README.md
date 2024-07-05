# NBU-TCMB029
New Bulgarian University
Course: TCMB029 Introduction to Network Engineering - Part II
Professor: Mr. Milovanov
Name: malinka
faculty number: F108682

Project Condition:
- Install docker and familiarize yourself with it according to docker-ciriculum;
- Familiarize yourself with docker-compose and the ability to compose your application stack into containers;
- Familiarize yourself with the mininet;
- Familiarize yourself with the floodlight SDN controller;
- Make a repo in GitHub
- Write a sample mininet Python script that creates a network with a topology of 812 switches and 18 hosts connected to your chosen topology.
- Demonstrate how you configure bidirectional traffic rules between the two farthest hosts on your network with a script to the floodlight API.
You can find the video here.

----Commands used in the video----
sudo docker pull latarc/floodlight
sudo docker run -d -p 6653:6653 -p 8080:8080 --name=floodlight latarc/floodlight
sudo docker start floodlight
sudo docker images
sudo docker ps -a
(i already installed mininet, but you haven't, try `sudo apt install mininet`)
sudo mn --switch ovsbr --test pingall
sudo mn --custom custom_topology.py --topo=mytopo --controller=remote
h1 arp -a
h2 arp -a
dump
h1 ping s1
h2 ping s2
net
