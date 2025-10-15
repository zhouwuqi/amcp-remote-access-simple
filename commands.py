from terminal import *
import shlex


def command_tell_folder(path):
    if(path != "" and path != 0 and path != "0"):
        command = "ls "+str(path)+" -l"
    else:
        command = "ls / -l"
    return(run_command(command))

def command_tell_process():
    return(run_command("sudo lsof -nP -iTCP -sTCP:LISTEN"))

def command_tell_nvidia():
    return(run_command("nvidia-smi"))

def command_tell_memory():
    return(run_command("free -h"))

def command_tell_disk():
    return(run_command("df -h"))

def command_read_file(path, row=None):
    total_lines_cmd = f"wc -l < {path}"
    total_lines = int(run_command(total_lines_cmd).strip())

    if row is None:
        # 默认从第1行开始读取，最多读取100行
        read_from_row = 1
        read_to_row = min(100, total_lines)
        cmd = f"head -n {read_to_row} {path}"
        content = run_command(cmd)
        fully_read = total_lines <= 100
    else:
        # 从指定行开始读取，最多读取100行
        read_from_row = int(row)
        read_to_row = min(read_from_row + 99, total_lines)
        cmd = f"sed -n '{read_from_row},{read_to_row}p' {path}"
        content = run_command(cmd)
        fully_read = read_to_row == total_lines

    # 构造 metadata 字符串
    metadata = (
        "############### FILE METADATA ###############\n"
        f"path:{path}\n"
        f"max_row:{total_lines}\n"
        f"read_from_row_this_time:{read_from_row}\n"
        f"read_to_row_this_time:{read_to_row}\n"
        f"if_have_read_all:{'True' if fully_read else 'False'}\n"
        "#############################################\n"
    )
    return metadata + content


def find_keyword_in_file(path, keyword):
    # 使用 shlex.quote 对关键字和路径做安全转义，避免 shell 注入问题
    safe_path = shlex.quote(path)
    safe_keyword = shlex.quote(keyword)

    # 使用 grep 的 -F 参数表示把 pattern 当作固定的字符串而不是正则表达式
    # -n 显示行号；用 cut 提取出冒号前的行号部分
    cmd = f"grep -F -n {safe_keyword} {safe_path} | cut -d: -f1"
    result = run_command(cmd).strip()

    # 处理结果：将行号字符串拆分成整数列表
    if result:
        line_numbers = list(map(int, result.split()))
    else:
        line_numbers = []
    return {"find_in_row": line_numbers}


def command_tell_cpu():
    return(run_command("lscpu"))


def command_search_file_folder(path,value):
    return(run_command("find "+path+" -name" + value))

if __name__ == "__main__":

    path = "/home"
    # print(command_tell_folder(path))

    # print(command_tell_process())
    path = "/home/lighthouse/code_here/mtPlusProjects/agentPlusFront/react-webapp-agentplus/src/App.js"
    row = 100
    # print(command_read_file(path, row))

    keyword = "changeFavicon"
    print(find_keyword_in_file(path, keyword))
    pass