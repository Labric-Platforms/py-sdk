def get_table_id_by_name(client, table_name):
    tables = client.tools.read(
        target_type="core-table",
        target_name="table",
        filters={"name": table_name},
        mode="multiple",
    )
    if not tables:
        raise ValueError(f"No table found with name {table_name!r}")
    return tables[0]["id"]
