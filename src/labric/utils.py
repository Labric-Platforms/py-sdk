from typing import Any


def get_or_create_operation(
    client,
    step_name: str,
    step_params: dict[str, Any],
    table_id: int,
    organization_id: str,
    start_time: str,
    end_time: str | None = None,
    has_effect: bool = True,
    job_execution_id: str | None = None,
) -> dict[str, Any]:
    """Create (or reuse) the procedurestep + operation pair backing a process step or measurement."""
    end_time = end_time or start_time
    step = client.tools.write(
        target_type="core-table",
        target_name="procedurestep",
        data=[
            {
                "name": step_name,
                "parameters": step_params,
                "organization_id": organization_id,
                "table_id": table_id,
                "has_effect": has_effect,
            }
        ],
        mode="create-or-update",
        params_to_match_for_update=["name", "parameters", "table_id", "has_effect"],
        defaults={
            "id": "UUID4",
            "date_created": "DATETIME_NOW",
            "date_updated": "DATETIME_NOW",
        },
        job_execution_id=job_execution_id,
        collect_output=True,
    )[0]
    return client.tools.write(
        target_type="core-table",
        target_name="operation",
        data=[
            {
                "name": f"{step_name} {start_time}",
                "step_id": step["id"],
                "status": "completed",
                "organization_id": organization_id,
                "is_atomic": True,
                "start_time": start_time,
                "end_time": end_time,
            }
        ],
        mode="create-or-update",
        params_to_match_for_update=[
            "name",
            "step_id",
            "organization_id",
            "start_time",
            "end_time",
            "is_atomic",
        ],
        defaults={
            "id": "UUID4",
            "date_created": "DATETIME_NOW",
            "date_updated": "DATETIME_NOW",
        },
        job_execution_id=job_execution_id,
        collect_output=True,
    )[0]


def record_process_step(
    client,
    table_name: str,
    step_name: str,
    step_params: dict[str, Any],
    rows: list[dict[str, Any]],
    organization_id: str,
    table_id: int,
    start_time: str,
    end_time: str | None = None,
    has_effect: bool = True,
    params_to_match_for_update: list[str] | None = None,
    job_execution_id: str | None = None,
) -> list[dict[str, Any]]:
    """Record a process step: create its operation, then write rows to table_name with operation_id merged in.

    Set has_effect=False (or use record_measurement_step) for characterizations that don't
    change sample state.
    """
    operation = get_or_create_operation(
        client,
        step_name,
        step_params,
        table_id,
        organization_id,
        start_time,
        end_time,
        has_effect,
        job_execution_id,
    )
    data = [{**row, "operation_id": operation["id"]} for row in rows]
    return client.tools.write(
        target_type="table",
        target_name=table_name,
        data=data,
        mode="create-or-update",
        params_to_match_for_update=params_to_match_for_update or list(data[0].keys()),
        defaults={"id": "UUID4"},
        job_execution_id=job_execution_id,
        collect_output=True,
    )


def record_measurement_step(
    client,
    table_name: str,
    step_name: str,
    step_params: dict[str, Any],
    rows: list[dict[str, Any]],
    organization_id: str,
    table_id: int,
    start_time: str,
    end_time: str | None = None,
    params_to_match_for_update: list[str] | None = None,
    job_execution_id: str | None = None,
) -> list[dict[str, Any]]:
    """Record a measurement/characterization step (has_effect=False process step)."""
    return record_process_step(
        client,
        table_name,
        step_name,
        step_params,
        rows,
        organization_id,
        table_id,
        start_time,
        end_time,
        has_effect=False,
        params_to_match_for_update=params_to_match_for_update,
        job_execution_id=job_execution_id,
    )
