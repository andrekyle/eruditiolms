"""Build a 50-question Final Exam for AZ-900.

Distribution per Skills Measured:
- Cloud concepts (25-30%):                      14 questions
- Azure architecture and services (35-40%):     19 questions
- Azure management and governance (30-35%):     17 questions
"""
from app import app, db, Course, Lesson, Quiz, Question, QuestionOption

EXAM_TITLE = 'Final Exam \u2014 AZ-900 Practice (50 Questions)'
LESSON_TITLE = 'Final Exam: AZ-900 Practice (50 Questions)'
# Also clean up the older 30-question variant if it exists
LEGACY_EXAM_TITLES = ['Final Exam \u2014 AZ-900 Practice (30 Questions)']
LEGACY_LESSON_TITLES = ['Final Exam: AZ-900 Practice (30 Questions)']

# Each Q: (question_html, [(option_html, is_correct), x4], feedback)
QUESTIONS = [
    # =============== Domain 1: Cloud concepts (8) ===============
    ('<p>Which cloud benefit allows you to add or remove resources almost instantly to match demand without long-term commitments?</p>',
     [('Elasticity', True),
      ('High availability', False),
      ('Disaster recovery', False),
      ('Fault tolerance', False)],
     'Elasticity is the ability to dynamically scale resources up or down to match changing demand.'),

    ('<p>A company wants to shift from buying servers up-front to paying only for what it consumes. Which financial model does this represent?</p>',
     [('CapEx (Capital Expenditure)', False),
      ('OpEx (Operational Expenditure)', True),
      ('Total Cost of Ownership (TCO)', False),
      ('Return on Investment (ROI)', False)],
     'Cloud computing uses a consumption-based OpEx model where you pay for resources as you use them rather than purchasing them up-front (CapEx).'),

    ('<p>Which cloud service model gives the customer the MOST control over the underlying operating system?</p>',
     [('Software as a Service (SaaS)', False),
      ('Platform as a Service (PaaS)', False),
      ('Infrastructure as a Service (IaaS)', True),
      ('Function as a Service (FaaS)', False)],
     'IaaS exposes the operating system to the customer, who is responsible for patching and configuring it. PaaS and SaaS abstract the OS away.'),

    ('<p>Microsoft 365 is an example of which cloud service model?</p>',
     [('IaaS', False),
      ('PaaS', False),
      ('SaaS', True),
      ('Serverless', False)],
     'Microsoft 365 delivers fully managed applications (Outlook, Word, Teams) over the internet \u2014 the defining characteristic of SaaS.'),

    ('<p>Which cloud model combines on-premises infrastructure with a public cloud, allowing data and applications to move between them?</p>',
     [('Public cloud', False),
      ('Private cloud', False),
      ('Hybrid cloud', True),
      ('Community cloud', False)],
     'A hybrid cloud integrates on-premises (private) infrastructure with a public cloud so workloads can be shared between the two.'),

    ('<p>Under the shared responsibility model for IaaS, who is responsible for patching the guest operating system on a virtual machine?</p>',
     [('Microsoft (the cloud provider)', False),
      ('The customer', True),
      ('Shared equally between Microsoft and the customer', False),
      ('Azure Update Manager, automatically with no customer action', False)],
     'For IaaS, the customer is responsible for the guest OS, including patching, configuration, and security. Microsoft is responsible for the physical hosts.'),

    ('<p>Which characteristic of cloud computing refers to a system\u2019s ability to remain operational during a component failure?</p>',
     [('Scalability', False),
      ('Elasticity', False),
      ('High availability', True),
      ('Agility', False)],
     'High availability means the system stays operational and accessible even when individual components fail, typically by using redundancy.'),

    ('<p>A workload that scales by adding more virtual machines of the same size is using which type of scaling?</p>',
     [('Vertical scaling (scale up)', False),
      ('Horizontal scaling (scale out)', True),
      ('Diagonal scaling', False),
      ('Manual scaling only', False)],
     'Horizontal scaling (scale out) adds more instances. Vertical scaling (scale up) increases the size of an existing instance.'),

    # =============== Domain 2: Azure architecture and services (12) ===============
    ('<p>Which Azure resource is the logical container used to group resources that share the same lifecycle, permissions, and policies?</p>',
     [('Subscription', False),
      ('Management group', False),
      ('Resource group', True),
      ('Region', False)],
     'A resource group is a logical container for resources deployed to Azure. Resources in the same group typically share lifecycle and access control.'),

    ('<p>What is an Azure region pair?</p>',
     [('Two regions in different geographies linked for low-latency networking', False),
      ('Two regions within the same geography, at least 300 miles apart, used for replication and sequential updates', True),
      ('A primary region and an on-premises datacenter joined by ExpressRoute', False),
      ('Two availability zones inside one region', False)],
     'Region pairs are two regions in the same geography (usually 300+ miles apart). Azure replicates some services between paired regions and applies platform updates sequentially.'),

    ('<p>Which Azure compute service lets you run small pieces of code on demand without managing servers, and is billed only when the code runs?</p>',
     [('Azure Virtual Machines', False),
      ('Azure App Service', False),
      ('Azure Functions', True),
      ('Azure Kubernetes Service', False)],
     'Azure Functions is a serverless compute service \u2014 you write a function and Azure runs and bills it only when it executes.'),

    ('<p>You need to deploy a managed Kubernetes cluster on Azure. Which service should you use?</p>',
     [('Azure Container Instances (ACI)', False),
      ('Azure Kubernetes Service (AKS)', True),
      ('Azure Virtual Machine Scale Sets', False),
      ('Azure Service Fabric', False)],
     'AKS provides a managed Kubernetes control plane so you only manage and pay for the agent nodes.'),

    ('<p>Which Azure storage service is most appropriate for storing large amounts of unstructured data such as images, videos, and backups?</p>',
     [('Azure Files', False),
      ('Azure Blob Storage', True),
      ('Azure Table Storage', False),
      ('Azure Queue Storage', False)],
     'Blob storage is optimized for storing massive amounts of unstructured data (objects) such as media files, documents, and backups.'),

    ('<p>You need an SMB file share that on-premises servers and Azure VMs can mount with a drive letter. Which service should you use?</p>',
     [('Azure Blob Storage', False),
      ('Azure Files', True),
      ('Azure Disk Storage', False),
      ('Azure Data Lake Storage Gen2', False)],
     'Azure Files provides fully managed SMB (and NFS) file shares that can be mounted from cloud or on-premises clients.'),

    ('<p>Which Azure networking service is used to securely connect an on-premises network to Azure over a private, dedicated connection that does NOT traverse the public internet?</p>',
     [('VPN Gateway', False),
      ('Azure Bastion', False),
      ('ExpressRoute', True),
      ('Azure Front Door', False)],
     'ExpressRoute provides a private, dedicated connection between on-premises and Azure through a connectivity provider \u2014 it does not use the public internet.'),

    ('<p>Which service allows you to securely RDP/SSH to a virtual machine in the Azure portal without exposing a public IP address on the VM?</p>',
     [('Azure VPN Gateway', False),
      ('Azure Bastion', True),
      ('Azure Firewall', False),
      ('Network Security Group', False)],
     'Azure Bastion provides browser-based RDP/SSH access through the portal over TLS, so the target VM does not need a public IP.'),

    ('<p>Which Azure service provides a globally distributed, multi-model NoSQL database with single-digit-millisecond latency?</p>',
     [('Azure SQL Database', False),
      ('Azure Cosmos DB', True),
      ('Azure Database for PostgreSQL', False),
      ('Azure Synapse Analytics', False)],
     'Azure Cosmos DB is the globally distributed, multi-model NoSQL service offering low-latency reads and writes worldwide.'),

    ('<p>An availability zone is BEST described as:</p>',
     [('A logical group of subscriptions used for governance', False),
      ('A physically separate datacenter within an Azure region, with independent power, cooling, and networking', True),
      ('A pair of Azure regions used for disaster recovery', False),
      ('A geographic boundary that contains one or more regions', False)],
     'Availability zones are physically separate datacenters within a single Azure region. Spreading resources across zones protects from datacenter-level failures.'),

    ('<p>You need to expose a public web app to the internet with global load balancing, SSL offload, and a web application firewall (WAF). Which service is the BEST fit?</p>',
     [('Azure Load Balancer', False),
      ('Azure Application Gateway', False),
      ('Azure Front Door', True),
      ('Azure Traffic Manager', False)],
     'Azure Front Door is a global, layer-7 entry point that provides global load balancing, SSL offload, and integrated WAF for public web applications.'),

    ('<p>Which migration tool helps you discover, assess, and migrate on-premises servers, databases, and web apps to Azure from a central hub?</p>',
     [('Azure Arc', False),
      ('Azure Migrate', True),
      ('Azure Site Recovery (only)', False),
      ('Azure Advisor', False)],
     'Azure Migrate is the central hub that coordinates discovery, assessment, and migration of servers, databases, web apps, and virtual desktops to Azure.'),

    # =============== Domain 3: Azure management and governance (10) ===============
    ('<p>You want to enforce that all virtual machines deployed to a subscription use only approved SKUs. Which service should you use?</p>',
     [('Microsoft Entra ID (formerly Azure AD)', False),
      ('Azure Policy', True),
      ('Azure Blueprints', False),
      ('Role-based access control (RBAC)', False)],
     'Azure Policy evaluates and enforces rules over resources \u2014 for example, restricting allowed VM SKUs or required tags.'),

    ('<p>Which Azure service is used to assign permissions that let users perform specific actions on specific resources?</p>',
     [('Azure Policy', False),
      ('Role-based access control (RBAC)', True),
      ('Microsoft Defender for Cloud', False),
      ('Azure Locks', False)],
     'RBAC controls who can do what on which Azure resources by assigning roles to security principals at a scope.'),

    ('<p>Which feature prevents users from accidentally deleting or modifying a critical Azure resource, even if they have full permissions?</p>',
     [('Resource locks (CanNotDelete / ReadOnly)', True),
      ('Azure Policy assignments', False),
      ('Tags', False),
      ('Management groups', False)],
     'Resource locks (CanNotDelete or ReadOnly) protect resources from accidental modification or deletion regardless of the user\u2019s RBAC permissions.'),

    ('<p>You need to organize multiple Azure subscriptions and apply policies and RBAC across all of them at once. What should you use?</p>',
     [('Resource groups', False),
      ('Management groups', True),
      ('Tags', False),
      ('Availability zones', False)],
     'Management groups sit above subscriptions and let you apply governance (policy, RBAC) across many subscriptions at once.'),

    ('<p>Which Azure tool provides personalized recommendations to improve cost, security, reliability, performance, and operational excellence?</p>',
     [('Azure Monitor', False),
      ('Azure Service Health', False),
      ('Azure Advisor', True),
      ('Microsoft Cost Management', False)],
     'Azure Advisor analyzes your configuration and usage and gives recommendations across cost, security, reliability, performance, and operational excellence.'),

    ('<p>Which tool helps you estimate the monthly cost of Azure services BEFORE you deploy them?</p>',
     [('Azure Pricing Calculator', True),
      ('Total Cost of Ownership (TCO) Calculator', False),
      ('Microsoft Cost Management', False),
      ('Azure Advisor', False)],
     'The Pricing Calculator lets you model a configuration of Azure services and see an estimated monthly cost before deployment. The TCO Calculator compares on-premises costs to Azure.'),

    ('<p>Which Azure SLA characteristic applies to a single-instance VM that uses Premium SSD disks for all operating system and data disks?</p>',
     [('No SLA is offered for single-instance VMs', False),
      ('99.9% connectivity uptime', True),
      ('99.95% (requires availability set)', False),
      ('99.99% (requires availability zones)', False)],
     'A single-instance VM with all Premium (or Ultra) SSDs has a 99.9% connectivity SLA. Availability sets reach 99.95%, and availability zones reach 99.99%.'),

    ('<p>Which support plan is the MINIMUM that provides 24x7 access to Microsoft support engineers by phone for non-critical issues?</p>',
     [('Basic', False),
      ('Developer', False),
      ('Standard', True),
      ('Free trial', False)],
     'Standard is the lowest paid support plan that includes 24x7 technical support by phone and email. Developer is business-hours only; Basic has no technical support.'),

    ('<p>Which Azure service shows the current health of Azure services in your regions and notifies you of planned maintenance and outages affecting your resources?</p>',
     [('Azure Advisor', False),
      ('Azure Monitor', False),
      ('Azure Service Health', True),
      ('Microsoft Defender for Cloud', False)],
     'Azure Service Health provides personalized alerts and guidance about Azure service issues, planned maintenance, and health advisories that affect your resources.'),

    ('<p>Which Azure tool is used to track and analyze your actual Azure spending and set budgets with alerts?</p>',
     [('Azure Pricing Calculator', False),
      ('Microsoft Cost Management', True),
      ('Azure Advisor', False),
      ('Azure Policy', False)],
     'Microsoft Cost Management lets you analyze actual spending, forecast costs, and create budgets with alerts. The Pricing Calculator only estimates costs before deployment.'),

    # =============== Domain 1: Cloud concepts (6 more) ===============
    ('<p>Which cloud deployment model is owned and used by a single organization and offers the highest level of control and isolation?</p>',
     [('Public cloud', False),
      ('Private cloud', True),
      ('Hybrid cloud', False),
      ('Multi-cloud', False)],
     'A private cloud is dedicated to a single organization, providing maximum control, customization, and isolation \u2014 typically at higher cost than public cloud.'),

    ('<p>Using more than one public cloud provider (for example, Azure and AWS) for different workloads is BEST described as:</p>',
     [('Hybrid cloud', False),
      ('Multi-cloud', True),
      ('Private cloud', False),
      ('Community cloud', False)],
     'A multi-cloud strategy uses services from two or more public cloud providers. Hybrid cloud specifically combines on-premises with public cloud.'),

    ('<p>In the shared responsibility model, which item is ALWAYS the customer\u2019s responsibility regardless of the service model (IaaS, PaaS, or SaaS)?</p>',
     [('Physical security of datacenters', False),
      ('Patching of host operating systems', False),
      ('Information and data, and user account/identity management', True),
      ('Network controls for the physical hosts', False)],
     'Data, devices, accounts, and identities are always the customer\u2019s responsibility across IaaS, PaaS, and SaaS. The provider always handles physical infrastructure.'),

    ('<p>A startup needs to launch a product quickly without buying servers and wants to expand to new regions easily. Which cloud benefit BEST describes this?</p>',
     [('Agility', True),
      ('Disaster recovery', False),
      ('Governance', False),
      ('Capital expense', False)],
     'Agility is the ability to rapidly provision resources and deploy to new locations \u2014 a hallmark of cloud computing.'),

    ('<p>What is a serverless compute model?</p>',
     [('A model where the customer manages virtual machines but not the network', False),
      ('A model where the cloud provider manages the underlying infrastructure and the customer is billed only for code execution', True),
      ('A model where applications run on dedicated bare-metal hardware', False),
      ('A private-cloud-only deployment style', False)],
     'Serverless abstracts away the servers \u2014 the provider runs and scales the infrastructure, and the customer pays only when code executes.'),

    ('<p>Increasing the size (CPU/RAM) of an existing VM to handle more load is an example of which scaling approach?</p>',
     [('Scale out (horizontal)', False),
      ('Scale up (vertical)', True),
      ('Elastic load balancing', False),
      ('Geo-replication', False)],
     'Scale up (vertical scaling) increases the resources of an existing instance. Scale out (horizontal) adds more instances.'),

    # =============== Domain 2: Azure architecture and services (7 more) ===============
    ('<p>Which Azure compute option is the FASTEST way to run a single container without orchestrating a cluster?</p>',
     [('Azure Kubernetes Service (AKS)', False),
      ('Azure Container Instances (ACI)', True),
      ('Azure Virtual Machines', False),
      ('Azure Service Fabric', False)],
     'ACI lets you run a container in Azure on demand with no cluster to manage \u2014 ideal for simple, isolated workloads.'),

    ('<p>Which Azure service provides a managed platform for hosting web apps, REST APIs, and mobile back-ends with built-in scaling and deployment slots?</p>',
     [('Azure Functions', False),
      ('Azure App Service', True),
      ('Azure Virtual Machines', False),
      ('Azure Batch', False)],
     'Azure App Service is a PaaS offering for web apps, APIs, and mobile back-ends, with built-in auto-scaling, custom domains, SSL, and deployment slots.'),

    ('<p>Which Azure storage tier offers the LOWEST storage cost but the HIGHEST retrieval cost and latency, suitable for long-term archival?</p>',
     [('Hot', False),
      ('Cool', False),
      ('Cold', False),
      ('Archive', True)],
     'The Archive access tier has the lowest storage cost but the highest retrieval cost and latency \u2014 ideal for data that is rarely accessed but must be retained long-term.'),

    ('<p>You need to distribute traffic across regional Azure backends based on DNS responses and routing methods such as performance and geographic. Which service should you use?</p>',
     [('Azure Application Gateway', False),
      ('Azure Load Balancer', False),
      ('Azure Traffic Manager', True),
      ('Azure Bastion', False)],
     'Traffic Manager is a DNS-based traffic load balancer that distributes user traffic across global Azure regions using methods like performance, geographic, and priority routing.'),

    ('<p>Which Azure service helps you manage and govern servers, Kubernetes clusters, and databases running OUTSIDE Azure (for example, on-premises or in other clouds)?</p>',
     [('Azure Arc', True),
      ('Azure Lighthouse', False),
      ('Azure Migrate', False),
      ('Azure Stack Hub', False)],
     'Azure Arc extends Azure management and governance (policy, RBAC, monitoring) to resources running on-premises and in other clouds.'),

    ('<p>Which database service is a fully managed relational database engine based on the latest stable Microsoft SQL Server?</p>',
     [('Azure Database for MySQL', False),
      ('Azure Cosmos DB', False),
      ('Azure SQL Database', True),
      ('Azure Synapse Analytics', False)],
     'Azure SQL Database is a fully managed PaaS relational database engine built on the latest stable SQL Server. Cosmos DB is NoSQL; Synapse is an analytics service.'),

    ('<p>Which Azure offering provides a managed virtual desktop and remote app delivery service, supporting Windows 11 multi-session?</p>',
     [('Azure Bastion', False),
      ('Azure Virtual Desktop (AVD)', True),
      ('Azure App Service', False),
      ('Azure Virtual WAN', False)],
     'Azure Virtual Desktop delivers a managed virtual desktop and remote app experience, including multi-session Windows 10/11.'),

    # =============== Domain 3: Azure management and governance (7 more) ===============
    ('<p>Which feature in Microsoft Entra ID requires users to provide additional verification (such as a phone or app prompt) beyond a password?</p>',
     [('Conditional Access', False),
      ('Multi-factor authentication (MFA)', True),
      ('Privileged Identity Management (PIM)', False),
      ('Single sign-on (SSO)', False)],
     'MFA strengthens sign-in security by requiring two or more verification methods. Conditional Access can enforce MFA based on conditions.'),

    ('<p>Which Microsoft Entra ID feature lets administrators enforce policies such as "require MFA when accessing from outside the corporate network"?</p>',
     [('Privileged Identity Management', False),
      ('Identity Protection (only)', False),
      ('Conditional Access', True),
      ('Microsoft Defender for Identity', False)],
     'Conditional Access uses signals (user, location, device, app, risk) to enforce access policies such as requiring MFA or blocking access.'),

    ('<p>Which service provides unified security posture management and threat protection across Azure, hybrid, and multi-cloud workloads?</p>',
     [('Microsoft Defender for Cloud', True),
      ('Microsoft Sentinel', False),
      ('Azure Advisor', False),
      ('Azure Service Health', False)],
     'Microsoft Defender for Cloud is a CSPM/CWPP solution that assesses security posture and protects workloads across Azure, hybrid, and other clouds.'),

    ('<p>Which Azure service is a cloud-native SIEM and SOAR solution that collects security data across the enterprise for detection, investigation, and response?</p>',
     [('Microsoft Defender for Cloud', False),
      ('Microsoft Sentinel', True),
      ('Azure Monitor', False),
      ('Azure Policy', False)],
     'Microsoft Sentinel is the cloud-native SIEM/SOAR that ingests security logs and orchestrates detection and response.'),

    ('<p>Which tool centrally collects metrics and logs from Azure resources and lets you create alerts, dashboards, and workbooks?</p>',
     [('Azure Service Health', False),
      ('Azure Monitor', True),
      ('Microsoft Cost Management', False),
      ('Azure Blueprints', False)],
     'Azure Monitor is the unified observability platform for collecting metrics and logs and configuring alerts, dashboards, and workbooks.'),

    ('<p>You want to group resources from many subscriptions for billing purposes using metadata key/value pairs (for example, costCenter=Finance). Which feature should you use?</p>',
     [('Resource locks', False),
      ('Tags', True),
      ('Management groups', False),
      ('Azure Policy', False)],
     'Tags are key/value metadata applied to resources and resource groups. Cost Management can group costs by tag.'),

    ('<p>Under most Azure online service-level agreements, what is the customer\u2019s typical remedy if Microsoft fails to meet the published SLA?</p>',
     [('A full refund of all subscription fees for the affected service', False),
      ('A service credit applied to a future bill', True),
      ('Free migration to another Azure region', False),
      ('No remedy; SLAs are best-effort only', False)],
     'Azure SLAs provide service credits (a percentage of the monthly bill for the affected service), not refunds, when uptime targets are missed.'),
]


