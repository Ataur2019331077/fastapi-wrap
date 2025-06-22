import subprocess

def test_cli_runs():
    result = subprocess.run(
        ["simple-fastapi-backend-server"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=5
    )
    # We only check that it starts up correctly
    assert result.returncode == 0 or result.returncode is None
