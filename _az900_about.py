"""Replace AZ-900 About lesson content with the official Skills Measured (Jan 14, 2026)
study guide rendered as semantic HTML. Idempotent."""
from app import app, db, Course, Lesson

COURSE_TITLE_LIKE = 'AZ-900%'
ABOUT_TITLE = 'About this course'

ABOUT_HTML = """
<h2>Purpose of this document</h2>
<p>This study guide should help you understand what to expect on the AZ-900 exam and includes a summary of the topics the exam might cover and links to additional resources. The information and materials in this document should help you focus your studies as you prepare for the exam.</p>

<table>
  <thead>
    <tr><th>Useful links</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td>Review the skills measured as of January 14, 2026</td><td>This list represents the skills measured on the exam after the date shown. Study this list if you plan to take the exam after that date.</td></tr>
    <tr><td>How to earn the certification</td><td>Some certifications only require passing one exam, while others require passing multiple.</td></tr>
    <tr><td>Certification renewal</td><td>Microsoft associate, expert, and specialty certifications expire annually. You can renew by passing a free online assessment on Microsoft Learn.</td></tr>
    <tr><td>Your Microsoft Learn profile</td><td>Connecting your certification profile to Microsoft Learn helps you schedule and renew exams and share and print certificates.</td></tr>
    <tr><td>Exam scoring and score reports</td><td>A score of 700 or greater is required to pass.</td></tr>
    <tr><td>Exam sandbox</td><td>You can explore the exam environment by visiting the exam sandbox.</td></tr>
    <tr><td>Request accommodations</td><td>If you use assistive devices, require extra time, or need modification to any part of the exam experience, you can request an accommodation.</td></tr>
  </tbody>
</table>

<h2>About the exam</h2>
<p>The content of this exam was updated on January 14, 2026. Please download the exam skills outline to see what changed.</p>

<blockquote><p><strong>Note:</strong> Passing score: 700. Learn more about exam scores.</p></blockquote>
<blockquote><p><strong>Note:</strong> The English version of this exam was updated on January 14, 2026. Review the study guide available on the Microsoft Learn exam page for details about recent changes. If there is a localized version of this exam, it will be updated approximately eight weeks after this date. While Microsoft makes every effort to update localized versions as noted, there may be times when the localized versions of an exam are not updated on this schedule.</p></blockquote>

<h2>Skills measured as of January 14, 2026</h2>

<h3>Audience profile</h3>
<p>As a candidate for this exam, you&rsquo;re a technology professional who wants to demonstrate foundational knowledge of cloud concepts in general and Microsoft Azure in particular. This exam is a common starting point in a journey towards a career in Azure.</p>
<p>You can describe Azure architectural components and Azure services, such as:</p>
<ul>
  <li>Compute</li>
  <li>Networking</li>
  <li>Storage</li>
</ul>
<p>You can also describe features and tools to secure, govern, and administer Azure.</p>
<p>You should have skills and experience working with an area of IT, such as:</p>
<ul>
  <li>Infrastructure management</li>
  <li>Database management</li>
  <li>Software development</li>
</ul>

<h3>Skills at a glance</h3>
<ul>
  <li>Describe cloud concepts (25&ndash;30%)</li>
  <li>Describe Azure architecture and services (35&ndash;40%)</li>
  <li>Describe Azure management and governance (30&ndash;35%)</li>
</ul>

<h2>Describe cloud concepts (25&ndash;30%)</h2>

<h3>Describe cloud computing</h3>
<ul>
  <li>Define cloud computing</li>
  <li>Describe the shared responsibility model</li>
  <li>Define cloud models, including public, private, and hybrid</li>
  <li>Identify appropriate use cases for each cloud model</li>
  <li>Describe the consumption-based model</li>
  <li>Compare cloud pricing models</li>
  <li>Describe serverless</li>
</ul>

<h3>Describe the benefits of using cloud services</h3>
<ul>
  <li>Describe the benefits of high availability and scalability in the cloud</li>
  <li>Describe the benefits of reliability and predictability in the cloud</li>
  <li>Describe the benefits of security and governance in the cloud</li>
  <li>Describe the benefits of manageability in the cloud</li>
</ul>

<h3>Describe cloud service types</h3>
<ul>
  <li>Describe infrastructure as a service (IaaS)</li>
  <li>Describe platform as a service (PaaS)</li>
  <li>Describe software as a service (SaaS)</li>
  <li>Identify appropriate use cases for each cloud service type (IaaS, PaaS, and SaaS)</li>
</ul>

<h2>Describe Azure architecture and services (35&ndash;40%)</h2>

<h3>Describe the core architectural components of Azure</h3>
<ul>
  <li>Describe Azure regions, region pairs, and sovereign regions</li>
  <li>Describe availability zones</li>
  <li>Describe Azure datacenters</li>
  <li>Describe Azure resources and resource groups</li>
  <li>Describe subscriptions</li>
  <li>Describe management groups</li>
  <li>Describe the hierarchy of resource groups, subscriptions, and management groups</li>
</ul>

<h3>Describe Azure compute and networking services</h3>
<ul>
  <li>Compare compute types, including containers, virtual machines, and functions</li>
  <li>Describe virtual machine options, including Azure virtual machines, Azure Virtual Machine Scale Sets, availability sets, and Azure Virtual Desktop</li>
  <li>Describe the resources required for virtual machines</li>
  <li>Describe application hosting options, including web apps, containers, and virtual machines</li>
  <li>Describe virtual networking, including the purpose of Azure virtual networks, Azure virtual subnets, peering, Azure DNS, Azure VPN Gateway, and ExpressRoute</li>
  <li>Define public and private endpoints</li>
</ul>

<h3>Describe Azure storage services</h3>
<ul>
  <li>Compare Azure Storage services</li>
  <li>Describe storage tiers</li>
  <li>Describe redundancy options</li>
  <li>Describe storage account options and storage types</li>
  <li>Identify options for moving files, including AzCopy, Azure Storage Explorer, and Azure File Sync</li>
  <li>Describe migration options, including Azure Migrate and Azure Data Box</li>
</ul>

<h3>Describe Azure identity, access, and security</h3>
<ul>
  <li>Describe directory services in Azure, including Microsoft Entra ID and Microsoft Entra Domain Services</li>
  <li>Describe authentication methods in Azure, including single sign-on (SSO), multifactor authentication (MFA), and passwordless</li>
  <li>Describe external identities in Azure</li>
  <li>Describe Microsoft Entra Conditional Access</li>
  <li>Describe Azure role-based access control (RBAC)</li>
  <li>Describe the concept of Zero Trust</li>
  <li>Describe the purpose of the defense-in-depth model</li>
  <li>Describe the purpose of Microsoft Defender for Cloud</li>
</ul>

<h2>Describe Azure management and governance (30&ndash;35%)</h2>

<h3>Describe cost management in Azure</h3>
<ul>
  <li>Describe factors that can affect costs in Azure</li>
  <li>Explore the pricing calculator</li>
  <li>Describe cost management capabilities in Azure</li>
  <li>Describe the purpose of tags</li>
</ul>

<h3>Describe features and tools in Azure for governance and compliance</h3>
<ul>
  <li>Describe the purpose of Microsoft Purview in Azure</li>
  <li>Describe the purpose of Azure Policy</li>
  <li>Describe the purpose of resource locks</li>
</ul>

<h3>Describe features and tools for managing and deploying Azure resources</h3>
<ul>
  <li>Describe the Azure portal</li>
  <li>Describe Azure Cloud Shell, including Azure Command-Line Interface (CLI) and Azure PowerShell</li>
  <li>Describe the purpose of Azure Arc</li>
  <li>Describe infrastructure as code (IaC)</li>
  <li>Describe Azure Resource Manager (ARM) and ARM templates</li>
</ul>

<h3>Describe monitoring tools in Azure</h3>
<ul>
  <li>Describe the purpose of Azure Advisor</li>
  <li>Describe Azure Service Health</li>
  <li>Describe Azure Monitor, including Log Analytics, Azure Monitor alerts, and Application Insights</li>
</ul>

<h2>How this course is aligned</h2>
<p>The six content lessons in this course map directly onto the Skills Measured outline above:</p>
<table>
  <thead>
    <tr><th>Lesson</th><th>Skills Measured domain covered</th></tr>
  </thead>
  <tbody>
    <tr><td>Lesson 3 &mdash; Cloud Concepts</td><td>Describe cloud concepts (25&ndash;30%) &mdash; cloud computing, shared responsibility, cloud models, benefits, IaaS/PaaS/SaaS</td></tr>
    <tr><td>Lesson 4 &mdash; Azure Architecture and Core Services</td><td>Describe the core architectural components of Azure (regions, availability zones, datacenters, resources, resource groups, subscriptions, management groups)</td></tr>
    <tr><td>Lesson 5 &mdash; Azure Compute and Networking Services</td><td>Describe Azure compute and networking services (VMs, VMSS, containers, functions, App Service, VNets, peering, DNS, VPN Gateway, ExpressRoute, endpoints)</td></tr>
    <tr><td>Lesson 6 &mdash; Azure Storage Services</td><td>Describe Azure storage services (Blob, Files, Queues, Tables; tiers; redundancy; AzCopy, Storage Explorer, File Sync, Azure Migrate, Data Box)</td></tr>
    <tr><td>Lesson 7 &mdash; Azure Identity, Access, and Security</td><td>Describe Azure identity, access, and security (Entra ID, SSO/MFA/passwordless, external identities, Conditional Access, RBAC, Zero Trust, defense-in-depth, Defender for Cloud)</td></tr>
    <tr><td>Lesson 8 &mdash; Azure Cost Management, SLAs, and Governance</td><td>Describe Azure management and governance (30&ndash;35%) &mdash; pricing factors, calculator, Cost Management, tags, Purview, Azure Policy, resource locks, portal, Cloud Shell, Arc, IaC, ARM, Advisor, Service Health, Monitor</td></tr>
  </tbody>
</table>

<h2>Study resources</h2>
<p>We recommend that you train and get hands-on experience before you take the exam. We offer self-study options and classroom training as well as links to documentation, community sites, and videos.</p>
<table>
  <thead>
    <tr><th>Study resources</th><th>Links to learning and documentation</th></tr>
  </thead>
  <tbody>
    <tr><td>Get trained</td><td>Choose from self-paced learning paths and modules or take an instructor-led course</td></tr>
    <tr><td>Find documentation</td><td>Azure on Microsoft Learn; Azure documentation; Microsoft Cloud Adoption Framework for Azure; Accelerate cloud adoption with the Microsoft Cloud Adoption Framework for Azure</td></tr>
    <tr><td>Ask a question</td><td>Microsoft Q&amp;A | Microsoft Docs</td></tr>
    <tr><td>Get community support</td><td>Azure Community Support</td></tr>
    <tr><td>Follow Microsoft Learn</td><td>Microsoft Learn - Microsoft Tech Community</td></tr>
    <tr><td>Find a video</td><td>Exam Readiness Zone; Azure Fridays; Browse other Microsoft Learn shows</td></tr>
  </tbody>
</table>
"""


def run():
    with app.app_context():
        course = Course.query.filter(Course.title.like(COURSE_TITLE_LIKE)).first()
        if not course:
            print(f'{COURSE_TITLE_LIKE} not found.')
            return
        about = Lesson.query.filter_by(course_id=course.id, title=ABOUT_TITLE).first()
        if not about:
            print(f'About lesson not found in {course.title}.')
            return
        about.content = ABOUT_HTML.strip()
        about.content_type = 'lesson'
        db.session.commit()
        print(f'updated About lesson {about.id} for {course.title} ({len(ABOUT_HTML)} chars).')


if __name__ == '__main__':
    run()
