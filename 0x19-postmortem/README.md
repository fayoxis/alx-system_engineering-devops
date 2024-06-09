🧮 BOTH MANDATORY OR ADVCANCED QUESTION ANSWERED HERE  🧑


0. My first postmortem
:Postmortem: Resolving the Dbazz Website Downtime 💯 🧑‍⚖️

It was a sudden and alarming situation when our highly popular website, Dbazz Website, which is widely used by Africans in the Diaspora to transfer money in any currency to their families back home without any hidden charges or costs, went DOWN!

The panic was real because we have close to 50 million individuals who visit our website daily to perform various transactions, and we could not afford to lose our dedicated customers to competition. As one of Dbazz's System DevOps Engineers, it was my primary responsibility to debug and resolve such issues when they arise, which happens occasionally.

To solve this, I performed all the required system administration and configuration management checks by troubleshooting and debugging. This was done to identify and resolve issues related to system performance and configuration to understand the root cause of the problem.

During the debugging process, I spotted the bug: Something was preventing Dbazz's Ubuntu container's Nginx installation from listening on port 80. This is highly problematic because if Nginx is not listening on port 80, it can lead to the servers being inaccessible from the internet. Port 80 is the default port for HTTP traffic, and if Nginx is not properly configured to listen on this port, incoming web requests won't be directed to the appropriate backend servers, resulting in a downtime situation, which was the case with the Dbazz Website.

When I debugged, the observed configuration was as follows:

server {
    listen 8080;  // Incorrect port number
    server_name 197767-web-01.ubuntu.com;

    location / {
        proxy_pass http://backend_servers;
    }
}

upstream backend_servers {
    server 192.168.1.10;
    server 192.168.1.11;
}


This configuration was obviously incorrect for Dbazz's Ubuntu container's Nginx installation, which was supposed to be listening on port 80. Instead, it was listening on port 8080.

The correct configuration should be:


server {
    listen 80;
    server_name 197767-web-01.ubuntu.com;

    location / {
        proxy_pass http://backend_servers;
    }
}

upstream backend_servers {
    server 192.168.1.10;
    server 192.168.1.11;
}

This detailed incident report (postmortem) outlines the troubleshooting and debugging process that took place to resolve the Dbazz Website downtime.

Changes:
1. Changed "ever so often" to "occasionally" to better reflect the frequency.
2. Added "server_name" directive in the Nginx configuration blocks, which was missing.
3. Corrected minor grammar and phrasing issues.
## Issue Summary

On August 11, 2023, our website experienced a significant outage from 10:00 AM to 11:30 AM UTC. During this period, the Nginx service, which is the backbone of our web server infrastructure, went down, resulting in a complete disruption of our services. Users reported slow page loading times and were ultimately unable to access our website. Approximately 85% of our user base was affected by this downtime, causing widespread frustration and potential loss of trust in our platform.

The root cause of the issue was a misconfigured Nginx server configuration, which prevented the service from listening on the default HTTP port (80).

## Timeline

- 10:05 AM UTC: The issue was detected by our monitoring system, which raised an alert regarding the unresponsiveness of our web servers.
- 10:10 AM UTC: Our on-call DevOps engineer acknowledged the alert and initiated an investigation.
- 10:15 AM UTC: The initial assumption was that the issue might be related to a sudden spike in web traffic, leading to resource exhaustion.
- 10:30 AM UTC: After ruling out the traffic spike hypothesis, the investigation shifted towards potential network issues and firewall configurations.
- 10:45 AM UTC: Escalation to the broader DevOps team and senior engineers took place as the root cause remained elusive.
- 11:00 AM UTC: A thorough review of the Nginx configuration files revealed the culprit – the service was misconfigured to listen on the wrong port.
- 11:15 AM UTC: The issue was resolved by correcting the Nginx configuration and restarting the service.
- 11:30 AM UTC: Monitoring confirmed that the web servers were back online, and user traffic was gradually restored.

## Root Cause and Resolution

The root cause of the outage was a misconfigured Nginx server configuration file. Instead of listening on the default HTTP port (80), the configuration had been mistakenly set to listen on port 8080. As a result, incoming HTTP requests were not being properly handled, leading to the website becoming inaccessible.

:accessibility: Make people want to read your postmortem
To resolve the issue, the following steps were taken:

1. The Nginx configuration file (`/etc/nginx/nginx.conf`) was accessed and inspected.
2. The `listen` directive in the default server block was identified as `listen 8080` instead of `listen 80`.
3. The incorrect port specification was corrected by changing `listen 8080` to `listen 80`.
4. The Nginx service was restarted using the command `sudo systemctl restart nginx`.
5. Monitoring confirmed that the service was now listening on the correct port, and web traffic was successfully being handled.

## Corrective and Preventative Measures

While the issue was resolved promptly, we recognize the need for improvements to prevent similar incidents from occurring in the future. To this end, the following corrective and preventative measures will be implemented:

- Automated configuration validation scripts will be developed and integrated into our deployment pipeline to detect misconfigured settings before they reach production environments.
- Stricter code review processes will be established for configuration changes to critical services, ensuring multiple pairs of eyes review and approve changes before deployment.
- Regular internal training sessions will be conducted to educate team members about common misconfigurations, best practices, and the importance of thorough testing.
- A comprehensive playbook for debugging and resolving service disruptions will be created, including common pitfalls, their solutions, and clear escalation paths.

By implementing these measures, we aim to enhance our overall system reliability, reduce the likelihood of similar incidents, and foster a culture of continuous improvement within our DevOps team.

## Closing Thoughts

In the ever-evolving world of technology, even the smallest misconfiguration can have significant consequences. While we deeply regret the inconvenience caused to our users, this incident has served as a valuable learning experience. We remain committed to providing the best possible service and user experience, and we will continue to prioritize system stability and resilience.

0. My first postmortem
**Issue Summary**

- Duration: The outage lasted for 7 hours, from 2:00 AM to 9:00 AM UTC on June 1st, 2023.
- Impact: Our e-commerce website experienced severe slowdowns and intermittent downtime, affecting approximately 60% of our user base. Customers were unable to browse products, add items to their carts, or complete purchases during this period.
- Root Cause: The issue was caused by a memory leak in our Nginx web server, leading to resource exhaustion and service disruption.

**Timeline**

- 2:15 AM - The issue was detected by our monitoring system, which flagged elevated response times and error rates on the website.
- 2:30 AM - The on-call engineering team was alerted and began investigating the issue.
- 3:00 AM - Initial investigations pointed to a potential database issue, but after examining logs and metrics, the team ruled out the database as the root cause.
- 4:30 AM - The incident was escalated to the web server team, who noticed increasing memory consumption on the Nginx servers.
- 5:45 AM - After several failed attempts to mitigate the issue by restarting Nginx and adjusting configurations, the team decided to redeploy the web servers with updated Nginx binaries.
- 7:30 AM - The redeployment process was completed successfully, and the website gradually began to recover.
- 9:00 AM - The website was fully operational, and the incident was resolved.
  
🪗Make people want to read your postmortem

**Root Cause and Resolution**

The root cause of the outage was a memory leak in the version of Nginx deployed on our web servers. With each incoming request, a small amount of memory was not being properly released, leading to a gradual buildup of memory consumption over time. Once the servers reached critical memory levels, Nginx became unresponsive, causing the website to slow down and eventually crash.

To resolve the issue, we redeployed the web servers with an updated version of Nginx that had the memory leak fixed. Additionally, we implemented stricter memory monitoring and automatic restarts for Nginx processes exceeding configurable thresholds.

**Corrective and Preventative Measures**

- Conduct thorough testing and review of software updates, including third-party components like Nginx, before deploying to production environments.
- Implement comprehensive monitoring for critical system resources (CPU, memory, disk) on all production servers, with appropriate alert thresholds and automated remediation actions.
- Establish a robust incident management process, including clear escalation paths and communication channels, to ensure efficient coordination during outages.
- Review and update our disaster recovery plan to minimize the impact of similar incidents in the future.
- Regularly review and update our software stack, adhering to the latest stable releases and security patches.

**ToDo List**

- Patch Nginx servers across all environments with the latest stable version.
- Configure Prometheus monitoring for Nginx memory usage, with alerts and automatic restarts.
- Conduct a retrospective meeting to review the incident response process and identify areas for improvement.
- Schedule periodic load testing and stress testing of the website to identify potential bottlenecks and vulnerabilities.
- Implement a centralized logging and monitoring solution for easier troubleshooting and root cause analysis.

To make this postmortem more engaging, we could include a humorous anecdote or metaphor related to the incident, or perhaps a lighthearted cartoon diagram illustrating the sequence of events. The goal is to capture the reader's attention while maintaining a professional and informative tone.

BY
Name : Arthur Tchaye I : dtchayearthur@gmail.som : Fayoxis 
