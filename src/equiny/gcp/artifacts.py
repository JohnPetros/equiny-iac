import pulumi_gcp as gcp


def create_artifact_registry(project_id: str, region: str, repository_id: str):
    return gcp.artifactregistry.Repository(
        "equiny-repo",
        project=project_id,
        location=region,
        repository_id=repository_id,
        format="DOCKER",
        description="Docker repository for Equiny",
    )
