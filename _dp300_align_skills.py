"""Align DP-300 course lessons & quizzes with the official Skills Measured.

Source: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300
Skills measured as of April 24, 2026:

  1. Plan and implement data platform resources                                (15–20%)
  2. Implement a secure environment                                            (20–25%)
  3. Monitor, configure, and optimize database resources                       (20–25%)
  4. Configure and manage automation of tasks                                  (15–20%)
  5. Plan and configure a high availability and disaster recovery environment  (20–25%)

Changes made by this script (idempotent):

* Remove Lesson 8 ('Perform Administrative and Data Movement Tasks') and its
  quiz — it is no longer a top-level functional group in the current exam.
* Update Lesson 7 / Lesson 7 Quiz titles to include "(HA/DR)" to match the
  official wording exactly.
* Append a "Skills measured — sub-skills covered in this lesson" block to each
  of Lessons 3–7 so students can see which exam bullets the lesson maps to.
* Re-sequence the remaining lessons so the order field is contiguous.
"""
from app import app, db, Lesson, Quiz

COURSE_ID = 5

LESSON_TO_DELETE_IDS = [84, 85]  # Lesson 8 lesson + quiz

# (lesson_id, new_lesson_title, new_quiz_title_or_None)
RENAMES = [
    (
        82,
        "Lesson 7: Plan and Configure a High Availability and Disaster Recovery (HA/DR) Environment",
        "Lesson 7 Quiz — Plan and Configure a High Availability and Disaster Recovery (HA/DR) Environment",
    ),
]

