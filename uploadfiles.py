import dropbox as dpx

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from)
        relative_path= os.path.relpath(local_path, file_from)
        dropbox_path= os.path.join(file_to, relative_path)
        with open (local_path, 'rb') as f:
            dpx.files_upload(f.read(), dropbox_path, mode=writeMode('overwrite'))

    def main():
    access_token='sl.A6KBtL1FS394HaHC6UdnPJOBZfOvqqY6CXQeES2TqubYOGCnn-Ou6-J4BAfj_EiJJ3qws_YMTel3idBqQ8RyNM7jor2qZ3oE3kggqGpq_nMxIpAYfaYmmR-0FgnvJJbH4seyUEU'
    transferData=TransferData(access_token)

    file_from = input("enter the file path to transfer: ")
    file_to = input("enter the full path to upload to dropbox")

    transferData.upload_file(file_from,file_to)
    print("the file has been moved")

main()
