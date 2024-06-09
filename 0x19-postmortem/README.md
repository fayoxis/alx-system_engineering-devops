# 0x19-postmortem - The ALX Project
--------------

![NGINX image](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLP9iIfWr_njC9WzuVPJ1nHqDRbcmJVLfHQA&usqp=CAU)

It happened in a flash; Our upcoming, highly vibrant and popular website among Africans in the Diaspora (Dbazz Website — a site used by African Individuals in the Diaspora to transfer money in any currency to their families back home without any hidden charges or costs) was DOWN!!!

The panic is real because we have close to 50 million individuals who visit our Website on a daily basis to perform various transactions and we cannot afford to lose our dedicated customers to competition. Ha! nope not happening on my watch.

I am one of Dbazz System DevOps Engineer’s and one of my primary responsibilities is to debug issues like these when they arise; which happens ever so often. First to solve this, I performed all the required system administration and configuration management checks by troubleshooting and debugging. This was done to identify and resolve issues related to system performance and configuration to understand what the issue was.

Then I spotted the bug: Something was keeping Dbazz Ubuntu container’s Nginx installation from listening on port 80. This is highly problematic because if Nginx is not listening on port 80, it can lead to the servers being inaccessible from the internet. Port 80 is the default port for HTTP traffic, and if Nginx is not properly configured to listen on this port, incoming web requests won’t be directed to the appropriate backend servers, resulting in a downtime situation which is what happened to Dbazz Website.

When I debugged, the image below  was what I observed;

  server {
    listen 8080;  // Incorrect port number
 197767-web-01 ubuntu.com;

    location / {
        proxy_pass http://backend_servers;
    }
}

upstream backend_servers {
    server 192.168.1.10;
    server 192.168.1.11;

   }

which is obviously the wrong configuration for Dbazz Ubuntu container’s Nginx installation which is supposed to be listening on `port 80`. Here, it is listening in `port 8080`.
The correct configuration is, here it is listening to `port 80`:

   server {
    listen 80;
    197767-web-01 ubuntu.com;

    location / {
        proxy_pass http://backend_servers;
    }
}

upstream backend_servers {
    server 192.168.1.10;
    server 192.168.1.11;

   }

Here is a Detailed Incident Report (Postmortem) on how the troubleshooting and debugging took place in Dbazz:

Issue Summary: The outage occurred on August 11, 2023, from 10:00 AM to 11:30 AM (UTC). During this period, the Nginx service was unavailable on the Ubuntu server, resulting in a complete disruption of web services. Users experienced slow page loading and were unable to access the Dbazz website hosted on the server. Approximately 85% of users were affected by the downtime.

Root Cause and Resolution: The root cause of the issue was a misconfigured Nginx server configuration. The Nginx process was not listening to port 80 due to a wrong port specification in the configuration file. As a result, incoming HTTP requests were not being properly handled.

To resolve the issue, the following steps were taken:
- Accessed the Nginx configuration file located at /etc/nginx/nginx.conf.
- Verified the listen directive in the default server block, which was set to listen 8080 instead of listen 80.
- Corrected the listen directive to listen 80.
- Restarted the Nginx service using the command sudo service nginx restart.

Similarly, the following Corrective and Preventative Measures to prevent similar issues in the future using the following actions will be taken:

- Implement automated configuration validation scripts to detect misconfigured settings.
- Establish stricter code review processes for configuration changes to critical services.
- Set up regular internal training sessions to educate team members about common misconfigurations.
- Create a comprehensive playbook for debugging and resolving service disruptions, including common pitfalls and their solutions.

In conclusion, the outage was caused by a misconfigured Nginx server that prevented it from listening to port 80, resulting in downtime for users. The incident was resolved by correcting the misconfiguration and restarting the Nginx service. Moving forward, more preventive measures will be implemented by I and the team to detect and address similar issues promptly, ensuring better service availability and user experience.

At Dbazz, we pride ourselves at giving the best experience to our customers, always.

Thank you for taking the required time (you, the amazing reader) to read my Incident Report to the end.

Please stay tuned for more insightful shares like this from me.
