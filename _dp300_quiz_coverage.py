"""Backfill DP-300 quiz questions so every official sub-skill is covered.

For each of the five DP-300 lesson quizzes (33–37), this script adds any
missing multiple-choice questions tagged against the Microsoft DP-300 study
guide sub-skills (skills measured as of April 24, 2026).

Idempotent: questions are tagged with a hidden marker so re-runs don't
duplicate. Also renames Quiz 37 to the official wording.
"""
from __future__ import annotations
from app import app, db, Quiz, Question, QuestionOption

MARKER = "<!-- dp300_coverage_v1 -->"


def add_question(quiz_id: int, prompt_html: str, options: list[tuple[str, bool]],
                 feedback: str, points: float = 1.0) -> None:
    """Add a multiple_choice question unless a marker-tagged copy already exists."""
    qhtml = f"{MARKER}\n{prompt_html}"
    existing = (
        Question.query
        .filter_by(quiz_id=quiz_id)
        .filter(Question.question_html == qhtml)
        .first()
    )
    if existing is not None:
        return
    q = Question(
        quiz_id=quiz_id,
        question_type="multiple_choice",
        question_html=qhtml,
        points=points,
        feedback=feedback,
    )
    db.session.add(q)
    db.session.flush()
    for idx, (text, is_correct) in enumerate(options, start=1):
        db.session.add(QuestionOption(
            question_id=q.id,
            option_html=text,
            is_correct=is_correct,
            order=idx,
        ))


