# ❓ HyperArmor-Skill: 常见问题解答 (FAQ)

### Q1: HyperArmor-Skill 支持哪些编程语言开发的项目？
**A**: 支持几乎所有主流语言编译产物：
- **Python 项目**：通过内置原生跃迁转化为 C++ 后深度加壳
- **C / C++ / Rust / Go / .NET / C#**：直接对编译生成的 `.exe`、`.dll`、`.so`、`Mach-O` 进行整函数级虚拟化加壳
- **Android / iOS**：支持移动端 `.so` 原生动态库与 App Store 合规加固

### Q2: 加固后软件运行性能损耗大吗？
**A**: 极低！HyperArmor 采用精准的“整函数与核心算法级虚拟化”策略：
- 核心鉴权、核心业务逻辑与私钥运算进行 **最高强度虚拟化**；
- 频繁的界面渲染和通用 IO 操作保持 **高效原生执行**；
- 整体软件运行 CPU 开销增加小于 1%~3%，用户端毫无感知。

### Q3: 会不会被杀毒软件误报？
**A**: 本系统采用企业级正规编译流水线与标准 PE 头规范，实测对 Windows Defender、火绒、ESET 等主流杀软拥有极高的免杀纯净度。

### Q4: 如何获取商业版与一机一码授权 SDK？
- 💬 **官方微信**: `JAY_Secretsignal` *(备注: HyperArmor 咨询)*
- ✈️ **官方 Telegram**: [@Jay_Star666](https://t.me/Jay_Star666)
