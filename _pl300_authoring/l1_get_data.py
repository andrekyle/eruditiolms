LESSON_HTML = """
<h2>Connecting to Data Sources</h2>

<h3>Understanding Data Sources in Power BI</h3>
<p>Power BI connects to diverse data sources to provide real-time and historical business insights. Whether your data resides in <strong>Excel files</strong> on your computer, <strong>SQL Server databases</strong> in your organization, <strong>cloud services like Azure SQL Database</strong>, <strong>web APIs</strong>, <strong>SharePoint lists</strong>, <strong>Dataflows</strong>, or <strong>OneLake</strong> in Microsoft Fabric, Power BI provides connectors for seamless integration. The connection process involves selecting a source type, providing authentication credentials, configuring privacy levels, choosing a storage mode, and optionally creating parameters for dynamic filtering and gateway configuration for on-premises sources.</p>

<h3>Identifying and Connecting to Data Sources</h3>
<p>Power BI supports hundreds of data source connectors organized by category. The most commonly used sources include:</p>
<ul>
<li><strong>File sources:</strong> Excel (.xlsx, .xls), CSV, JSON, XML, PDF, and folder structures. These are ideal for local analysis and small-to-medium datasets.</li>
<li><strong>Database sources:</strong> SQL Server, Azure SQL Database, MySQL, PostgreSQL, Snowflake, and others. These are enterprise-grade sources supporting large datasets and real-time queries.</li>
<li><strong>Cloud services:</strong> Azure Synapse Analytics, Google BigQuery, Amazon Redshift, and Salesforce provide scalable cloud-native data platforms.</li>
<li><strong>Web sources:</strong> REST APIs, OData feeds, and web pages enable integration with external systems and real-time web data.</li>
<li><strong>SharePoint:</strong> Lists and document libraries facilitate collaboration-based data sources within your organization.</li>
<li><strong>Dataflows:</strong> Reusable data preparation pipelines that other reports can reference, promoting consistency and reducing maintenance.</li>
<li><strong>OneLake:</strong> Microsoft Fabric's unified data lake provides centralized storage accessible from Power BI for analytics.</li>
</ul>

<p>To connect to a data source, open Power BI Desktop, select <strong>Get Data</strong>, choose your source type, enter the connection details (server address, file path, or URL), and click <strong>Connect</strong>. Power BI will prompt for authentication and then display available tables and views for selection.</p>

<h3>Data Source Credentials and Privacy Levels</h3>
<p>Securing your data connections requires proper credential management. When you first connect to a data source, Power BI prompts for authentication credentials such as username/password, Windows authentication, API keys, or service account tokens. These credentials are stored securely in your Power BI settings and used automatically when refreshing data. On the Power BI Service, gateway administrators manage credentials centrally to enable scheduled refreshes.</p>

<p><strong>Privacy levels</strong> control how Power BI handles data flowing between sources during queries. Three privacy levels exist:</p>
<ul>
<li><strong>Public:</strong> Any external data source can access this data without restriction. Use for non-sensitive, publicly available datasets.</li>
<li><strong>Organizational:</strong> Data remains within your organization's scope. External data sources cannot access it. This is the default for most enterprise scenarios.</li>
<li><strong>Private:</strong> Data cannot be combined with other sources without explicit user permission. Use for highly sensitive information requiring isolation.</li>
</ul>

<p>Privacy level mismatches can cause query errors when combining sources. If a private table is queried together with an organizational source, Power BI will fail the operation by default to prevent unintended data exposure. When you encounter privacy-related errors, adjust source settings in <strong>File &gt; Options and settings &gt; Data source settings</strong> to modify credentials or privacy levels.</p>

<h3>Semantic Models: Shared vs. Local</h3>
<p>When connecting to data, you can choose to create a new local semantic model or reference an existing shared semantic model. A <strong>local semantic model</strong> exists within your Power BI file (.pbix) and is used exclusively by reports in that file. This approach provides complete control over the model structure but requires maintenance if multiple reports need the same data preparation logic.</p>

<p>A <strong>shared semantic model</strong> (also called a published dataset) resides on the Power BI Service and can be referenced by multiple reports. This approach promotes consistency and reduces duplication: one curated data model serves many reports. When you create a report using a shared semantic model, your report file contains only the visualizations and queries, significantly reducing file size and simplifying updates.</p>

<p>To use a shared semantic model, select <strong>Power BI datasets</strong> when choosing a data source in Power BI Desktop. This automatically establishes a Live Connection to the published model. Changes to the underlying model are immediately available to all dependent reports, making governance and consistency easier.</p>

<h3>Storage Modes: Import, DirectQuery, Dual, and Live Connection</h3>
<p>Storage mode determines how data is processed and cached in Power BI. Your choice significantly impacts performance, data freshness, and refresh requirements.</p>

<table border="1" cellpadding="8" cellspacing="0">
<tr>
<th>Storage Mode</th>
<th>Data Location</th>
<th>Refresh Behavior</th>
<th>Performance</th>
<th>Feature Support</th>
</tr>
<tr>
<td><strong>Import</strong></td>
<td>In-memory in Power BI</td>
<td>Scheduled refresh</td>
<td>Fastest; all operations in-memory</td>
<td>All Power BI features available</td>
</tr>
<tr>
<td><strong>DirectQuery</strong></td>
<td>Source system</td>
<td>Always current; no refresh needed</td>
<td>Slower; source-dependent</td>
<td>Some advanced features limited</td>
</tr>
<tr>
<td><strong>Dual</strong></td>
<td>Both in-memory and source</td>
<td>Scheduled + real-time queries</td>
<td>Fast for aggregations; slower for details</td>
<td>Most features supported</td>
</tr>
<tr>
<td><strong>Live Connection</strong></td>
<td>External Analysis Services or datasets</td>
<td>Data owner's refresh schedule</td>
<td>Source-dependent</td>
<td>Limited to connected model features</td>
</tr>
</table>

<p><em>Import mode</em> copies data into Power BI's columnar storage, enabling extremely fast queries and supporting all visualization features. However, data freshness is limited by refresh frequency (up to 8 times per day in Power BI Service), and dataset size is constrained by memory capacity. Use Import for historical analysis, stable reference data, and scenarios where slight data latency is acceptable.</p>

<p><em>DirectQuery mode</em> sends queries directly to the source system without caching data. Results reflect the latest source data, making it ideal for real-time requirements and scenarios where data volume exceeds Power BI capacity. However, performance depends entirely on source system responsiveness, and some advanced features like Quick Insights and certain visual types are unavailable. Use DirectQuery for compliance-sensitive scenarios requiring audit trails of all queries, compliance-driven data governance, and real-time dashboards.</p>

<p><em>Dual mode</em> intelligently combines both approaches. Power BI initially attempts DirectQuery to fetch fresh data but caches results for faster repeat queries. This mode provides reasonable freshness and performance but can be complex to optimize. Use Dual mode when you need both responsiveness and relative freshness with aggregated data tables combined with detailed source queries.</p>

<p><em>Live Connection</em> connects directly to SQL Server Analysis Services, Azure Analysis Services, or shared Power BI datasets. This mode delegates all processing to the connected model, making Power BI act as a visualization layer only. Use Live Connection to avoid data duplication and maintain a single source of truth across an organization.</p>

<h3>Query Parameters and Dynamic Filtering</h3>
<p>Query parameters enable dynamic, reusable values throughout your Power BI model. Rather than hardcoding filter values, create a parameter once and reference it across multiple queries and measures. Parameters support text, numeric, date, and logical data types.</p>

<p>To create a parameter, open Power Query Editor and select <strong>Manage Parameters &gt; New Parameter</strong>. Define the parameter name, data type, default value, and whether users can select from a predefined list. Common use cases include filtering by fiscal year, selecting regions dynamically, switching between development and production databases, or adjusting date ranges for rolling analyses.</p>

<p>Once created, reference a parameter in queries using the syntax <strong>Parameter.ParameterName</strong>. When you change the parameter value, all dependent queries automatically recalculate. This centralized approach reduces maintenance and enables what-if scenarios without modifying underlying queries.</p>

<p>Example: Create a <strong>FilterYear</strong> parameter with default value 2024. In your sales query, add a filter step: <strong>Table.SelectRows(Sales, each [Year] = FilterYear)</strong>. Now changing the FilterYear parameter instantly updates all reports using this query.</p>

<h3>Connecting to Dataflows and OneLake</h3>
<p>Dataflows represent a best practice for centralizing data preparation logic. Rather than duplicating transformation steps across multiple reports, create a dataflow that cleans and shapes data once, then reference it from any report. Dataflows execute in the cloud on the Power BI Service, reducing the need for scheduled refresh of each individual Power BI file.</p>

<p>When connecting to a dataflow, select <strong>Power BI dataflows</strong> as your source. This automatically discovers available dataflows in your organization's workspace. Dataflows support both Import and Linked Entity connections. A <strong>Linked Entity</strong> maintains a live connection to the dataflow output, ensuring your report reflects the latest transformation results.</p>

<p><strong>OneLake</strong> is Microsoft Fabric's unified data lake providing centralized storage for all organizational data. When your organization migrates to Fabric, Power BI can connect directly to lakehouse tables and semantic models stored in OneLake. This integration eliminates separate data silos and enables a unified analytics experience across BI, data engineering, and data science workloads. Connect via <strong>Microsoft Fabric</strong> connectors in Power BI to access lakehouses and warehouses seamlessly.</p>

<h3>Gateway Configuration for On-Premises Data</h3>
<p>When your data source resides on-premises behind a firewall, the Power BI Service cannot connect directly. A <strong>gateway</strong> acts as a bridge, securely forwarding queries from the cloud to your on-premises systems. Two gateway types exist: <strong>Standard gateways</strong> support multiple users and support multiple data sources, while <strong>Personal gateways</strong> are single-user instances useful for development.</p>

<p>To use a gateway, install it on a machine with network access to your on-premises data sources. Then, when configuring a data source connection in Power BI Service, select the gateway from the dropdown. The gateway encapsulates and routes credentials securely without exposing them to the internet. Administrators manage gateway health, user permissions, and data source credentials centrally, ensuring consistency and security across your organization's Power BI infrastructure.</p>
"""