# ----------------------------------------------------------------------
# Quiz 33 — Plan and implement data platform resources
# ----------------------------------------------------------------------
QUIZ_33 = [
    (
        "Your hospital runs SQL Server on-premises in a remote location with intermittent "
        "internet connectivity but must be governed and monitored from Azure. Which option "
        "lets you manage the instance from Azure Resource Manager and receive Microsoft "
        "Defender for Cloud recommendations?",
        [
            ("Migrate the database to Azure SQL Database", False),
            ("Enable Azure Arc-enabled SQL Server", True),
            ("Lift-and-shift the server to an Azure VM", False),
            ("Configure Always On Availability Groups to Azure", False),
        ],
        "Azure Arc-enabled SQL Server projects on-premises instances into Azure "
        "Resource Manager so they can be inventoried, monitored, and protected by "
        "Defender for Cloud while staying on-premises.",
    ),
    (
        "Your analytics team needs a SQL database that is part of the unified Microsoft "
        "Fabric workspace, automatically replicates to OneLake for cross-engine analytics, "
        "and is provisioned without you managing infrastructure. Which offering fits?",
        [
            ("Azure SQL Database in Microsoft Fabric", True),
            ("Azure SQL Managed Instance", False),
            ("SQL Server on Azure VM", False),
            ("Azure Synapse dedicated SQL pool", False),
        ],
        "Azure SQL Database in Microsoft Fabric is a SaaS SQL offering integrated "
        "with Fabric workspaces and auto-mirrored to OneLake.",
    ),
    (
        "A 4 TB orders table is queried mostly by month. Which physical design should you "
        "plan to improve maintenance windows and enable partition-level operations?",
        [
            ("Horizontal database sharding across many databases", False),
            ("Range-based table partitioning on the order date", True),
            ("Columnstore index on every column", False),
            ("In-Memory OLTP tables", False),
        ],
        "Range partitioning by date allows partition switching, sliding-window "
        "archive, and partition-aligned index maintenance.",
    ),
    (
        "You need to scale a multi-tenant SaaS workload beyond the limits of a single "
        "Azure SQL Database and isolate tenants. Which strategy should you recommend?",
        [
            ("Database sharding with the Elastic Database tools", True),
            ("Increase the DTU tier to Premium P15", False),
            ("Convert the database to Hyperscale", False),
            ("Enable Read Scale-Out", False),
        ],
        "Sharding distributes tenants across multiple databases and is the "
        "recommended pattern for very large multi-tenant SaaS solutions.",
    ),
    (
        "A hybrid SQL Server deployment uses on-premises instances replicated to SQL "
        "Server on an Azure VM. Which Azure service centrally orchestrates OS and SQL "
        "Server patching for the IaaS VM?",
        [
            ("Azure Update Manager with the SQL IaaS Agent extension", True),
            ("Azure SQL Database Automatic tuning", False),
            ("Microsoft Entra Privileged Identity Management", False),
            ("Azure Migrate", False),
        ],
        "Azure Update Manager combined with the SQL IaaS Agent extension applies "
        "Windows and SQL Server cumulative updates on a managed schedule.",
    ),
    (
        "You deploy SQL Server on an Azure VM for an OLTP workload requiring the best "
        "log-write latency. Which storage configuration should you choose?",
        [
            ("OS disk only", False),
            ("Premium SSD for data and log on separate disks with write accelerator on the log disk", True),
            ("Standard HDD with read caching enabled", False),
            ("Temporary D: drive for the transaction log", False),
        ],
        "Place data and log on separate Premium SSDs and enable Write Accelerator "
        "(on M-series) for the log disk to minimize log-write latency.",
    ),
    (
        "You enable PAGE compression on a heavily read OLTP table that is rarely "
        "updated. What is the primary benefit?",
        [
            ("Lower CPU usage during scans", False),
            ("Reduced storage and lower logical reads, improving buffer-pool efficiency", True),
            ("Automatic encryption of the table data", False),
            ("Eliminates the need for indexes", False),
        ],
        "PAGE compression reduces the on-disk and in-memory footprint so more "
        "data fits in the buffer pool and fewer pages are read.",
    ),
    (
        "A 2 TB on-premises database must move to Azure SQL Managed Instance with "
        "minimum downtime; the application can tolerate seconds of cutover. Which "
        "migration approach is appropriate?",
        [
            ("Offline migration using BACPAC import", False),
            ("Online migration via Azure Database Migration Service with continuous log replay", True),
            ("Detach-and-attach to the managed instance", False),
            ("Generate-scripts wizard from SSMS", False),
        ],
        "Azure DMS online migration ships transaction-log backups continuously, "
        "enabling a short cutover window for large databases.",
    ),
    (
        "Which tool performs an online migration of an on-premises SQL Server database "
        "to Azure SQL Database with the lowest cutover time?",
        [
            ("BACPAC export/import via SqlPackage", False),
            ("Azure Database Migration Service (online mode)", True),
            ("Data Migration Assistant assessment only", False),
            ("Azure Data Factory copy activity", False),
        ],
        "Azure Database Migration Service in online mode keeps the target in sync "
        "until cutover, minimizing downtime.",
    ),
    (
        "You need to perform a one-time offline migration of a 50 GB on-premises SQL "
        "Server database to Azure SQL Database during a maintenance window. Which "
        "lightweight tool is appropriate?",
        [
            ("SqlPackage export to BACPAC and import to Azure", True),
            ("Always On Availability Group to Azure", False),
            ("Transactional replication", False),
            ("Backup to URL with WITH NORECOVERY", False),
        ],
        "BACPAC via SqlPackage is the standard offline method for moving a "
        "small/medium database into Azure SQL Database.",
    ),
    (
        "You are migrating an Azure SQL Database from the General Purpose tier to "
        "Hyperscale to support a 30 TB workload. Which statement is true?",
        [
            ("You must export to BACPAC and re-import", False),
            ("In-place upgrade is supported via the Azure portal or T-SQL ALTER DATABASE", True),
            ("The database must be moved to a different server first", False),
            ("Hyperscale requires a separate logical server in another region", False),
        ],
        "Migration between Azure SQL service tiers (including to Hyperscale) is "
        "an in-place ALTER DATABASE / portal operation.",
    ),
    (
        "You need to relocate a user database from one Azure SQL Managed Instance to "
        "another in the same region with minimal scripting. Which feature should you use?",
        [
            ("Azure SQL Managed Instance database copy and move", True),
            ("Backup to URL and RESTORE on the target", False),
            ("Cross-database transactional replication", False),
            ("Service Broker dialog migration", False),
        ],
        "The Managed Instance database copy/move feature performs a managed "
        "cross-instance copy or move directly between MIs.",
    ),
    (
        "An online migration via Azure Database Migration Service is stuck at the "
        "schema validation phase, reporting unsupported features in the source. Which "
        "tool should you run first to identify and remediate blocking issues?",
        [
            ("SQL Server Profiler", False),
            ("Data Migration Assistant (DMA) assessment", True),
            ("Activity Monitor", False),
            ("Database Engine Tuning Advisor", False),
        ],
        "DMA produces a pre-migration assessment report listing breaking and "
        "behavior changes, including features unsupported on the target.",
    ),
]


