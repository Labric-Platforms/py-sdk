# Reference
## Agent
<details><summary><code>client.agent.<a href="src/labric/agent/client.py">run</a>(...) -> AgentRunResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run the Labric data-analysis agent to completion and return its final
answer alongside the tool calls it made. Pass chat_id to continue a saved
conversation, or persist=true to save the run as a new chat visible in the
web UI; if saving fails, the response still carries the answer but its
chat_id is null. Long-running analyses should prefer the streaming
variant.
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

client.agent.run(
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

**request:** `AgentRunRequest` 
    
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

<details><summary><code>client.agent.<a href="src/labric/agent/client.py">run_stream</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stream an agent run as server-sent events. Each event is an
AgentRunEvent; the stream closes after a terminal `result` event, which
carries the same summary the non-streaming endpoint returns, or after a
terminal `error` event if the run fails. Persistence (chat_id / persist)
behaves as in the non-streaming variant.
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

**request:** `AgentRunRequest` 
    
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

## Tools
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

<details><summary><code>client.tools.<a href="src/labric/tools/client.py">upload_file</a>(...) -> LabricUploadFileSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a job artifact file.

Intended for use by jobs running in sandboxes. Accepts a multipart/form-data
file upload, stores it in GCS, records provenance linking the file to the
job execution, and returns the created file record.
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

client.tools.upload_file(
    file="example_file",
    job_execution_id="job_execution_id",
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

**job_execution_id:** `str` 
    
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

<details><summary><code>client.tools.<a href="src/labric/tools/client.py">list_files</a>(...) -> typing.List[ToolsFileInfoSchema]</code></summary>
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

client.tools.list_files()

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

<details><summary><code>client.tools.<a href="src/labric/tools/client.py">get_file_content</a>(...) -> ToolsFileContentSchema</code></summary>
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

client.tools.get_file_content(
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

<details><summary><code>client.tools.<a href="src/labric/tools/client.py">start_job_execution</a>(...) -> ToolsJobExecutionSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Open a job execution for a script running outside the platform.

Returns a job_execution_id to pass to the write and upload-file tools, so
everything a single script run produces is attributed to one execution and
can be inspected or reverted as a unit. Run under an existing job by passing
its job_id, or pass a job_name to run under a job of that name, creating it
if it does not exist; with neither, the execution lands under a default
off-platform job. The execution is marked running immediately; close it with
the update-status tool when the script finishes.
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

client.tools.start_job_execution(
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

<details><summary><code>client.tools.<a href="src/labric/tools/client.py">update_job_execution_status</a>(...) -> ToolsJobExecutionSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Close a job execution as completed or failed.

Use this when an off-platform script finishes, so the platform stops
reporting the run as in progress. Either status is final: re-sending the
status the execution already has is a no-op, but changing it afterwards is
rejected. Only executions opened by the start tool are accepted — every
other execution's status is recorded by the platform itself.
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

client.tools.update_job_execution_status(
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

<details><summary><code>client.tools.<a href="src/labric/tools/client.py">revert_job_execution</a>(...) -> RevertResultSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revert a test parse by deleting the rows it created.

Deletes the CREATE'd objects of a job execution and their linked raw rows,
in a single transaction. Use this to undo a test write whose validation
failed. UPDATE and DELETE operations cannot be reversed and are surfaced as
warnings in the result.
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

client.tools.revert_job_execution(
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

<details><summary><code>client.tools.<a href="src/labric/tools/client.py">predict</a>(...) -> PredictResponseSchema</code></summary>
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

client.tools.predict(
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

<details><summary><code>client.tools.<a href="src/labric/tools/client.py">list_ml_models</a>() -> typing.List[ToolsMlModelSchema]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the organization's ML models and the inputs each expects.

Returns each non-archived model with its serving status and prediction
interface: feature_columns (plus image_columns for image models) are the
fields each data row passed to the predict tool should contain, and
target_column is what the model predicts. Only models with status 'ready'
can serve predictions.
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

client.tools.list_ml_models()

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

