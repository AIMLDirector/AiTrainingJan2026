def check_error_logs(file_path: str):
    error_list = []
    try:
        with open(file_path, 'r') as file:
            logs = file.readlines()
            for line in logs:
                if "ERROR" in line:
                    error_list.append(line.strip())
            return False
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return error_list


print(check_error_logs("system_logs.txt"))
