# run_workflow.py
import os
from cozepy import Coze, TokenAuth

def main():
    coze_token = os.environ["COZE_TOKEN"]
    workflow_id = os.environ["WORKFLOW_ID"]
    api_base = os.environ.get("COZE_API_BASE")  # 可选，中国站可以配 https://api.coze.cn

    auth = TokenAuth(coze_token)

    # 如果需要自定义 base_url（比如中国站），可以这样：
    if api_base:
        client = Coze(auth=auth, base_url=api_base)
    else:
        client = Coze(auth=auth)

    # 这里的 parameters 要和你工作流的“开始节点输入变量”名称对应
    # 比如你前面 workflow 是完全自动跑邮箱的，那可能根本不需要输入；
    # 那就传一个空 dict。
    params = {}

    print("[Job Daily Agent] Start run workflow:", workflow_id)
    result = client.workflows.runs.create(
        workflow_id=workflow_id,
        parameters=params,
    )

    # 打一点日志，方便在 GitHub Actions 里看
    print("[Job Daily Agent] Run result:")
    print(result)

if __name__ == "__main__":
    main()
