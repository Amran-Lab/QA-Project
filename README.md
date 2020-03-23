# QA-Project
## Index

[Brief](#brief)
   * [My Solution](#mysolution)
   
[ERD and Diagrams](#erdanddiagrams)

[Risk Assessment](#RA)

[Trello and Planning](#TAP)
  * [Trello Before](#Tap1)
  * [Trello After](#Tap2)

[Deployment](#Deploy)
  * [Pipline](#Pipeline)

[Testing](#Testing)

[Retrospective](#Retro)  

<a name="brief"></a>

### Brief

The Brief was to create a CRUD (Create, Read, Update, Delete) functioning website made by flask and deployed by Jenkins. The website must also have a minimum of two tables in a relational databases.

I decided to create a website where users can post movie and game reviews. This would be the create part of CRUD. For the read functionality I would let users be able to see reviews of their own and other people's reviews. Update would work by editing a review that already exists and delete will be able to delete both records and users.

<a name="erdanddiagrams"></a>

### ERD

![GitHub Logo](https://github.com/Amran-Lab/QA-SFIA/blob/master/SFIA-Entity%20Relation%20Diagram.png?raw=true)

I have created 4 tables excluding the user table. The four tables are paired up with one of each pair being connected to the accounts table, meeting the requirements for the relational database.



<a name="RA"></a>

### Risk Assessment

| Risk Assessment                                 | Risk Factor | Mitigating                                        | New Risk Factor |
|-------------------------------------------------|-------------|---------------------------------------------------|-----------------|
| Corrupted Files                                 | 8/10        | Online Version Control                            | 3/10            |
| Deleted Files                                   | 6/10        | Online Version Control                            | 1/10            |
| Losing Git Password                             | 9/10        | Have Email Recovery                               | 2/10            |
| Falling Sick                                    | 9/10        | Maintain Health/Visiting Doc/Sanitizing/Isolating | 7/10            |
| Data of Site Leaked                             | 3/10        | Hashing/Storing Sensitive Information In Secure Locations             | 1/10            |
| Not Understanding Own Code                      | 7/10        | Good Commenting                                   | 5/10            |
| Underestimation of the time/resource commitment | 6/10        | Trello Board                                      | 4/10            |
| Running out of Money for Cloud                  | 3/10        | Pausing instance when not in use                  | 2/10            |
| Getting Hacked                                  | 7/10        | Strong password                                   | 4/10            |



\
\
\
\
\



<a name="TAP"></a>
<a name="TAP1"></a>

### Trello and Planning

![GitHub Logo](https://github.com/Amran-Lab/QA-SFIA/blob/master/Trello1.PNG?raw=true)




<a name="TAP2"></a>

![GitHub Logo](https://github.com/Amran-Lab/QA-SFIA/blob/master/Trello2.PNG?raw=true)



For my planning I used Trello. I have moved over tasks when completed to done or when something is ongoing such as the readme it is in the doing tab. I also have a tab of
for the user stories and requirements, to make sure I am meeting the requirements.



<a name="Deploy"></a>
<a name="Pipeline"></a>

### Deployment

![GitHub Logo](https://github.com/Amran-Lab/QA-SFIA/blob/master/Pipline1.PNG?raw=true)

<a name="Testing"></a>

### Testing

![GitHub Logo](https://github.com/Amran-Lab/QA-SFIA/blob/master/tests.png?raw=true)

![GitHub Logo](https://github.com/Amran-Lab/QA-SFIA/blob/master/cov.png?raw=true)

<a name="Retrospective"></a>

### Retrospective

I have created a flask application and deployed it onto a virtual machine with jenkins,
using Agile methodology. The application can connect to a gcp database and read write to it.
If I was to have more time or do it again I would allow functionality to users to be able to log in with a password, for a layer of authentication and security.
