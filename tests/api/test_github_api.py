import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    user = github_api.get_user("butenkosergii")
    assert user["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    user = github_api.search_repo("become-qa-auto")
    assert user["total_count"] == 29


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    user = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert user["total_count"] == 0
