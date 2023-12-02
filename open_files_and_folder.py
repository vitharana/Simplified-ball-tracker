import subprocess



import os

def open_cam_port():

    current_directory = os.getcwd()
    folder_name = 'camera_port.txt'

    joined_path = os.path.join(current_directory, folder_name)
    #print("Joined path:", joined_path)


    subprocess.Popen(['explorer', joined_path])


def open_com_port():

    current_directory = os.getcwd()
    folder_name = 'com_port.txt'

    joined_path = os.path.join(current_directory, folder_name)
    #print("Joined path:", joined_path)


    subprocess.Popen(['explorer', joined_path])

def open_excel():

    current_directory = os.getcwd()
    folder_name = 'Data.xlsx'

    joined_path = os.path.join(current_directory, folder_name)
    #print("Joined path:", joined_path)


    subprocess.Popen(['explorer', joined_path])

def open_source_code():

    current_directory = os.getcwd()
    folder_name = 'Source_Code'

    joined_path = os.path.join(current_directory, folder_name)
    #print("Joined path:", joined_path)


    subprocess.Popen(['explorer', joined_path])