# ----------------------------------------------------------------------
# Quiz 34 — Implement a secure environment
# ----------------------------------------------------------------------
QUIZ_34 = [
    (
        "You need to grant a junior DBA permission to view server configuration and "
        "Always On health on a SQL Server instance without granting sysadmin. Which "
        "fixed server role should you add the login to?",
        [
            ("sysadmin", False),
            ("serveradmin", False),
            ("##MS_ServerStateReader##", True),
            ("dbcreator", False),
        ],
        "The ##MS_ServerStateReader## fixed server role grants VIEW SERVER STATE-"
        "equivalent rights without administrative privileges.",
    ),
    (
        "You need to add a Microsoft Entra ID group as a contained database user in "
        "Azure SQL Database. Which T-SQL statement is correct?",
        [
            ("CREATE LOGIN [hr-readers] FROM EXTERNAL PROVIDER;", False),
            ("CREATE USER [hr-readers] FROM EXTERNAL PROVIDER;", True),
            ("CREATE USER [hr-readers] WITH PASSWORD = 'P@ssw0rd!';", False),
            ("EXEC sp_addrolemember 'db_datareader','hr-readers';", False),
        ],
        "Azure SQL Database uses CREATE USER ... FROM EXTERNAL PROVIDER to map "
        "Entra ID users and groups as contained database users.",
    ),
    (
        "Following least privilege, you must allow an application to read three tables "
        "in a schema while preventing access to other tables. What is the best approach?",
        [
            ("Add the app user to db_datareader", False),
            ("Grant SELECT on the schema, then DENY SELECT on the protected tables", False),
            ("GRANT SELECT on only the three required tables directly to the role used by the application", True),
            ("Grant the app user the sysadmin role", False),
        ],
        "Granting the minimum object-level rights needed (SELECT on exactly the "
        "required tables) is the least-privilege approach.",
    ),
    (
        "A user reports the error 'Login failed for user '<token-identified principal>'' "
        "when connecting to Azure SQL Database with their Entra ID account. What is "
        "the most likely cause?",
        [
            ("The Azure SQL server firewall is blocking the client IP", False),
            ("The user has not been created in the target database with CREATE USER ... FROM EXTERNAL PROVIDER", True),
            ("Always Encrypted is enabled for the connection", False),
            ("TDE has not been configured", False),
        ],
        "Entra ID authentication succeeded at the server but the principal does "
        "not exist as a database user — create it with FROM EXTERNAL PROVIDER.",
    ),
    (
        "Your compliance team requires the TDE encryption key to be customer-managed and "
        "rotatable on demand. Which configuration should you use?",
        [
            ("Service-managed TDE", False),
            ("Customer-managed TDE with a key in Azure Key Vault (BYOK)", True),
            ("Column-level encryption with EncryptByPassPhrase", False),
            ("Always Encrypted with randomized encryption", False),
        ],
        "Customer-managed keys for TDE store the TDE protector in Azure Key Vault "
        "so the customer controls rotation and revocation.",
    ),
    (
        "You need to restrict an Azure SQL logical server so only a specific Azure "
        "Virtual Network subnet can connect, without traversing the public internet "
        "and without managing public IP allow-lists. Which feature should you use?",
        [
            ("Server-level firewall rule for the subnet CIDR", False),
            ("Service endpoint with a VNet rule", False),
            ("Private endpoint via Azure Private Link", True),
            ("IP-based database-level firewall rule", False),
        ],
        "Private Link assigns a private IP inside the VNet and traffic stays on "
        "the Microsoft backbone — the strongest network isolation.",
    ),
    (
        "Which Always Encrypted configuration allows rich computations (range, LIKE, "
        "JOIN) on encrypted columns while keeping plaintext invisible to DBAs?",
        [
            ("Deterministic encryption only", False),
            ("Randomized encryption only", False),
            ("Always Encrypted with secure enclaves (VBS enclaves)", True),
            ("Transparent Data Encryption", False),
        ],
        "VBS-enclave-enabled Always Encrypted lets the engine perform rich "
        "operations inside a trusted enclave while DBAs still cannot see plaintext.",
    ),
    (
        "Your security team wants Azure SQL traffic from an Azure VM to use the "
        "Microsoft backbone over a service endpoint, restricted to a specific VNet "
        "subnet. Which object enforces the subnet restriction on the SQL server?",
        [
            ("A virtual network rule on the Azure SQL server", True),
            ("A network security group on the SQL VNet", False),
            ("An application security group", False),
            ("A route table assigned to the subnet", False),
        ],
        "VNet (virtual network) rules on the Azure SQL server limit access to "
        "the specified subnets that have the SQL service endpoint enabled.",
    ),
    (
        "You must catalogue and label columns containing PII so audits and Defender "
        "for SQL recommendations can highlight sensitive data. Which feature provides "
        "labels and information types stored as extended properties?",
        [
            ("Dynamic Data Masking", False),
            ("Data Discovery & Classification (SQL Data Classification)", True),
            ("Row-Level Security", False),
            ("Always Encrypted", False),
        ],
        "SQL Data Classification adds Sensitivity Labels and Information Types "
        "to columns and feeds vulnerability assessment and audits.",
    ),
    (
        "Compliance requires that every successful and failed login to Azure SQL "
        "Database be retained for one year in an immutable store. Which configuration "
        "meets this requirement most directly?",
        [
            ("Enable Azure SQL Database auditing to a Log Analytics workspace or Storage account with retention", True),
            ("Enable Query Store", False),
            ("Turn on Extended Events on the SQL server", False),
            ("Enable change data tracking on the master database", False),
        ],
        "Azure SQL Auditing writes audit logs to Storage/Log Analytics/Event Hubs "
        "with configurable retention to meet compliance.",
    ),
    (
        "You need to capture which rows in a Customers table have changed since the "
        "last ETL run, including the type of DML operation, without rewriting the "
        "application. Which feature should you enable?",
        [
            ("Change Tracking (CT)", False),
            ("Change Data Capture (CDC)", True),
            ("Temporal tables only", False),
            ("Triggers writing to a shadow table", False),
        ],
        "CDC records insert/update/delete operations with before/after images, "
        "ideal for incremental ETL.",
    ),
    (
        "Auditors must be able to cryptographically prove that historical rows in a "
        "compliance table have not been tampered with. Which Azure SQL feature should "
        "you implement?",
        [
            ("Always Encrypted", False),
            ("Ledger tables in Azure SQL", True),
            ("Transparent Data Encryption", False),
            ("Dynamic Data Masking", False),
        ],
        "Azure SQL ledger provides tamper-evidence with cryptographically chained "
        "history and database digests that can be verified.",
    ),
]


