import os
import sys
import subprocess
import pandas as pd
from io import StringIO

def get_packages_dataframe():
    """获取包列表并返回为DataFrame"""
    try:
        # 尝试使用 conda list
        result = subprocess.run(
            ['conda', 'list', '--json'],
            capture_output=True,
            text=True,
            check=True
        )
        # 解析JSON输出
        import json
        packages = json.loads(result.stdout)
        df = pd.DataFrame(packages)[['name', 'version', 'channel']]
        df['source'] = 'conda'
        return df
        
    except (subprocess.CalledProcessError, FileNotFoundError):
        try:
            # 尝试使用pip list
            result = subprocess.run(
                [sys.executable, '-m', 'pip', 'list', '--format=json'],
                capture_output=True,
                text=True,
                check=True
            )
            # 解析JSON输出
            import json
            packages = json.loads(result.stdout)
            df = pd.DataFrame(packages)[['name', 'version']]
            df['channel'] = None
            df['source'] = 'pip'
            return df
            
        except subprocess.CalledProcessError:
            return None

# 获取环境信息
conda_env = os.environ.get('CONDA_DEFAULT_ENV', '未检测到Conda环境')
python_version = sys.version.split()[0]
print(f"当前Conda环境: {conda_env}")
print(f"Python版本: {python_version}")

# 获取包列表
df = get_packages_dataframe()

if df is not None:
    print("\n当前环境安装的包:")
    print(df.to_string(index=False))
else:
    print("\n无法获取包列表信息")