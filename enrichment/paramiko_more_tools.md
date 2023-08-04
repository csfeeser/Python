Here are some things you can do with the SFTP connection you created!

| Action                      | Method                                      | Description                                                                                                           |
|-----------------------------|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| List Directory Contents     | `sftp.listdir(remote_path)`                     | Returns a list of files and directories in the specified remote path.                                                 |
| Get File                    | `sftp.get(remote_path, local_path)`             | Downloads a file from the remote SFTP server to the local file system.                                                |
| Put File                    | `sftp.put(local_path, remote_path)`             | Uploads a file from the local file system to the remote SFTP server.                                                  |
| Remove File                 | `sftp.remove(remote_path)`                      | Deletes a file on the remote SFTP server.                                                                             |
| Create Directory            | `sftp.mkdir(remote_path)`                       | Creates a new directory on the remote SFTP server.                                                                    |
| Remove Directory            | `sftp.rmdir(remote_path)`                       | Removes a directory on the remote SFTP server.                                                                       |
| Rename File or Directory    | `sftp.rename(oldpath, newpath)`                 | Renames a file or directory on the remote SFTP server.                                                                |
| Get Remote File's Metadata  | `sftp.stat(remote_path)`                        | Returns information about a file on the remote SFTP server, such as size, permissions, etc.                          |
| Change Permissions          | `sftp.chmod(remote_path, permissions)`          | Changes the permissions of a file or directory on the remote SFTP server.                                            |
| Change Ownership            | `sftp.chown(remote_path, uid, gid)`             | Changes the owner and group of a file or directory on the remote SFTP server.                                        |
