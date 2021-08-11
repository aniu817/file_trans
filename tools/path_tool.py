import datetime
import os


class PathTool:

    @staticmethod
    def get_project_dir():
        return os.path.abspath(os.path.dirname(os.getcwd()))
        # return os.path.abspath(os.path.join(os.getcwd()))

    @staticmethod
    def get_package_dir(package_name):
        return os.path.join(PathTool.get_project_dir(), package_name)

    @staticmethod
    def dir_make(dirs):
        if not os.path.exists(dirs):
            os.makedirs(dirs)

    @staticmethod
    def out_path(file, file_dirs='output'):
        file_path = PathTool.get_package_dir(file_dirs)
        today = datetime.date.today().strftime('%Y-%m-%d')
        dirs = file_path + '/' + today
        PathTool.dir_make(dirs)
        output_name = os.path.basename(file).split('.xls')[0] + '-转换.xlsx'
        output_path = dirs + '/' + output_name
        return output_path


if __name__ == "__main__":
    print(PathTool().get_project_dir())
    print(PathTool().get_package_dir('row_list'))
