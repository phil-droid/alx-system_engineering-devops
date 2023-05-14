Postmortem Report
Incident report for Server Downtime and 504 Error

Summary: On May 14th, 2023 at 11:30 PM EST, the server went down, resulting in a 504 error for anyone trying to access the website. The server was based on a LEMP stack.
Timeline: 11:30 PM EST - Website access was unavailable, resulting in a 504 error for anyone trying to access it. 
11:35 PM EST - The server was checked, and it was found that the server was working correctly. 
11:40 PM EST - Checking the NGINX configuration file and logs, it was discovered that there were errors in the configuration file that were causing the server to go down.
11:50 PM EST - The error was identified and resolved by removing the offending code from the NGINX configuration file. 12:00 AM EST - The server was restarted, and the website was tested to ensure it was running correctly.
Root Cause and Resolution: The root cause of the issue was due to incorrect configuration settings in the NGINX configuration file, which caused the server to go down. Specifically, an incorrect parameter was added in the configuration file, which caused the server to fail.
The issue was resolved by identifying the error in the configuration file and removing the offending code. After removing the code, the server was restarted, and the website was tested to ensure it was running correctly.
Corrective and Preventive Measures: To prevent similar issues from occurring in the future, we will take the following corrective and preventive measures:
Regular monitoring and review of server logs and configuration files to identify potential issues before they become major problems.
Implementing an automated monitoring system to quickly identify and alert us to any issues that arise on the server.
Ensuring all configuration changes are thoroughly tested before being implemented on the production server.
Maintaining up-to-date backups of the server to enable quick restoration in case of any failures or crashes.
Developing a disaster recovery plan to ensure the website's availability in the event of a server failure.
