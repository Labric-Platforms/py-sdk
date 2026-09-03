# Reference
## files
<details><summary><code>client.files.<a href="src/labric/files/client.py">list</a>(...) -> typing.List[FileInfoSchema]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List source data files available for parser development.

Returns a representative set of uploaded files for the org, newest first.
Filter by instrument_id, comma-separated file extensions (e.g. "csv,txt"),
or a substring of the file name. Use the file-content tool to inspect a
file's raw contents.

Requires an API key with the `read` scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from labric import Labric
from labric.environment import LabricEnvironment

client = Labric(
    api_key="<token>",
    environment=LabricEnvironment.DEFAULT,
)

client.files.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**instrument_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**extensions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/labric/files/client.py">upload</a>(...) -> FileUploadSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a file.

Accepts a multipart/form-data file upload, stores it in GCS, and returns the
created file record. At least one of job_execution_id and instrument_id is
required: pass a job_execution_id for an artifact of a job running in a
sandbox, which also records provenance linking the file to that execution,
and pass an instrument_id for data captured off-platform by an instrument the
Sync app cannot reach, which attaches the file to that instrument so
instrument triggers and parsers pick it up.

Requires an API key with the `write` scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from labric import Labric
from labric.environment import LabricEnvironment

client = Labric(
    api_key="<token>",
    environment=LabricEnvironment.DEFAULT,
)

