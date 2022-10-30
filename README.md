# backup-restore-challenge

This solution solve the [backup_restore](https://hackattic.com/challenges/backup_restore) challenge.

## How to run the solution
You need to take the following steps to solve the `backup_restore` challenge:
1. Run the `make init` command (create the `.env` file)
2. Fill the `ACCESS_TOKEN`(from the https://hackattic.com/challenges/backup_restore) and the `DB_USER_PASSWORD` (random value)
3. Run the `make build` command (build the custom image with the script)
4. Run the `make up` command (get data from the challenge and send result)
5. Run the `make down` (remove running containers)