# Sub-skills from the official study guide, grouped by lesson id.
SUBSKILLS = {
    74: (
        "1. Plan and implement data platform resources (15–20%)",
        [
            ("Plan and deploy Azure SQL solutions", [
                "Recommend a database offering based on specific requirements",
                "Choose an automated deployment method",
                "Identify use cases for Azure Arc-enabled SQL services",
                "Identify use cases for Azure SQL Database in Microsoft Fabric",
                "Plan for table partitioning",
                "Recommend a database sharding solution",
                "Deploy database offerings on selected platforms",
                "Deploy hybrid SQL Server solutions",
                "Apply patches and updates for hybrid and IaaS deployments",
            ]),
            ("Configure resources for scale and performance", [
                "Configure Azure SQL Database for scale and performance",
                "Configure Azure SQL Managed Instance for scale and performance",
                "Configure SQL Server on Azure Virtual Machines for scale and performance",
                "Configure table partitioning",
                "Configure data compression",
            ]),
            ("Plan and implement a migration strategy", [
                "Evaluate requirements for a migration",
                "Evaluate offline or online migration strategies",
                "Implement an online migration strategy",
                "Implement an offline migration strategy",
                "Implement a migration to Azure",
                "Implement a migration between Azure SQL services",
                "Implement Azure SQL Managed Instance database copy and move",
                "Troubleshoot a migration",
            ]),
        ],
    ),
    76: (
        "2. Implement a secure environment (20–25%)",
        [
            ("Configure database authentication and authorization", [
                "Configure Microsoft Entra ID authentication for Azure SQL Database, "
                "Azure SQL Managed Instance, and SQL Server",
                "Configure authentication for SQL on Azure VMs and Azure SQL Managed Instance",
                "Configure security principals",
                "Create users from Microsoft Entra identities",
                "Configure database and object-level permissions using graphical tools",
                "Apply the principle of least privilege for all securables",
                "Troubleshoot authentication and authorization issues",
                "Manage authentication and authorization by using T-SQL",
            ]),
            ("Implement security for data at rest and data in transit", [
                "Implement transparent data encryption (TDE)",
                "Implement object-level encryption",
                "Configure server- and database-level firewall rules",
                "Implement Always Encrypted",
                "Implement Always Encrypted with VBS enclaves",
                "Configure private links and service endpoints",
            ]),
            ("Implement compliance controls for sensitive data", [
                "Apply a data classification strategy",
                "Configure server and database audits",
                "Implement change data tracking",
                "Implement dynamic data masking",
                "Implement ledger in Azure SQL",
                "Implement row-level security",
            ]),
        ],
    ),
    78: (
        "3. Monitor, configure, and optimize database resources (20–25%)",
        [
            ("Monitor resource activity and performance", [
                "Prepare an operational performance baseline",
                "Determine sources for performance metrics",
                "Interpret performance metrics",
                "Configure and monitor activity and performance",
                "Monitor by using database watcher",
                "Monitor by using Extended Events",
            ]),
            ("Monitor and optimize query performance", [
                "Configure Query Store",
                "Monitor by using Query Store",
                "Identify and resolve session blocking",
                "Identify performance issues using dynamic management views (DMVs)",
                "Identify and implement index changes for queries",
                "Recommend query construct modifications based on resource usage",
                "Review execution plans",
                "Monitor by using Intelligent Insights",
            ]),
            ("Configure database solutions for optimal performance", [
                "Implement index maintenance tasks",
                "Implement statistics maintenance tasks",
                "Implement database integrity checks",
                "Configure database automatic tuning",
                "Configure server settings for performance",
                "Configure Resource Governor for performance",
                "Implement database-scoped configuration",
                "Configure compute and storage resources for scaling",
                "Identify use cases for intelligent query processing (IQP) features",
            ]),
        ],
    ),
    80: (
        "4. Configure and manage automation of tasks (15–20%)",
        [
            ("Create and manage SQL Server Agent jobs", [
                "Manage schedules for regular maintenance jobs",
                "Configure job alerts and notifications",
                "Troubleshoot SQL Server Agent jobs",
            ]),
            ("Automate deployment of database resources", [
                "Automate deployment by using Azure Resource Manager (ARM) and Bicep templates",
                "Automate deployment by using Azure PowerShell",
                "Automate deployment by using Azure CLI",
                "Monitor and troubleshoot deployments",
            ]),
            ("Create and manage database tasks in Azure", [
                "Create and configure elastic jobs",
                "Create and configure database tasks by using automation",
                "Configure alerts and notifications on database tasks",
                "Troubleshoot automated database tasks",
            ]),
        ],
    ),
    82: (
        "5. Plan and configure a high availability and disaster recovery (HA/DR) environment (20–25%)",
        [
            ("Plan an HA/DR strategy for database solutions", [
                "Recommend HA/DR strategy based on RPO/RTO requirements",
                "Evaluate HA/DR for hybrid deployments",
                "Evaluate Azure-specific HA/DR solutions",
                "Plan a testing procedure for an HA/DR solution",
            ]),
            ("Plan and perform backup and restore of a database", [
                "Recommend a database backup and restore strategy",
                "Perform a database backup by using native tools",
                "Perform a database restore by using native tools",
                "Perform a database restore to a point in time",
                "Configure long-term backup retention",
                "Backup and restore a database by using T-SQL",
                "Backup to and restore from cloud storage",
            ]),
            ("Configure HA/DR for database solutions", [
                "Configure active geo-replication",
                "Configure Always On availability groups on SQL Managed Instance and Azure VMs",
                "Configure failover groups",
                "Configure Always On Failover Cluster Instances on Azure virtual machines",
                "Configure log shipping",
                "Monitor an HA/DR solution",
                "Troubleshoot an HA/DR solution",
            ]),
        ],
    ),
}

MAPPING_MARKER_START = "<!-- DP300_SKILLS_MAPPING:START -->"
MAPPING_MARKER_END = "<!-- DP300_SKILLS_MAPPING:END -->"


def build_mapping_html(area_title: str, groups: list[tuple[str, list[str]]]) -> str:
    parts = [
        MAPPING_MARKER_START,
        '<hr>',
        '<div class="dp300-skills-mapping">',
        f'<h3>Skills measured &mdash; covered in this lesson</h3>',
        f'<p><strong>Functional group:</strong> {area_title}</p>',
        '<p class="text-muted">'
        'Source: Microsoft official '
        '<a href="https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300" '
        'target="_blank" rel="noopener">DP-300 study guide</a> '
        '(skills measured as of April 24, 2026).</p>',
    ]
    for group_title, bullets in groups:
        parts.append(f'<h4>{group_title}</h4>')
        parts.append('<ul>')
        parts.extend(f'  <li>{b}</li>' for b in bullets)
        parts.append('</ul>')
    parts.append('</div>')
    parts.append(MAPPING_MARKER_END)
    return "\n".join(parts)


