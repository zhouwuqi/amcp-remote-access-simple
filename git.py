import requests
import base64

# 可选：添加 GitHub Token 来提高请求频率限制
GITHUB_TOKEN = None  # 如果你有 token，可以设置在这里


def get_default_branch(owner, repo):
    """获取仓库的默认分支"""
    url = f'https://api.github.com/repos/{owner}/{repo}'
    headers = {}
    if GITHUB_TOKEN:
        headers['Authorization'] = f'token {GITHUB_TOKEN}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('default_branch', 'main')
    else:
        print(f"[Error] 获取默认分支失败: {response.status_code}")
        return 'main'


def get_repo_files(owner, repo):
    """
    获取特定仓库的文件列表
    """
    branch = get_default_branch(owner, repo)
    url = f'https://api.github.com/repos/{owner}/{repo}/contents'
    params = {'ref': branch}
    headers = {}
    if GITHUB_TOKEN:
        headers['Authorization'] = f'token {GITHUB_TOKEN}'

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        return response.json(), branch
    else:
        print(f"[Error] 获取文件列表失败: {response.status_code}")
        return [], branch


def get_file_content(file_path, owner='zhouwuqi', repo='amcp-remote-access-simple'):
    """
    获取特定仓库中特定文件的内容
    """
    branch = get_default_branch(owner, repo)
    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{file_path}'
    params = {'ref': branch}
    headers = {}
    if GITHUB_TOKEN:
        headers['Authorization'] = f'token {GITHUB_TOKEN}'

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        file_data = response.json()
        if 'content' in file_data:
            content = base64.b64decode(file_data['content']).decode('utf-8')
            return content
        else:
            print("[Warning] 文件没有内容字段")
            return None
    elif response.status_code == 404:
        print(f"[Error] 文件未找到: {file_path}")
        return None
    else:
        print(f"[Error] 获取文件内容失败: {response.status_code}")
        return None


# 使用示例
if __name__ == '__main__':
    owner = 'zhouwuqi'
    repo = 'amcp-remote-access-simple'

    # 获取文件列表
    files, branch = get_repo_files(owner, repo)
    print(f"仓库默认分支: {branch}\n")
    # print(files)
    for file in files:
        print(file['name'])

    # 获取特定文件的内容
    file_path = 'readme.md'  # 注意大小写敏感性
    print("\n--- 文件内容 ---")
    content = get_file_content(file_path, owner, repo)
    if content:
        print(content)
    else:
        print("无法获取文件内容")