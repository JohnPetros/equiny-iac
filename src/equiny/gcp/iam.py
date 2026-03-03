import pulumi_gcp as gcp


def grant_github_deploy_permissions(project_id: str, github_deploy_sa):
    roles = [
        "roles/run.admin",
        "roles/artifactregistry.writer",
    ]

    for i, role in enumerate(roles):
        gcp.projects.IAMMember(
            f"github-deploy-role-{i}",
            project=project_id,
            role=role,
            member=github_deploy_sa.email.apply(lambda e: f"serviceAccount:{e}"),
        )


def allow_github_to_use_runtime_sa(github_deploy_sa, runtime_sa):
    gcp.serviceaccount.IAMBinding(
        "github-actas-runtime",
        service_account_id=runtime_sa.name,
        role="roles/iam.serviceAccountUser",
        members=[github_deploy_sa.email.apply(lambda e: f"serviceAccount:{e}")],
    )


def allow_runtime_to_read_secrets(project_id: str, runtime_sa):
    gcp.projects.IAMMember(
        "runtime-secret-accessor",
        project=project_id,
        role="roles/secretmanager.secretAccessor",
        member=runtime_sa.email.apply(lambda e: f"serviceAccount:{e}"),
    )


def allow_wif_to_impersonate_sa(github_deploy_sa, principal):
    gcp.serviceaccount.IAMBinding(
        "github-wif-user",
        service_account_id=github_deploy_sa.name,
        role="roles/iam.workloadIdentityUser",
        members=[principal],
    )
