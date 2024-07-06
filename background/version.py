__version__ = "1.0.8"
release_date = "2024-07-05"
description = "更新"

#去除UE4检测部分代码，回退至1.0.8

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