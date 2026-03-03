from src.equiny.gcp.config import AppConfig
from src.equiny.gcp.artifacts import create_artifact_registry
from src.equiny.gcp.secrets import create_application_secrets
from src.equiny.gcp.service_accounts import create_service_accounts
from src.equiny.gcp.workload_identity import create_github_wif
from src.equiny.gcp.iam import (
    grant_github_deploy_permissions,
    allow_github_to_use_runtime_sa,
    allow_runtime_to_read_secrets,
    allow_wif_to_impersonate_sa,
)
from src.equiny.gcp.outputs import export_outputs


def build_stack():
    cfg = AppConfig()

    repo = create_artifact_registry(
        project_id=cfg.project_id,
        region=cfg.region,
        repository_id=cfg.gar_repository,
    )

    create_application_secrets(
        project_id=cfg.project_id,
        app_secrets=cfg.app_secrets,
    )

    github_deploy_sa, runtime_sa = create_service_accounts(cfg.project_id)

    _, provider, principal = create_github_wif(
        project_id=cfg.project_id,
        github_owner=cfg.github_owner,
        github_repo=cfg.github_repo,
    )

    grant_github_deploy_permissions(cfg.project_id, github_deploy_sa)
    allow_github_to_use_runtime_sa(github_deploy_sa, runtime_sa)
    allow_runtime_to_read_secrets(cfg.project_id, runtime_sa)
    allow_wif_to_impersonate_sa(github_deploy_sa, principal)

    export_outputs(
        project_id=cfg.project_id,
        region=cfg.region,
        repo=repo,
        provider=provider,
        github_deploy_sa=github_deploy_sa,
        runtime_sa=runtime_sa,
        cloud_run_service=cfg.cloud_run_service,
    )
