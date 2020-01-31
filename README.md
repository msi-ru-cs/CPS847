# CPS847
CPS847: Assignment 1
Created on: January 26, 2020
Assignment due date: February 5, 2020, end of the day
		 	 	 		
This assignment is group work. Typically, a group gets the same mark for a given assignment. However, if the contribution of some group members is considered not acceptable by their peers, then a peer-review process can be enacted that may lead to a reduction of marks for these group members. Please see the slides of the first lecture for details. 

Note Step 14a: at least one of the group members should come to the lab on Feb. 6 to show to the TA “live” bot so that he can test it.


1. Create Slack Team (i.e., workspace) for your lab group
2. Create GitHub repo for your group
3. [5%] Add ZenHub shell to your GitHub repo 
4. [5%] Integrate ZenHub notifications into Slack and create #zenhub slack channel for the notifications 
5. [5%] Integrate GitHub notifications into Slack and create #github slack channel for the notifications 
6. [5%] Create two Epics with two issues/requirements in each in ZenHub
7. [5%] Add estimates to each issue (select estimate values at random) 
8. [5%] Create: 
      a) “Sprint 1” starting on Jan 27, 2020, and ending on Feb 9, 2020, and 
      b) “Sprint 2” starting on Feb 10, 2020, and ending on February 24, 2020.
9. [5%] For each Epic, assign one issue/requirement to Sprint 1 and the other one -- to Sprint 2. 
10. [5%] Close first issue in Sprint 1
11. [5%] Close Sprint 1
12. [5%] Add users msi-ru-cs and avm-ru-cs to GitHub account
13. [5%] Send an invite to your slack group to mohammad.s.islam@ryerson.ca
14. [10%] Build Slack bot echoing questions asked to the bot, add it to your Slack group 
       a) You will have to run your bot from your machine in the lab so that we can validate its functionality
15. [5%] Commit the source code of your Slack bot to GitHub repository
16. [5%] Create file ./git_tst/index.html with some content
17. [10%] Create two additional branches and modify./git_tst/index.html in both of these branches in such a way that a merge conflict will be provoked. Merge both branches into the master branch and resolve the conflict. 
18. [5%] While committing the code in step 17, close one of the issues created in step 6 using commit message.
19. [10%] Create a pull request with a branch name cps847-pull-1 for some modification of ./git_tst/index.html; do the code review (by commenting on the commit in the pull request); merge and close the commit.


Deliverables

To submit to D2L 
A URL of your GitHub repo
A URL of your Slack group (workspace)
A snapshot (screen capture) of the burndown chart for Sprint 1
A snapshot (screen capture) of the velocity tracking chart

Bonus questions (to be verified in class as part of step 14):

[10% extra mark] The incoming message from Slack to your bot can be treated as an input string for many additional activities. One such activity is as follows. 
If the input string is the name of a city, then it can be sent to a 3rd party API such as Weather API (https://openweathermap.org/api). The Weather API then returns the current weather details (normally in JSON or XML format) and you can send them to your slack channel.
[5% extra mark] If you are up for a more challenging task, you could take the input string and apply NLP (Natural Language Processing) techniques on it before sending it to the 3rd-party API.  The benefit of the NLP is that even if the user doesn’t enter the correct spelling of a city, we can, with the help of the NLP techniques, correct the string before using it for any retrieval action.



