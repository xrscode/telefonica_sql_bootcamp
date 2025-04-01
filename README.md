# telefonica_sql_bootcamp
telefonica_sql_bootcamp

<!-- Requirements -->
1. Download and install ODBC Driver:
https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16

2.  Download and install Chocolatey:
https://chocolatey.org/install

3.  Install Terraform with Chocolatey
choco install terraform --pre
https://community.chocolatey.org/packages/Terraform

4. Deploy package:
Run the following command in the terminal:
.\deploy.ps1

5.  SSMS:
When Terraform has finished deploying resources you should be able to connect
to SSMS.  To see the user credentials check the .env file created during setup.

6.  When finished to destroy run the following command in the terminal:
cd terraform && terraform destroy -auto-approve && cd ..



Useful commands:
1. To set the python path enter into terminal (from root folder of project):
$env:PYTHONPATH = "$PWD"