client.files.upload(
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**job_execution_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**instrument_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/labric/files/client.py">get_content</a>(...) -> FileContentSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch a source file's content for inspecting raw instrument output.

Returns a presigned download URL plus a best-effort UTF-8 text preview of
the start of the file. Large files return a URL only (no inline preview);
fetch the full bytes via the URL when needed.

Requires an API key with the `read` scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from labric import Labric
from labric.environment import LabricEnvironment

client = Labric(
    api_key="<token>",
    environment=LabricEnvironment.DEFAULT,
)

client.files.get_content(
    file_id="file_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## agent
<details><summary><code>client.agent.<a href="src/labric/agent/client.py">run_stream</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run the Labric data-analysis agent and return its final answer
alongside the tool calls it made. With stream=true the response is
instead a stream of server-sent AgentRunEvent events, closing after a
terminal `result` event that carries the same summary, or an `error`
event if the run fails; prefer streaming for long analyses. Pass chat_id
to continue a saved conversation, or save=true to save the run as a new
chat visible in the web UI; if saving fails, the answer is still returned
but its chat_id is null.

Requires an API key with the `read` scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from labric import Labric
from labric.environment import LabricEnvironment

client = Labric(
    api_key="<token>",
    environment=LabricEnvironment.DEFAULT,
)

client.agent.run_stream(
    prompt="prompt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Literal` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**chat_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**save:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/labric/agent/client.py">run</a>(...) -> AgentRunResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run the Labric data-analysis agent and return its final answer
alongside the tool calls it made. With stream=true the response is
instead a stream of server-sent AgentRunEvent events, closing after a
terminal `result` event that carries the same summary, or an `error`
event if the run fails; prefer streaming for long analyses. Pass chat_id
to continue a saved conversation, or save=true to save the run as a new
chat visible in the web UI; if saving fails, the answer is still returned
but its chat_id is null.

Requires an API key with the `read` scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from labric import Labric
from labric.environment import LabricEnvironment

client = Labric(
    api_key="<token>",
    environment=LabricEnvironment.DEFAULT,
)

client.agent.run_stream(
    prompt="prompt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Literal` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**chat_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**save:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## jobs
<details><summary><code>client.jobs.<a href="src/labric/jobs/client.py">start</a>(...) -> OffPlatformJobExecutionSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Open a job execution for a script running outside the platform.

Pass the returned job_execution_id to the write and upload-file tools so
everything one script run produces is attributed to a single execution and
can be inspected or reverted as a unit. Pass job_id to run under an
existing job, job_name to run under a job of that name (created if
missing), or neither to run under the default off-platform job.

The execution is marked running immediately. Close it as completed or
failed when the script finishes. Pass timeout_minutes to have the platform
fail it after that long if the script has not closed it, so a crashed
script does not leave it running forever.

Requires an API key with the `write` scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from labric import Labric, StartJobExecutionSchema
from labric.environment import LabricEnvironment

client = Labric(
    api_key="<token>",
    environment=LabricEnvironment.DEFAULT,
)

client.jobs.start(
    request=StartJobExecutionSchema(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Optional[StartJobExecutionSchema]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/labric/jobs/client.py">close</a>(...) -> OffPlatformJobExecutionSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Close a job execution as completed or failed.

Call this when an off-platform script finishes. Either status is final:
re-sending the same status is a no-op, and changing it is rejected. Only
executions opened by the start tool are accepted; the platform records
every other execution's status itself.

Requires an API key with the `write` scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from labric import Labric
from labric.environment import LabricEnvironment

client = Labric(
    api_key="<token>",
    environment=LabricEnvironment.DEFAULT,
)

client.jobs.close(
    execution_id="execution_id",
    status="completed",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**execution_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `UpdateJobExecutionStatusSchemaStatus` — How the run ended. Either status is final: the execution cannot change status afterwards.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/labric/jobs/client.py">revert</a>(...) -> RevertResultSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revert a job execution by deleting the rows it created.

Deletes the execution's created objects and their linked raw rows in one
transaction, for undoing a test write that failed validation. Updates and
deletes cannot be reversed and are reported as warnings in the result.

Requires an API key with the `write` scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from labric import Labric
from labric.environment import LabricEnvironment

client = Labric(
    api_key="<token>",
    environment=LabricEnvironment.DEFAULT,
)

client.jobs.revert(
    execution_id="execution_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**execution_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## tools
<details><summary><code>client.tools.<a href="src/labric/tools/client.py">write</a>(...) -> typing.List[typing.Dict[str, typing.Any]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Write records to a table.

Inserts or updates records in the specified target table. Supports batch
inserts, upserts with match columns, default value functions (DATETIME_NOW,
UUID4), and optional dry-run validation. A job execution is created
automatically if one is not provided.

Requires an API key with the `write` scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from labric import Labric
from labric.environment import LabricEnvironment

client = Labric(
    api_key="<token>",
    environment=LabricEnvironment.DEFAULT,
)

client.tools.write(
    target_name="target_name",
    target_type="table",
    data=[
        {
            "key": "value"
        }
    ],
    mode="mode",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**target_name:** `str` — The name of the table to write to.
    
</dd>
</dl>

<dl>
<dd>

**target_type:** `LabricWriteSchemaTargetType` — The type of target. Currently 'table' or 'core-table'.
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.List[typing.Dict[str, typing.Any]]` — List of record dicts to write.
    
</dd>
</dl>

<dl>
<dd>

**mode:** `str` — Write mode (e.g. 'create', 'create-or-update').
    
</dd>
</dl>

<dl>
<dd>

**batch_insert_ok:** `typing.Optional[bool]` — If True, allow batch insert of multiple records.
    
</dd>
</dl>

<dl>
<dd>

**params_to_match_for_update:** `typing.Optional[typing.List[str]]` — Column names to match on when updating existing records.
    
</dd>
</dl>

<dl>
<dd>

**defaults:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — Map of field names to default function names (e.g. 'DATETIME_NOW', 'UUID4').
    
</dd>
</dl>

<dl>
<dd>

**job_execution_id:** `typing.Optional[str]` — Existing job execution ID to associate with this write. If omitted, a new one is created.
    
</dd>
</dl>

<dl>
<dd>

**job_name:** `typing.Optional[str]` — Name for the auto-created job. Defaults to 'Off-Platform Manual Job'.
    
</dd>
</dl>

<dl>
<dd>

**collect_output:** `typing.Optional[bool]` — If True, return the written records in the response.
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — If True, resolve references, check table and column validity, and return the execution plan without committing changes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/labric/tools/client.py">read</a>(...) -> typing.List[typing.Dict[str, typing.Any]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read records from a table.

Returns records from the specified table matching the given filters.
Use 'single' mode to retrieve exactly one record, or 'multiple' mode
to retrieve all matching records.

Requires an API key with the `read` scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from labric import Labric
from labric.environment import LabricEnvironment

client = Labric(
    api_key="<token>",
    environment=LabricEnvironment.DEFAULT,
)

client.tools.read(
    target_name="target_name",
    target_type="table",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**target_name:** `str` — The name of the table to read from.
    
</dd>
</dl>

<dl>
<dd>

**target_type:** `LabricReadSchemaTargetType` — The type of target. Either 'table' or 'core-table'.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.Dict[str, typing.Any]]` — Key-value filters to apply to the query. Omit to match all records.
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[LabricReadSchemaMode]` — 'single' returns exactly one record and throws an error if more than one matching record exists, 'multiple' returns all matches.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/labric/tools/client.py">execute_sql</a>(...) -> QueryResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a read-only SQL query.

Runs the query against the organization's read replica, so it cannot
mutate data. Only SELECT statements are accepted. Supports positional
parameters via a params list. Use the schema tool to discover tables
first, and reference each column by its sql_column_name — foreign keys
carry an _id suffix in SQL (e.g. a 'sample' reference is the 'sample_id'
column).

Requires an API key with the `read` scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from labric import Labric
from labric.environment import LabricEnvironment

client = Labric(
    api_key="<token>",
    environment=LabricEnvironment.DEFAULT,
)

client.tools.execute_sql(
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[typing.List[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/labric/tools/client.py">get_schema</a>() -> typing.List[TableSchemaInfoSchema]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Describe the organization's data schema.

Returns every table the agent can target, including its semantic category
(e.g. raw vs. curated), description, and full column definitions with types,
nullability, uniqueness, and foreign-key targets. Each column carries two
names: 'name' is what the read and write tools accept, and 'sql_column_name'
is the physical column for SQL queries (foreign keys carry an _id suffix).
This is the map a parser writes into: use it to plan which tables to
populate and how rows link.

Requires an API key with the `read` scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from labric import Labric
from labric.environment import LabricEnvironment

client = Labric(
    api_key="<token>",
    environment=LabricEnvironment.DEFAULT,
)

client.tools.get_schema()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/labric/tools/client.py">batch_write</a>(...) -> BatchWriteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Write records to multiple tables in a single transaction.

Supports:
- Batch references: Use "_ref" to label records, "@refname" to reference them
- Natural keys: Use human-readable values for foreign keys (e.g., recipe name)
- Automatic FK ordering: Tables are inserted in dependency order
- Upsert mode: Update existing records based on match columns
- Dry run: Validate without committing changes

Committed writes are recorded against a job execution (created automatically
if not supplied) and the job_execution_id is returned, so the write can be
reverted as a unit.

Requires an API key with the `write` scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from labric import Labric
from labric.environment import LabricEnvironment

client = Labric(
    api_key="<token>",
    environment=LabricEnvironment.DEFAULT,
)

client.tools.batch_write(
    tables={
        "key": [
            {
                "key": "value"
            }
        ]
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tables:** `typing.Dict[str, typing.List[typing.Dict[str, typing.Any]]]` — Map of table_name to list of records to insert.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[BatchWriteOptions]` — Optional write options (mode, match_on, dry_run, return_records).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## models
<details><summary><code>client.models.<a href="src/labric/models/client.py">predict</a>(...) -> PredictResponseSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run predictions with a trained ML model.

Identify the model by ml_model_id, or by ml_model_name (the name of a
non-archived model). Each row in data maps the model's feature columns to
values -- use the ml-models tool to discover models and the columns each
expects. Returns one prediction per input row, plus per-class
probabilities for classifiers.

Requires an API key with the `read` scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from labric import Labric
from labric.environment import LabricEnvironment

client = Labric(
    api_key="<token>",
    environment=LabricEnvironment.DEFAULT,
)

client.models.predict(
    data=[
        {
            "key": "value"
        }
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**data:** `typing.List[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**ml_model_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ml_model_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/labric/models/client.py">get</a>(...) -> ToolsMlModelDetailSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one ML model's training status and results.

Requires an API key with the `read` scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from labric import Labric
from labric.environment import LabricEnvironment

client = Labric(
    api_key="<token>",
    environment=LabricEnvironment.DEFAULT,
)

client.models.get(
    ml_model_id="ml_model_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ml_model_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/labric/models/client.py">list</a>() -> typing.List[ToolsMlModelDetailSchema]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about models in the organization.
If model_id is given, return information about that model.
If model_id is None, return a list of all models.

Returns every non-archived model. To fetch one model by id, use the
get-ml-model tool instead.


Note that the currently active model may not be the most recently trained one.
Also note that the status might not be perfectly up-to-date.

Requires an API key with the `read` scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from labric import Labric
from labric.environment import LabricEnvironment

client = Labric(
    api_key="<token>",
    environment=LabricEnvironment.DEFAULT,
)

client.models.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/labric/models/client.py">train</a>(...) -> ToolsMlModelDetailSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

API endpoint trains a ML model.
To train a new model, the name is required and model_id should not be provided.
To retrain an existing model, provide the model_id and do not provide the name.

Requires an API key with the `write` scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from labric import Labric
from labric.environment import LabricEnvironment

client = Labric(
    api_key="<token>",
    environment=LabricEnvironment.DEFAULT,
)

client.models.train(
    target_column="target_column",
    dataset_id="dataset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**target_column:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**task_type:** `typing.Optional[MlModelTaskType]` 
    
</dd>
</dl>

<dl>
<dd>

**quality_preset:** `typing.Optional[QualityPreset]` 
    
</dd>
</dl>

<dl>
<dd>

**feature_columns:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**image_columns:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**problem_type:** `typing.Optional[MlProblemType]` 
    
</dd>
</dl>

<dl>
<dd>

**ml_model_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/labric/models/client.py">cancel_training</a>(...) -> ToolsMlModelDetailSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel the model's in-flight training runs.

Overlapping retrains can leave several versions pending or training at
once, so the cancel is model-wide: every in-flight version is marked
'cancelled' and its cloud training jobs are stopped. Returns 400 when
no training is pending or running.

Requires an API key with the `write` scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from labric import Labric
from labric.environment import LabricEnvironment

client = Labric(
    api_key="<token>",
    environment=LabricEnvironment.DEFAULT,
)

client.models.cancel_training(
    ml_model_id="ml_model_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ml_model_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

