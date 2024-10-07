1. Create a "primary" cloud server (your ansible host) and place an ansible playbook into /root/deploy called deploy.yaml
2. Create a second cloud server, add it to the ansible inventory in the group [red] and use the deploy.yaml file to install a web server on it which serves one page, /hw1.html, with the string "Red Team" in the page body.
   2a. HINT: Use a new ssh key to allow your primary server to connect to the new cloud server.
3. Create a third cloud server, add it to the ansible inventory in the group [blue] and use the deploy.yaml file to install a web server on it which serves one page, /hw1.html, with the string "Blue Team" in the page body.
4. Modify the playbook to install the "curl" package on all deployed servers.
5. Create 8 more (small) cloud servers, add four to the [red] team and four to the [blue] team, and use your ansible playbook to deploy web servers on your whole 10-server fleet.
6. Add our grader SSH key to your authorized_keys file on the primary server and make sure to update the DNS entry in the grading site to point to this server's IP.
7. Remember to DELETE your servers after successfully completing the assignment to ensure that you're not draining credits.