# ----------------------------------------------------------------------
# Quiz 35 — Monitor, configure, optimize
# ----------------------------------------------------------------------
QUIZ_35 = [
    (
        "Before tuning a problem workload, your team needs a 'normal' point of "
        "reference. Which artifact is essential for ongoing performance work?",
        [
            ("A performance baseline collected over a representative period", True),
            ("A single execution plan from the slowest query", False),
            ("The current wait-stats snapshot only", False),
            ("Index fragmentation report", False),
        ],
        "A baseline captures normal CPU, IO, waits and durations so you can "
        "detect regressions and quantify improvements.",
    ),
    (
        "You want a managed, low-touch monitoring service that uses Azure-collected "
        "telemetry to surface degradations across all your Azure SQL databases. Which "
        "service should you enable?",
        [
            ("Database Watcher for Azure SQL", True),
            ("SQL Server Profiler", False),
            ("SQL Agent operator alerts", False),
            ("Resource Governor", False),
        ],
        "Database Watcher (Azure SQL monitoring) collects high-frequency "
        "telemetry across Azure SQL Database/MI with managed dashboards.",
    ),
    (
        "Which built-in capability of Azure SQL Database analyzes telemetry and emits "
        "actionable diagnostic events such as plan-choice regression and excessive "
        "waits?",
        [
            ("Intelligent Insights", True),
            ("Query Store force-plan", False),
            ("Microsoft Defender for SQL", False),
            ("Automatic tuning CREATE_INDEX action", False),
        ],
        "Intelligent Insights produces JSON diagnostic events identifying root "
        "causes of performance regressions.",
    ),
    (
        "A web app intermittently times out. You suspect blocking. Which DMV pair is "
        "most useful to identify head blockers and their wait chains?",
        [
            ("sys.dm_exec_query_stats and sys.dm_exec_cached_plans", False),
            ("sys.dm_exec_requests and sys.dm_os_waiting_tasks", True),
            ("sys.dm_io_virtual_file_stats and sys.dm_os_performance_counters", False),
            ("sys.dm_db_index_usage_stats and sys.dm_db_missing_index_details", False),
        ],
        "sys.dm_exec_requests + sys.dm_os_waiting_tasks reveals blocked sessions "
        "and their blocking_session_id wait chains.",
    ),
    (
        "After reviewing a slow report query, the execution plan shows a Key Lookup "
        "with a high cost. What is the most targeted fix?",
        [
            ("Add the missing output columns to the nonclustered index INCLUDE list", True),
            ("Rebuild the clustered index", False),
            ("Increase MAXDOP for the query", False),
            ("Switch to a columnstore index", False),
        ],
        "Adding the required columns as INCLUDEs creates a covering index and "
        "eliminates the key lookup.",
    ),
    (
        "Statistics on a large table are stale and the optimizer is producing poor "
        "row estimates. Which maintenance step addresses this directly?",
        [
            ("UPDATE STATISTICS WITH FULLSCAN (or scheduled stats maintenance)", True),
            ("DBCC SHRINKFILE", False),
            ("ALTER INDEX REORGANIZE", False),
            ("Enable Resource Governor", False),
        ],
        "UPDATE STATISTICS (ideally FULLSCAN for skewed columns) refreshes "
        "histogram data the optimizer relies on.",
    ),
    (
        "You need to verify the logical and physical integrity of a critical database "
        "after suspected hardware issues. Which command should you run as part of your "
        "maintenance plan?",
        [
            ("DBCC CHECKDB", True),
            ("DBCC FREEPROCCACHE", False),
            ("DBCC SHRINKDATABASE", False),
            ("DBCC INPUTBUFFER", False),
        ],
        "DBCC CHECKDB validates allocation, system-table, and per-object "
        "consistency for the entire database.",
    ),
    (
        "On a SQL Server with mixed OLTP and reporting workloads, reporting queries "
        "are starving OLTP for CPU. Which feature lets you cap CPU/memory per workload "
        "group?",
        [
            ("Resource Governor", True),
            ("Database Mail", False),
            ("Query Store force-plan", False),
            ("Always On read-only routing", False),
        ],
        "Resource Governor classifies sessions into workload groups whose CPU, "
        "memory and IOPS can be capped and prioritized.",
    ),
    (
        "You want to enable the new cardinality estimator for one database only "
        "without affecting compatibility level globally. Which configuration should "
        "you set?",
        [
            ("Database-scoped configuration LEGACY_CARDINALITY_ESTIMATION = OFF", True),
            ("Server-level trace flag 4199", False),
            ("Enable Lock Pages in Memory", False),
            ("Set MAXDOP = 0 at the server level", False),
        ],
        "Database-scoped configurations (such as LEGACY_CARDINALITY_ESTIMATION) "
        "scope optimizer behavior to a single database.",
    ),
    (
        "An Azure SQL Hyperscale database is hitting CPU saturation during business "
        "hours. What is the fastest way to add capacity without downtime?",
        [
            ("Scale up the compute tier (more vCores) online", True),
            ("Recreate the database in a higher tier", False),
            ("Enable Resource Governor", False),
            ("Reduce the number of read replicas", False),
        ],
        "Hyperscale supports near-instant online compute scaling.",
    ),
    (
        "Which Intelligent Query Processing (IQP) feature helps queries that have "
        "skewed row-estimates on table-valued parameters and local variables by "
        "deferring optimization until runtime values are known?",
        [
            ("Batch Mode on Rowstore", False),
            ("Adaptive Joins", False),
            ("Parameter Sensitive Plan optimization / Deferred compilation", True),
            ("Memory Grant Feedback only", False),
        ],
        "Deferred compilation and Parameter Sensitive Plan optimization defer "
        "plan choice to use real runtime values for better cardinality estimates.",
    ),
    (
        "You configure Query Store and need to ensure long-running historical data is "
        "retained for trend analysis. Which Query Store setting controls retention?",
        [
            ("STALE_QUERY_THRESHOLD_DAYS", True),
            ("MAX_PLANS_PER_QUERY", False),
            ("DATA_FLUSH_INTERVAL_SECONDS", False),
            ("QUERY_CAPTURE_MODE", False),
        ],
        "STALE_QUERY_THRESHOLD_DAYS controls how long Query Store retains data "
        "before cleanup.",
    ),
]


