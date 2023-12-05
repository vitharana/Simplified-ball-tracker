import pandas as pd
from datetime import datetime
import os
# Set your Excel file path
class Data_Saver:
    def __init__(self, excel_file_name = 'Ball_Data'):
        self.session = 0
        self.excel_file_name = excel_file_name
        self.current_datetime = datetime.now()
        self.current_time = datetime.now().time()
        self.formatted_time = self.current_time.strftime("%H%M%S")
        self.excel_file_path = f"{self.excel_file_name}_{self.current_datetime.date()}_{self.formatted_time}_{self.session}.xlsx"



    def export_data(self,cv2):

        # Convert the list of dictionaries to a Pandas DataFrame
        df = pd.DataFrame(cv2.d_data_points)
        # self.excel_file_path = f"{self.excel_file_name}_{self.current_datetime.date()}_{self.session}.xlsx"

        self.current_time = datetime.now().time()

        # Format time without colons
        self.formatted_time = self.current_time.strftime("%H%M%S")

        folder_name = f"Data Folder_{cv2.d_folder_no}"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Create the file path with folder
        self.excel_file_path = os.path.join(folder_name,
                                            f"{self.excel_file_name}_{self.current_datetime.date()}_{self.formatted_time}_{self.session}.xlsx")

        # Create an instance of YourClass



        print(self.excel_file_path)


        # Save the DataFrame to an Excel file
        df.to_excel(self.excel_file_path, index=False)
        self.session += 1
        #self.coordinate_data.clear()

        print("Coordinates saved to Excel.")
