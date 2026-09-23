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

Upload a file in one multipart/form-data request.

Request bodies over 4.5 MB are rejected at the platform edge before they
reach this route. For larger files, create an upload URL and PUT the bytes
to it instead; the SDK's files.upload() does that for files of any size.
The [Upload files](https://docs.labric.co/upload-files) guide walks
through both flows.

At least one of job_execution_id and instrument_id is required: pass a
job_execution_id for an artifact of a job running in a sandbox, which also
records provenance linking the file to that execution, and pass an
instrument_id for data captured off-platform by an instrument the Sync app
cannot reach, which attaches the file to that instrument so instrument
triggers and parsers pick it up.

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

<details><summary><code>client.files.<a href="src/labric/files/client.py">create_upload_url</a>(...) -> FileUploadUrlSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start an upload that sends the file bytes straight to storage.

Creates the file record and returns a signed URL that accepts the bytes as
the body of an HTTP PUT for the next 15 minutes. Send exactly the returned
headers on the PUT and no Authorization header, then confirm the upload to
make the file visible. The URL only creates the object, never replaces one,
and refuses bodies over 500 MB. Asking again for an instrument path whose
upload was never confirmed returns a fresh URL for the same file, so a
failed PUT can be retried. The SDK's files.upload() runs all three steps;
the [Upload files](https://docs.labric.co/upload-files) guide shows them
with curl.

At least one of job_execution_id and instrument_id is required: pass a
job_execution_id for an artifact of a job running in a sandbox, which also
records provenance linking the file to that execution, and pass an
instrument_id for data captured off-platform by an instrument the Sync app
cannot reach, which attaches the file to that instrument so instrument
triggers and parsers pick it up.

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

client.files.create_upload_url(
    file_name="file_name",
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

**file_name:** `str` — The file name to record, e.g. results.csv.
    
</dd>
</dl>

<dl>
<dd>

**content_type:** `typing.Optional[str]` — MIME type of the file. Defaults to application/octet-stream, which is also substituted for types a browser could render as a page.
    
</dd>
</dl>

<dl>
<dd>

**job_execution_id:** `typing.Optional[str]` — The job execution producing the file, for a job artifact.
    
</dd>
</dl>

<dl>
<dd>

**instrument_id:** `typing.Optional[str]` — The instrument that captured the file, for off-platform data.
    
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

<details><summary><code>client.files.<a href="src/labric/files/client.py">confirm_upload</a>(...) -> FileUploadSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Finish an upload after the PUT to its upload URL has succeeded.

Records the stored file's size and checksum, makes the file visible in
listings, and notifies triggers and parsers. Files over 500 MB and native
executables are discarded with a 400, as the one-request upload rejects
them. Confirming a file that is already confirmed returns its record again
without notifying anyone twice. The
[Upload files](https://docs.labric.co/upload-files) guide shows the full
sequence.

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

client.files.confirm_upload(
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
<details><summary><code>client.jobs.<a href="src/labric/jobs/client.py">list</a>(...) -> typing.List[ToolsJobSchema]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the organization's jobs, newest first.

Pass name to look up one job, since job names are unique within an
organization; the list is then empty or holds that job. Archived jobs
are left out unless archived is true.

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

client.jobs.list()

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

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.jobs.<a href="src/labric/jobs/client.py">create</a>(...) -> ToolsJobSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a job that runs a Python script on the platform.

The code becomes the job's script; declare its dependencies inline in a
PEP 723 `# /// script` block. The job then appears on the platform, where
it can be run and its executions reviewed. To change an existing job's
name, description, or code, use update_job instead.

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

client.jobs.create(
    name="name",
    code="code",
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

**name:** `str` — Name of the job. Unique within the organization.
    
</dd>
</dl>

<dl>
<dd>

**code:** `str` — Python source of the script the job runs. Declare dependencies inline in a PEP 723 `# /// script` block.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — What the job does.
    
</dd>
</dl>

<dl>
<dd>

**trigger_enabled:** `typing.Optional[bool]` — True runs the job automatically when its trigger fires.
    
</dd>
</dl>

<dl>
<dd>

**trigger_category:** `typing.Optional[JobTriggerCategory]` — What runs the job automatically: file_uploaded runs it on each uploaded file that matches the conditions; job_completed runs it on the output files of another job's executions. Required when trigger_enabled is true.
    
</dd>
</dl>

<dl>
<dd>

**trigger_instrument_id:** `typing.Optional[str]` — Restricts a file_uploaded trigger to files from this instrument.
    
</dd>
</dl>

<dl>
<dd>

**trigger_conditions:** `typing.Optional[typing.Dict[str, typing.Any]]` — Filters on the triggering event. For file_uploaded, any of file_name_pattern (glob or regex), file_extensions (list of strings starting with '.'), source_type, min_size_kb, and max_size_kb. For job_completed, source_job_id (required) and statuses (list drawn from completed and failed; defaults to completed).
    
</dd>
</dl>

<dl>
<dd>

**parameter_definitions:** `typing.Optional[typing.List[ParameterDefinitionSchema]]` — Inputs the script reads at run time. Each is rendered as a form control when the job is run on the platform.
    
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

<details><summary><code>client.jobs.<a href="src/labric/jobs/client.py">update</a>(...) -> ToolsJobSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Change a job's name, description, code, trigger, or parameters, or
archive it.

Only the fields passed are changed. New code is stored as a new version of
the job's script, so earlier executions keep the version they ran. To
create a job, use create_job instead.

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

client.jobs.update(
    job_id="job_id",
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

**job_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — New name for the job.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — New description for the job. Pass an empty string to clear it.
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` — New Python source for the job's script, stored as a new script version. Declare dependencies inline in a PEP 723 `# /// script` block.
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` — True archives the job, hiding it from the active job list; false restores it.
    
</dd>
</dl>

<dl>
<dd>

**trigger_enabled:** `typing.Optional[bool]` — True creates or replaces the job's trigger from the trigger fields; false removes it.
    
</dd>
</dl>

<dl>
<dd>

**trigger_category:** `typing.Optional[JobTriggerCategory]` — What runs the job automatically: file_uploaded runs it on each uploaded file that matches the conditions; job_completed runs it on the output files of another job's executions. Required when trigger_enabled is true.
    
</dd>
</dl>

<dl>
<dd>

**trigger_instrument_id:** `typing.Optional[str]` — Restricts a file_uploaded trigger to files from this instrument.
    
</dd>
</dl>

<dl>
<dd>

**trigger_conditions:** `typing.Optional[typing.Dict[str, typing.Any]]` — Filters on the triggering event. For file_uploaded, any of file_name_pattern (glob or regex), file_extensions (list of strings starting with '.'), source_type, min_size_kb, and max_size_kb. For job_completed, source_job_id (required) and statuses (list drawn from completed and failed; defaults to completed).
    
</dd>
</dl>

<dl>
<dd>

**parameter_definitions:** `typing.Optional[typing.List[ParameterDefinitionSchema]]` — Inputs the script reads at run time. Each is rendered as a form control when the job is run on the platform.
    
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

Core tables are writable only if they appear in the write allowlist. Tables
that describe the organization itself, such as organizationmember, are
read-only and can only be reached through the read tool.

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

**target_type:** `LabricWriteSchemaTargetType` — The type of target. Currently 'table' or 'core-table'. Only some core tables are writable. Tables describing the organization, such as organizationmember, are read-only.
    
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

**on_match:** `typing.Optional[LabricWriteSchemaOnMatch]` — How a matched record takes the provided columns in create-or-update mode. 'fill_missing' only sets columns that are currently null. 'overwrite' replaces them, and a provided null clears the column. Columns absent from the record and default functions never overwrite an existing value.
    
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

**filters:** `typing.Optional[typing.Dict[str, typing.Any]]` — Key-value filters to apply to the query. Omit to match all records. A key may follow a foreign key onto another readable table, as in instrument_type__name; tables the read tool does not return are not traversable.
    
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
parameters: write %s placeholders in the query and pass the values in
order in the params list. Named :param placeholders belong to saved
dataset queries and are not accepted here. Use the schema tool to discover tables
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

<details><summary><code>client.tools.<a href="src/labric/tools/client.py">get_schema</a>() -> typing.List[QueryableTableSchema]</code></summary>
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
The org's own tables are followed by the platform tables (core_experiment,
core_instrument, and similar) that SQL queries can join against; those have
no id or semantic category. This is the map a parser writes into: use it to
plan which tables to populate and how rows link.

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

## images
<details><summary><code>client.images.<a href="src/labric/images/client.py">annotate</a>(...) -> typing.List[AnnotationSchema]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Save masks on an image as annotations, one per entry.

Each entry is a binary mask PNG (white-on-transparent, base64-encoded)
for a label; labels are created on first use. Saving is additive, so
a label can accumulate several masks on the same image. The annotations
a segmentation model returns from predict can be passed straight through;
each names the file it was predicted for, and one for a different file
rejects the request. Leave is_human_vetted false for automated saves:
the mask editor flags unvetted masks for review, and only vetted masks
feed training. The file must be a processed image. All-or-nothing: one
bad entry rejects the whole request.

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
from labric import Labric, SaveAnnotationSchema
from labric.environment import LabricEnvironment

client = Labric(
    api_key="<token>",
    environment=LabricEnvironment.DEFAULT,
)

client.images.annotate(
    file_id="file_id",
    annotations=[
        SaveAnnotationSchema(
            mask="mask",
            label="label",
        )
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

**file_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**annotations:** `typing.List[SaveAnnotationSchema]` 
    
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

## notifications
<details><summary><code>client.notifications.<a href="src/labric/notifications/client.py">send</a>(...) -> SentNotificationSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a message to your own inbox, and to your email if you have enabled
email for the Message category in your notification preferences. Sends are
capped per hour and per organization per day; a 429 response carries a
Retry-After header. Messages sent with an API key are attributed to it, so
the recipient can tell where they came from.

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

client.notifications.send(
    title="title",
    dedupe_key="dedupe_key",
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

**title:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**dedupe_key:** `str` — Idempotency key; a repeat send with the same key is dropped
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**action_url:** `typing.Optional[str]` — Platform path the notification opens, such as /jobs/<id>
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Optional[typing.Dict[str, typing.Any]]` — Structured context stored with the notification. The keys sender and api_key_id are reserved for sender attribution.
    
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