def upsert():
    assert len(QUESTIONS) == 50, f'expected 50 questions, got {len(QUESTIONS)}'
    for qh, opts, fb in QUESTIONS:
        assert len(opts) == 4, 'each question must have 4 options'
        assert sum(1 for _, c in opts if c) == 1, f'each question needs exactly 1 correct option: {qh[:60]}'

    with app.app_context():
        course = Course.query.filter(Course.title.like('AZ-9%')).first()
        if not course:
            raise SystemExit('AZ-9xx course not found')
        print(f'course: id={course.id} title={course.title!r}')

        # Remove any legacy 30-question variants so the course shows only the 50-Q exam
        for old_title in LEGACY_LESSON_TITLES:
            old_lesson = Lesson.query.filter_by(course_id=course.id, title=old_title).first()
            if old_lesson:
                db.session.delete(old_lesson)
                print(f'deleted legacy lesson: {old_title!r}')
        for old_qtitle in LEGACY_EXAM_TITLES:
            old_quiz = Quiz.query.filter_by(course_id=course.id, title=old_qtitle).first()
            if old_quiz:
                for q in list(old_quiz.questions):
                    db.session.delete(q)
                db.session.delete(old_quiz)
                print(f'deleted legacy quiz: {old_qtitle!r}')
        db.session.flush()

        # Find or create the quiz
        quiz = Quiz.query.filter_by(course_id=course.id, title=EXAM_TITLE).first()
        if quiz:
            # Wipe existing questions for clean rebuild
            for q in list(quiz.questions):
                db.session.delete(q)
            db.session.flush()
            print(f'reusing quiz id={quiz.id}, cleared old questions')
        else:
            quiz = Quiz(
                course_id=course.id,
                title=EXAM_TITLE,
                description='A 50-question practice exam covering all three AZ-900 skill domains: Cloud concepts (25-30%), Azure architecture and services (35-40%), and Azure management and governance (30-35%).',
            )
            db.session.add(quiz)
            db.session.flush()
            print(f'created quiz id={quiz.id}')

        # Insert questions
        for qh, opts, fb in QUESTIONS:
            q = Question(
                quiz_id=quiz.id,
                question_type='multiple_choice',
                question_html=qh,
                points=1.0,
                feedback=fb,
            )
            db.session.add(q)
            db.session.flush()
            for i, (oh, is_correct) in enumerate(opts):
                db.session.add(QuestionOption(
                    question_id=q.id,
                    option_html=oh,
                    is_correct=is_correct,
                    order=i,
                ))

        # Find or create the lesson (exam) entry; place it as the new last item
        lesson = Lesson.query.filter_by(course_id=course.id, title=LESSON_TITLE).first()
        # determine the highest existing order excluding the legacy parked exam
        max_order = db.session.query(db.func.max(Lesson.order)).filter(
            Lesson.course_id == course.id
        ).scalar() or 0
        new_order = max_order + 1

        if lesson:
            lesson.quiz_id = quiz.id
            lesson.content_type = 'exam'
            lesson.order = new_order
            print(f'updated existing lesson id={lesson.id} order={new_order}')
        else:
            lesson = Lesson(
                course_id=course.id,
                title=LESSON_TITLE,
                content='<p>This 50-question practice exam mirrors the structure and difficulty of the AZ-900 exam. Take it under timed conditions to gauge your readiness.</p>',
                content_type='exam',
                quiz_id=quiz.id,
                order=new_order,
                points=1.0,
            )
            db.session.add(lesson)
            print(f'created new lesson order={new_order}')

        db.session.commit()
        print(f'DONE. quiz_id={quiz.id} questions={len(quiz.questions)} lesson_order={new_order}')


if __name__ == '__main__':
    upsert()
