import subprocess

def run_command(command):
    try:
        # 使用subprocess.run执行命令，并捕获输出和错误信息
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout  # 返回标准输出
    except subprocess.CalledProcessError as e:
        # 如果命令执行失败，则返回错误信息
        return f"Error: {e.stderr}"


if __name__ == "__main__":
    output = run_command("ls / -l")
    print(output)