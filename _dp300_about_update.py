"""Replace the DP-300 'About this course' lesson body with a summary of the
official Microsoft study guide for Exam DP-300 (skills measured as of
April 24, 2026). Idempotent: re-running just refreshes the content.
"""
from app import app, db, Lesson

LESSON_ID = 17

CONTENT = """
<h2>Study Guide Summary — Exam DP-300: Administering Microsoft Azure SQL Solutions</h2>

<p>This About page summarizes the official Microsoft <em>Study Guide for Exam DP-300</em>
(skills measured as of <strong>April 24, 2026</strong>). Use it to scope your preparation,
plan study sessions, and check coverage before sitting the exam.</p>

<h3>Purpose</h3>
<p>DP-300 leads to the <strong>Microsoft Certified: Azure Database Administrator Associate</strong>
credential. The exam validates that you can administer SQL Server-based database solutions
running across <strong>Azure SQL Database</strong>, <strong>Azure SQL Managed Instance</strong>,
<strong>SQL Server on Azure Virtual Machines</strong>, and <strong>SQL Server on-premises</strong>.
A scaled score of <strong>700 or greater</strong> is required to pass.</p>

<h3>Audience profile</h3>
<p>You are a database administrator who:</p>
<ul>
  <li>Implements and manages cloud-native and hybrid data platforms built on Azure SQL services and SQL Server.</li>
  <li>Uses <strong>T-SQL</strong> and a variety of Azure tools to automate day-to-day operations.</li>
  <li>Owns <strong>management, availability, security, and performance</strong> of database solutions.</li>
  <li>Evaluates and implements <strong>migration strategies</strong> between on-premises and Azure.</li>
  <li>Collaborates with Azure data engineers, solution architects, developers, and data scientists.</li>
</ul>

<h3>Skills measured at a glance</h3>
<table class="table table-bordered table-striped">
  <thead>
    <tr><th>Functional area</th><th>Weight</th></tr>
  </thead>
  <tbody>
    <tr><td>Plan and implement data platform resources</td><td>15–20%</td></tr>
    <tr><td>Implement a secure environment</td><td>20–25%</td></tr>
    <tr><td>Monitor, configure, and optimize database resources</td><td>20–25%</td></tr>
    <tr><td>Configure and manage automation of tasks</td><td>15–20%</td></tr>
    <tr><td>Plan and configure a high availability and disaster recovery (HA/DR) environment</td><td>20–25%</td></tr>
  </tbody>
</table>

<h3>1. Plan and implement data platform resources (15–20%)</h3>
<ul>
  <li><strong>Plan and deploy Azure SQL solutions:</strong> recommend a database offering, choose an automated deployment method, identify use cases for <em>Azure Arc-enabled SQL services</em> and <em>Azure SQL Database in Microsoft Fabric</em>, plan table partitioning, recommend sharding, deploy hybrid SQL Server solutions, and apply patches/updates for hybrid and IaaS deployments.</li>
  <li><strong>Configure resources for scale and performance:</strong> tune Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure VMs; configure table partitioning and data compression.</li>
  <li><strong>Migration strategy:</strong> evaluate requirements, choose between offline and online migrations, implement migrations to Azure or between Azure SQL services, perform Managed Instance database copy/move, and troubleshoot migrations.</li>
</ul>

<h3>2. Implement a secure environment (20–25%)</h3>
<ul>
  <li><strong>Authentication and authorization:</strong> configure Microsoft Entra ID auth for Azure SQL Database, Managed Instance, and SQL Server; configure security principals; create users from Entra identities; manage permissions with graphical tools and T-SQL; apply least privilege; troubleshoot access issues.</li>
  <li><strong>Data at rest and in transit:</strong> Transparent Data Encryption (TDE), object-level encryption, server/database firewall rules, Always Encrypted (including VBS enclaves), private links, and service endpoints.</li>
  <li><strong>Compliance for sensitive data:</strong> data classification, server/database audits, change data tracking, dynamic data masking, ledger in Azure SQL, row-level security.</li>
</ul>

<h3>3. Monitor, configure, and optimize database resources (20–25%)</h3>
<ul>
  <li><strong>Monitor activity and performance:</strong> set a baseline, pick metric sources, interpret metrics, use <em>database watcher</em> and <em>Extended Events</em>.</li>
  <li><strong>Query performance:</strong> Query Store, blocking-session diagnosis, DMVs, index changes, query rewrites, execution-plan review, Intelligent Insights.</li>
  <li><strong>Optimal performance:</strong> index/statistics maintenance, integrity checks, automatic tuning, server settings, Resource Governor, database-scoped configuration, compute/storage scaling, intelligent query processing (IQP).</li>
</ul>

<h3>4. Configure and manage automation of tasks (15–20%)</h3>
<ul>
  <li><strong>SQL Server Agent jobs:</strong> schedules, alerts/notifications, troubleshooting.</li>
  <li><strong>Automated deployment:</strong> ARM/Bicep templates, Azure PowerShell, Azure CLI; monitor and troubleshoot deployments.</li>
  <li><strong>Azure database tasks:</strong> create/configure elastic jobs, automation, alerts/notifications, troubleshooting.</li>
</ul>

<h3>5. Plan and configure HA/DR (20–25%)</h3>
<ul>
  <li><strong>Plan an HA/DR strategy:</strong> map to RPO/RTO requirements, evaluate hybrid and Azure-native options, plan a test procedure.</li>
  <li><strong>Backup and restore:</strong> recommend a strategy, use native tools and T-SQL, point-in-time restore, long-term retention, backup to/restore from cloud storage.</li>
  <li><strong>Configure HA/DR:</strong> active geo-replication, Always On availability groups on Managed Instance and VMs, failover groups, Always On Failover Cluster Instances on VMs, log shipping; monitor and troubleshoot.</li>
</ul>

<h3>Key updates since the previous version (April 24, 2026)</h3>
<ul>
  <li><em>Configure database authentication and authorization</em> — minor changes.</li>
  <li><em>Automate deployment of database resources</em> — minor changes.</li>
  <li>All other skill areas: no change.</li>
</ul>

<h3>Recommended study resources</h3>
<ul>
  <li><strong>Microsoft Learn</strong> — self-paced learning paths and modules for DP-300, plus instructor-led courses.</li>
  <li><strong>Documentation</strong> — Azure SQL, Azure SQL Database, and broader Azure docs.</li>
  <li><strong>Practice Assessment</strong> — free, on Microsoft Learn.</li>
  <li><strong>Exam sandbox</strong> — explore the exam UI before test day.</li>
  <li><strong>Community</strong> — Microsoft Q&amp;A, Azure Data Tech Community, and the Microsoft Learn show <em>Data Exposed</em> and the <em>Exam Readiness Zone</em>.</li>
  <li><strong>Hands-on practice</strong> — most important: deploy and operate Azure SQL Database, Managed Instance, and SQL Server on Azure VMs in a sandbox subscription.</li>
</ul>

<h3>Exam logistics worth knowing</h3>
<ul>
  <li>The English version of the exam is updated first; localized versions follow about <strong>eight weeks</strong> later.</li>
  <li>If your preferred language is unavailable, you can request an extra <strong>30 minutes</strong>.</li>
  <li>Most questions cover <strong>GA</strong> features, but commonly used <strong>Preview</strong> features may appear.</li>
  <li><strong>Accommodations</strong> are available for assistive devices, extra time, or other modifications.</li>
  <li>Microsoft associate, expert, and specialty certifications expire annually and are renewed via a free assessment on Microsoft Learn.</li>
</ul>

<p class="text-muted"><em>Source: Microsoft official Study Guide for Exam DP-300 — skills measured as of April 24, 2026; document last updated 03/26/2026.</em></p>
""".strip()


def main() -> None:
    with app.app_context():
        lesson = db.session.get(Lesson, LESSON_ID)
        if lesson is None:
            raise SystemExit(f"Lesson {LESSON_ID} not found")
        lesson.content = CONTENT
        db.session.commit()
        print(f"Updated lesson {lesson.id} '{lesson.title}' ({len(CONTENT)} chars).")


if __name__ == "__main__":
    main()
