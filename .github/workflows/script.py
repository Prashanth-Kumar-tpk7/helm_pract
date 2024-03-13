import subprocess
cmd = ["helm", "upgrade" , "--install", "package-name", "./pathofchart", "--namespace","namespace_name","--create-namespace"]
subprocess.run(cmd, check=True)