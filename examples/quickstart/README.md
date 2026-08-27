# 🚀 Quickstart Example (快速上手示例)

本目录提供了一个简单的待保护商业算法示例：

## 体验步骤
1. 查看示例源码：[`sample_target.py`](sample_target.py)
2. 运行加固演示工具：
```bash
python ../../scripts/demo_protect_lite.py --input sample_target.py
```
3. 检测生成文件的香农熵：
```bash
python ../../scripts/verify_entropy.py --file "dist/sample_target_protected.exe"
```
