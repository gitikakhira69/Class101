from os import access
import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_files(self,files_from,files_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(files_from,'rb') as f:
            dbx.files_upload(f.read(),files_to)

def main():
    access_token = 'sl.BE7GmNLMRFL57BIw-JPBI771V3xfwpy5u-vXPq03tUtvOq8ppknSZV1LKb3cOzZb0ysSzZjfh_Utymryj7eoG4Ssrbln44v4_Upls-z7_VWU3TaC-i7mc9xs1028H1t_qNVIRUc'
    transferdata = TransferData(access_token)
    files_from = input("Enter the path name to transfer")
    files_to = input("Enter the full path to upload to dropbox")
    transferdata.upload_files(files_from,files_to)
    print("File has been moved!!")
main()