# ----------------------------------------------------------------------
# Quiz 36 — Configure and manage automation
# ----------------------------------------------------------------------
QUIZ_36 = [
    (
        "Your team needs to deploy an Azure SQL logical server and database as "
        "Infrastructure as Code with a strict JSON schema that integrates with "
        "existing pipelines that already consume ARM templates. Which artifact is "
        "the right primary choice?",
        [
            ("An ARM template", True),
            ("A T-SQL backup script", False),
            ("An Azure Automation runbook", False),
            ("A Logic App workflow", False),
        ],
        "ARM JSON templates remain the canonical IaC artifact directly consumed "
        "by Azure Resource Manager.",
    ),
    (
        "Which Azure PowerShell module/cmdlet should you use to create an Azure SQL "
        "Database from a deployment script?",
        [
            ("New-AzSqlDatabase (Az.Sql)", True),
            ("Invoke-Sqlcmd (SqlServer)", False),
            ("New-AzResourceGroup (Az.Resources)", False),
            ("Set-AzContext (Az.Accounts)", False),
        ],
        "Az.Sql's New-AzSqlDatabase provisions a database on an existing logical "
        "server.",
    ),
    (
        "In a CI/CD pipeline you want to provision an Azure SQL Managed Instance "
        "using a cross-platform command-line tool. Which command is appropriate?",
        [
            ("az sql mi create", True),
            ("sqlcmd -S server -Q 'CREATE MANAGED INSTANCE'", False),
            ("kubectl create mi", False),
            ("Get-AzSqlInstance", False),
        ],
        "az sql mi create is the Azure CLI command for Managed Instance "
        "provisioning.",
    ),
    (
        "A Bicep deployment to provision Azure SQL is failing. Which built-in feature "
        "lets you stream the deployment progress and inspect resource-level errors?",
        [
            ("Azure Resource Manager deployment history and 'az deployment group show'", True),
            ("SQL Server Profiler", False),
            ("Activity Monitor", False),
            ("Query Store", False),
        ],
        "ARM deployment history (visible via portal or az/PS) returns the "
        "operation-level error details for failed templates.",
    ),
    (
        "You schedule an Elastic Job that runs T-SQL across 30 Azure SQL databases. "
        "One database failed and you need root-cause information. Where do you look?",
        [
            ("The Elastic Job target-execution status and jobs_executions tables in the job database", True),
            ("Azure Storage Explorer", False),
            ("Microsoft Entra ID sign-in logs", False),
            ("SQL Server Agent error log", False),
        ],
        "Elastic Jobs store per-target execution status (success, failed, "
        "lifecycle messages) in the jobs database tables and views.",
    ),
    (
        "A SQL Server Agent job runs nightly maintenance. You need an email when the "
        "job fails AND when it succeeds with warnings. Which combination is required?",
        [
            ("Database Mail profile + operator + job notifications with the correct condition", True),
            ("Resource Governor classifier function", False),
            ("Azure Service Bus topic subscription", False),
            ("Azure Front Door rule", False),
        ],
        "SQL Agent uses Database Mail + an operator + per-job notification "
        "rules (on failure/success/completion).",
    ),
    (
        "A scheduled SQL Server Agent job is suddenly failing with 'The EXECUTE "
        "permission was denied'. Which step is the most appropriate first diagnostic?",
        [
            ("Inspect the job step's Run As (proxy) credential and underlying account permissions", True),
            ("Restart the server", False),
            ("Rebuild all indexes", False),
            ("Drop and recreate the job", False),
        ],
        "Permission failures almost always trace to the proxy/credential used "
        "by the step or the SQL Agent service account.",
    ),
    (
        "You need Azure to email the on-call engineer when an Elastic Job step fails "
        "more than three times in 10 minutes. Which Azure service raises the alert "
        "based on log telemetry?",
        [
            ("Azure Monitor alert rule on the job's Log Analytics signal", True),
            ("SQL Server Database Mail", False),
            ("Azure Front Door rule", False),
            ("Microsoft Entra Conditional Access", False),
        ],
        "Azure Monitor alerts on logs/metrics emitted by Elastic Jobs (via "
        "diagnostic settings to Log Analytics) and notify via action groups.",
    ),
    (
        "An automated database task that runs via Azure Automation runbook fails "
        "intermittently with throttling errors. What should you implement to make the "
        "task more resilient?",
        [
            ("Retry logic with exponential back-off in the runbook", True),
            ("Lower the database service tier", False),
            ("Disable connection pooling", False),
            ("Drop and recreate the database", False),
        ],
        "Transient errors (throttling, network) should be handled with retry "
        "logic and exponential back-off in the automation layer.",
    ),
    (
        "Which deployment automation artifact lets you embed a database schema and "
        "objects into an Azure DevOps pipeline so the application's database state is "
        "versioned alongside code?",
        [
            ("A SQL Database Project (.sqlproj) producing a DACPAC", True),
            ("An ARM template only", False),
            ("A BACPAC file", False),
            ("An SQL Agent job", False),
        ],
        "A SQL Database Project compiles to a DACPAC that pipelines deploy as "
        "the source of truth for schema state.",
    ),
]


