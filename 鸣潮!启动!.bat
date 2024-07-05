@echo off
:: 本程序旨在检查鸣潮是否运行并自动启动鸣潮游戏本体以及auto脚本
:: 将本程序放置于 config.example.yaml 同级目录
:: 免责开源声明：本程序为适配开源项目 地址 https://github.com/lazydog28/mc_auto_boss 的便捷启动程序，免费分享禁止倒卖牟利，作者企鹅群号：689545101

@REM 通过注册表读取游戏路径
set "reg_path=SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\KRInstall Wuthering Waves"
set "reg_key=InstallPath"
set "folder_name=Wuthering Waves Game"
set "exe_name=Wuthering Waves.exe"

for /f "tokens=2*" %%a in ('reg query "HKLM\%reg_path%" /v "%reg_key%" ^| findstr "%reg_key%"') do (
    set "program_path=%%b"
)

REM 拼接完整路径
set "mc_full_path=%program_path%\%folder_name%\%exe_name%"

chcp 65001
echo.

net session >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo 请以管理员权限运行此脚本。
    pause
    exit /b 1
)

:main
echo 检查鸣潮是否运行

@REM 检测进程是否存在
tasklist /FI "IMAGENAME eq Wuthering Waves.exe" 2>NUL | find /I /N "Wuthering Waves.exe">NUL
if %ERRORLEVEL% NEQ 0 (
rem 启动鸣潮
    echo 鸣潮并未运行，唤醒程序
    echo.
    start "" "%mc_full_path%"
    if %ERRORLEVEL% NEQ 0 (
        timeout /t 3 /nobreak >nul
        goto :main   
    )
) else (
    echo 鸣潮已在运行
    timeout /t 3 /nobreak >nul
)
echo 启动脚本

echo.
echo 激活环境 '鸣潮'
call conda activate mc

rem 检查环境是否激活成功
if %ERRORLEVEL% NEQ 0 (
    echo 激活Conda环境'mc'失败，请检查项目依赖配置
    pause
    exit /b 1
)

rem 进入当前文件夹
cd /d %~dp0
echo 当前目录  %CD%
echo 开始运行  main.py
echo.
echo -------------------------------------------鸣潮启动!!!-------------------------------------------------
python .\background\main.py
if %ERRORLEVEL% NEQ 0 (
    echo 启动脚本失败，请检查本程序是否置于项目路径
    pause
    exit /b 1
)

pause
exit /b 1