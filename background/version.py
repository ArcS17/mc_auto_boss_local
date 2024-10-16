__version__ = "1.2.7"
release_date = "2024-09-17"
description = "更新"

# ver1.3.0
# update:2024-10-8
# updated by ArcS17
# 0.鸣潮1.3版本相关适配
# 1.修复背包声骸锁定筛选
# 2.支持周本Boss快速重新挑战
# 3.支持新世界Boss无归的谬误
# 4.优化Boss传送ocr范围
# 5.todo:批量声骸合成锁定(实在懒得做)

# ver1.2.7
# update:2024-09-17
# updated by ArcS17
# 1.修复世界Boss模型切换问题
# 2.完善轮次用时统计逻辑
# 3.修复依赖版本问题
# 4.修复Boss等待时间问题

# ver1.2.6
# update:2024-09-08
# updated by ArcS17
# 0.【主仓归档】迁移新分支
# 1.修复1.2版本UI适配问题(声骸合成、背包锁定)&(720p/768p/900p/1080p)
# 2.修复时序之寰-角传送逻辑
# 3.优化声骸套装识别逻辑
# 4.新增轮次用时统计
# 5.支持多显示器 From RinRose0

# ver1.2.5
# update:2024-07-19
# updated by ArcS17
# 1.连招支持闪避动作: l(小写L)
# 2.首次治疗传送自动调整地图缩放 From RinRose0
# 3.加快搜索声骸镜头重置
# 4.增加大招动画等待所支持分辨率

# ver1.2.4
# update:2024-07-16
# updated by ArcS17
# 1.新增指定周本Boss等待时间
# 2.新增声骸文件配置提醒
# 3.修复截取窗口失败TypeError，默认连续已锁声骸检测阈值过低，声骸分值计算功能角色名称错误
# 4.重写F9后调用逻辑，重写F9功能使用提醒

# ver1.2.3
# update:2024-07-08
# updated by wakening
# 1.支持国服、b服账号登录弹窗识别，并自动点击登录

# ver1.2.2
# update:2024-07-08
# updated by ArcS17
# 1.新增初始化时config文件不存在以example为模板自动生成完整格式及风格的config文件
# 2.absorption_action完成后统计一次吸收率
# 3.config.example.TargetBoss示例增加角
# 4.对齐日志各Level输出


# ver1.2.1
# update:2024-07-08
# updated by wang115t
# 1.重构代码，副本打完BOSS卡加载后，自动重启游戏的功能
# 2.过副本支持显示进度条


# ver1.2.0
# update:2024-07-07
# updated by wang115t
# 1.重构代码，角脚本卡加载后，自动重启游戏的功能

# ver1.1.0
# update:2024-07-06
# updated by wang115t
# 1.新增角脚本卡加载后，自动重启游戏的功能

# ver1.0.9
# update:2024-07-05
# updated by wang115t
# 1.游戏更新完成后，通过点击退出按钮来重新启动游戏。
# 2.新增UE4弹窗崩溃后，自动重启游戏。
# 3.注意：需要安装pyautogui依赖
# 4.自定义检测UE4崩溃弹窗间隔时间，在config.yaml中进行配置

# ver1.0.8
# update:2024-07-05
# updated by ArcS17
# 1.优化了游戏窗口崩溃后重启启动游戏及脚本的逻辑
# 2.修复了一个BUG（崩溃后log统计战斗次数为0会抛出TypeError: cannot unpack non-iterable NoneType object）
# 3.增加了在config文件设置游戏定时重启的功能
# 4.增加了多次截取游戏窗口失败后重启游戏及脚本的功能
# 5.增加了声骸锁定及声骸合成功能对1600*900分辨率1.0缩放、1366*768分辨率1.0缩放的适配
# 6.增加了声骸识别失败后主动抛出适配分辨率提醒

# ver1.0.7
# update:2024-07-03
# updated by wakening
# 1.修复声骸锁定异常退出bug
# 2.声骸锁定代码逻辑优化，提升执行速度

# ver1.0.6
# update:2024-06-27
# updated by wakening
# 1.增加了命令行参数-t/--task，可以在启动后立即打boss，无需再按快捷键
# 2.增加了命令行参数-c/--config，可以指定自定义的配置文件，打不同boss使用不同配置启动

# ver1.0.5
# update:2024-06-26
# updated by RoseRin0
# 1.增强了合成功能的实用性。
# 2.修改了部分变量的名字
# 3.修复了部分设备上对【湮灭】词条的识别问题。
# 4.将isCrashes.txt移至项目根目录

# ver1.0.4
# update:2024-06-22
# updated by wang115t
# 1.新增防止游戏崩溃的功能，实时检测游戏窗口
# 2.修复游戏崩溃后，数据重置为0的问题

# ver1.0.3
# update:2024-06-22
# updated by RoseRin0
# 1.增加了背包自动识别声骸属性并锁定的功能。实验性

# ver1.0.2
# update:2024-06-19
# updated by RoseRin0
# 1.修复了一个BUG，该BUG导致直接使用example配置会闪退。（删除了example文件中的大招技能连段后的“,”）
# 2.增加了BOSS起身无敌时间的判断。
# 3.将日志文件默认路径改为了项目根目录。
# 4.增加了防倒卖的受骗说明。

# ver1.0.1
# update:2024-06-19
# updated by RoseRin0
# 1.更新了大招连段。（如大招动画判断可用）
# 2.添加了版本管理文件，以方便管理版本。
# 3.添加了日志功能，可在config中更改日志文件路径，默认为：C:\mc_log.txt
