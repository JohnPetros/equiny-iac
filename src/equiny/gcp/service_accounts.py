import pulumi_gcp as gcp


def create_service_accounts(project_id: str):
    github_deploy_sa = gcp.serviceaccount.Account(
        "github-deploy-sa",
        project=project_id,
        account_id="github-deploy-sa",
        display_name="GitHub Deploy Service Account",
    )

    cloud_run_runtime_sa = gcp.serviceaccount.Account(
        "cloud-run-runtime-sa",
        project=project_id,
        account_id="cloud-run-runtime-sa",
        display_name="Cloud Run Runtime Service Account",
    )

    return github_deploy_sa, cloud_run_runtime_sa
