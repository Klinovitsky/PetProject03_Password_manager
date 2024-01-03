"""Archive the encrypted list of accounts to and from the archive"""
import zipfile

# [+] Unzip the file with password from the archive to the working folder
# [+] Move the file to archive back (or delete accounts, resource file after archiving)
# [+] Complete the code (write, read, data from functions)

FILE_NAME = 'my_resources.zip'


def zip_file(password_for_zip):
    """Zip the file to an archive"""

    # TODO. Add compression level
    with zipfile.ZipFile(FILE_NAME, 'w') as file:
        file.setpassword(pwd=bytes(password_for_zip, 'utf-8'))
        file.write("my_resources.txt")
        print('... Zip_file()')


def unzip_file(password_for_zip):
    """Unzip the file from the archive (with password)"""

    with zipfile.ZipFile(FILE_NAME) as file:
        # Password must be in the bytes converted 'str' into 'bytes'
        # 'setpassword' method is used to give a password to the 'Zip'
        file.setpassword(pwd=bytes(password_for_zip, 'utf-8'))
        file.extractall()   # Unzip file to the working folder
    print('... Unzip_file()')

