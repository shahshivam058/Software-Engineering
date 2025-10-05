- IAAC : Infrastructure as a code 


- Application delivery with tradional infrastructre 
    - Business comes with requirments 
    - Business analyst provides high level technical spasefications , USE Cases 
    - Use case passed to solution architect or team lead they will design the applications 
    - They come with infrastructure need as they need infra where all applications can be deployed 
    - Provide hardware requirment to procurment team 
    - they make request to vendors 
    - they will take sometime to procure hardware 
    - as part of infra they will have a team will take care of organizing all staks 
    - they communicate with sys admins and network engineer for makings server available 
    - storage team and backup team will take care of respective domain 
    - whole process is time taking with above process each team require their time its uses kind of waterfall model 
    - everything is expensive , capital expenditure , procure to hardware as well as man power for managing servers
    - lots of people manage to data center 
    - chance of human error results in inconstitancy 
    - resources westage we many not able to do as soon as possible 
    - we need to go through whole process

- To solve above issue people have started using cloud computing 
- we can eliminate slow deployment. it provide pay as you go 
- based on demand we can provison or remove 
- pay for what service you are using 

- some of tasks are creating and managing infrastructure 
- we can automate 
- we have a scope for automation 
- How Cloud service can be managed :
    - Console (GUI) , Possibality of human error , Inconsistancy across envioumrnts 
    - To Manage Consistancy across env infrastructure as code came into picture :
        - Managing or provisoning infr using code 
        - as infra defined as code 
        - Through infrastructre you can achieve desiered state and infra which is reproducable 
        - combination of stanceard practices tools process to manage infrastructure 
        - Infra deployment is quick and error free 
        - we can use ci cd with code to deploy infra which maintain consistancy across all env 
        - with iac we can create a reusable module we can write anc call modules multiple times 
        - devops can write infra using terraform arm cloudformation 
        - configration files sent to master server , managment api 
        - platform takes files and apply changes 
        - there is configration managment tools for configration managment once resources are created for managing them 

Terraform :
- Terraform is Infrastructure as a code tool allows us to manage both cloud premised and on prem resources through human readable configrations files 
- Its cloud agnostic tool . written in go and was created by hashicorp 
- terraform has concept of provider has provider for all major cloud resources 
- terraform can manage low level components as well as high level components 
- terraform uses  write - plan - apply concept 


- Using terraform we can create a resource on any major cloud provider 
- How to manage cloud resources using console 

- In traddional architecture we had different server one just for database 
- On premise means Organization maintains all it infrastructure Needed by business is owned and locateted and used by compnies in their premises 
    - Time consuming 
    - Expensive
    - Limited scalabality 
    - Limited automation 

- Any application should be :
    - Highly available 
    - Fault Tolerent 
    - scalable 
    - Elasticity :  Grow and shrink Infrastructure as needed to handle workload in automatic manner 


- Cloud service : Service made available to user on demand via internet from cloud computing provider server 

- Cloud Computing :
    - On demand delivery of computing resources power usage via internet pay as you go 
    - Cloud Computing Service Provides Verious way we can access Resources , GUI , CLI , API , SDK 

- There are verious advantage of cloud services :
    - Highly available and reliable 
    - Scalable and elasticity 
    - Cost is less 
    - Speed 
    - Deploy Global Within minutes 


- Public Cloud :
    - Reqyired hardware and data centers  OWNED BY Managed By 3rd Party 
    - accisible to any one 
    - any one can create a resources on cloud 
    - AWS , Azure , GCP 

- Private Cloud :
    - Hardware Owned by Single Business Unit or company 
    - Company on premise data center is private cloud 

- Hybrid Cloud :
    - Combination of public and private cloud 
    - we can deploy securely and we can achieve compience requirments 
    - we can achieve availability as well as scalability

- Multi Cloud :
    - User Two or more cloud Computimg Platform 
    - more than one public cloud 



Cloud Computing services model :

- IAAS : Infrastructure as a service 
    - Provides raw computing resources like virtual machines, storage, and networking over the internet.
    - You manage the OS, applications, and configurations, while the provider manages the physical servers and data centers.
    - What you manage: Applications, runtime, data, middleware, and OS.
    - What provider manages: Virtualization, servers, storage, networking, data centers.  

- PaaS : Platform as a services 
    - Provides a ready-made platform (runtime environment + tools + frameworks) for developing and deploying applications.
    - You don’t manage OS or servers—just your code and configurations.
    - What you manage: Applications and data.
    - What provider manages: OS, runtime, middleware, servers, networking, storage, virtualization.

- SaaS : Software as a service 
    - Ready-to-use software applications delivered over the internet.
    - No need to worry about infrastructure, deployment, or updates—the provider manages everything.
    - What you manage: Just use the software (maybe some configuration).
    - What provider manages: Everything (infrastructure, platform, app updates, security, availability).

- Amazon is fastest growing cloud Provider 

- Amazon Sub company founded by amazon.com  Provide on demand cloud computing services 
    - Pay as you go 
    - elasticity 
    - flexibality 
    - security 
    - reliable and high perfomance 

- aws has a free tier refer limited usage of resources 
- aws provides Free tier for students for learning 
- under free tear they provides verious services 
- each service untill some limit are free 
- Only available for new accounts 