QUESTIONS = [
    (
        "multiple_choice",
        """When connecting to a SQL Server database containing real-time financial transactions for a live dashboard that updates every 15 minutes, which storage mode should you select?""",
        [
            ("""Import mode to maximize query performance""", 0),
            ("""DirectQuery mode to ensure data is always current from the source""", 1),
            ("""Dual mode to balance import and source queries""", 0),
            ("""Live Connection mode exclusively for Analysis Services""", 0),
        ],
        """DirectQuery connects directly to the source system on each query, ensuring real-time accuracy. Import mode cannot provide the 15-minute freshness requirement since it refreshes on a schedule. Dual mode is less suitable here without specific aggregation tables. Live Connection requires Analysis Services, not SQL Server directly.""",
    ),
    (
        "multiple_choice",
        """Your organization has 500 GB of historical sales data in a data warehouse, but Power BI's dataset capacity limit is 1 GB for Import mode. Which storage mode must you use?""",
        [
            ("""Import mode to load all data at once""", 0),
            ("""DirectQuery mode to query the warehouse without importing 500 GB""", 1),
            ("""Dual mode to split the dataset evenly""", 0),
            ("""Live Connection to eliminate the size constraint""", 0),
        ],
        """DirectQuery queries the source system without caching data in Power BI, allowing you to analyze datasets larger than Power BI's in-memory capacity. Import mode would fail due to size constraints. Dual mode still requires in-memory storage. Live Connection is for Analysis Services, not data warehouses.""",
    ),
    (
        "multiple_choice",
        """You are building an interactive sales report with monthly trends, comparisons, and drill-through capabilities. The data fits within Power BI's capacity, and freshness is required daily. Which storage mode is most appropriate?""",
        [
            ("""Import mode for all visualization features and daily refresh schedule""", 1),
            ("""DirectQuery mode to eliminate refresh overhead""", 0),
            ("""Dual mode for superior responsiveness""", 0),
            ("""Live Connection to external datasets""", 0),
        ],
        """Import mode provides the fastest, most responsive experience for rich visualizations and drill-through. Daily scheduled refresh meets freshness requirements. DirectQuery would be slower for interactive use. Dual mode adds complexity without clear benefit for this scenario.""",
    ),
    (
        "multiple_choice",
        """When configuring a connection to an on-premises SQL Server database from Power BI Service, what component is essential to enable the connection?""",
        [
            ("""A gateway installed on a machine with network access to the on-premises database""", 1),
            ("""A cloud-hosted proxy server""", 0),
            ("""A VPN connection on every user's computer""", 0),
            ("""Direct firewall port forwarding to the database""", 0),
        ],
        """A gateway acts as a secure bridge between Power BI Service and on-premises data sources, routing queries without exposing credentials to the internet. Cloud proxies, individual VPNs, and firewall forwarding are neither secure nor scalable.""",
    ),
    (
        "multiple_choice",
        """You have created a dataflow that transforms raw customer data by removing duplicates and standardizing names. You want multiple reports to reference this prepared data without duplicating transformation logic. How should reports connect?""",
        [
            ("""Create separate dataflows for each report""", 0),
            ("""Use Linked Entities to connect to the dataflow output, maintaining a live reference""", 1),
            ("""Import the raw data into each report and repeat the transformations""", 0),
            ("""Connect via DirectQuery to the original source""", 0),
        ],
        """Linked Entities maintain a live connection to the dataflow, enabling centralized transformation logic reused by multiple reports. Creating separate dataflows duplicates work. Importing raw data and repeating transformations violates DRY principles and increases maintenance burden.""",
    ),
    (
        "multiple_choice",
        """In Power Query Editor, you create a parameter called &quot;SelectedYear&quot; with a default value of 2024. You add this parameter to your sales query filter. What is the immediate benefit?""",
        [
            ("""The parameter automatically sets the storage mode to Import""", 0),
            ("""Changing the SelectedYear value updates all queries and reports referencing it without manual edits""", 1),
            ("""The parameter eliminates the need for scheduled refreshes""", 0),
            ("""Parameters reduce the file size by compressing data""", 0),
        ],
        """Query parameters centralize configuration. When SelectedYear changes, all dependent queries recalculate automatically, enabling dynamic filtering and what-if analysis. Parameters do not affect storage mode, refresh requirements, or file compression.""",
    ),
    (
        "multiple_choice",
        """You connect to a data source and Power BI prompts you to set privacy levels. Your dataset contains confidential payroll information that should not combine with external web sources. Which privacy level is most appropriate?""",
        [
            ("""Public, since all company data is internal""", 0),
            ("""Organizational, to keep data within company scope""", 0),
            ("""Private, to isolate sensitive data from external sources""", 1),
            ("""No privacy level needed if the report is internal""", 0),
        ],
        """Private privacy level prevents combination with external sources, ensuring confidential payroll data remains isolated. Organizational allows internal combinations but does not prevent external data mixing. Public disables all protections. Privacy levels apply regardless of internal/external report scope.""",
    ),
    (
        "multiple_choice",
        """Your organization has published a curated semantic model on Power BI Service that combines cleaned customer and sales data. Multiple analysts need to build reports using this shared model. What is the most efficient approach?""",
        [
            ("""Each analyst duplicates the data preparation steps locally in their own Power BI files""", 0),
            ("""Each analyst creates a Live Connection to the published semantic model, using it as a data source""", 1),
            ("""The organization republishes the semantic model for each analyst""", 0),
            ("""Analysts connect via DirectQuery to the source database instead of the semantic model""", 0),
        ],
        """Live Connections to shared semantic models enable consistency, reduce duplication, and simplify updates—one model serves many reports. Duplicating preparation steps wastes effort and risks inconsistency. Republishing per analyst is inefficient. Bypassing the model defeats the purpose of sharing governance.""",
    ),
]