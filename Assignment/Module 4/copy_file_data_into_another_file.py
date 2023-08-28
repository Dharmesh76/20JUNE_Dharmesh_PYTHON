def copy_file(base_file,destination_file):
  try:
    with open (base_file,'r') as base:
        with open(destination_file,'a') as destination:
            content = base.read()
            destination.write(content)
            print("File Copied Successfully")
  except FileNotFoundError:
    print("File Not Found")
  except Exception as e:
     print("Error occured :",str(e))

copy_file('D:\Python_Tops_Center\count.txt','D:\Python_Tops_Center\copied.txt')