def strip_existing_mapping(html: str) -> str:
    if MAPPING_MARKER_START not in html:
        return html.rstrip()
    start = html.find(MAPPING_MARKER_START)
    end = html.find(MAPPING_MARKER_END)
    if end == -1:
        return html[:start].rstrip()
    return (html[:start] + html[end + len(MAPPING_MARKER_END):]).rstrip()


def main() -> None:
    with app.app_context():
        # 1) Delete out-of-scope Lesson 8 lesson + quiz
        for lid in LESSON_TO_DELETE_IDS:
            lesson = db.session.get(Lesson, lid)
            if lesson is None:
                print(f"  (lesson {lid} already absent)")
                continue
            qid = lesson.quiz_id
            print(f"  deleting lesson {lid}: {lesson.title!r}")
            db.session.delete(lesson)
            if qid:
                q = db.session.get(Quiz, qid)
                if q is not None:
                    print(f"  deleting quiz {qid}: {q.title!r}")
                    db.session.delete(q)

        # 2) Rename L7 lesson and quiz
        for lid, new_lesson_title, new_quiz_title in RENAMES:
            lesson = db.session.get(Lesson, lid)
            if lesson is None:
                print(f"  (lesson {lid} not found, skipping rename)")
                continue
            if lesson.title != new_lesson_title:
                print(f"  rename lesson {lid}: {lesson.title!r} -> {new_lesson_title!r}")
                lesson.title = new_lesson_title
            if new_quiz_title and lesson.quiz_id:
                q = db.session.get(Quiz, lesson.quiz_id)
                if q is not None and q.title != new_quiz_title:
                    print(f"  rename quiz {q.id}: {q.title!r} -> {new_quiz_title!r}")
                    q.title = new_quiz_title
            # Also rename the lesson record for the quiz "lesson" wrapper
            wrapper = (
                db.session.query(Lesson)
                .filter_by(course_id=COURSE_ID, quiz_id=lesson.quiz_id, content_type="exam")
                .first()
                if lesson.quiz_id
                else None
            )
            if wrapper is not None and wrapper.id != lesson.id and wrapper.title != new_quiz_title:
                print(f"  rename quiz wrapper lesson {wrapper.id}: {wrapper.title!r} -> {new_quiz_title!r}")
                wrapper.title = new_quiz_title

        # Also rename the standalone quiz wrapper for lesson 82 (id 83)
        wrapper_l7 = db.session.get(Lesson, 83)
        if wrapper_l7 is not None:
            target = (
                "Lesson 7 Quiz — Plan and Configure a High Availability and "
                "Disaster Recovery (HA/DR) Environment"
            )
            if wrapper_l7.title != target:
                print(f"  rename lesson {wrapper_l7.id}: {wrapper_l7.title!r} -> {target!r}")
                wrapper_l7.title = target

        # 3) Append/refresh the skills-mapping block on each content lesson
        for lid, (area_title, groups) in SUBSKILLS.items():
            lesson = db.session.get(Lesson, lid)
            if lesson is None:
                print(f"  (lesson {lid} not found, skipping mapping)")
                continue
            base = strip_existing_mapping(lesson.content or "")
            block = build_mapping_html(area_title, groups)
            lesson.content = f"{base}\n\n{block}\n"
            print(f"  refreshed skills mapping on lesson {lid}")

        # 4) Re-sequence orders so they're contiguous after deletion
        from sqlalchemy import select
        from app import Course
        course = db.session.get(Course, COURSE_ID)
        if course is not None:
            ordered = sorted(course.lessons, key=lambda l: l.order)
            for idx, l in enumerate(ordered, start=1):
                if l.order != idx:
                    print(f"  reorder lesson {l.id}: {l.order} -> {idx}")
                    l.order = idx

        db.session.commit()
        print("Done.")


if __name__ == "__main__":
    main()