# ----------------------------------------------------------------------
# Quiz 37 — HA/DR
# ----------------------------------------------------------------------
QUIZ_37 = [
    (
        "A hybrid deployment has SQL Server on-premises with read-only reporting "
        "replicas hosted on SQL Server on Azure VMs. Which evaluation step is most "
        "important when planning HA/DR?",
        [
            ("Measure the WAN latency and verify it meets the AG synchronous-commit budget", True),
            ("Enable Dynamic Data Masking", False),
            ("Enable Query Store", False),
            ("Reduce the on-prem SQL Server compatibility level", False),
        ],
        "Cross-site AG latency directly limits whether synchronous commit is "
        "viable and dictates the realistic RPO/RTO of the hybrid design.",
    ),
    (
        "Your DR plan requires a documented annual failover test. Which approach "
        "validates RPO/RTO most realistically without affecting production?",
        [
            ("A scheduled forced failover drill into the secondary using a non-production traffic shadow", True),
            ("Reviewing the runbook in a meeting", False),
            ("Running DBCC CHECKDB", False),
            ("Enabling Resource Governor", False),
        ],
        "A live failover drill against shadowed traffic measures actual RTO and "
        "data-loss, validating the plan end-to-end.",
    ),
    (
        "Your backup strategy must combine weekly full, daily differentials and "
        "log backups every 15 minutes for a SQL Server on Azure VM. Which native "
        "Azure service can centrally orchestrate this?",
        [
            ("Azure Backup for SQL Server in Azure VMs", True),
            ("Azure Site Recovery", False),
            ("Azure Front Door", False),
            ("Azure Monitor metrics", False),
        ],
        "Azure Backup for SQL in VM provides scheduled full/differential/log "
        "backups with central policy and long-term retention.",
    ),
    (
        "Which T-SQL statement performs a full backup of a database to a URL-based "
        "Azure Blob container?",
        [
            ("BACKUP DATABASE Sales TO URL = 'https://acct.blob.core.windows.net/backups/Sales.bak';", True),
            ("RESTORE DATABASE Sales FROM DISK = 'c:\\backups\\Sales.bak';", False),
            ("EXPORT DATABASE Sales TO 'azure://sales';", False),
            ("BACKUP LOG Sales TO TAPE = 'azure1';", False),
        ],
        "SQL Server supports BACKUP/RESTORE TO/FROM URL with a SAS credential "
        "for Azure Blob targets.",
    ),
    (
        "A production database must be restored from full + differential + several "
        "log backups. Which RESTORE option keeps the database in a state that allows "
        "applying additional log backups?",
        [
            ("WITH NORECOVERY", True),
            ("WITH RECOVERY", False),
            ("WITH REPLACE", False),
            ("WITH STANDBY = NULL", False),
        ],
        "WITH NORECOVERY leaves the database in restoring state so subsequent "
        "differential/log backups can be applied.",
    ),
    (
        "You need to keep weekly full backups of an Azure SQL Database for seven "
        "years to meet a regulatory requirement. Which feature should you configure?",
        [
            ("Long-Term Retention (LTR) policy", True),
            ("Point-in-time restore", False),
            ("Geo-restore", False),
            ("Active geo-replication", False),
        ],
        "LTR retains weekly/monthly/yearly full backups for up to 10 years.",
    ),
    (
        "On an Azure SQL Managed Instance Business Critical tier in a single region, "
        "you need cross-region disaster recovery. Which feature should you configure?",
        [
            ("An Always On Availability Group between two SQL Managed Instances (auto-failover group)", True),
            ("Log shipping to an on-prem SQL Server", False),
            ("Backup-to-URL only", False),
            ("Stretch Database", False),
        ],
        "Managed Instance auto-failover groups configure Always On AGs across "
        "MIs in different regions.",
    ),
    (
        "You are designing HA for SQL Server on Azure VMs that require shared "
        "storage semantics and instance-level failover with a single virtual network "
        "name. Which solution should you implement?",
        [
            ("Always On Failover Cluster Instance with Azure Shared Disks or Storage Spaces Direct", True),
            ("Always On Availability Group with read-scale only", False),
            ("Database snapshots", False),
            ("Active geo-replication", False),
        ],
        "An FCI on Azure VMs uses Azure Shared Disks (or S2D) and a Windows "
        "Server Failover Cluster to give instance-level failover.",
    ),
    (
        "A small budget DR scenario between two on-premises SQL Server instances "
        "tolerates manual failover and a few minutes of data loss. Which classic "
        "feature delivers warm-standby copies cheaply?",
        [
            ("Log shipping", True),
            ("Always On synchronous-commit availability group", False),
            ("Active geo-replication", False),
            ("Service Broker mirroring", False),
        ],
        "Log shipping ships transaction-log backups to a warm-standby on a "
        "schedule and is the lowest-cost HA/DR option.",
    ),
    (
        "Which signal in Azure Monitor lets you alert when an Always On Availability "
        "Group's secondary replica falls behind the primary by more than a defined "
        "threshold?",
        [
            ("Log_send_queue_size / redo_queue_size metric from the SQL IaaS agent or DMV-based custom metric", True),
            ("CPU percentage on the master database", False),
            ("Blob container ingress bytes", False),
            ("Microsoft Entra sign-in count", False),
        ],
        "Replica lag is best monitored via send/redo queue sizes (from "
        "sys.dm_hadr_database_replica_states or the SQL IaaS extension).",
    ),
    (
        "Failover of an auto-failover group did not trigger automatically when the "
        "primary region became unreachable. Which configuration is most likely the "
        "cause?",
        [
            ("Grace period and read/write failover policy set to Manual or to a long grace value", True),
            ("Lack of TDE on the primary database", False),
            ("Missing Resource Governor pool", False),
            ("Query Store turned off", False),
        ],
        "Auto-failover groups will not flip automatically if the failover "
        "policy is Manual or the grace period has not elapsed.",
    ),
    (
        "You restored a database in Azure SQL Database to a point in time 90 minutes "
        "ago to recover from accidental data deletion. Which best practice should you "
        "follow next?",
        [
            ("Validate the restored database, then rename or swap it into production using a controlled cutover", True),
            ("Drop the production database immediately", False),
            ("Disable backups on the restored database", False),
            ("Run sp_attach_db on the restored copy", False),
        ],
        "PITR creates a new database — validate it, then perform a controlled "
        "cutover (rename/swap) to replace the source.",
    ),
]


def rename_quiz_37() -> None:
    """Align Quiz 37 title with the official wording."""
    target = (
        "Lesson 7 Quiz — Plan and Configure a High Availability and "
        "Disaster Recovery (HA/DR) Environment"
    )
    q = db.session.get(Quiz, 37)
    if q is None:
        print("  (quiz 37 not found)")
        return
    if q.title != target:
        print(f"  rename quiz 37: {q.title!r} -> {target!r}")
        q.title = target


def main() -> None:
    with app.app_context():
        rename_quiz_37()

        bundles = [
            (33, QUIZ_33),
            (34, QUIZ_34),
            (35, QUIZ_35),
            (36, QUIZ_36),
            (37, QUIZ_37),
        ]
        for quiz_id, items in bundles:
            before = Question.query.filter_by(quiz_id=quiz_id).count()
            for prompt, options, feedback in items:
                add_question(quiz_id, prompt, options, feedback)
            db.session.flush()
            after = Question.query.filter_by(quiz_id=quiz_id).count()
            print(f"  Quiz {quiz_id}: {before} -> {after} questions ({after - before} added)")

        db.session.commit()
        print("Done.")


if __name__ == "__main__":
    main()
