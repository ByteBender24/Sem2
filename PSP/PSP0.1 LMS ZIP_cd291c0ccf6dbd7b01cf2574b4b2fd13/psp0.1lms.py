
import os
import zipfile


def count_lines_of_code(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        non_comment_lines = [line for line in lines if not line.strip().startswith("#")]
        return len(non_comment_lines)


def get_module_size(module_path):
    total_size = 0
    num_functions = 0
    num_classes = 0
    num_methods = 0
    other_size = 0

    for dirpath, dirnames, filenames in os.walk(module_path):
        for filename in filenames:
            if filename.endswith(".py"):
                filepath = os.path.join(dirpath, filename)
                size = count_lines_of_code(filepath)
                if dirpath == module_path:
                    num_functions += size
                else:
                    num_methods += size
                total_size += size

    # count classes and other lines of code
    with os.scandir(module_path) as entries:
        for entry in entries:
            if entry.is_file() and entry.name.endswith(".py"):
                with open(entry.path) as f:
                    lines = f.readlines()
                    non_comment_lines = [line for line in lines if not line.strip().startswith("#")]
                    for line in non_comment_lines:
                        if line.strip().startswith("class "):
                            num_classes += 1
                        else:
                            other_size += 1

    return total_size, num_functions, num_classes, num_methods, other_size


def report_loc(package_path):
    # create directory for extracting the package
    extract_dir = os.path.join(os.getcwd(), "extracted_package")
    os.makedirs(extract_dir, exist_ok=True)

    try:
        # extract the package to the temporary directory
        with zipfile.ZipFile(package_path, 'r') as zip_file:
            zip_file.extractall(extract_dir)

        # find all modules (sub-directories) in the package
        modules = [os.path.join(extract_dir, name) for name in os.listdir(extract_dir) if os.path.isdir(os.path.join(extract_dir, name))]

        # report total package size
        total_size = 0
        for module in modules:
            size, _, _, _, _ = get_module_size(module)
            total_size += size
        print("Total code size (Total LOC of the package):", total_size)

        # report module size
        for module in modules:
            print()
            print("Module:", os.path.basename(module))
            size, num_functions, num_classes, num_methods, other_size = get_module_size(module)
            print("Size:", size)
            print("Number of sub-modules:", len(os.listdir(module)))
            print("Number of independent functions:", num_functions)
            print("Number of classes:", num_classes)
            print("Number of methods:", num_methods)
            print("Size of other lines of code:", other_size)

    finally:
        # delete the extracted package directory
        os.chdir(os.path.dirname(os.path.abspath(__file__)))  # change working directory to script location
        


if __name__ == '__main__':
    package_path = r"D:\Python\Singaram-UIT2201-psp-ex-02.zip\xml.zip"
    report_loc(package_path)





