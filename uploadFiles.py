
import dropbox
import os
from dropbox.files import WriteMode


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token        

    def upload_file(self, file_from, file_to):     
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for filename in files:
               local_path = os.path.join(root, filename)


        relative_path = os.path.relpath(local_path, file_from)
        dropbox_path = os.path.join(file_to, relative_path)

        with open(file_from, 'rb') as f:        
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite')) 

def main():
    access_token = 'sl.BHzBYkVCwS2I10q6U32r_vXy5NpCSVgBuzIBC3s-S0HgFzBTg89dPH5-eR_dWHwIe-sccqBpn_3sBAV1SWfms4gBdLtcrfOQUFyzf0FlhGfxvxwDBBtHza_R_SH8EogQ97sT4oJKUhM'
    transferData = TransferData(access_token)

    file_from = 'C:/Users/HP/Desktop/folder/text.txt'
    file_to = '/Test2/text  "'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print('done')
main()