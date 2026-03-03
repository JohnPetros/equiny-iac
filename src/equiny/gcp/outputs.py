import pulumi


def export_outputs(
    project_id: str,
    region: str,
    repo,
    provider,
    github_deploy_sa,
    runtime_sa,
    cloud_run_service: str,
):
    pulumi.export("gcpProjectId", project_id)
    pulumi.export("gcpRegion", region)
    pulumi.export("garLocation", region)
    pulumi.export("garRepository", repo.repository_id)
    pulumi.export("cloudRunService", cloud_run_service)
    pulumi.export("workloadIdentityProvider", provider.name)
    pulumi.export("githubDeployServiceAccount", github_deploy_sa.email)
    pulumi.export("cloudRunRuntimeServiceAccount", runtime_sa.email)
