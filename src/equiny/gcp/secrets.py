import pulumi_gcp as gcp


def create_application_secrets(project_id: str, app_secrets: dict):
    created = {}

    for secret_id, secret_value in app_secrets.items():
        secret = gcp.secretmanager.Secret(
            f"secret-{secret_id}",
            project=project_id,
            secret_id=secret_id,
            replication={"auto": {}},
        )

        gcp.secretmanager.SecretVersion(
            f"secret-version-{secret_id}",
            secret=secret.id,
            secret_data=secret_value,
        )

        created[secret_id] = secret

    return created
