import os


def write_core_table(
    client,
    target_name,
    data,
    params_to_match_for_update=None,
    mode="create-or-update",
    defaults=None,
    collect_output=True,
):
    job_execution_id = os.getenv("LABRIC_JOB_EXECUTION_ID")
    return client.tools.write(
        target_type="core-table",
        target_name=target_name,
        data=data,
        mode=mode,
        params_to_match_for_update=params_to_match_for_update,
        job_execution_id=job_execution_id,
        defaults=defaults,
        collect_output=collect_output,
    )


def write_labric_table(
    client,
    target_name,
    data,
    params_to_match_for_update=None,
    mode="create-or-update",
    defaults=None,
    batch_insert_ok=False,
    collect_output=True,
):
    job_execution_id = os.getenv("LABRIC_JOB_EXECUTION_ID")
    return client.tools.write(
        target_type="table",
        target_name=target_name,
        data=data,
        mode=mode,
        params_to_match_for_update=params_to_match_for_update,
        job_execution_id=job_execution_id,
        defaults=defaults,
        batch_insert_ok=batch_insert_ok,
        collect_output=collect_output,
    )
